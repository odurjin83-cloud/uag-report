# 6a / 02 — `SubmitCountEvents` flow (бүтээх заавар)

Аппаас ирсэн ≤25 тооллогын event-ийг **шалгаж**, Events-д **нэмж**, Final-ыг **шинэчилж**, мөр тус бүрийн receipt буцаана.
Зөвхөн стандарт connector (Power Apps V2 trigger, SharePoint, Data operations). Premium хэрэггүй.

## 0. Яагаад ийм бүтэцтэй вэ
| Шаардлага | Шийдэл |
|---|---|
| **Хурд, лимит.** Microsoft 365 лицензтэй үед Power Platform-ийн өдрийн хүсэлтийн хязгаар бага. Microsoft-ын эх сурвалжууд 6,000 эсвэл 40,000 гэж зөрүүтэй заадаг тул admin center-ээс шалгана. | Event бүрт Apply to each (≈5 action/мөр) **хэрэглэхгүй**. Бүх логик нь `Select`/`Filter array`, бичилт нь **нэг SharePoint `$batch`** хүсэлт. Ингэснээр ≈45 action/batch болно, 25 мөртэй batch-д **≈1.8 action/мөр**. 30,000 event ≈ 54,000 action (Apply to each ашиглавал ≈150,000). |
| **Давхардал.** Ижил мөр 2 удаа ирж болно (сүлжээ тасрах, retry). | `Title=ClientRowId` нь **unique**. Ижил ID ирвэл flow хадгалсан `CanonicalPayload`-тэй тулгана: таарвал өмнөх үр дүнг буцаана, таарахгүй бол `conflict` буцаана. |
| **Power Fx болон flow-д SHA hash функц байхгүй.** | Hash ашиглахгүй. Canonical мөрийг **flow өөрөө** талбаруудаас бүрдүүлж, бүтэн текстээр нь тэнцүү эсэхийг шалгана. |
| **Уралдаан (race).** 2 нярав ижил барааг зэрэг тоолж болно. | Concurrency=1 **хэрэглэхгүй**: Power Apps-ийн дуудлага дараалал хүлээж timeout болно. Оронд нь Final-ыг үүсгэхэд unique, шинэчлэхэд `IF-MATCH: <etag>` ашиглана. Мөргөлдсөн мөр `retry` буцаана. Дахин ирэхэд event аль хэдийн байгаа тул зөвхөн Final-ыг дахин тооцно (idempotent). |
| Нэг batch дотор ижил түлхүүр | **Апп** нэг batch-д нэг `LogicalCountKey`-д нэг л event хийнэ (03_APP_CONTRACT). Flow үүнийг шалгаж, зөрчвөл `bad_request` буцаана. |

## 1. Оролт / гаралт (гэрээ)
Trigger: **Power Apps (V2)**, нэг **Text** оролт `payload`.
```json
{"v":1,"batchId":"<guid>","sessionId":"S-2026-11-001","events":[
 {"clientRowId":"<guid>","attemptId":"<guid>","locationCode":"P-MAIN","binCode":"NO-BIN","itemNo":"0500010005",
  "qty":12.5,"attemptType":"Initial","countedAtUtc":"2026-11-20T09:15:31Z","deviceId":"<guid>",
  "bookQty":14,"bookAsOfUtc":"2026-11-20T01:00:00Z"}]}
```
Гаралт (*Respond to a Power App or flow*, Text `result`):
```json
{"ok":true,"batchId":"…","serverUtc":"…","results":[
 {"clientRowId":"…","result":"accepted|rejected|conflict|retry","reason":"Received|Rejected…|Conflict","firstTime":true,"finalStatus":"Counted|VarianceDetected|RecountRequired|…"}]}
```
Алдаа: `{"ok":false,"code":"bad_request|no_identity|server_error","message":"…"}`.

Апп `accepted` болон `rejected` мөрийг pending-ээс хасна. `rejected` мөрийг тусад нь харуулна. `conflict` мөрийг хадгалж улаан анхааруулга өгнө. `retry` мөр болон `ok:false` хариутай бүх мөрийг хадгалж, дараа дахин илгээнэ.

