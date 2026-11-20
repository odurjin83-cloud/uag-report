# v10-1_5 — Studio-д хуулах заавар (засвар 1, 3, 4)

**Суурь:** `TME-v10-1-personal-bc-verified.msapp` = `v10-1_4` (18 дэлгэцийн `false` нөхцөл, мөрийн дугаарууд таарсан).
**Өөрчлөлт:** 21 дэлгэцийн 28 property. Өөр юу ч өөрчлөөгүй. Бүгд хаалтын тэнцвэр шалгасан; Power Fx compiler-ээр шалгаагүй.

## Ерөнхий дараалал
1. Studio-д `v10-1_4`-ийг нээж **`v10-1_5 TEST`** нэрээр хуулбар хадгална. Production-д шууд бүү хийгээрэй.
2. Доорх хүснэгтийн дарааллаар файл бүрийн **бүх агуулгыг** (Ctrl+A → Ctrl+C) хуулна.
3. Studio-д: зүүн талын **Tree view**-ээс *Дэлгэц* (screen)-ийг, эсвэл *Control*-ийг нэрээр нь хайж сонгоно → дээд талын **Property** жагсаалтаас *Property*-г сонгоно → formula bar дээр **Ctrl+A** → **Ctrl+V**.
   - "Control" нь дэлгэцийн нэртэй ижил бол **дэлгэц өөрөө** (`OnVisible`). `App` бол Tree view-ийн хамгийн дээд **App** объект (`OnStart`).
4. Property бүрийн дараа formula bar-д улаан алдаа гараагүйг шалгана. Бүгдийг оруулсны дараа **App Checker** ажиллуулна.

| # | Файл | Дэлгэц | Control | Property | Засвар |
|---|---|---|---|---|---|
| 1 | `01_App_App_OnStart.txt` | App | (дэлгэц өөрөө) | `OnStart` | 4 |
| 2 | `02_IMPORT_IMPORT_OnVisible.txt` | IMPORT | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 3 | `03_ITEMS_ITEMS_OnVisible.txt` | ITEMS | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 4 | `04_Master-Edit_Master-Edit_OnVisible.txt` | Master Edit | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 5 | `05_ScrAccess_ScrAccess_OnVisible.txt` | ScrAccess | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 6 | `06_ScrAccess_phoneProfileSync_OnSelect.txt` | ScrAccess | phoneProfileSync | `OnSelect` | 4 |
| 7 | `07_ScrAccess_pLogin_OnSelect.txt` | ScrAccess | pLogin | `OnSelect` | 1 |
| 8 | `08_ScrAccess_pgAclWatch_OnTimerEnd.txt` | ScrAccess | pgAclWatch | `OnTimerEnd` | 1 |
| 9 | `09_ScrCameraSearch_ScrCameraSearch_OnVisible.txt` | ScrCameraSearch | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 10 | `10_ScrCombined_ScrCombined_OnVisible.txt` | ScrCombined | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 11 | `11_ScrCountHome_ScrCountHome_OnVisible.txt` | ScrCountHome | (дэлгэц өөрөө) | `OnVisible` | 1+4 |
| 12 | `12_ScrDashboard_ScrDashboard_OnVisible.txt` | ScrDashboard | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 13 | `13_ScrHistory_ScrHistory_OnVisible.txt` | ScrHistory | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 14 | `14_ScrIssueA25Test_ScrIssueA25Test_OnVisible.txt` | ScrIssueA25Test | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 15 | `15_ScrIssueRequests_ScrIssueRequests_OnVisible.txt` | ScrIssueRequests | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 16 | `16_ScrItemPhotos_ScrItemPhotos_OnVisible.txt` | ScrItemPhotos | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 17 | `17_ScrPageAdmin_ScrPageAdmin_OnVisible.txt` | ScrPageAdmin | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 18 | `18_ScrPageMenu_ScrPageMenu_OnVisible.txt` | ScrPageMenu | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 19 | `19_ScrReport1_ScrReport1_OnVisible.txt` | ScrReport1 | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 20 | `20_ScrSync_ScrSync_OnVisible.txt` | ScrSync | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 21 | `21_ScrSync_btnSyncItems_OnSelect.txt` | ScrSync | btnSyncItems | `OnSelect` | 4 |
| 22 | `22_ScrSync_Button18_OnSelect.txt` | ScrSync | Button18 | `OnSelect` | 4 |
| 23 | `23_Screen1_Screen1_OnVisible.txt` | Screen1 | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 24 | `24_scrWarehouses_scrWarehouses_OnVisible.txt` | scrWarehouses | (дэлгэц өөрөө) | `OnVisible` | 1+3 |
| 25 | `25_scrWarehouses_Button1_2_OnSelect.txt` | scrWarehouses | Button1_2 | `OnSelect` | 3 |
| 26 | `26_Бараа-засвар-хийх_Бараа-засвар-хийх_OnVisible.txt` | Бараа засвар хийх | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 27 | `27_Барааны-бүх-үзүүлэлт-харах_Барааны-бүх-үзүүлэлт-харах_OnVisible.txt` | Барааны бүх үзүүлэлт харах | (дэлгэц өөрөө) | `OnVisible` | 1 |
| 28 | `28_нүүр_нүүр_OnVisible.txt` | нүүр | (дэлгэц өөрөө) | `OnVisible` | 1+4 |

