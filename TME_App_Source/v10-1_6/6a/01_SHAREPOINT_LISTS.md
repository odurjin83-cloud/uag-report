# 6a / 01 — SharePoint жагсаалтууд (TME_Finance)

Premium лицензгүй → бүх өгөгдөл **SharePoint**, бүх бичилт **Power Automate (стандарт connector)**-оор.
4 жагсаалт. Баганын **дотоод нэр (internal name) латин үсгээр** байх ёстой — flow-ийн томьёо эдгээр нэрийг шууд ашиглана.
Монгол нэрээр багана үүсгэвэл дотоод нэр `_x0422_...` болж эвдэрнэ. Тиймээс доорх **Provision flow**-оор үүсгэхийг зөвлөж байна (гараар бол нэрийг яг ингэж бичээд, дараа нь харагдах нэрийг солих).

Бүх тоон багана **Number** (одоогийн `InventoryCount`-ын text + locale асуудлыг давтахгүй). Огноо/цагийг canonical харьцуулалтад ордог газарт **Text** (ISO `yyyy-MM-ddTHH:mm:ssZ`) байдлаар хадгална — SharePoint DateTime-ийн цагийн бүсийн хөрвүүлэлтээс зайлсхийнэ.

## 1. Жагсаалт ба баганууд

### CountSessions — сесс (supervisor SharePoint дээр гараар үүсгэнэ, 6a)
| Багана | Төрөл | Index | Тайлбар |
|---|---|---|---|
| `Title` | Text | ✅ **unique** | `CountSessionId`, жишээ `S-2026-11-001` (том үсэг, `|` `"` `'` хориотой) |
| `SessionName` | Text | | Хүнд ойлгомжтой нэр |
| `LocationScope` | Text | | `|P-MAIN|P-OM|` эсвэл `*` |
| `Status` | Text | ✅ | `Draft` / `Open` / `CountingClosed` / `UnderReview` / `Approved` / `Posted` / `Cancelled` |
| `OwnerEmail` | Text | | |
| `SnapshotAsOfUtc` | Text | | Excel snapshot-ийн `asOf` |
| `OpenedAtUtc`, `CountingClosedAtUtc`, `ApprovedAtUtc`, `PostedAtUtc` | DateTime | | |
| `ApprovedBy`, `BCDocumentNo` | Text | | |
| `CancelReason` | Note (plain) | | |

### CountAssignments — хэн аль агуулахад тоолох
| Багана | Төрөл | Index | Тайлбар |
|---|---|---|---|
| `Title` | Text | ✅ | Чөлөөт (жишээ `S-2026-11-001 / bat@tme.mn / P-MAIN`) |
| `CountSessionId` | Text | ✅ | |
| `CounterEmail` | Text | ✅ | жижиг үсгээр |
| `LocationCode` | Text | | нэг агуулах = нэг мөр |
| `ZoneCode`, `BinFrom`, `BinTo` | Text | | 6a-д мэдээллийн чанартай, v10-1_7-д zone lock |
| `AssignedQty` | Number | | |
| `DeviceSyncDoneAtUtc` | DateTime | | |

### InventoryCountEvents — append-only, **зөвхөн flow бичнэ**
| Багана | Төрөл | Index | Тайлбар |
|---|---|---|---|
| `Title` | Text | ✅ **unique** | `ClientRowId` (GUID) — давхар илгээлтийн хамгаалалт |
| `LogicalCountKey` | Text | ✅ | `SESSION|LOC|BIN|ITEM` |
| `CountAttemptId` | Text | | |
| `CountSessionId` | Text | ✅ | |
| `LocationCode`, `BinCode`, `ItemNo` | Text | | |
| `CounterEmail` | Text | ✅ | trigger header-ээс (аппын илгээснээс биш) |
| `DeviceId` | Text | | |
| `PhysicalCountQty` | Number | | |
| `BookQtyAtCount` | Number | | Тоолох үеийн snapshot үлдэгдэл (мэдээлэл) |
| `BookAsOfUtc` | Text | | snapshot `asOf` |
| `CountedAtUtc` | Text | | Апп үүсгэсэн мөчид нэг удаа тогтоосон ISO текст |
| `AttemptType` | Text | | `Initial` / `Legacy` (6b: `Recount`, `SupervisorCount`) |
| `CanonicalPayload` | Note (plain) | | Flow өөрөө бүрдүүлсэн canonical мөр — давтан ирэлтийг тулгана |
| `ServerReceivedAtUtc` | DateTime | | |
| `Status` | Text | ✅ | `Received` / `RejectedSessionClosed` / `RejectedNoPermission` / `RejectedBadQty` / `RejectedAttemptType` |
| `BatchId` | Text | | |

