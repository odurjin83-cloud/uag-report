# v10-1_5b — эрх, формат, нэгдсэн тайлан, хурдны хэмжилт

**Суурь:** v10-1_5 (эхлээд v10-1_5/PASTE-ийн 28 файлыг оруулсан байна). Энэ багц 22 property-г өөрчилнө.
`scrWarehouses.OnVisible` ба `Button1_2.OnSelect` нь v10-1_5-ийн засварыг **агуулсан** бүтэн утга — v10-1_5-ынхыг дарж бичнэ.

Studio-д: Tree view → дэлгэц эсвэл control → Property → formula bar Ctrl+A → Ctrl+V. Бүгдийг оруулаад App Checker ажиллуулна.

| # | Файл | Дэлгэц | Control | Property | Засвар |
|---|---|---|---|---|---|
| 1 | `01_ScrCameraSearch_cResults_Items.txt` | ScrCameraSearch | cResults | `Items` | 1 эрх |
| 2 | `02_ScrCameraSearch_cResultRow_Text.txt` | ScrCameraSearch | cResultRow | `Text` | 1 эрх |
| 3 | `03_ScrCameraSearch_cStockInfo_Text.txt` | ScrCameraSearch | cStockInfo | `Text` | 1 эрх |
| 4 | `04_ScrCombined_ScrCombined_OnVisible.txt` | ScrCombined | (дэлгэц өөрөө) | `OnVisible` | 3 тайлан |
| 5 | `05_ScrCombined_pgKpi1_Text.txt` | ScrCombined | pgKpi1 | `Text` | 2 формат |
| 6 | `06_ScrCombined_pgKpi4_Text.txt` | ScrCombined | pgKpi4 | `Text` | 2 формат |
| 7 | `07_ScrCombined_pgPeriod0_OnSelect.txt` | ScrCombined | pgPeriod0 | `OnSelect` | 3 тайлан |
| 8 | `08_ScrCombined_pgPeriod1_OnSelect.txt` | ScrCombined | pgPeriod1 | `OnSelect` | 3 тайлан |
| 9 | `09_ScrCombined_pgPeriod2_OnSelect.txt` | ScrCombined | pgPeriod2 | `OnSelect` | 3 тайлан |
| 10 | `10_ScrItemPhotos_photoLoadV28_OnSelect.txt` | ScrItemPhotos | photoLoadV28 | `OnSelect` | 1 эрх |
| 11 | `11_ScrReport1_rptHeroValue_Text.txt` | ScrReport1 | rptHeroValue | `Text` | 2 формат |
| 12 | `12_ScrReport1_rptCoverageVal_Text.txt` | ScrReport1 | rptCoverageVal | `Text` | 2 формат |
| 13 | `13_ScrReport1_mobRDiff0_Text.txt` | ScrReport1 | mobRDiff0 | `Text` | 2 формат |
| 14 | `14_ScrReport1_mobRDiff0_Tooltip.txt` | ScrReport1 | mobRDiff0 | `Tooltip` | 2 формат |
| 15 | `15_ScrReport1_mobRDiff1_Text.txt` | ScrReport1 | mobRDiff1 | `Text` | 2 формат |
| 16 | `16_ScrReport1_mobRDiff1_Tooltip.txt` | ScrReport1 | mobRDiff1 | `Tooltip` | 2 формат |
| 17 | `17_ScrReport1_mobRDiff2_Text.txt` | ScrReport1 | mobRDiff2 | `Text` | 2 формат |
| 18 | `18_ScrReport1_mobRDiff2_Tooltip.txt` | ScrReport1 | mobRDiff2 | `Tooltip` | 2 формат |
| 19 | `19_scrWarehouses_scrWarehouses_OnVisible.txt` | scrWarehouses | (дэлгэц өөрөө) | `OnVisible` | 4 хурд (+v10-1_5 засвар агуулсан) |
| 20 | `20_scrWarehouses_Label8_22_Text.txt` | scrWarehouses | Label8_22 | `Text` | 2 формат |
| 21 | `21_scrWarehouses_Label18_1_Text.txt` | scrWarehouses | Label18_1 | `Text` | 2 формат |
| 22 | `22_scrWarehouses_Button1_2_OnSelect.txt` | scrWarehouses | Button1_2 | `OnSelect` | 4 хурд (+v10-1_5 засвар агуулсан) |

## 1. Агуулахын эрхийн алдагдал (4 property)
- `ScrCameraSearch` (cResults.Items, cResultRow.Text, cStockInfo.Text) ба `ScrItemPhotos.photoLoadV28` — `colOfflineStock`-ийг барааны кодоос гадна **эрхтэй агуулахаар** шүүнэ (нийлбэр ба "Агуулах:" жагсаалт хоёулаа).
- Энэ нь дэлгэцийн хамгаалалт. **Flow-оос эрхгүй мөр огт ирэхгүй** байх үндсэн засвар: `v10-1_5/FLOW_REQUIREMENTS_fix2.md`.
- Тест: Одончимэгээр 0500010005 → камер, хайлт, дэлгэрэнгүй гурвуулаа **17**, зөвхөн CAMP.

