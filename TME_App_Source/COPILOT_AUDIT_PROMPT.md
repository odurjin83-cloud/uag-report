# Copilot аудитын заавар / Audit prompt

Upload `ARCHITECTURE_SUMMARY.md`, `formulas_key_functions.csv` and the `raw/Src/*.pa.yaml` files (or the `formulas_by_screen/*.md` for the screens you are auditing), then paste:

> You are auditing a Power Apps canvas app (TME inventory counting, Business Central + SharePoint + Power Automate).
> Using the attached source, review for:
> 1. Correctness of stock balance / count variance logic (BC itemLedgerEntries vs SharePoint InventoryCount, location scoping).
> 2. Delegation and data row limit risks (Filter/LookUp/Sum/CountRows/ClearCollect on BC and SharePoint).
> 3. Patch / ForAll / Collect write logic: duplicates, partial failures, offline queue and timers.
> 4. Security and access control (AssetUserAccess roles, hard-coded users, Visible-only protection).
> 5. Performance (OnStart, OnVisible, Concurrent use, screen size).
> 6. Dead code: unused variables, test screens, unused media.
> For each finding give: screen, control.property, severity (High/Medium/Low), explanation, and a corrected Power Fx formula.
