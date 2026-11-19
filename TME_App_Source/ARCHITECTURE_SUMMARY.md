# TME Inventory App (Mobile/Tablet A25 v3.6.6) — Architecture Summary

_Auto-generated from the .msapp package for audit purposes. The original .msapp was not modified._

## 1. Package structure

| Path | Contents |
|---|---|
| `raw/Src/*.pa.yaml` | Readable Power Fx source: App + one file per screen |
| `raw/Controls/*.json` | Compiled control tree (binary-equivalent of Src) |
| `raw/References/DataSources.json` | Data source & connector definitions |
| `raw/References/Themes.json, Templates.json` | Themes / control templates |
| `raw/Assets, raw/Resources` | Images and media |
| `raw/Properties.json, Header.json` | App settings, doc version |
| `raw/AppCheckerResult.sarif` | Built-in App Checker results |

- Doc version: `1.349`, min version `1.349`
- Data row limit (`DefaultConnectedDataSourceMaxGetRowsCount`): **5000**
- Total formulas: **28066**, total controls: **1610**

## 2. Screens and components

No custom components (component library / `ComponentDefinitions`) are defined in this app.

| Screen | Source file | Controls | Formulas | Patch | Collect | ClearCollect | ForAll | Concurrent | Filter | LookUp |
|---|---|---|---|---|---|---|---|---|---|---|
| IMPORT | `IMPORT.pa.yaml` | 3 | 49 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| ITEMS | `ITEMS.pa.yaml` | 55 | 796 | 0 | 0 | 0 | 0 | 0 | 8 | 13 |
| Master Edit | `Master Edit.pa.yaml` | 4 | 56 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| ScrAccess | `ScrAccess.pa.yaml` | 118 | 2225 | 10 | 28 | 26 | 15 | 1 | 26 | 29 |
| ScrCameraSearch | `ScrCameraSearch.pa.yaml` | 27 | 527 | 0 | 1 | 1 | 0 | 0 | 6 | 3 |
| ScrCombined | `ScrCombined.pa.yaml` | 34 | 489 | 0 | 16 | 4 | 8 | 0 | 38 | 6 |
| ScrCountHome | `ScrCountHome.pa.yaml` | 24 | 494 | 7 | 2 | 18 | 11 | 1 | 18 | 18 |
| ScrDashboard | `ScrDashboard.pa.yaml` | 258 | 4367 | 1 | 1 | 15 | 4 | 0 | 19 | 7 |
| ScrHistory | `ScrHistory.pa.yaml` | 58 | 1135 | 16 | 4 | 16 | 8 | 0 | 30 | 26 |
| ScrIssueA25Test | `ScrIssueA25Test.pa.yaml` | 108 | 1722 | 4 | 5 | 8 | 3 | 0 | 79 | 17 |
| ScrItemPhotos | `ScrItemPhotos.pa.yaml` | 31 | 604 | 0 | 0 | 1 | 1 | 0 | 2 | 4 |
| ScrPageAdmin | `ScrPageAdmin.pa.yaml` | 44 | 746 | 1 | 7 | 17 | 1 | 0 | 15 | 14 |
| ScrPageMenu | `ScrPageMenu.pa.yaml` | 14 | 235 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| ScrReport1 | `ScrReport1.pa.yaml` | 205 | 3752 | 4 | 6 | 22 | 15 | 0 | 28 | 5 |
| ScrSync | `ScrSync.pa.yaml` | 17 | 341 | 5 | 3 | 18 | 12 | 0 | 8 | 4 |
| Screen1 | `Screen1.pa.yaml` | 142 | 2611 | 1 | 7 | 13 | 6 | 0 | 29 | 23 |
| scrWarehouses | `scrWarehouses.pa.yaml` | 95 | 1743 | 2 | 1 | 4 | 3 | 0 | 14 | 11 |
| Бараа засвар хийх | `Бараа засвар хийх.pa.yaml` | 58 | 986 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах.pa.yaml` | 79 | 1360 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| нүүр | `нүүр.pa.yaml` | 236 | 3823 | 14 | 14 | 20 | 13 | 1 | 59 | 30 |
| **App** (OnStart etc.) | `App.pa.yaml` | – | – | 2 | 5 | 33 | 17 | 1 | 13 | 3 |

**Control types used:**

Label@2.5.1 ×706, Classic/Button@2.2.0 ×452, GroupContainer@1.5.0 ×192, Image@2.2.3 ×55, Classic/TextInput@2.3.2 ×47, Classic/Icon@2.5.0 ×36, Gallery@2.15.0 ×33, Rectangle@2.3.0 ×32, TypedDataCard@1.0.7 ×23, Classic/DatePicker@2.6.0 ×8, Timer@2.1.0 ×7, AddMedia@2.2.1 ×6, BarcodeReader@1.0.25 ×4, Arrow@2.3.0 ×2, Classic/CheckBox@2.1.0 ×2, Form@2.4.4 ×2, Classic/Toggle@2.1.0 ×2, Circle@2.3.0 ×1

## 3. Data sources and connectors

| Name | Connector | Kind | Dataset / site |
|---|---|---|---|
| PowerAppV2->Getrecord(V3) | Power Automate flow | ServiceInfo |  |
| PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo... | Power Automate flow | ServiceInfo |  |
| PA_GetAllItemsOffline | Power Automate flow | ServiceInfo |  |
| PA_GetAllStockOffline | Power Automate flow | ServiceInfo |  |
| PA_GetAllBinsOffline | Power Automate flow | ServiceInfo |  |
| Office365Outlook | Office 365 Outlook | ServiceInfo |  |
| PA_ExportInventoryCSV | Power Automate flow | ServiceInfo |  |
| PA_GetStockFromExcel | Power Automate flow | ServiceInfo |  |
| PA_GetItemsSnapshot | Power Automate flow | ServiceInfo |  |
| items (v2.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| CustomGallerySample | StaticDataSourceInfo | StaticDataSourceInfo |  |
| itemLedgerEntries (microsoft/analytics/v1.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| InventoryCount | SharePoint | ConnectedDataSourceInfo | https://tsetsensmining.sharepoint.com/sites/TME_Finance |
| ComboBoxSample | StaticDataSourceInfo | StaticDataSourceInfo |  |
| PieChartSample | StaticDataSourceInfo | StaticDataSourceInfo |  |
| LegendSample | StaticDataSourceInfo | StaticDataSourceInfo |  |
| ColumnChartSample | StaticDataSourceInfo | StaticDataSourceInfo |  |
| fixedAssets (v2.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| fixedAssetLocations (v2.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| locations (v2.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| bins (microsoft/analytics/v1.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| warehouseEntries (microsoft/analytics/v1.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| itemLedgerEntries (v2.0) | Business Central | ConnectedDataSourceInfo | PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0 |
| AssetCounts | SharePoint | ConnectedDataSourceInfo | https://tsetsensmining.sharepoint.com/sites/TME_Finance |
| AssetUserAccess | SharePoint | ConnectedDataSourceInfo | https://tsetsensmining.sharepoint.com/sites/TME_Finance |
| TMEIssueA25Test | Power Automate flow | ServiceInfo |  |

## 4. Business Central integration

BC environment/company: `PRODUCTION,5150f047-26b6-f011-bbd1-000d3aa334f0` via connector `shared_dynamicssmbsaas`.

BC tables used: `items (v2.0)`, `itemLedgerEntries (microsoft/analytics/v1.0)`, `fixedAssets (v2.0)`, `fixedAssetLocations (v2.0)`, `locations (v2.0)`, `bins (microsoft/analytics/v1.0)`, `warehouseEntries (microsoft/analytics/v1.0)`, `itemLedgerEntries (v2.0)`

Additionally, Power Automate flows (likely also reading BC/Excel) are called: `PowerAppV2->Getrecord(V3)`, `PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo...`, `PA_GetAllItemsOffline`, `PA_GetAllStockOffline`, `PA_GetAllBinsOffline`, `PA_ExportInventoryCSV`, `PA_GetStockFromExcel`, `PA_GetItemsSnapshot`, `TMEIssueA25Test`

| Screen | Control/Property | BC tables | Functions |
|---|---|---|---|
| ITEMS | `ITEMS/BarcodeReader1.OnScan` | items (v2.0), itemLedgerEntries (microsoft/analytics/v1.0) | LookUp, First |
| ITEMS | `ITEMS/galSuggestions.Items` | items (v2.0) | Filter |
| ITEMS | `ITEMS/galSuggestions.OnSelect` | itemLedgerEntries (microsoft/analytics/v1.0) | LookUp |
| ITEMS | `ITEMS/Label8_5.Text` | items (v2.0) | LookUp |
| ITEMS | `ITEMS/txtSearch.OnChange` | items (v2.0), itemLedgerEntries (microsoft/analytics/v1.0) | LookUp |
| ITEMS | `ITEMS/Label8_3.Text` | itemLedgerEntries (microsoft/analytics/v1.0) | LookUp |
| ITEMS | `ITEMS/Label8_4.Text` | itemLedgerEntries (microsoft/analytics/v1.0) | LookUp |
| ITEMS | `ITEMS/Label18.Color` | itemLedgerEntries (microsoft/analytics/v1.0) | Filter, LookUp, Sum |
| ITEMS | `ITEMS/Label18.Fill` | itemLedgerEntries (microsoft/analytics/v1.0) | Filter, LookUp, Sum |
| ITEMS | `ITEMS/Label18.Text` | itemLedgerEntries (microsoft/analytics/v1.0) | Filter, LookUp, Sum, CountRows |
| ITEMS | `ITEMS/Label8_23.Text` | itemLedgerEntries (microsoft/analytics/v1.0) | LookUp |
| ScrAccess | `ScrAccess.OnVisible` | locations (v2.0) | Collect, ClearCollect, ForAll, Filter, LookUp, Refresh |
| ScrAccess | `ScrAccess/pReloadWarehouses.OnSelect` | locations (v2.0) | Collect, ClearCollect, ForAll, Filter, LookUp |
| ScrDashboard | `ScrDashboard/dReadBC.OnSelect` | itemLedgerEntries (microsoft/analytics/v1.0) | ClearCollect, ForAll, Filter, CountRows, Sort |
| ScrPageAdmin | `ScrPageAdmin.OnVisible` | locations (v2.0) | ClearCollect, Filter, LookUp, Refresh |
| Screen1 | `Screen1.OnVisible` | locations (v2.0) | ClearCollect, LookUp, Refresh, First |
| Screen1 | `Screen1/wReadBC.OnSelect` | itemLedgerEntries (microsoft/analytics/v1.0), warehouseEntries (microsoft/analytics/v1.0) | ClearCollect, Filter, CountRows |
| Бараа засвар хийх | `Бараа засвар хийх/Label8_7.Text` | itemLedgerEntries (microsoft/analytics/v1.0) | LookUp |
| Бараа засвар хийх | `Бараа засвар хийх/txtSearch_1.OnChange` | items (v2.0) | LookUp |
| Бараа засвар хийх | `Бараа засвар хийх/Label8_10.Text` | itemLedgerEntries (microsoft/analytics/v1.0) | LookUp |
| Бараа засвар хийх | `Бараа засвар хийх/Form1.DataSource` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1.Item` | items (v2.0) | LookUp |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/No._DataCard1.DisplayName` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/No._DataCard1.MaxLength` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Display Name_DataCard1.DisplayName` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Display Name_DataCard1.MaxLength` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Display Name 2_DataCard1.DisplayName` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Display Name 2_DataCard1.MaxLength` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Type_DataCard1.DisplayName` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Type_DataCard1.MaxLength` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Item Category Code_DataCard1.DisplayName` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Item Category Code_DataCard1.MaxLength` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Blocked_DataCard1.DisplayName` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/GTIN_DataCard1.DisplayName` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/GTIN_DataCard1.MaxLength` | items (v2.0) |  |
| Бараа засвар хийх | `Бараа засвар хийх/Form1/Inventory_DataCard1.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1.DataSource` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1.Item` | items (v2.0) | First |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/General Product Posting Group Code_DataCard1.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/General Product Posting Group Code_DataCard1.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/General Product Posting Group Id_DataCard1.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Base Unit Of Measure Code_DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Base Unit Of Measure Code_DataCard2.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Inventory Posting Group Code_DataCard1.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Inventory Posting Group Code_DataCard1.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Tax Group Code_DataCard1.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Tax Group Code_DataCard1.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Unit Cost_DataCard1.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Unit Price_DataCard1.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/No._DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/No._DataCard2.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Display Name_DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Display Name_DataCard2.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Display Name 2_DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Display Name 2_DataCard2.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Type_DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Type_DataCard2.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Item Category Code_DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Item Category Code_DataCard2.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Blocked_DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/GTIN_DataCard2.DisplayName` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/GTIN_DataCard2.MaxLength` | items (v2.0) |  |
| Барааны бүх үзүүлэлт харах | `Барааны бүх үзүүлэлт харах/EditForm1/Inventory_DataCard2.DisplayName` | items (v2.0) |  |

