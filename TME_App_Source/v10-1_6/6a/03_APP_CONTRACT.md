# 6a / 03 — Аппын тал: гэрээ ба дүрэм (код биш)

> Аппын `.pa.yaml`-д **одоо хүрэхгүй**. Codex v10-1_5b-г тестэлж байгаа тул суурь код тест дуусах хүртэл тогтворгүй.
> Тест дууссаны дараа эцсийн суурь дээр (5b + тестийн засвар) 6a-ийн PASTE багцыг хийнэ. Энэ файл нь flow-той тохирох **гэрээ**.

## 1. Локал өгөгдөл
| Нэр | Хадгалалт | Агуулга |
|---|---|---|
| `colPendingV16a` | `SaveData("CountPendingV16a_" & <ObjectId>)` бичилт бүрт | Илгээгдээгүй event-үүд. Ихэвчлэн 0–30 мөр |
| `colHoldV16a` | `SaveData("CountHoldV16a_" & <ObjectId>)` | `conflict` / `bad_request` болсон мөрүүд. **Хэзээ ч автоматаар устгахгүй** |
| `varDeviceIdV16a` | `SaveData`, анх нэг удаа `Lower(Text(GUID()))` | |
| `varSessionV16a` | `SaveData` | Сонгосон сесс (Id, Scope, Status), assignment-ийн агуулахууд |
| `colRecentV16a` | санах ойд, ≤200 | Сүүлд `accepted` болсон мөрүүд (дэлгэцэд харуулах) |
| `varMyAcceptedV16a` | `SaveData` | `firstTime=true` ирсэн мөрийн тоо (локал progress) |

## 2. Event үүсгэх (Хадгалах товч)
- `ClientRowId` = `Lower(Text(GUID()))`, `AttemptId` = `Lower(Text(GUID()))`. Retry болон restart-ын үед **өөрчлөгдөхгүй**.
- `CountedAtUtc` = `Text(DateAdd(Now(),TimeZoneOffset(Now()),TimeUnit.Minutes),"yyyy-mm-ddThh:mm:ss","en-US") & "Z"`. **Нэг удаа тооцоод текстээр хадгална**, дахин тооцохгүй (canonical тогтвортой байна). Урт нь яг 20 тэмдэгт.
- `LocationCode`, `BinCode`, `ItemNo` нь `Upper(Trim())`. Хоосон bin бол `"NO-BIN"`. `|` `"` `'` `\` тэмдэгт агуулсан кодыг **хадгалахгүй** (flow `bad_request` буцаадаг тул тэр мөр хэзээ ч илгээгдэхгүй гацна).
- `LogicalCountKey` = `Session & "|" & Loc & "|" & Bin & "|" & Item` (бүгд Upper).
- `Qty` нь Number ба ≥ 0.
- Дараалал: Collect → `SaveData(colPendingV16a)` → **амжилттай бол л** дараагийн бараа руу шилжинэ. Амжилтгүй бол улаан мэдэгдэл гаргаж, хадгалсанд тооцохгүй (v10-1_5-ийн дүрэм).
- Cloud хүлээхгүй. Илгээх нь timer-ийн ажил.

## 3. Batch бүрдүүлэх
- Нэг batch: **≤25 мөр, нэг `LogicalCountKey`-д нэг event, нэг сесс**. Ижил түлхүүрийн дараагийн event (засвар) дараагийн batch-д явна.
```
With({b:FirstN(SortByColumns(colPendingV16a,"Seq",SortOrder.Ascending),100)},
 With({pick:FirstN(ForAll(Distinct(b,LogicalCountKey) As d,LookUp(b,LogicalCountKey=d.Value)),25)}, … ))
```
- Payload: `JSON({v:1,batchId:Lower(Text(GUID())),sessionId:…,events:ForAll(pick As p,{clientRowId:p.ClientRowId,attemptId:p.AttemptId,locationCode:p.LocationCode,binCode:p.BinCode,itemNo:p.ItemNo,qty:p.Qty,attemptType:p.AttemptType,countedAtUtc:p.CountedAtUtc,deviceId:varDeviceIdV16a,bookQty:p.BookQty,bookAsOfUtc:p.BookAsOfUtc})},JSONFormat.Compact)`
  (`JSON()` нь тоог locale-оос үл хамааран `12.5` хэлбэрээр бичдэг. Энэ нь одоогийн text/locale асуудлыг шийднэ.)

## 4. Хариу боловсруулах
| `result` | Апп |
|---|---|
| `accepted` | pending-ээс хасна → `colRecentV16a`. `firstTime=true` бол `varMyAcceptedV16a+1` |
| `rejected` | pending-ээс хасна → `colHoldV16a`-д `reason`-той (хэрэглэгчид харуулна. Сервер Events-д аль хэдийн хадгалсан) |
| `conflict` | pending-ээс → `colHoldV16a` (улаан). Supervisor шийднэ |
| `retry` | pending-д үлдэнэ |
| `ok:false` / сүлжээний алдаа | Бүгд pending-д үлдэнэ. `bad_request` бол тэр batch-ийн мөрүүдийг `colHoldV16a` руу шилжүүлнэ (давтаад ч амжилтгүй) |

Хасахаас өмнө `colHoldV16a`-г `SaveData` хийнэ. Дараа нь `RemoveIf(colPendingV16a,…)` → `SaveData(colPendingV16a)`.
Хасалт хадгалагдахаас өмнө апп унтарвал мөр дахин илгээгдэнэ. Сервер `accepted, firstTime=false` буцаана, тиймээс **давхардахгүй**.
`finalStatus = RecountRequired` ирвэл тухайн бараан дээр "Дахин тоолох шаардлагатай" тэмдэг харуулна.

## 5. Timer
- 15 сек тутам: `!IsEmpty(colPendingV16a) && Connection.Connected && !varSyncBusyV16a`
- Нэг дуудлага зэрэг явна (`varSyncBusyV16a`). Хариу ирэхэд дараагийн batch-ийг шууд илгээнэ (pending дуустал).
- UI-г хаахгүй. Зөвхөн "Илгээгдээгүй: N" тоолуур харуулна.

## 6. Тооллогын дэлгэцээс хасагдах зүйлс (хурдны гол ашиг)
- Бичилт бүрт `JSON(colOfflineInventory)` / бүх түүхийг `SaveData` хийх (15 газар) → зөвхөн `colPendingV16a`.
- `Text`/`Items` property доторх `colOfflineInventory` scan (20+) → `colPendingV16a` / `colRecentV16a` / `varMyAcceptedV16a`.
- `Patch(InventoryCount…)` (9 газар) → `SubmitCountEvents`.