## 2. Формат (10 property)
- Хувь: `rptHeroValue`, `rptCoverageVal`, `pgKpi1`, `pgKpi4` — `Text(x,"0.0%")` → `Text(100*x,"0.0") & "%"` (Power Fx-ийн `%` 100-аар үржүүлдэггүй). Тест: 11/42 → утас, таблет хоёуланд **26.2%**.
- Сөрөг зөрүү: `mobRDiff0–2` (Text, Tooltip) — `"+#,##0.##;-#,##0.##;0"` (Power Fx `;` хэсэг дэмждэггүй) → тэмдэг + бүхэл/бутархай. Тест: −249 → **-249**, +10 → **+10**, 0 → **0**.
- `scrWarehouses.Label8_22`, `Label18_1` — `"0.###"` бүхэл тоонд `0.` гаргадаг → бүхэл бол `"0"`.

## 3. Нэгдсэн тайлан (4 property)
- Тайлан бүрдүүлэх бүрт эхлээд `Refresh(InventoryCount)`.
- Админ/тест горимд ДИАГ мэдэгдэл **Одын 2026-11-20-ны CAMP-ийн 40 хяналтын ID**-аар (TME-v36-device-check.md, PLE110 хүснэгт) тулгана: `уншсан N/40`, `тайланд үлдсэн M/40`, **УНШААГҮЙ** ID-ууд, **ШҮҮЛТЭД ХАСАГДСАН** ID-ууд, мөн нийт уншсан/тайланд орсон мөрийн тоо.
- Тайлбар: УНШААГҮЙ жагсаалт хоосон биш бол SharePoint-оос унших хүсэлт/огнооны шүүлтэд асуудал. ШҮҮЛТЭД ХАСАГДСАН хоосон биш бол аппын ARCHIVED/эрхийн шүүлтэд асуудал.
- ⚠ Тайлангийн хугацаа **2026-11-20-ыг агуулсан** байх ёстой (11-р сарын "Сар" сонголт). Өөр сард шалгавал 40 бүгд "уншаагүй" гэж гарах нь хүлээгдэх үр дүн — тестийн алдаа биш.
- ДИАГ нь зөвхөн тестийн хэрэгсэл; production-оос өмнө хасна.
- Тайлан бүрэн ачаалагдаагүй үед KPI-ууд `pgReportReady`-гээр аль хэдийн хаалттай.

## 4. Хадгалалтын хурдны хэмжилт (2 property)
- `Button1_2.OnSelect`: Хадгалах дарсан мөч (T0), төхөөрөмжид бичигдсэн мөч (T1), томьёо дууссан мөчийг `colPerfV1015`-д (`LocalMs`, `TotalMs`, `HistoryRows`) хадгалж, `SaveData("PerfV1015_<ObjectId>")` хийнэ.
- 20 хадгалалт тутамд мэдэгдэл: медиан, хамгийн удаан, локал бичилт, түүхийн мөрийн тоо.
- `scrWarehouses.OnVisible`-ийн эхэнд `Set(varPerfDiagV1015,true)` — **зөвхөн TEST**. Production-д `false` болгоно.
- `TotalMs` нь томьёо дуусах хүртэл; дэлгэц дахин зурагдах хугацаа орохгүй. Дэлгэцийн бичлэгийн хугацаатай харьцуулбал удаашрал томьёонд уу, зураглалд уу гэдэг тодорно.

## Давхацсан хоёр property-д заавал давтах v10-1_5 шалгалт
`scrWarehouses.OnVisible`, `Button1_2.OnSelect` дээр 5b-г тавьсны дараа:
1. Online нэвтэрнэ → сүлжээ таслана → Цэс → ScrCountHome → тооллого → хадгална (амжилттай байх ёстой).
2. Дискэнд хадгалах алдааг simulate хийж online хадгална → хариуг тасална → апп хаагаад нээнэ → "дахин хадгалах" → SharePoint-д **яг 1** мөр.

## Хурдны үр дүнг тайлагнах
- Мэдэгдлийн медиан/максимум нь удаашралыг олоход; v36-тай харьцуулахдаа Samsung, PLE110 тус бүрийн **түүхий** `colPerfV1015` (`PerfV1015_<ObjectId>`)-ээс P95 гаргана.
- `LocalMs` нь зөвхөн `SaveData` амжилттай үед бүртгэгдэнэ (алдаатай бол мөр бүртгэгдэхгүй).
- `TotalMs` = томьёо дууссан; "дараагийн код оруулахад бэлэн" гэсэн мөчийг дэлгэцийн бичлэгээр тулгана.