### Power Automate flow calls

| Flow | Screen | Control.Property |
|---|---|---|
| PA_ExportInventoryCSV | ScrAccess | `ScrAccess/pExportModal/pExportSend.OnSelect` |
| PA_ExportInventoryCSV | ScrDashboard | `ScrDashboard/dExportModal/dExportSend.OnSelect` |
| PA_ExportInventoryCSV | ScrDashboard | `ScrDashboard/dPdfTimerV23.OnTimerEnd` |
| PA_ExportInventoryCSV | ScrHistory | `ScrHistory/Icon2.OnSelect` |
| PA_ExportInventoryCSV | ScrReport1 | `ScrReport1/rptExportModal/rptExportConfirm.OnSelect` |
| PA_ExportInventoryCSV | ScrReport1 | `ScrReport1/rptPdfTimer.OnTimerEnd` |
| PA_ExportInventoryCSV | Screen1 | `Screen1/wExportModal/wExportSend.OnSelect` |
| PA_GetAllBinsOffline | App | `App.OnStart` |
| PA_GetAllBinsOffline | ScrAccess | `ScrAccess/phoneProfileSync.OnSelect` |
| PA_GetAllBinsOffline | ScrCountHome | `ScrCountHome.OnVisible` |
| PA_GetAllBinsOffline | ScrSync | `ScrSync/btnSyncBins.OnSelect` |
| PA_GetAllBinsOffline | нүүр | `нүүр.OnVisible` |
| PA_GetAllStockOffline | ScrSync | `ScrSync/tmrItemSync.OnTimerEnd` |
| PA_GetAllStockOffline | ScrSync | `ScrSync/tmrStockSync.OnTimerEnd` |
| PA_GetItemsSnapshot | App | `App.OnStart` |
| PA_GetItemsSnapshot | ScrAccess | `ScrAccess/phoneProfileSync.OnSelect` |
| PA_GetItemsSnapshot | ScrCountHome | `ScrCountHome.OnVisible` |
| PA_GetItemsSnapshot | ScrSync | `ScrSync/btnSyncItems.OnSelect` |
| PA_GetItemsSnapshot | нүүр | `нүүр.OnVisible` |
| PA_GetStockFromExcel | App | `App.OnStart` |
| PA_GetStockFromExcel | ScrAccess | `ScrAccess/phoneProfileSync.OnSelect` |
| PA_GetStockFromExcel | ScrCountHome | `ScrCountHome.OnVisible` |
| PA_GetStockFromExcel | ScrSync | `ScrSync/btnSyncStock.OnSelect` |
| PA_GetStockFromExcel | нүүр | `нүүр.OnVisible` |
| PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo... | ITEMS | `ITEMS/galSuggestions.OnSelect` |
| PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo... | ScrCameraSearch | `ScrCameraSearch/cLoad.OnSelect` |
| PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo... | ScrItemPhotos | `ScrItemPhotos/photoLoadV28.OnSelect` |
| PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo... | Screen1 | `Screen1/wDetail/wLoadPhoto.OnSelect` |
| PowerAppV2->Getrecord(V3) | ITEMS | `ITEMS/Icon13.OnSelect` |
| PowerAppV2->Getrecord(V3) | ScrCameraSearch | `ScrCameraSearch/cPhotoNotice.OnSelect` |
| PowerAppV2->Getrecord(V3) | ScrItemPhotos | `ScrItemPhotos/photoConfirmYesV28.OnSelect` |
| PowerAppV2->Getrecord(V3) | scrWarehouses | `scrWarehouses/Icon13_1.OnSelect` |
| TMEIssueA25Test | ScrIssueA25Test | `ScrIssueA25Test/A25OK.OnSelect` |
| TMEIssueA25Test | ScrIssueA25Test | `ScrIssueA25Test/A25Search.OnSelect` |
| TMEIssueA25Test | ScrIssueA25Test | `ScrIssueA25Test/issueProceed.OnSelect` |
| TMEIssueA25Test | ScrPageAdmin | `ScrPageAdmin/pgNew.OnSelect` |
| TMEIssueA25Test | ScrPageAdmin | `ScrPageAdmin/pgUser0.OnSelect` |
| TMEIssueA25Test | ScrPageAdmin | `ScrPageAdmin/pgUser1.OnSelect` |
| TMEIssueA25Test | ScrPageAdmin | `ScrPageAdmin/pgUser2.OnSelect` |
| TMEIssueA25Test | ScrPageAdmin | `ScrPageAdmin/pgUser3.OnSelect` |
| TMEIssueA25Test | ScrPageAdmin | `ScrPageAdmin/pgUser4.OnSelect` |