### InventoryCountFinal — түлхүүр тутамд 1 мөр, **зөвхөн flow бичнэ**
| Багана | Төрөл | Index | Тайлбар |
|---|---|---|---|
| `Title` | Text | ✅ **unique** | `LogicalCountKey` |
| `CountSessionId` | Text | ✅ | |
| `LocationCode` | Text | ✅ | |
| `BinCode`, `ItemNo` | Text | | |
| `ExpectedQtyAtCount` | Number | | Анх үүсэх үеийн `BookQtyAtCount` (v10-1_7-д watermark-аар солигдоно) |
| `CounterA`, `CounterB` | Text | ✅ / ✅ | Эхний ба хоёр дахь тоологч |
| `AQty`, `BQty` | Number | | Тухайн тоологчийн **хамгийн сүүлийн** тоо |
| `AAtUtc`, `BAtUtc` | Text | | Тэр тооны `CountedAtUtc` (хуучин event шинийг дарахгүй) |
| `AClientRowId`, `BClientRowId` | Text | | Ижил event-ийг хоёр удаа хэрэглэхгүй (idempotency) |
| `ThirdCounter` | Yes/No | | 3 дахь өөр хүн тоолсон → `RecountRequired` |
| `FinalCountQty` | Number | | `RecountRequired` үед хоосон |
| `VarianceQty` | Number | | `FinalCountQty − ExpectedQtyAtCount` |
| `Status` | Text | ✅ | `Counted` / `VarianceDetected` / `RecountRequired` / `UnderReview` / `Approved` / `Rejected` / `Posted` |
| `LastEventAtUtc` | DateTime | | |
| `ApprovedBy` | Text | | 6b |
| `ApprovedAtUtc` | DateTime | | 6b |

**Index-ийг жагсаалт хоосон үед** үүсгэнэ (5,000 давсны дараа index нэмэх боломжгүй болдог). Unique нь index шаарддаг.

## 2. Эрх (security)
| Жагсаалт | Нярав | Supervisor/нябо | Flow эзэмшигч (холболт) |
|---|---|---|---|
| CountSessions | Read | Contribute | Read |
| CountAssignments | Read | Contribute | Read |
| InventoryCountEvents | **хандахгүй** | Read | Contribute |
| InventoryCountFinal | **хандахгүй** (6b-д тайлан flow-оор) | Read | Contribute |

List settings → Permissions → *Stop inheriting* → дээрх байдлаар. Нярав Events/Final-д шууд бичих боломжгүй тул бүх бичилт flow-ийн шалгалтаар (эрх, сесс, idempotency) заавал дамжина.
⚠️ Flow-ийн SharePoint холболт таны (od.u) хувийн бүртгэлээр ажиллана. Production-д тусгай service account руу шилжүүлэхийг дараа нь шийднэ.

## 3. Provision flow (нэг удаа ажиллуулна)
Instant cloud flow → **Manually trigger a flow**. Доорх 4 алхам.

**A. Compose `Site`** → `https://<tenant>.sharepoint.com/sites/TME_Finance` (одоогийн InventoryCount-ын сайт)

**B. Apply to each `MakeLists`** — From: `json('["CountSessions","CountAssignments","InventoryCountEvents","InventoryCountFinal"]')`, Concurrency = 1
- *Send an HTTP request to SharePoint* — Site: `outputs('Site')`, Method `POST`, Uri `_api/web/lists`
- Headers: `Accept: application/json;odata=verbose`, `Content-Type: application/json;odata=verbose`
- Body:
```json
{"__metadata":{"type":"SP.List"},"BaseTemplate":100,"Title":"@{item()}"}
```

