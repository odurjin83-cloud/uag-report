# Paste set v3.6.8 (on top of the Studio-verified v3.6.7 .msapp)

Base: `TME ... Mobile 6 Tablet A25 v3.6.7.msapp` (Studio-verified, not published).
Property-level 3-way compare (v3.6.6 / Studio v3.6.7 / this branch):
- Studio v3.6.7 changed only `ScrIssueA25Test` (A25OK, cartCheckBack, cartReceiptTimer, cartStartNew). Copy kept in `../base_v3.6.7_studio/`.
- This paste set changes only the 10 properties below. No overlap -> no merge conflict.
- App / ScrSync / scrWarehouses / нүүр in Studio v3.6.7 are identical to v3.6.6 (line endings only).

Open the Studio v3.6.7 file, save a copy as v3.6.8 TEST, then replace these 10 properties in full:
01 App.OnStart · 02 scrWarehouses.Button1_2.DisplayMode · 03 Button1_2.OnSelect · 04 Label8_22.Text ·
05 BarcodeReader3.OnScan · 06 txtSearch_4.OnChange · 07 galSuggestions_3.OnSelect ·
08 ScrSync.tmrStockSync.Start · 09 ScrSync.tmrItemSync.Start · 10 нүүр.hOverlaySearchRow.OnSelect
Do NOT touch ScrIssueA25Test.