## 5. Key function usage (Patch, Collect, ClearCollect, ForAll, Concurrent, Filter, LookUp)

| Function | Occurrences |
|---|---|
| Patch | 67 |
| Collect | 100 |
| ClearCollect | 216 |
| ForAll | 117 |
| Concurrent | 4 |
| Filter | 392 |
| LookUp | 222 |

Full per-formula list: `formulas_key_functions.csv`. All formulas: `formulas_all.csv` and `formulas_by_screen/*.md`.

## 6. State: collections, variables, timers, navigation

**Collections** (ClearCollect/Collect target → count): `colPAudit`(21), `colCountDiskV21`(17), `colPPrefs`(16), `colHistoryMergeV16`(12), `colOfflineInventory`(10), `colDJoinV17`(10), `pgRights`(9), `colOfflineStock`(8), `pgFullDays`(8), `pgRaw`(8), `pgWh`(8), `colOfflineItems`(6), `colOfflineBins`(6), `colDStockBaseV17`(6), `colRestoreCloudV16`(6), `colRestoreRowsV16`(6), `colHistoryMergedV16`(6), `colPLocationCodes`(6), `colToSync`(5), `a25Cart`(5), `pgAssigned`(5), `colAutoItemsV16`(4), `colAutoStockV16`(4), `colAutoBinsV16`(4), `colHomeLatest`(4), `colHomeMonths`(4), `pgRows`(4), `colReportWarehouses`(4), `colWDrafts`(4), `colItemSyncInfo`(3), `colPSelected`(3), `colHistoryActionResultV22`(3), `colStockSyncInfo`(3), `colWMinimums`(3), `colCountLocationsV19`(3), `colNewItemsSnapshot`(2), `colNewStockSnapshot`(2), `colPLocationMaster`(2), `colPLocations`(2), `colCPhotos`(2), `colDMinimums`(2), `colDValueHistory`(2), `colHistoryNoteBeforeV22`(2), `colHistoryDeleteV16`(2), `a25Matches`(2), `issueRecent`(2), `a25Stock`(2), `a25NormLines`(2), `colRptWarehouseCodes`(2), `colRItemCandidatesV16`(2), `colRptCategoryTop`(2), `colStockEntries`(2), `colStockDelta`(2), `colWLocationCodes`(2), `colLegacyInventory`(1), `colPreviousCountV21`(1), `colStockMasterCheck`(1), `colStockMismatch`(1), `colPScopedStock`(1), `colPScopedItems`(1), `colPScopedBins`(1), `colDLatest`(1), `colDValid`(1), `colDVariance`(1), `colDReasons`(1), `colDStock`(1), `colDWarehouses`(1), `colDUsage`(1), `colDTop`(1), `colDMonths`(1), `colDTrend`(1), `colDLedgerRaw`(1), `colDLedger`(1), `colHistoryActionV22`(1), `colPhotoLocationsV28`(1), `pgLocations`(1), `pgBCMatches`(1), `colRptSearchItemsV16`(1), `colRptSource`(1), `colRptWarehouses`(1), `colRRaw`(1), `colRLatest`(1), `colRStock`(1), `colRItems`(1), `colRptVariance`(1), `colRptCategoryRaw`(1), `colRptCategories`(1), `colRptPeople`(1), `colNewBinsV16`(1), `colBCStockCheck`(1), `colWRestoreMinimums`(1), `colWRestoreDrafts`(1), `colWLocationMaster`(1), `colWStock`(1), `colWLocations`(1), `colWLedger`(1), `colWLiveBins`(1), `colPAuditDraftKeys`(1)

