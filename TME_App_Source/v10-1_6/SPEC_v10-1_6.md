# v10-1_6 — Тооллогын сесс, хурдан локал бичилт, баталгаат синк (техникийн тодорхойлолт)

Суурь код: `v10-1_5` + `v10-1_5b` (Codex-ийн төхөөрөмжийн тест дууссаны дараах хувилбар).
Зорилго: **15,000 код, 5–10 нярав, нэг нярав 5,000–7,000 мөр** — 5,000 дахь тооллого эхнийх шиг хурдан, нэг ч мөр алдахгүй, давхардахгүй.

---

## 0. Батлагдсан шийдвэрүүд
| Сэдэв | Шийдвэр |
|---|---|
| Сесс | Supervisor/эрх бүхий ахлах нярав үүсгэж хаана. Төлөв: `Draft → Open → CountingClosed → UnderReview → Approved → Posted` (+`Cancelled`). `Approved`-оос хойш тоо өөрчлөгдөхгүй; засвар нь шинэ event. `Posted` бүрэн immutable. |
| Хоёр тоологч | Ижил `CountSessionId+LocationCode+BinCode+ItemNo` дээр тоо зөрвөл **хүлцэлгүй** `RecountRequired`. Ижил бол нэг дүн (нэмэхгүй). Эцсийн дүнд зөвхөн `Approved`. |
| Book зөрүү | `VarianceDetected` → supervisor review. Физик тоог автоматаар хүчингүй болгохгүй. Бодит 6, бүртгэл 8 бол тайланд −2. |
| Хөдөлгөөн | Бүх агуулахыг freeze хийхгүй. Тоолж буй бүс/тавиурыг түр зогсооно (zone lock). Rolling reconciliation (BC `Entry No.` watermark) — **v10-1_7** (§9). |
| Тавиур | Тавиургүй location → `NO-BIN` автоматаар. Тавиур заавал location дээр сонголтгүй бол хадгалахгүй. Хуучин мөр → `LEGACY`. |
| Давтан илгээлт | `ClientRowId` дээр SharePoint **Enforce unique**. Ижил ID дахин ирвэл агуулга тулгана; таарвал амжилт, таарахгүй бол локал мөрийг устгахгүй (Conflict). |
| Хадгалалт | **SharePoint** (Power Apps premium лиценз байхгүй — 2026-11-20). Dataverse-ийг лиценз гарвал дахин үнэлнэ. Бүх бичилт стандарт connector-той flow-оор. |

## 1. Санал болгосон загварт оруулсан залруулга (Power Apps-ийн бодит хязгаар)
1. **Серверийн шалгалт = flow.** Одоо апп SharePoint руу шууд `Patch` хийдэг (9 газар). SharePoint өөрөө "сесс Open эсэх"-ийг шалгаж чадахгүй. Тиймээс бүх илгээлт **нэг flow** (`SubmitCountEvents`)-оор явна. Flow: сессийн төлөв, эрх, idempotency, final нэгтгэлийг хийнэ.
2. **Hash байхгүй (Power Fx-д ч, стандарт flow-д ч SHA функц алга).** Flow canonical мөрийг (`v1|SESSION|LOC|BIN|ITEM|qty|type|countedAtUtc|caller`) **өөрөө** бүрдүүлж `CanonicalPayload`-д хадгална; дахин ирэхэд бүтэн текстээр тулгана (таарвал өмнөх үр дүн, таарахгүй бол `conflict`). `PayloadHash` багана хасагдсан. → `6a/02_FLOW_SubmitCountEvents.md`
3. **Хаагдсан сесс рүү ирсэн офлайн мөр устахгүй.** Flow түүнийг `Events`-д `Status=RejectedSessionClosed`-оор **хадгалж** supervisor-т харуулна (audit). Апп receipt авмагц pending-ээс хасна.
4. **Final нэгтгэлийг апп хийхгүй.** Flow event бүрт `InventoryCountFinal`-ыг upsert хийнэ. **Concurrency control = 1 хэрэглэхгүй** (Power Apps-ийн дуудлага дараалалд хүлээж timeout болно) — оронд нь Final үүсгэхэд `Title` unique, шинэчлэхэд `IF-MATCH: etag`; мөргөлдвөл `retry`, дахин ирэхэд event байгаа тул зөвхөн Final-ыг idempotent байдлаар (`AClientRowId`/`BClientRowId`, `AAtUtc`/`BAtUtc`) дахин тооцно.
7. **Лимит/хурд.** Microsoft 365 лицензийн өдрийн хүсэлтийн хязгаар бага тул flow event бүрт давталт хийхгүй: бүх логик `Select`-ээр, бичилт **нэг SharePoint `$batch`**-аар (≈1.8 action/мөр). Апп нэг batch-д нэг түлхүүрт нэг л event илгээнэ.
5. **Incremental counter дангаараа хангалтгүй.** `varCounted+1` нь restart, олон төхөөрөмж, recount үед зөрнө. Progress = **серверийн нэгтгэл** (`GetSessionProgress`) + **локал pending тоо**. Синк бүрийн дараа серверээс шинэчилнэ.
6. **Rolling reconciliation-ийг тусад нь.** `ExpectedQtyAtCount`-ыг Entry No.-ээр тооцох нь BC-д item+location+entry range-аар хөдөлгөөн өгдөг API шаардана (BC `Posting Date` цаггүй). Иймд v10-1_7.