## 2. Canonical (flow бүрдүүлнэ)
```
v1|SESSION|LOC|BIN|ITEM|string(float(qty))|attemptType|countedAtUtc|callerEmail
```
`SESSION/LOC/BIN/ITEM` = `toUpper(trim())`, хоосон bin = `NO-BIN`, caller = trigger header-ийн и-мэйл (жижиг үсэг).
`countedAtUtc` нь аппын **анх хадгалсан текст** тул retry бүрт ижил байна.

## 3. Алхмууд
Action-ийн нэрийг **яг ингэж** өгнө (томьёонд нэрээр нь хандана). Бүгдийг **Scope `Try`** дотор хийнэ.
Томьёонд аргумент бүрийг `coalesce`-оор хамгаалсан. Учир нь `if()` хоёр салааг хоёуланг нь тооцоолж болзошгүй тул `null`-аас болж алдаа гарахаас сэргийлнэ.

### 3.1 Оролт
| # | Төрөл / нэр | Томьёо |
|---|---|---|
| 1 | Compose `Caller` | `toLower(trim(coalesce(triggerOutputs()?['headers']?['x-ms-user-email'],'')))` |
| 2 | Compose `Req` | `json(triggerBody()?['text'])` *(trigger-ийн оролтын түлхүүр `text` эсэхийг trigger outputs-оос шалгана)* |
| 3 | Compose `S` | `toUpper(trim(string(coalesce(outputs('Req')?['sessionId'],''))))` |
| 4 | Compose `BatchId` | `string(coalesce(outputs('Req')?['batchId'],guid()))` |
| 5 | Compose `BB` | `concat('batch_',guid())` |

**6. Select `E1`** — From: `coalesce(outputs('Req')?['events'],json('[]'))`, **key-value** горим:
| Түлхүүр | Утга |
|---|---|
| id | `trim(string(coalesce(item()?['clientRowId'],'')))` |
| att | `trim(string(coalesce(item()?['attemptId'],'')))` |
| L | `toUpper(trim(string(coalesce(item()?['locationCode'],''))))` |
| B | `if(empty(trim(string(coalesce(item()?['binCode'],'')))),'NO-BIN',toUpper(trim(string(coalesce(item()?['binCode'],'')))))` |
| I | `toUpper(trim(string(coalesce(item()?['itemNo'],''))))` |
| qs | `string(coalesce(item()?['qty'],''))` |
| t | `trim(string(coalesce(item()?['attemptType'],'Initial')))` |
| at | `trim(string(coalesce(item()?['countedAtUtc'],'')))` |
| dev | `string(coalesce(item()?['deviceId'],''))` |
| bq | `item()?['bookQty']` |
| bqAt | `string(coalesce(item()?['bookAsOfUtc'],''))` |

**7. Filter array `Bad`** — From: `body('E1')`, advanced:
```
@or(empty(item()?['id']),empty(item()?['L']),empty(item()?['I']),not(isFloat(item()?['qs'])),
 not(equals(length(item()?['at']),20)),not(endsWith(item()?['at'],'Z')),not(contains(item()?['at'],'T')),
 contains(concat(item()?['id'],item()?['L'],item()?['B'],item()?['I']),'|'),
 contains(concat(item()?['id'],item()?['L'],item()?['B'],item()?['I']),'"'),
 contains(concat(item()?['id'],item()?['L'],item()?['B'],item()?['I']),'\'),
 contains(concat(item()?['id'],item()?['L'],item()?['B'],item()?['I']),''''))
```
**8. Condition `InputOk`**: `and(not(empty(outputs('Caller'))),not(empty(outputs('S'))),greater(length(body('E1')),0),lessOrEquals(length(body('E1')),25),equals(length(body('Bad')),0))`
- **No** → Respond: `{"ok":false,"code":"@{if(empty(outputs('Caller')),'no_identity','bad_request')}","message":"invalid input"}` → **Terminate** (Succeeded).
- **Yes** → дараагийн бүх алхам Yes дотор.