**C. Compose `Fields`** — доорх массивыг яг хуулна (XML-д зөвхөн дан хашилт `'` ашигласан тул JSON эвдрэхгүй):
```json
[
{"l":"CountSessions","x":"<Field Type='Text' Name='SessionName' StaticName='SessionName' DisplayName='SessionName' MaxLength='255'/>"},
{"l":"CountSessions","x":"<Field Type='Text' Name='LocationScope' StaticName='LocationScope' DisplayName='LocationScope' MaxLength='255'/>"},
{"l":"CountSessions","x":"<Field Type='Text' Name='Status' StaticName='Status' DisplayName='Status' MaxLength='50' Indexed='TRUE'/>"},
{"l":"CountSessions","x":"<Field Type='Text' Name='OwnerEmail' StaticName='OwnerEmail' DisplayName='OwnerEmail' MaxLength='255'/>"},
{"l":"CountSessions","x":"<Field Type='Text' Name='SnapshotAsOfUtc' StaticName='SnapshotAsOfUtc' DisplayName='SnapshotAsOfUtc' MaxLength='40'/>"},
{"l":"CountSessions","x":"<Field Type='DateTime' Format='DateTime' Name='OpenedAtUtc' StaticName='OpenedAtUtc' DisplayName='OpenedAtUtc'/>"},
{"l":"CountSessions","x":"<Field Type='DateTime' Format='DateTime' Name='CountingClosedAtUtc' StaticName='CountingClosedAtUtc' DisplayName='CountingClosedAtUtc'/>"},
{"l":"CountSessions","x":"<Field Type='DateTime' Format='DateTime' Name='ApprovedAtUtc' StaticName='ApprovedAtUtc' DisplayName='ApprovedAtUtc'/>"},
{"l":"CountSessions","x":"<Field Type='Text' Name='ApprovedBy' StaticName='ApprovedBy' DisplayName='ApprovedBy' MaxLength='255'/>"},
{"l":"CountSessions","x":"<Field Type='DateTime' Format='DateTime' Name='PostedAtUtc' StaticName='PostedAtUtc' DisplayName='PostedAtUtc'/>"},
{"l":"CountSessions","x":"<Field Type='Text' Name='BCDocumentNo' StaticName='BCDocumentNo' DisplayName='BCDocumentNo' MaxLength='50'/>"},
{"l":"CountSessions","x":"<Field Type='Note' Name='CancelReason' StaticName='CancelReason' DisplayName='CancelReason' NumLines='4' RichText='FALSE'/>"},

{"l":"CountAssignments","x":"<Field Type='Text' Name='CountSessionId' StaticName='CountSessionId' DisplayName='CountSessionId' MaxLength='100' Indexed='TRUE'/>"},
{"l":"CountAssignments","x":"<Field Type='Text' Name='CounterEmail' StaticName='CounterEmail' DisplayName='CounterEmail' MaxLength='255' Indexed='TRUE'/>"},
{"l":"CountAssignments","x":"<Field Type='Text' Name='LocationCode' StaticName='LocationCode' DisplayName='LocationCode' MaxLength='50'/>"},
{"l":"CountAssignments","x":"<Field Type='Text' Name='ZoneCode' StaticName='ZoneCode' DisplayName='ZoneCode' MaxLength='50'/>"},
{"l":"CountAssignments","x":"<Field Type='Text' Name='BinFrom' StaticName='BinFrom' DisplayName='BinFrom' MaxLength='50'/>"},
{"l":"CountAssignments","x":"<Field Type='Text' Name='BinTo' StaticName='BinTo' DisplayName='BinTo' MaxLength='50'/>"},
{"l":"CountAssignments","x":"<Field Type='Number' Name='AssignedQty' StaticName='AssignedQty' DisplayName='AssignedQty'/>"},
{"l":"CountAssignments","x":"<Field Type='DateTime' Format='DateTime' Name='DeviceSyncDoneAtUtc' StaticName='DeviceSyncDoneAtUtc' DisplayName='DeviceSyncDoneAtUtc'/>"},

{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='LogicalCountKey' StaticName='LogicalCountKey' DisplayName='LogicalCountKey' MaxLength='255' Indexed='TRUE'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='CountAttemptId' StaticName='CountAttemptId' DisplayName='CountAttemptId' MaxLength='100'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='CountSessionId' StaticName='CountSessionId' DisplayName='CountSessionId' MaxLength='100' Indexed='TRUE'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='LocationCode' StaticName='LocationCode' DisplayName='LocationCode' MaxLength='50'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='BinCode' StaticName='BinCode' DisplayName='BinCode' MaxLength='50'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='ItemNo' StaticName='ItemNo' DisplayName='ItemNo' MaxLength='50'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='CounterEmail' StaticName='CounterEmail' DisplayName='CounterEmail' MaxLength='255' Indexed='TRUE'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='DeviceId' StaticName='DeviceId' DisplayName='DeviceId' MaxLength='100'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Number' Name='PhysicalCountQty' StaticName='PhysicalCountQty' DisplayName='PhysicalCountQty'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Number' Name='BookQtyAtCount' StaticName='BookQtyAtCount' DisplayName='BookQtyAtCount'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='BookAsOfUtc' StaticName='BookAsOfUtc' DisplayName='BookAsOfUtc' MaxLength='40'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='CountedAtUtc' StaticName='CountedAtUtc' DisplayName='CountedAtUtc' MaxLength='40'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='AttemptType' StaticName='AttemptType' DisplayName='AttemptType' MaxLength='30'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Note' Name='CanonicalPayload' StaticName='CanonicalPayload' DisplayName='CanonicalPayload' NumLines='3' RichText='FALSE'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='DateTime' Format='DateTime' Name='ServerReceivedAtUtc' StaticName='ServerReceivedAtUtc' DisplayName='ServerReceivedAtUtc'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='Status' StaticName='Status' DisplayName='Status' MaxLength='50' Indexed='TRUE'/>"},
{"l":"InventoryCountEvents","x":"<Field Type='Text' Name='BatchId' StaticName='BatchId' DisplayName='BatchId' MaxLength='100'/>"},

{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='CountSessionId' StaticName='CountSessionId' DisplayName='CountSessionId' MaxLength='100' Indexed='TRUE'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='LocationCode' StaticName='LocationCode' DisplayName='LocationCode' MaxLength='50' Indexed='TRUE'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='BinCode' StaticName='BinCode' DisplayName='BinCode' MaxLength='50'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='ItemNo' StaticName='ItemNo' DisplayName='ItemNo' MaxLength='50'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Number' Name='ExpectedQtyAtCount' StaticName='ExpectedQtyAtCount' DisplayName='ExpectedQtyAtCount'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='CounterA' StaticName='CounterA' DisplayName='CounterA' MaxLength='255' Indexed='TRUE'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Number' Name='AQty' StaticName='AQty' DisplayName='AQty'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='AAtUtc' StaticName='AAtUtc' DisplayName='AAtUtc' MaxLength='40'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='AClientRowId' StaticName='AClientRowId' DisplayName='AClientRowId' MaxLength='100'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='CounterB' StaticName='CounterB' DisplayName='CounterB' MaxLength='255' Indexed='TRUE'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Number' Name='BQty' StaticName='BQty' DisplayName='BQty'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='BAtUtc' StaticName='BAtUtc' DisplayName='BAtUtc' MaxLength='40'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='BClientRowId' StaticName='BClientRowId' DisplayName='BClientRowId' MaxLength='100'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Boolean' Name='ThirdCounter' StaticName='ThirdCounter' DisplayName='ThirdCounter'><Default>0</Default></Field>"},
{"l":"InventoryCountFinal","x":"<Field Type='Number' Name='FinalCountQty' StaticName='FinalCountQty' DisplayName='FinalCountQty'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Number' Name='VarianceQty' StaticName='VarianceQty' DisplayName='VarianceQty'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='Status' StaticName='Status' DisplayName='Status' MaxLength='50' Indexed='TRUE'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='DateTime' Format='DateTime' Name='LastEventAtUtc' StaticName='LastEventAtUtc' DisplayName='LastEventAtUtc'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='Text' Name='ApprovedBy' StaticName='ApprovedBy' DisplayName='ApprovedBy' MaxLength='255'/>"},
{"l":"InventoryCountFinal","x":"<Field Type='DateTime' Format='DateTime' Name='ApprovedAtUtc' StaticName='ApprovedAtUtc' DisplayName='ApprovedAtUtc'/>"}
]
```