## Засвар 1 — Offline эрх (22 property)
- Бүх эрх шалгах блокт `priorState:pgAclState` нэмсэн. Сүлжээ тасрах үед өмнө **баталгаажсан, хугацаа дуусаагүй, ижил хэрэглэгчийн** эрх (`same && valid && priorState="granted"`) хадгалагдана; бусад тохиолдолд өмнөх шигээ эрхийг арилгана.
- **Offline-д нээлттэй** (эрхийг хадгална): `нүүр`, `scrWarehouses`, `ScrAccess`, **`ScrPageMenu`, `ScrCountHome`, `ScrHistory`** (шинээр).
- **Offline-д хаалттай** 15 дэлгэц (IMPORT, ITEMS, Master Edit, ScrCameraSearch, ScrCombined, ScrDashboard, ScrIssueA25Test, ScrIssueRequests, ScrItemPhotos, ScrPageAdmin, ScrReport1, ScrSync, Screen1, Бараа засвар хийх, Барааны бүх үзүүлэлт харах): эрхийг **устгахгүй**, харин "Энэ хуудас офлайн үед хаалттай" гэж мэдэгдээд `Back()`-аар өмнөх дэлгэц рүү буцаана (`App.ActiveScreen` шалгалттай тул өөр дэлгэцээс санамсаргүй буцахгүй).
- Хязгаарлалт: эрх зөвхөн **session дотор** хадгалагдана. Апп-ыг offline үед шинээр нээвэл (cold start) эрх байхгүй — өмнөхтэй адил.
- Хаалттай дэлгэцийн `OnVisible`-ийн үлдсэн хэсэг `Back()`-аас өмнө ажиллаж дуусна (жишээ нь дата татах оролдлого offline үед алдаа өгч болно) — хор хөнөөлгүй.

## Засвар 3 — Тооллогын receipt (2 property, `scrWarehouses`)
- Дискэнд хадгалах алдаатай үед SharePoint руу шууд илгээхийн **өмнө** receipt-ийг тусдаа жижиг файлд (`CountReceiptV1015_<EntraObjectId>`) `SaveData` хийнэ.
- **Хадгалж чадахгүй бол илгээхгүй** (зөвшөөрсөн бодлого): receipt цэвэрлэгдэж, "Тооллогын баримтыг төхөөрөмжид хадгалж чадсангүй тул SharePoint руу илгээгээгүй…" алдаа гарна.
- Амжилттай илгээсний дараа (шинэ хадгалалт ба дахин оролдлого 2 газар) `ClearData` хийнэ.
- `scrWarehouses.OnVisible`-ийн эхэнд: receipt санах ойд байхгүй бол дискнээс сэргээнэ (эзэмшигч таарсан, 1 мөр). Тэгснээр апп дахин нээгдсэн ч **ижил SyncKey**-ээр дахин оролдож, давхар мөр үүсэхгүй.
- Анхаар: сэргээгдсэн receipt байх үед хадгалах товч "дахин хадгалах" горимд, **online** шаардана (одоогийн v369 дүрэм).

## Засвар 4 — OfflineItems кэш (6 property)
- Түлхүүр `"OfflineItems"` → `"OfflineItems_V1015_" & <EntraObjectId>` (Stock/Bins-ийн V30 загвартай ижил). App.OnStart, нүүр, ScrCountHome, ScrAccess.phoneProfileSync, ScrSync (btnSyncItems, Button18).
- `App.OnStart`: шинэ кэш хоосон бол хуучин нийтлэг `"OfflineItems"`-ийг **нэг удаа** уншиж шинэ түлхүүрээр хадгалаад хуучныг `ClearData`. (Барааны мастер өгөгдөл бүх хэрэглэгчид ижил тул шилжүүлэх нь аюулгүй; хуучин нийтлэг файл устна.)

## Заавал хийх тест
1. **Offline эрх:** online нэвтэрнэ → сүлжээ таслана → Цэс → ScrCountHome → тооллого → хадгална (амжилттай байх ёстой).
2. **Offline админ:** offline үед Dashboard/Admin/Sync руу орно → мэдэгдэл гараад буцах ёстой; дараа нь тооллогын дэлгэц хэвээр ажиллах ёстой.
3. **Хугацаа:** туршилтын хэрэглэгчийн `ExpiresAt`-ийг ойрын цаг болгоод offline хүлээнэ → хугацаа дуусмагц эрх арилах ёстой.
4. **Receipt:** дискэнд хадгалах алдааг simulate хийнэ (тест товчоор `varCountDiskSafeV21=false`) → online хадгалах → хариуг тасална (сүлжээ таслах) → апп хаагаад нээнэ → "дахин хадгалах" товч гарч, SharePoint-д **яг 1** мөр үлдэх ёстой.
5. **Receipt хадгалж чадахгүй:** (жишээ нь EntraObjectId хоосон туршилт) → SharePoint-д мөр **үүсэхгүй**, алдааны мэдэгдэл гарах ёстой.
6. **Items кэш:** шинэчилсэн апп-ыг offline анх нээхэд бараа хайлт ажиллах ёстой (хуучин кэш шилжсэн); online синкийн дараа хоёр өөр хэрэглэгч ижил төхөөрөмж дээр өөр өөрийн кэштэй байх ёстой.