**9. Select `E2`** — From `body('E1')`, **text** горим (Map нүдэнд нэг томьёо):
```
addProperty(addProperty(addProperty(item(),'q',float(item()?['qs'])),
 'key',concat(outputs('S'),'|',item()?['L'],'|',item()?['B'],'|',item()?['I'])),
 'canon',concat('v1|',outputs('S'),'|',item()?['L'],'|',item()?['B'],'|',item()?['I'],'|',string(float(item()?['qs'])),'|',item()?['t'],'|',item()?['at'],'|',outputs('Caller')))
```
**10. Select `Ids`** (text): `item()?['id']` **11. Select `Keys`** (text): `item()?['key']` (хоёулаа From `body('E2')`)
**12. Condition `UniqueOk`**: `and(equals(length(union(body('Ids'),body('Ids'))),length(body('Ids'))),equals(length(union(body('Keys'),body('Keys'))),length(body('Keys'))))`
- **No** → Respond `{"ok":false,"code":"bad_request","message":"duplicate clientRowId or key in batch"}` → Terminate.

### 3.2 Сесс, эрх, хуваарилалт (3 SharePoint уншилт)
| # | Үйлдэл | Тохиргоо |
|---|---|---|
| 13 | Get items `GetSession` | List `CountSessions`, Filter: `Title eq '@{replace(outputs('S'),'''','''''')}'`, Top 1 |
| 14 | Compose `Sess` | `first(body('GetSession')?['value'])` |
| 15 | Compose `Open` | `equals(string(coalesce(outputs('Sess')?['Status'],'')),'Open')` |
| 16 | Compose `Scope` | `concat('|',toUpper(string(coalesce(outputs('Sess')?['LocationScope'],''))),'|')` |
| 17 | Get items `GetAcl` | List `AssetUserAccess`, Filter: `CompanyCode eq 'TME-Inventory-Pages' and UserEmail eq '@{outputs('Caller')}'` |
| 18 | Filter array `AclOk` | From `body('GetAcl')?['value']`: `@and(equals(item()?['Active'],true),contains(string(coalesce(item()?['Title'],'')),'|count|'),greater(ticks(coalesce(item()?['ExpiresAt'],'9999-12-31T00:00:00Z')),ticks(utcNow())))` |
| 19 | Select `AclLocList` (text) | From `body('AclOk')`: `toUpper(trim(string(coalesce(item()?['LocationCode'],''))))` |
| 20 | Compose `AclLocs` | `concat('|',join(body('AclLocList'),'|'),'|')` |
| 21 | Get items `GetAsg` | List `CountAssignments`, Filter: `CountSessionId eq '@{replace(outputs('S'),'''','''''')}' and CounterEmail eq '@{outputs('Caller')}'` |
| 22 | Select `AsgLocList` (text) | From `body('GetAsg')?['value']`: `toUpper(trim(string(coalesce(item()?['LocationCode'],''))))` |
| 23 | Compose `AsgLocs` | `concat('|',join(body('AsgLocList'),'|'),'|')` |

Апптай ижил ACL дүрэм: `Active`, `ExpiresAt`, `Title`-д `|count|`, `LocationCode` = `*` эсвэл `|A|B|`. **Админы и-мэйлийг hard-code хийхгүй**: админ `LocationCode="*"` мөртэй байна.

### 3.3 Өмнө ирсэн event ба Final (2 SharePoint уншилт)
| # | Үйлдэл | Тохиргоо |
|---|---|---|
| 24 | Select `IdQ` (text) | From `body('E2')`: `concat('Title eq ''',item()?['id'],'''')` |
| 25 | Get items `GetEvents` | List `InventoryCountEvents`, Filter: `@{join(body('IdQ'),' or ')}`, Top 25 |
| 26 | Select `ExParts` (text) | From `body('GetEvents')?['value']`: `concat('"',item()?['Title'],'":',string(item()))` |
| 27 | Compose `ExMap` | `json(concat('{',join(body('ExParts'),','),'}'))` |
| 28 | Select `KeyQ` (text) | From `body('E2')`: `concat('Title eq ''',item()?['key'],'''')` |
| 29 | Get items `GetFinals` | List `InventoryCountFinal`, Filter: `@{join(body('KeyQ'),' or ')}`, Top 25 |
| 30 | Select `FinParts` (text) | From `body('GetFinals')?['value']`: `concat('"',item()?['Title'],'":',string(item()))` |
| 31 | Compose `FinMap` | `json(concat('{',join(body('FinParts'),','),'}'))` |