## 2. Архитектур
```
Tablet (Power Apps)                                  Server
┌──────────────────────────────┐                     ┌───────────────────────────────┐
│ colItems  (15k, per-user key)│                     │ CountSessions                 │
│ colBins / colAssignment      │                     │ CountAssignments              │
│ colPending  ← SaveData/бичилт │──SubmitCountEvents─▶│ InventoryCountEvents (append) │
│   (ихэвчлэн 0–20 мөр)         │◀──── receipts ──────│ InventoryCountFinal (1/key)   │
│ colRecent (≤200, санах ой)    │◀─GetSessionProgress─│ flows: progress, report       │
│ varSession, varDeviceId       │                     └───────────────────────────────┘
└──────────────────────────────┘
Save: validate → Collect(colPending) → SaveData(colPending) → дараагийн бараа (cloud хүлээхгүй)
Sync: timer, batch ≤25 → flow → receipt шалгах → colPending-ээс хасах → colRecent-д нэмэх
```

## 3. SharePoint бүтэц
**CountSessions**: `CountSessionId`(unique, idx), `Title`, `LocationScope`, `Status`(idx), `OwnerEmail`, `SnapshotAsOfUtc`, `OpeningEntryNoWatermark`, `ClosingEntryNoWatermark`, `OpenedAtUtc`, `CountingClosedAtUtc`, `ApprovedAtUtc`, `ApprovedBy`, `PostedAtUtc`, `BCDocumentNo`, `CancelReason`.

**CountAssignments**: `CountSessionId`(idx), `CounterEmail`(idx), `LocationCode`, `ZoneCode`, `BinFrom`, `BinTo`, `AssignedQty`, `DeviceSyncDoneAtUtc` (Closing үед "синк дууссан" тэмдэг).

**InventoryCountEvents** (append-only): `ClientRowId`(**unique**, idx), `LogicalCountKey`(idx), `CountAttemptId`, `CountSessionId`(idx), `LocationCode`, `BinCode`, `ItemNo`, `CounterEmail`(idx), `DeviceId`, `PhysicalCountQty`(Number), `BookQtyAtCount`, `BookAsOfUtc`, `CountedAtUtc`(Text ISO), `AttemptType`(Initial/Legacy; 6b: Recount/SupervisorCount), `CanonicalPayload`, `ServerReceivedAtUtc`, `Status`(Received/RejectedSessionClosed/RejectedNoPermission/RejectedBadQty/RejectedAttemptType), `BatchId`. Conflict мөр хадгалагдахгүй (unique).

**InventoryCountFinal**: `LogicalCountKey`(**unique**, idx), `CountSessionId`(idx), `LocationCode`(idx), `BinCode`, `ItemNo`, `ExpectedQtyAtCount`, `CounterA`(idx)/`AQty`/`AAtUtc`/`AClientRowId`, `CounterB`(idx)/`BQty`/`BAtUtc`/`BClientRowId`, `ThirdCounter`, `FinalCountQty`, `VarianceQty`, `Status`(idx: Counted/VarianceDetected/RecountRequired/UnderReview/Approved/Rejected/Posted), `LastEventAtUtc`, `ApprovedBy`, `ApprovedAtUtc`.

Дэлгэрэнгүй (дотоод нэр, provisioning, эрх): `6a/01_SHAREPOINT_LISTS.md`. Нярав Events/Final-д **шууд хандахгүй** — зөвхөн flow бичнэ.

Тоон баганууд **Number** төрөл (одоогийн text + locale асуудлыг шинэ жагсаалтад давтахгүй). Index-ийг жагсаалт хоосон байхад үүсгэнэ.