**Global variables** set via `Set()`: 270 distinct. Most used: `pgAccess`(60), `varPView`(36), `varCountStorageError`(27), `varRptDetail`(22), `varPAuditSaveError`(21), `varRptSelectedItem`(20), `varRptSelectedLocation`(20), `varOpeningBalance`(19), `pgPane`(18), `varLocationCode`(16), `varCountUploadQueue`(16), `varReportTab`(16), `varCountRetryAtV27`(15), `pgPerson`(15), `varWView`(15), `varShowWarehouseList`(14), `varHomeLanguage`(14), `issueLookupMessage`(14), `varItem`(13), `issueSubmissionMessage`(13), `pgBusy`(13), `varCountMenuV21`(12), `varLocationName`(12), `varAutoItemsError`(12), `varAutoStockError`(12), `varAutoBinsError`(12), `varHistoryLoading`(12), `varHistoryCloudError`(12), `varHistoryCacheError`(12), `varPOldLanguage`(12), `varPhotoMessageV28`(12), `varRptExportDialog`(12), `varCountSyncBusy`(11), `varNewPicture`(11), `varDStockReadyV17`(11), `pgRank`(11), `varDExport`(11), `pgReadOk`(11), `varRptSettings`(11), `varCountCacheReady`(10)

**Timers (background jobs):** `ScrCountHome/uploadQueueV16_10`, `ScrDashboard/dPdfTimerV23`, `ScrHistory/uploadQueueV16_12`, `ScrReport1/rptPdfTimer`, `ScrSync/tmrStockSync`, `ScrSync/tmrItemSync`, `нүүр/uploadQueueV16_11`