(`ExMap["<clientRowId>"]` болон `FinMap["<key>"]` нь давталтгүйгээр хайх боломж олгоно. Түлхүүрт `"` `\` `'` `|` байхгүй гэдгийг 7-р алхам баталсан.)

### 3.4 Шийдвэр (Select-үүд, давталтгүй)
**32. Select `E3`** (text, From `body('E2')`):
```
addProperty(addProperty(item(),'ex',coalesce(outputs('ExMap')?[item()?['id']],json('{}'))),'fin',coalesce(outputs('FinMap')?[item()?['key']],json('{}')))
```
**33. Select `E4`** (text, From `body('E3')`). Event-ийн төлөв `st`:
```
addProperty(item(),'st',
 if(not(empty(item()?['ex'])),
   if(equals(string(coalesce(item()?['ex']?['CanonicalPayload'],'')),item()?['canon']),string(coalesce(item()?['ex']?['Status'],'Received')),'Conflict'),
 if(not(outputs('Open')),'RejectedSessionClosed',
 if(not(and(
      or(contains(outputs('AclLocs'),'|*|'),contains(outputs('AclLocs'),concat('|',item()?['L'],'|'))),
      or(contains(outputs('Scope'),'|*|'),contains(outputs('Scope'),concat('|',item()?['L'],'|'))),
      or(equals(outputs('S'),'LEGACY'),contains(outputs('AsgLocs'),concat('|',item()?['L'],'|'))))),'RejectedNoPermission',
 if(less(item()?['q'],0),'RejectedBadQty',
 if(not(equals(item()?['t'],if(equals(outputs('S'),'LEGACY'),'Legacy','Initial'))),'RejectedAttemptType',
 'Received'))))))
```
**34. Select `E5`** (text, From `body('E4')`). Аль тоологчийн байр `slot`: A = эхний, B = хоёр дахь, X = гурав дахь:
```
addProperty(item(),'slot',
 if(empty(item()?['fin']),'A',
 if(equals(toLower(string(coalesce(item()?['fin']?['CounterA'],''))),outputs('Caller')),'A',
 if(or(empty(string(coalesce(item()?['fin']?['CounterB'],''))),equals(toLower(string(coalesce(item()?['fin']?['CounterB'],''))),outputs('Caller'))),'B','X'))))
```
**35. Select `E6`** (text, From `body('E5')`). Final-д `apply` хийх эсэх: хүлээн авсан, түгжээгүй, өмнө хэрэглэгдээгүй, хуучин биш:
```
addProperty(item(),'apply',and(
 equals(item()?['st'],'Received'),
 not(contains('|Approved|Rejected|Posted|UnderReview|',concat('|',string(coalesce(item()?['fin']?['Status'],'')),'|'))),
 not(equals(string(coalesce(item()?['fin']?[concat(item()?['slot'],'ClientRowId')],'')),item()?['id'])),
 not(less(ticks(item()?['at']),ticks(string(coalesce(item()?['fin']?[concat(item()?['slot'],'AtUtc')],'1900-01-01T00:00:00Z')))))))
```
**36. Select `E7`** (text, From `body('E6')`). Шинэ A/B утгууд:
```
addProperty(addProperty(addProperty(addProperty(addProperty(addProperty(addProperty(addProperty(addProperty(addProperty(item(),
 'nA',  if(and(item()?['apply'],equals(item()?['slot'],'A')),outputs('Caller'),string(coalesce(item()?['fin']?['CounterA'],'')))),
 'nAq', if(and(item()?['apply'],equals(item()?['slot'],'A')),item()?['q'],item()?['fin']?['AQty'])),
 'nAat',if(and(item()?['apply'],equals(item()?['slot'],'A')),item()?['at'],string(coalesce(item()?['fin']?['AAtUtc'],'')))),
 'nAid',if(and(item()?['apply'],equals(item()?['slot'],'A')),item()?['id'],string(coalesce(item()?['fin']?['AClientRowId'],'')))),
 'nB',  if(and(item()?['apply'],equals(item()?['slot'],'B')),outputs('Caller'),string(coalesce(item()?['fin']?['CounterB'],'')))),
 'nBq', if(and(item()?['apply'],equals(item()?['slot'],'B')),item()?['q'],item()?['fin']?['BQty'])),
 'nBat',if(and(item()?['apply'],equals(item()?['slot'],'B')),item()?['at'],string(coalesce(item()?['fin']?['BAtUtc'],'')))),
 'nBid',if(and(item()?['apply'],equals(item()?['slot'],'B')),item()?['id'],string(coalesce(item()?['fin']?['BClientRowId'],'')))),
 'third',or(and(item()?['apply'],equals(item()?['slot'],'X')),equals(item()?['fin']?['ThirdCounter'],true))),
 'exp', if(empty(item()?['fin']),item()?['bq'],item()?['fin']?['ExpectedQtyAtCount']))
```
**37. Select `E8`** (text, From `body('E7')`). Final-ийн төлөв `fSt`. Хүлцэл 0: ижил бол нэг дүн, зөрвөл дахин тоолно:
```
addProperty(item(),'fSt',
 if(item()?['third'],'RecountRequired',
 if(and(not(empty(item()?['nB'])),not(equals(float(coalesce(item()?['nAq'],0)),float(coalesce(item()?['nBq'],0))))),'RecountRequired',
 if(or(equals(item()?['exp'],null),equals(float(coalesce(item()?['nAq'],0)),float(coalesce(item()?['exp'],0)))),'Counted','VarianceDetected'))))
```

### 3.5 Бичих биеүүд
**38. Select `EvBody`** (key-value, From `body('E8')`):
`Title`=`item()?['id']`, `LogicalCountKey`=`item()?['key']`, `CountAttemptId`=`item()?['att']`, `CountSessionId`=`outputs('S')`, `LocationCode`=`item()?['L']`, `BinCode`=`item()?['B']`, `ItemNo`=`item()?['I']`, `CounterEmail`=`outputs('Caller')`, `DeviceId`=`item()?['dev']`, `PhysicalCountQty`=`item()?['q']`, `BookQtyAtCount`=`item()?['bq']`, `BookAsOfUtc`=`item()?['bqAt']`, `CountedAtUtc`=`item()?['at']`, `AttemptType`=`item()?['t']`, `CanonicalPayload`=`item()?['canon']`, `ServerReceivedAtUtc`=`utcNow()`, `Status`=`item()?['st']`, `BatchId`=`outputs('BatchId')`

**39. Select `FinBody`** (key-value, From `body('E8')`):
`Title`=`item()?['key']`, `CountSessionId`=`outputs('S')`, `LocationCode`=`item()?['L']`, `BinCode`=`item()?['B']`, `ItemNo`=`item()?['I']`, `ExpectedQtyAtCount`=`item()?['exp']`, `CounterA`=`item()?['nA']`, `AQty`=`item()?['nAq']`, `AAtUtc`=`item()?['nAat']`, `AClientRowId`=`item()?['nAid']`, `CounterB`=`item()?['nB']`, `BQty`=`item()?['nBq']`, `BAtUtc`=`item()?['nBat']`, `BClientRowId`=`item()?['nBid']`, `ThirdCounter`=`item()?['third']`, `Status`=`item()?['fSt']`,
`FinalCountQty`=`if(equals(item()?['fSt'],'RecountRequired'),null,item()?['nAq'])`,
`VarianceQty`=`if(or(equals(item()?['fSt'],'RecountRequired'),equals(item()?['exp'],null)),null,sub(float(coalesce(item()?['nAq'],0)),float(coalesce(item()?['exp'],0))))`,
`LastEventAtUtc`=`utcNow()`

### 3.6 `$batch` (нэг HTTP хүсэлт)
Event бүрт **яг 2 үйлдэл** (event, final) байна. Бичих шаардлагагүй бол хоосон `GET` хийнэ. Тэгснээр хариуны дараалал `2i` = event, `2i+1` = final гэж шууд тохирно.

**40–43. Compose загварууд.** Compose нүдэнд **жинхэнэ мөр шилжилттэй** бичнэ. `SITE`-ийг өөрийн сайтаар солино. `##…##` хэсгийг flow өөрөө орлуулна.

`TplNoop`
```
--##BB##
Content-Type: application/http
Content-Transfer-Encoding: binary

GET https://SITE/sites/TME_Finance/_api/web?$select=Id HTTP/1.1
Accept: application/json;odata=nometadata

```
`TplCreate` (`##LIST##` = Events эсвэл Final)
```
--##BB##
Content-Type: multipart/mixed; boundary=##CS##

--##CS##
Content-Type: application/http
Content-Transfer-Encoding: binary

POST https://SITE/sites/TME_Finance/_api/web/lists/getbytitle('##LIST##')/items HTTP/1.1
Content-Type: application/json;odata=nometadata
Accept: application/json;odata=nometadata

##BODY##
--##CS##--

```
`TplMerge`
```
--##BB##
Content-Type: multipart/mixed; boundary=##CS##

--##CS##
Content-Type: application/http
Content-Transfer-Encoding: binary

POST https://SITE/sites/TME_Finance/_api/web/lists/getbytitle('InventoryCountFinal')/items(##ID##) HTTP/1.1
Content-Type: application/json;odata=nometadata
Accept: application/json;odata=nometadata
X-HTTP-Method: MERGE
IF-MATCH: ##ETAG##

##BODY##
--##CS##--

```
**44. Select `Parts`** (text, From `range(0,length(body('E8')))`):
```
concat(
 if(and(not(equals(body('E8')[item()]?['st'],'Conflict')),empty(body('E8')[item()]?['ex'])),
   replace(replace(replace(replace(outputs('TplCreate'),'##BB##',outputs('BB')),'##CS##',concat('cse',string(item()))),'##LIST##','InventoryCountEvents'),'##BODY##',string(body('EvBody')[item()])),
   replace(outputs('TplNoop'),'##BB##',outputs('BB'))),
 if(not(body('E8')[item()]?['apply']),
   replace(outputs('TplNoop'),'##BB##',outputs('BB')),
 if(empty(body('E8')[item()]?['fin']),
   replace(replace(replace(replace(outputs('TplCreate'),'##BB##',outputs('BB')),'##CS##',concat('csf',string(item()))),'##LIST##','InventoryCountFinal'),'##BODY##',string(body('FinBody')[item()])),
   replace(replace(replace(replace(replace(outputs('TplMerge'),'##BB##',outputs('BB')),'##CS##',concat('csf',string(item()))),'##ID##',string(coalesce(body('E8')[item()]?['fin']?['ID'],0))),'##ETAG##',string(coalesce(body('E8')[item()]?['fin']?['@odata.etag'],'*'))),'##BODY##',string(body('FinBody')[item()])))))
```
(`##BODY##`-г **хамгийн сүүлд** орлуулна. Тэгэхгүй бол өгөгдөл доторх тэмдэгтүүд загварын placeholder-той андуурагдаж эвдэрнэ.)

**45. Compose `BatchText`**: `concat(join(body('Parts'),''),'--',outputs('BB'),'--',decodeUriComponent('%0A'))`

**46. Send an HTTP request to SharePoint `SendBatch`**: Site = TME_Finance, `POST`, Uri `_api/$batch`,
Headers: `Content-Type: multipart/mixed; boundary=@{outputs('BB')}`, `Accept: application/json;odata=nometadata`, Body: `outputs('BatchText')`

**47. Compose `Resp`**: `if(equals(body('SendBatch')?['$content'],null),string(body('SendBatch')),base64ToString(body('SendBatch')?['$content']))`
**48. Compose `Codes`**: `skip(split(outputs('Resp'),'HTTP/1.1 '),1)`
**49. Condition `CodesOk`**: `equals(length(outputs('Codes')),mul(2,length(body('E8'))))` → No бол Respond `server_error` ("batch response count mismatch") → Terminate. *(Бүх мөр pending хэвээр үлдэнэ. Аюулгүй.)*

### 3.7 Хариу
**50. Select `Out`** (key-value, From `range(0,length(body('E8')))`):
| Түлхүүр | Утга |
|---|---|
| clientRowId | `body('E8')[item()]?['id']` |
| reason | `body('E8')[item()]?['st']` |
| result | `if(equals(body('E8')[item()]?['st'],'Conflict'),'conflict',if(or(greaterOrEquals(int(substring(outputs('Codes')[mul(item(),2)],0,3)),300),greaterOrEquals(int(substring(outputs('Codes')[add(mul(item(),2),1)],0,3)),300)),'retry',if(startsWith(body('E8')[item()]?['st'],'Rejected'),'rejected','accepted')))` |
| firstTime | `and(empty(body('E8')[item()]?['ex']),less(int(substring(outputs('Codes')[mul(item(),2)],0,3)),300))` |
| finalStatus | `if(body('E8')[item()]?['apply'],body('E8')[item()]?['fSt'],string(coalesce(body('E8')[item()]?['fin']?['Status'],'')))` |

**51. Respond to a Power App or flow** — Text `result`:
`string(addProperty(addProperty(addProperty(json('{"ok":true}'),'batchId',outputs('BatchId')),'serverUtc',utcNow()),'results',body('Out')))`

### 3.8 Catch
Scope `Try`-ийн дараа **Scope `Catch`** (Configure run after: Try → *has failed, has timed out*) → Respond:
`{"ok":false,"code":"server_error","message":"@{string(result('Try'))}"}` *(урт бол `substring(...,0,1000)`)*.
Апп энэ үед бүх мөрийг pending-д үлдээнэ.

## 4. Тохиргоо
- Trigger-т **Concurrency control-ийг асаахгүй** (§0).
- SharePoint "Get items": Pagination **OFF** (Top 25 хангалттай).
- Flow-ийн Run-only users: Power Apps-аас дуудах тул апп хуваалцсан хэрэглэгчид *Provided by run-only user* биш, **таны холболт** ашиглана (одоогийн flow-уудтай адил).
- **Хүсэлтийн хязгаар**: Power Platform admin center → Analytics/Capacity хэсгээс энэ flow-ийн өдрийн action-ийн тоог эхний туршилтын өдөр шалгана.

## 5. Хүлээн авах тест (flow-ийн Run history-оор, апп хэрэггүй)
Flow-ийг "Test → Manually" ажиллуулж, `payload`-д доорх JSON-ыг өгнө. Урьдчилсан нөхцөл: `CountSessions`-д `TEST-01` (Status=Open, LocationScope=`|CAMP|`), өөрт чинь `CountAssignments`-д CAMP мөр байх.
| # | Үйлдэл | Хүлээгдэх үр дүн |
|---|---|---|
| T1 | 1 шинэ event (CAMP, qty 5, bookQty 5) | `accepted`, firstTime=true; Events 1 мөр; Final `Counted`, FinalCountQty=5 |
| T2 | **T1-ийг яг дахин** илгээх | `accepted`, firstTime=**false**; Events-д шинэ мөр **нэмэгдэхгүй**; Final өөрчлөгдөхгүй |
| T3 | T1-ийн clientRowId, qty=**6** | `conflict`; Events/Final өөрчлөгдөхгүй |
| T4 | Шинэ clientRowId, ижил бараа, qty 6, countedAt **хожуу** | `accepted`; Final AQty=6, `VarianceDetected` (6≠5), VarianceQty=1 |
| T5 | Шинэ clientRowId, qty 4, countedAt **T4-өөс эрт** | `accepted` (event хадгалагдана); Final AQty **6 хэвээр** |
| T6 | Өөр хэрэглэгч (assignment-тэй) ижил бараа qty 6 | Final CounterB, `VarianceDetected` (A=B=6 ≠ 5) |
| T7 | T6-ийн хэрэглэгч qty 7 (шинэ ID, хожуу) | Final `RecountRequired`, FinalCountQty хоосон |
| T8 | locationCode `P-MAIN` (scope-д байхгүй) | `rejected`, reason `RejectedNoPermission`; Events-д Rejected мөр; Final өөрчлөгдөхгүй |
| T9 | Сессийг `CountingClosed` болгоод шинэ event | `rejected`, `RejectedSessionClosed` |
| T10 | T9-ийг дахин илгээх | `rejected` (ижил), Events-д нэмэгдэхгүй |
| T11 | Нэг batch-д ижил itemNo/bin 2 event | `ok:false`, `bad_request` |
| T12 | qty `"abc"` | `ok:false`, `bad_request` |
| T13 | 25 шинэ event | 25 `accepted`; run-ийн action тоо ≈ 45–55; хугацааг тэмдэглэнэ |
| T14 | Хоёр browser tab-аас нэг шинэ бараан дээр **зэрэг** (өөр 2 хэрэглэгч) | Нэг нь `accepted`, нөгөө нь `accepted` эсвэл `retry`. Retry-г дахин илгээвэл `accepted`; Final-д A ба B хоёулаа байна |