## 4. Flow-ууд
| Flow | Оролт | Үүрэг | Буцаах |
|---|---|---|---|
| `SubmitCountEvents` | ≤25 event (нэг түлхүүрт нэг) | Хэрэглэгч = trigger header и-мэйл; ACL + сессийн scope + assignment; сесс `Open`; `ClientRowId` байвал canonical тулгах; Events + Final нэг `$batch`-аар; etag/unique-аар race хамгаалалт | мөр бүрт `{clientRowId, result: accepted/rejected/conflict/retry, reason, firstTime, finalStatus}` — `6a/02` |
| `GetSessionProgress` | sessionId | Сервер талд нэгтгэл: assigned, counted, remaining, recount, variance (хэрэглэгчээр + нийт) | жижиг JSON |
| `GetMyAssignment` | sessionId | Тухайн хэрэглэгчийн бүс/тавиур | жагсаалт |
| `SessionAdmin` | action | Open, CountingClosed, OpenRecount, Approve, Cancel — зөвхөн supervisor | төлөв |
| `BuildSessionReport` | sessionId | Final-аас тайлан (pagination-тэй), "тоологдоогүй" = assignment − final | файл/JSON |

## 5. Апп: локал өгөгдөл ба хурдны дүрэм
- **Durable (SaveData)**: `colPending` (бичилт бүрт, жижиг), `varDeviceId` (анх GUID), сонгосон сесс/assignment, Items/Bins кэш (зөвхөн синкийн үед).
- **Санах ойд**: `colRecent` ≤200 (receipt авсан сүүлийн мөрүүд), серверийн progress.
- **Хориглох**: бүх түүхийг локалд барих, бичилт бүрт том JSON serialize хийх, `Text`/`Items` property-д түүх scan хийх.
- **Save замын дараалал**: (1) item local LookUp (`colItems`), (2) bin/assignment шалгалт, (3) event үүсгэх (`ClientRowId=GUID()`, `CountAttemptId=GUID()`, `LogicalCountKey`, canonical payload), (4) `Collect(colPending)`, (5) `SaveData(colPending,"CountPendingV16_"&ObjectId)`, (6) UI дараагийн бараа. SaveData амжилтгүй бол **хадгалсанд тооцохгүй**, мөрийг санах ойд үлдээж улаан анхааруулга.
- **Sync**: 15 сек timer, `colPending`-ээс ≤25 (нэг түлхүүрт нэг), flow; `accepted`/`rejected` бол pending-ээс хасна (rejected → hold, харуулна); `conflict` → hold (улаан); `retry`/алдаа бол pending-д үлдэнэ. Сүлжээ байхгүй бол UI-д нөлөөгүй. → `6a/03_APP_CONTRACT.md`

## 6. Одоогийн кодоос өөрчлөгдөх газрууд (v10-1_5 эх кодоос тоолсон)
| Төрөл | Тоо | Газрууд | v10-1_6-д |
|---|---|---|---|
| Бүх түүхийг JSON serialize (`JSON(colOfflineInventory)`) | **15 property** | App.OnStart(2), ScrAccess.phoneProfileSync, ScrCountHome (OnVisible, countHomeButton5, uploadQueueV16_10), ScrHistory (OnVisible, Button16, Button17, hDeleteConfirmV16, uploadQueueV16_12), ScrReport1.rptSync, scrWarehouses.Button1_2, нүүр (OnVisible, Button5, uploadQueueV16_11) | `SaveData(colPending)` нэг routine-оор солих |
| SharePoint руу шууд `Patch(InventoryCount` | **9** | ScrCountHome×2, ScrHistory×4, scrWarehouses.Button1_2×2, нүүр×2 | `SubmitCountEvents` flow (нэг sync routine); засах/устгах = шинэ event |
| Түүх сэргээх `ClearCollect(colRestoreCloudV16` | **6** | App.OnStart, ScrAccess, ScrCountHome, ScrHistory, ScrReport1, нүүр | Хасах. Progress/тайлан = flow |
| Локал түүх scan `colOfflineInventory` | **44 property** | **Text/Items property 20 гаруй**: нүүр (hPadActivity×8, badge, BusinessPower), ScrAccess (pStatValue0/1, pOfflineCounts, pExitWarning), scrWarehouses (phoneCountLocal, Label3_23), ScrHistory gallery×2, ScrCountHome text… | `colPending`/`colRecent`/серверийн progress руу |
| Schema 21 deserializer | 1 | App.OnStart | Pending queue-ийн шинэ schema + migration |