**D. Apply to each `MakeFields`** — From: `outputs('Fields')`, Concurrency = 1
- *Send an HTTP request to SharePoint* — `POST`, Uri `_api/web/lists/getbytitle('@{item()?['l']}')/fields/createfieldasxml`
- Headers: B-тэй ижил (verbose)
- Body (`Options: 24` = дотоод нэрийг `Name`-ээс авах + default view-д нэмэх):
```json
{"parameters":{"__metadata":{"type":"SP.XmlSchemaFieldCreationInformation"},"SchemaXml":"@{item()?['x']}","Options":24}}
```

**E. Apply to each `TitleKeys`** — From:
```json
[{"l":"CountSessions","n":"CountSessionId","u":true},{"l":"CountAssignments","n":"AssignmentTitle","u":false},{"l":"InventoryCountEvents","n":"ClientRowId","u":true},{"l":"InventoryCountFinal","n":"LogicalCountKey","u":true}]
```
- *Send an HTTP request to SharePoint* — `POST`, Uri `_api/web/lists/getbytitle('@{item()?['l']}')/fields/getbyinternalnameortitle('Title')`
- Headers: verbose хоёр + `X-HTTP-Method: MERGE` + `IF-MATCH: *`
- Body:
```json
{"__metadata":{"type":"SP.Field"},"Title":"@{item()?['n']}","Indexed":true,"EnforceUniqueValues":@{item()?['u']}}
```
(Дотоод нэр `Title` хэвээр, зөвхөн харагдах нэр солигдоно.)

## 4. Шалгах (flow ажилласны дараа)
1. List settings бүрт баганууд **дотоод нэрээрээ** (Column-ийн URL-д `Field=AQty` гэх мэт) байгаа.
2. *Indexed columns*: Sessions 2 (Title, Status), Assignments 3, Events 5 (Title, LogicalCountKey, CountSessionId, CounterEmail, Status), Final 6 (Title, CountSessionId, LocationCode, CounterA, CounterB, Status).
3. Events-д ижил `Title`-тай 2 мөр гараар оруулах → 2 дахь нь **"value must be unique"** алдаа өгнө. Туршсаны дараа устгана.
4. §2-ын эрхийг тохируулна.