**Navigation map:**

| From | To | Count |
|---|---|---|
| IMPORT | ScrAccess | 1 |
| IMPORT | нүүр | 1 |
| ITEMS | ScrAccess | 1 |
| ITEMS | scrWarehouses | 1 |
| ITEMS | нүүр | 2 |
| Master Edit | ScrAccess | 1 |
| Master Edit | Бараа засвар хийх | 1 |
| Master Edit | нүүр | 1 |
| ScrAccess | ScrDashboard | 1 |
| ScrAccess | ScrPageAdmin | 1 |
| ScrAccess | ScrPageMenu | 1 |
| ScrAccess | Screen1 | 1 |
| ScrAccess | scrWarehouses | 1 |
| ScrAccess | нүүр | 5 |
| ScrCameraSearch | ScrAccess | 1 |
| ScrCameraSearch | нүүр | 1 |
| ScrCombined | ScrAccess | 1 |
| ScrCombined | ScrCombined | 1 |
| ScrCombined | ScrCountHome | 1 |
| ScrCombined | ScrIssueA25Test | 1 |
| ScrCombined | ScrPageAdmin | 1 |
| ScrCombined | Screen1 | 1 |
| ScrCombined | нүүр | 1 |
| ScrCountHome | IMPORT | 1 |
| ScrCountHome | ITEMS | 1 |
| ScrCountHome | Master Edit | 1 |
| ScrCountHome | ScrAccess | 1 |
| ScrCountHome | ScrHistory | 1 |
| ScrCountHome | ScrItemPhotos | 1 |
| ScrCountHome | ScrReport1 | 1 |
| ScrCountHome | scrWarehouses | 1 |
| ScrCountHome | Бараа засвар хийх | 1 |
| ScrCountHome | нүүр | 1 |
| ScrDashboard | ScrAccess | 4 |
| ScrDashboard | ScrCameraSearch | 1 |
| ScrDashboard | ScrCountHome | 1 |
| ScrDashboard | Screen1 | 5 |
| ScrDashboard | scrWarehouses | 3 |
| ScrDashboard | нүүр | 4 |
| ScrHistory | ScrAccess | 1 |
| ScrHistory | scrWarehouses | 1 |
| ScrHistory | нүүр | 1 |
| ScrIssueA25Test | ScrAccess | 1 |
| ScrIssueA25Test | ScrPageMenu | 1 |
| ScrItemPhotos | ScrAccess | 1 |
| ScrItemPhotos | ScrCountHome | 1 |
| ScrItemPhotos | scrWarehouses | 1 |
| ScrPageAdmin | ScrAccess | 1 |
| ScrPageAdmin | ScrCombined | 1 |
| ScrPageAdmin | ScrCountHome | 1 |
| ScrPageAdmin | ScrIssueA25Test | 1 |
| ScrPageAdmin | ScrPageAdmin | 1 |
| ScrPageAdmin | Screen1 | 1 |
| ScrPageAdmin | нүүр | 1 |
| ScrPageMenu | Master Edit | 1 |
| ScrPageMenu | ScrCameraSearch | 1 |
| ScrPageMenu | ScrCombined | 1 |
| ScrPageMenu | ScrCountHome | 1 |
| ScrPageMenu | ScrDashboard | 1 |
| ScrPageMenu | ScrHistory | 1 |
| ScrPageMenu | ScrIssueA25Test | 1 |
| ScrPageMenu | ScrPageAdmin | 1 |
| ScrPageMenu | ScrReport1 | 1 |
| ScrPageMenu | ScrSync | 1 |
| ScrPageMenu | Screen1 | 1 |
| ScrPageMenu | нүүр | 1 |
| ScrReport1 | ScrAccess | 1 |
| ScrReport1 | ScrHistory | 4 |
| ScrReport1 | scrWarehouses | 3 |
| ScrReport1 | нүүр | 1 |
| ScrSync | ScrAccess | 1 |
| ScrSync | нүүр | 1 |
| Screen1 | ScrAccess | 1 |
| Screen1 | нүүр | 1 |
| scrWarehouses | ScrAccess | 6 |
| scrWarehouses | ScrCountHome | 1 |
| scrWarehouses | ScrHistory | 3 |
| scrWarehouses | ScrItemPhotos | 2 |
| scrWarehouses | ScrReport1 | 3 |
| scrWarehouses | Screen1 | 1 |
| scrWarehouses | Бараа засвар хийх | 1 |
| scrWarehouses | нүүр | 1 |
| Бараа засвар хийх | ScrAccess | 1 |
| Бараа засвар хийх | ScrCountHome | 2 |
| Барааны бүх үзүүлэлт харах | ScrAccess | 1 |
| Барааны бүх үзүүлэлт харах | нүүр | 1 |
| нүүр | IMPORT | 2 |
| нүүр | ITEMS | 1 |
| нүүр | Master Edit | 2 |
| нүүр | ScrAccess | 4 |
| нүүр | ScrCameraSearch | 5 |
| нүүр | ScrCombined | 1 |
| нүүр | ScrCountHome | 7 |
| нүүр | ScrDashboard | 2 |
| нүүр | ScrHistory | 2 |
| нүүр | ScrIssueA25Test | 5 |
| нүүр | ScrPageAdmin | 1 |
| нүүр | ScrReport1 | 2 |
| нүүр | Screen1 | 6 |
| нүүр | scrWarehouses | 6 |
| нүүр | Бараа засвар хийх | 2 |