**Хурдны гол олдвор:** `Text`/`Items` property-д `Filter/CountRows(colOfflineInventory…)` байгаа нь collection өөрчлөгдөх бүрт (= тооллого бүрт) 5,000+ мөрийг дахин scan хийнэ. Энэ нь бичилт бүрийн бүрэн serialize-тэй хамт 5,000 дахь мөрийн удаашралын хоёр үндсэн шалтгаан.

## 7. Migration
- **Сервер (нэг удаа)**: одоогийн `InventoryCount` мөрүүдийг `InventoryCountEvents`-д `CountSessionId="LEGACY"`, `BinCode="LEGACY"`, `ClientRowId=CountKeyV27` (байхгүй бол `"SP-"&ID`)-ээр хуулна. Хуучин жагсаалт read-only.
- **Төхөөрөмж**: Schema 21 cache-аас **`Synced=false`** мөрүүдийг `colPending` руу `LEGACY` event болгон хөрвүүлнэ (`ClientRowId=SyncKey`) → flow-оор илгээнэ → receipt авсны дараа л хуучин cache-ийг `ClearData`. Синк хийгдсэн хуучин мөрийг төхөөрөмжөөс хасна.
- v10-1_5-ийн receipt файл (`CountReceiptV1015_*`) байвал мөн pending болгоно.

## 8. Хүлээн авах шалгуур (production gate)
Төхөөрөмж: Samsung Galaxy Tab A11 (бодит), 15,000 кодтой туршилтын сесс, нэг нярав **5,001–7,000** мөр, бусад зэрэг.
| Үзүүлэлт | Босго |
|---|---|
| Item lookup P95 | < 0.5 сек |
| Save UI (Qty→дараагийн бараа) P95 | < 1.0 сек (зорилт 0.5–0.7) |
| 5,000 дахь save vs 1 дэх | мэдэгдэхүйц дордохгүй (P95 зөрүү < 30%) |
| UI 2 сек-ээс дээш гацах | 0 |
| Алдагдсан мөр / давхар мөр / буруу бараа-тоо | 0 / 0 / 0 |
| Restart, сүлжээ таслах, шинэ төхөөрөмж — сэргэлт | 100% |
| Серверийн тайлан vs хяналтын дүн | 100% таарна |
Хэмжилт: save бүрт `Now()` тэмдэглэж (start/end) локал жижиг лог; 1, 100, 500, 1,000, 3,000, 5,000, 7,000 дахь мөр дээр P50/P95/P99; SaveData хугацаа; pending хэмжээ; sync throughput.

## 9. Үе шат
- **6a**: CountSessions + Assignments (уншихад), Events + Final, `SubmitCountEvents`, pending queue, хурдан save, локал progress (`firstTime`), migration. Сесс/assignment-ийг supervisor 6a-д **SharePoint жагсаалтаас шууд** удирдана (`SessionAdmin` flow, серверийн progress → 6b). Дараалал: (1) жагсаалт `6a/01` (2) flow `6a/02` + T1–T14 (3) 5b тест дууссаны дараа аппын PASTE `6a/03`-ын гэрээгээр.
- **6b**: Recount/review/approve UI, `RecountRequired` урсгал, тайлан (`BuildSessionReport`), "тоологдоогүй".
- **v10-1_7**: Zone lock (Start/Complete Zone Count), BC Entry No. watermark-аар `ExpectedQtyAtCount`, rolling reconciliation, BC posting.

## 10. Нээлттэй асуудал
1. BC-ээс item+location+Entry No. range-аар хөдөлгөөн өгөх API байгаа эсэх (v10-1_7-ийн урьдчилсан нөхцөл).
2. "High-value/serial" ангиллын эх сурвалж (book variance-ийн эрсдэлийн дүрэмд).
3. Power Platform хүсэлтийн хязгаар: M365 лицензийн бодит тоо (эх сурвалжууд 6,000–40,000/24ц гэж зөрүүтэй) ба instant flow-ийн action хэнд тоологдох — admin center-ээс T13-ын дараа хэмжинэ. Тооцоо: 30,000 event ≈ 1,200 batch × ≈45 action ≈ 54,000.
4. Серверийн progress (`GetSessionProgress`): 5,000-аас олон Final мөртэй жагсаалтад index-тэй шүүлтийн paging-ийг 20,000 туршилтын мөрөөр шалгасны дараа (6b).