## 7. Architecture overview

```
          ┌──────────────── Power Apps canvas (phone/tablet) ────────────────┐
 User ──▶ │ Screens (UI) ─▶ Power Fx ─▶ local collections (offline cache,   │
          │                               SaveData/LoadData)                  │
          └───────┬──────────────────────┬──────────────────────┬─────────────┘
                  │ direct (read)        │ Patch (write)        │ .Run()
                  ▼                      ▼                      ▼
     Business Central (PRODUCTION)   SharePoint (TME_Finance)   Power Automate flows
     items, itemLedgerEntries,       InventoryCount,            PA_GetAllItemsOffline,
     warehouseEntries, bins,         AssetCounts,               PA_GetAllStockOffline, ...
     locations, fixedAssets...       AssetUserAccess (roles)    Office365Outlook (mail)
```

## 8. Pre-flagged audit focus areas

Findings from an earlier manual review (verify in this version):
1. **Stock balance via `LookUp(itemLedgerEntries,...).Quantity`** (ITEMS screen) returns a single ledger entry, not the balance; should be `Sum(Filter(...), Quantity)` scoped by location. Can cause stock mismatches.
2. **Count totals not filtered by location** (`Sum(Filter(InventoryCount, ItemNo=...))`) vs. BC `items.inventory` (all locations).
3. **Delegation**: `Sum`/`CountRows` on SharePoint and `ClearCollect` of whole BC ledger tables are capped at the data row limit (2000/5000).
4. **`ForAll` containing `Patch`/`Remove`** in upload timers; upload queue timer duplicated on 3 screens (home, ScrCountHome, ScrHistory).
5. **Hard-coded admin e-mail bypass** in Visible/permission formulas; test screen `ScrIssueA25Test` present.
6. App Checker: unused variables/media, `txtSearch.DelayOutput` off.
