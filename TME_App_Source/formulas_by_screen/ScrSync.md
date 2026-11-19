# ScrSync — Power Fx formulas

### `ScrSync` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrSync` . **Fill**  _(Screen)_
```powerfx
RGBA(255,255,255,1)
```

### `ScrSync` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrSync` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrSync` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrSync/lblLastStockEntry` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/lblLastStockEntry` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/lblLastStockEntry` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblLastStockEntry` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblLastStockEntry` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/lblLastStockEntry` . **Height**  _(Label@2.5.1)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrSync/lblLastStockEntry` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblLastStockEntry` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblLastStockEntry` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblLastStockEntry` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblLastStockEntry` . **Size**  _(Label@2.5.1)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblLastStockEntry` . **Text**  _(Label@2.5.1)_
```powerfx
"Last Entry No: " &
Text(
    Coalesce(
        First(colStockSyncInfo).LastEntryNo,
        0
    ),
    "#,##0"
)
```

### `ScrSync/lblLastStockEntry` . **Width**  _(Label@2.5.1)_
```powerfx
(310)*((App.Width/640))
```

### `ScrSync/lblLastStockEntry` . **X**  _(Label@2.5.1)_
```powerfx
(330)*((App.Width/640))
```

### `ScrSync/lblLastStockEntry` . **Y**  _(Label@2.5.1)_
```powerfx
(473)*((App.Height/1136))
```

### `ScrSync/btnSyncItems` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/btnSyncItems` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrSync/btnSyncItems` . **BorderStyle**  _(Classic/Button@2.2.0)_
```powerfx
BorderStyle.None
```

### `ScrSync/btnSyncItems` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncItems` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/btnSyncItems` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrSync/btnSyncItems` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varStartupSyncRunning,false),DisplayMode.Disabled,If(
    varItemLoading,
    DisplayMode.Disabled,
    DisplayMode.Edit
))
```

### `ScrSync/btnSyncItems` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(187, 221, 140, 1)
```

### `ScrSync/btnSyncItems` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncItems` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/btnSyncItems` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/btnSyncItems` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrSync/btnSyncItems` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/btnSyncItems` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrSync/btnSyncItems` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
// ==========================================
// ITEM SYNC - JSON SNAPSHOT
// ==========================================

If(
    !Connection.Connected,

    Notify(
        "Интернет холболт алга байна.",
        NotificationType.Warning
    ),

    Set(
        varItemLoading,
        true
    );

    IfError(

        // ==========================================
        // 1. SNAPSHOT FLOW ДУУДАХ
        // ==========================================

        Set(
            varItemsResponse,
            PA_GetItemsSnapshot.Run()
        );

        // ==========================================
        // 2. JSON -> TEMP COLLECTION
        // ==========================================

        ClearCollect(
            colNewItemsSnapshot,

            ForAll(
                Table(
                    ParseJSON(
                        Coalesce(
                            varItemsResponse.itemsjson,
                            "[]"
                        )
                    )
                ) As r,

                {
                    number:
                        Text(r.Value.number),

                    displayName:
                        Text(r.Value.displayName),

                    unitOfMeasure:
                        Text(r.Value.unitOfMeasure),

                    itemCategory:
                        Text(r.Value.itemCategory),

                    inventory:
                        Value(r.Value.inventory),

                    unitCost:
                        Value(r.Value.unitCost),

                    unitPrice:
                        Value(r.Value.unitPrice)
                }
            )
        );

        // ==========================================
        // 3. EMPTY PROTECTION
        // ==========================================

        If(
            CountRows(colNewItemsSnapshot) = 0,

            Notify(
                "Items snapshot хоосон ирлээ. Local items солигдоогүй.",
                NotificationType.Error
            ),

            // ======================================
            // 4. LOCAL ITEMS REPLACE
            // ======================================

            ClearCollect(
                colOfflineItems,
                colNewItemsSnapshot
            );

            // ======================================
            // 5. DEVICE STORAGE-Д ХАДГАЛАХ
            // ======================================

            IfError(

                SaveData(
                    colOfflineItems,
                    "OfflineItems"
                ),

                Notify(
                    "Items device-д хадгалагдсангүй: " &
                    FirstError.Message,
                    NotificationType.Error
                ),

                // ==================================
                // 6. SAVE SUCCESS
                // ==================================

                Set(
                    varLoadedItemRows,
                    CountRows(colOfflineItems)
                );

                Notify(
                    "Бараа амжилттай татагдлаа | " &
                    Text(
                        varLoadedItemRows,
                        "#,##0"
                    ) &
                    " мөр",
                    NotificationType.Success
                )
            )
        ),

        // ==========================================
        // FLOW ERROR
        // ==========================================

        Notify(
            "Бараа татах үед алдаа гарлаа: " &
            FirstError.Message,
            NotificationType.Error
        )
    );

    Set(
        varItemLoading,
        false
    )
);
ClearCollect(colHomeLatest,ForAll(GroupBy(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !IsBlank(ItemNo)),ItemNo,LocationCode,HomeRows) As g,Patch(First(SortByColumns(g.HomeRows,"CountDate",SortOrder.Descending,"SyncKey",SortOrder.Descending)),{ItemNo:g.ItemNo,LocationCode:g.LocationCode})));
ClearCollect(colHomeMonths,ForAll(Sequence(8) As m,With({d:DateAdd(Date(Year(Today()),Month(Today()),1),m.Value-8,TimeUnit.Months)},{MonthDate:d,Total:CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && CountDate>=d && CountDate<DateAdd(d,1,TimeUnit.Months))),Pending:CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced && CountDate>=d && CountDate<DateAdd(d,1,TimeUnit.Months)))})));
Set(varHomeAccuracy,If(IsEmpty(colHomeLatest),Blank(),CountRows(Filter(colHomeLatest,!IsBlank(OpeningBalance) && !IsBlank(CountQty) && CountQty=OpeningBalance))/CountRows(colHomeLatest)*100));
Set(varHomeEstimate,If(IsEmpty(colOfflineItems),Blank(),Sum(colOfflineItems,inventory*unitCost)))
```

### `ScrSync/btnSyncItems` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/btnSyncItems` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/btnSyncItems` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrSync/btnSyncItems` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncItems` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncItems` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncItems` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncItems` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncItems` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varItemLoading,
    "ТАТАЖ БАЙНА...",
    "БАРААГ ТАТАХ"
)
```

### `ScrSync/btnSyncItems` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(280)*((App.Width/640))
```

### `ScrSync/btnSyncItems` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((App.Width/640))
```

### `ScrSync/btnSyncItems` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(176)*((App.Height/1136))
```

### `ScrSync/btnSyncStock` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/btnSyncStock` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrSync/btnSyncStock` . **BorderStyle**  _(Classic/Button@2.2.0)_
```powerfx
BorderStyle.None
```

### `ScrSync/btnSyncStock` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncStock` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/btnSyncStock` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrSync/btnSyncStock` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varStartupSyncRunning,false),DisplayMode.Disabled,If(
    varStockLoading,
    DisplayMode.Disabled,
    DisplayMode.Edit
))
```

### `ScrSync/btnSyncStock` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(187, 221, 140, 1)
```

### `ScrSync/btnSyncStock` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncStock` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/btnSyncStock` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/btnSyncStock` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrSync/btnSyncStock` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/btnSyncStock` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrSync/btnSyncStock` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(
    !Connection.Connected,

    Notify(
        "Интернет холболт алга байна.",
        NotificationType.Warning
    ),

    Set(
        varStockLoading,
        true
    );

    IfError(

        // ==========================================
        // 1. MASTER SNAPSHOT ТАТАХ
        // ==========================================

        Set(
            varStockResponse,
            PA_GetStockFromExcel.Run()
        );

        // ==========================================
        // 2. JSON -> TEMP COLLECTION
        // ==========================================

        ClearCollect(
            colNewStockSnapshot,
            ForAll(
                Table(
                    ParseJSON(
                        Coalesce(
                            varStockResponse.stockjson,
                            "[]"
                        )
                    )
                ) As r,
                {
                    itemNo:
                        Text(r.Value.itemNo),

                    locationCode:
                        Text(r.Value.locationCode),

                    quantity:
                        Value(r.Value.quantity)
                }
            )
        );

        // ==========================================
        // 3. EMPTY SNAPSHOT PROTECTION
        // ==========================================

        If(
            CountRows(colNewStockSnapshot) = 0,

            Notify(
                "Stock snapshot хоосон ирсэн тул local stock солигдсонгүй.",
                NotificationType.Error
            ),

            // ======================================
            // 4. LOCAL STOCK REPLACE
            // ======================================

            ClearCollect(
                colOfflineStock,
                colNewStockSnapshot
            );

            // ======================================
            // 5. SAVE TO DEVICE
            // ======================================

            IfError(
                SaveData(
                    colOfflineStock,
                    "OfflineStock"
                ),

                Notify(
                    "Stock device-д хадгалагдсангүй: " &
                    FirstError.Message,
                    NotificationType.Error
                ),

                // ==================================
                // 6. SAVE SUCCESS
                // ==================================

                Set(
                    varLoadedStockRows,
                    CountRows(colOfflineStock)
                );

                Notify(
                    "Stock амжилттай хадгалагдлаа | Local мөр: " &
                    Text(
                        varLoadedStockRows,
                        "#,##0"
                    ),
                    NotificationType.Success
                )
            )
        ),

        // ==========================================
        // FLOW ERROR
        // ==========================================

        Notify(
            "Stock татах үед алдаа гарлаа: " &
            FirstError.Message,
            NotificationType.Error
        )
    );

    Set(
        varStockLoading,
        false
    )
);
ClearCollect(colHomeLatest,ForAll(GroupBy(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !IsBlank(ItemNo)),ItemNo,LocationCode,HomeRows) As g,Patch(First(SortByColumns(g.HomeRows,"CountDate",SortOrder.Descending,"SyncKey",SortOrder.Descending)),{ItemNo:g.ItemNo,LocationCode:g.LocationCode})));
ClearCollect(colHomeMonths,ForAll(Sequence(8) As m,With({d:DateAdd(Date(Year(Today()),Month(Today()),1),m.Value-8,TimeUnit.Months)},{MonthDate:d,Total:CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && CountDate>=d && CountDate<DateAdd(d,1,TimeUnit.Months))),Pending:CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced && CountDate>=d && CountDate<DateAdd(d,1,TimeUnit.Months)))})));
Set(varHomeAccuracy,If(IsEmpty(colHomeLatest),Blank(),CountRows(Filter(colHomeLatest,!IsBlank(OpeningBalance) && !IsBlank(CountQty) && CountQty=OpeningBalance))/CountRows(colHomeLatest)*100));
Set(varHomeEstimate,If(IsEmpty(colOfflineItems),Blank(),Sum(colOfflineItems,inventory*unitCost)))
```

### `ScrSync/btnSyncStock` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/btnSyncStock` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/btnSyncStock` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrSync/btnSyncStock` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncStock` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncStock` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncStock` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncStock` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncStock` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varStockLoading,
    "ТАТАЖ БАЙНА...",
    "STOCK SYNC"
)
```

### `ScrSync/btnSyncStock` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(280)*((App.Width/640))
```

### `ScrSync/btnSyncStock` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((App.Width/640))
```

### `ScrSync/btnSyncStock` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(447)*((App.Height/1136))
```

### `ScrSync/Icon1` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/Icon1` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/Icon1` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Icon1` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/Icon1` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Icon1` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Height/1136))
```

### `ScrSync/Icon1` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronLeft
```

### `ScrSync/Icon1` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate('нүүр')
```

### `ScrSync/Icon1` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Width/640))
```

### `ScrSync/Icon1` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(30)*((App.Width/640))
```

### `ScrSync/Icon1` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(31)*((App.Height/1136))
```

### `ScrSync/btnSyncBins` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/btnSyncBins` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrSync/btnSyncBins` . **BorderStyle**  _(Classic/Button@2.2.0)_
```powerfx
BorderStyle.None
```

### `ScrSync/btnSyncBins` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncBins` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/btnSyncBins` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrSync/btnSyncBins` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varStartupSyncRunning,false),DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrSync/btnSyncBins` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(187, 221, 140, 1)
```

### `ScrSync/btnSyncBins` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncBins` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/btnSyncBins` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/btnSyncBins` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrSync/btnSyncBins` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/btnSyncBins` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrSync/btnSyncBins` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!Connection.Connected,Notify("Интернет холболт алга.",NotificationType.Warning),
IfError(
    Set(varBinsResponse,PA_GetAllBinsOffline.Run());
    ClearCollect(colNewBinsV16,ForAll(Table(ParseJSON(Coalesce(varBinsResponse.binsjson,"[]"))) As r,
        {itemNo:Text(r.Value.itemNo),locationCode:Text(r.Value.locationCode),binCode:Text(r.Value.binCode)}));
    If(IsEmpty(colNewBinsV16),Notify("Тавиурын snapshot хоосон. Өмнөх өгөгдөл хадгалагдсан.",NotificationType.Warning),
        IfError(SaveData(colNewBinsV16,"OfflineBins"),
            Notify("Тавиур хадгалагдсангүй: " & FirstError.Message,NotificationType.Error),
            ClearCollect(colOfflineBins,colNewBinsV16);
            Notify("Тавиур хадгалагдлаа: " & Text(CountRows(colOfflineBins)),NotificationType.Success))),
    Notify("Тавиур татахад алдаа: " & FirstError.Message,NotificationType.Error)))
```

### `ScrSync/btnSyncBins` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/btnSyncBins` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/btnSyncBins` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrSync/btnSyncBins` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncBins` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncBins` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncBins` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncBins` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/btnSyncBins` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"АГУУЛАХ ТАТАХ"
```

### `ScrSync/btnSyncBins` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(280)*((App.Width/640))
```

### `ScrSync/btnSyncBins` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((App.Width/640))
```

### `ScrSync/btnSyncBins` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(317)*((App.Height/1136))
```

### `ScrSync/lblItemCount` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/lblItemCount` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/lblItemCount` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblItemCount` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(127, 178, 57, 1)
```

### `ScrSync/lblItemCount` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblItemCount` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/lblItemCount` . **Height**  _(Label@2.5.1)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/lblItemCount` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblItemCount` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblItemCount` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblItemCount` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblItemCount` . **Size**  _(Label@2.5.1)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblItemCount` . **Text**  _(Label@2.5.1)_
```powerfx
"Items: " & Text(
    CountRows(colOfflineItems),
    "#,##0"
)
```

### `ScrSync/lblItemCount` . **Width**  _(Label@2.5.1)_
```powerfx
(310)*((App.Width/640))
```

### `ScrSync/lblItemCount` . **X**  _(Label@2.5.1)_
```powerfx
(330)*((App.Width/640))
```

### `ScrSync/lblItemCount` . **Y**  _(Label@2.5.1)_
```powerfx
(156)*((App.Height/1136))
```

### `ScrSync/lblLastItemSync` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/lblLastItemSync` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/lblLastItemSync` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblLastItemSync` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblLastItemSync` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/lblLastItemSync` . **Height**  _(Label@2.5.1)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrSync/lblLastItemSync` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblLastItemSync` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblLastItemSync` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblLastItemSync` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblLastItemSync` . **Size**  _(Label@2.5.1)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblLastItemSync` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    CountRows(colItemSyncInfo) = 0,
    "Last Item Sync: -",
    With(
        {
            _syncDate: First(colItemSyncInfo).LastSyncDate
        },
        If(
            IsBlank(_syncDate),
            "Last Item Sync: -",
            "Last Item Sync: " &
            Text(
                DateTimeValue(_syncDate),
                "yyyy.mm.dd hh:mm"
            )
        )
    )
)
```

### `ScrSync/lblLastItemSync` . **Width**  _(Label@2.5.1)_
```powerfx
(298)*((App.Width/640))
```

### `ScrSync/lblLastItemSync` . **X**  _(Label@2.5.1)_
```powerfx
(330)*((App.Width/640))
```

### `ScrSync/lblLastItemSync` . **Y**  _(Label@2.5.1)_
```powerfx
(200)*((App.Height/1136))
```

### `ScrSync/lblStockRows` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/lblStockRows` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/lblStockRows` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblStockRows` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(127, 178, 57, 1)
```

### `ScrSync/lblStockRows` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblStockRows` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/lblStockRows` . **Height**  _(Label@2.5.1)_
```powerfx
(37)*((App.Height/1136))
```

### `ScrSync/lblStockRows` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblStockRows` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblStockRows` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/lblStockRows` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/lblStockRows` . **Size**  _(Label@2.5.1)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/lblStockRows` . **Text**  _(Label@2.5.1)_
```powerfx
"Stock мөр: " &
Text(
    CountRows(colOfflineStock),
    "#,##0"
)
```

### `ScrSync/lblStockRows` . **Width**  _(Label@2.5.1)_
```powerfx
(264)*((App.Width/640))
```

### `ScrSync/lblStockRows` . **X**  _(Label@2.5.1)_
```powerfx
(330)*((App.Width/640))
```

### `ScrSync/lblStockRows` . **Y**  _(Label@2.5.1)_
```powerfx
(447)*((App.Height/1136))
```

### `ScrSync/tmrStockSync` . **OnTimerStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrSync/tmrStockSync` . **AutoStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrSync/tmrStockSync` . **AutoPause**  _(Timer@2.1.0)_
```powerfx
false
```

### `ScrSync/tmrStockSync` . **BorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrSync/tmrStockSync` . **BorderThickness**  _(Timer@2.1.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/tmrStockSync` . **Color**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/tmrStockSync` . **DisabledBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 70%)
```

### `ScrSync/tmrStockSync` . **DisabledColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 90%)
```

### `ScrSync/tmrStockSync` . **DisabledFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 70%)
```

### `ScrSync/tmrStockSync` . **Duration**  _(Timer@2.1.0)_
```powerfx
500
```

### `ScrSync/tmrStockSync` . **Fill**  _(Timer@2.1.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrSync/tmrStockSync` . **FocusedBorderThickness**  _(Timer@2.1.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/tmrStockSync` . **Font**  _(Timer@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/tmrStockSync` . **Height**  _(Timer@2.1.0)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/tmrStockSync` . **HoverBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrSync/tmrStockSync` . **HoverColor**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/tmrStockSync` . **HoverFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrSync/tmrStockSync` . **OnTimerEnd**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),If(
    varStockAutoSync,

    If(
        !Connection.Connected,

        Set(
            varStockAutoSync,
            false
        );

        Notify(
            "Интернет тасарлаа. Sync зогслоо.",
            NotificationType.Warning
        ),

        // ==========================================
        // 1. CURRENT LAST ENTRY
        // ==========================================

        Set(
            varLastStockEntryNo,
            Coalesce(
                First(colStockSyncInfo).LastEntryNo,
                0
            )
        );

        // ==========================================
        // 2. GET NEXT BATCH
        // ==========================================

        Set(
            varStockResponse,
            PA_GetAllStockOffline.Run(
                varLastStockEntryNo
            )
        );

        // ==========================================
        // 3. JSON -> COLLECTION
        // ==========================================

        ClearCollect(
            colStockEntries,
            ForAll(
                Table(
                    ParseJSON(
                        varStockResponse.stockjson
                    )
                ) As r,
                {
                    entryNo: Value(r.Value.entryNo),
                    itemNo: Text(r.Value.itemNo),
                    locationCode: Text(r.Value.locationCode),
                    quantity: Value(r.Value.quantity)
                }
            )
        );

        Set(
            varStockBatchNo,
            varStockBatchNo + 1
        );

        // ==========================================
        // 4. DATA БАЙВАЛ UPDATE
        // ==========================================

        If(
            CountRows(colStockEntries) > 0,

            // --------------------------------------
            // ITEM + LOCATION-ООР НЭГТГЭХ
            // --------------------------------------

            ClearCollect(
                colStockDelta,
                AddColumns(
                    GroupBy(
                        colStockEntries,
                        itemNo,
                        locationCode,
                        StockRows
                    ),
                    DeltaQty,
                    Sum(
                        StockRows,
                        quantity
                    )
                )
            );

            // ======================================
            // 4A. LOCAL STOCK UPDATE
            // ======================================

            ForAll(
                colStockDelta As d,

                With(
                    {
                        existingStock:
                            LookUp(
                                colOfflineStock,
                                itemNo = d.itemNo &&
                                locationCode = d.locationCode
                            )
                    },

                    If(
                        IsBlank(existingStock),

                        Collect(
                            colOfflineStock,
                            {
                                itemNo: d.itemNo,
                                locationCode: d.locationCode,
                                quantity: d.DeltaQty
                            }
                        ),

                        Patch(
                            colOfflineStock,
                            existingStock,
                            {
                                quantity:
                                    existingStock.quantity +
                                    d.DeltaQty
                            }
                        )
                    )
                )
            );

            // ======================================
            // 4B. BC CHECK SNAPSHOT UPDATE
            // ======================================

            ForAll(
                colStockDelta As d,

                With(
                    {
                        existingCheck:
                            LookUp(
                                colBCStockCheck,
                                itemNo = d.itemNo &&
                                locationCode = d.locationCode
                            )
                    },

                    If(
                        IsBlank(existingCheck),

                        Collect(
                            colBCStockCheck,
                            {
                                itemNo: d.itemNo,
                                locationCode: d.locationCode,
                                quantity: d.DeltaQty
                            }
                        ),

                        Patch(
                            colBCStockCheck,
                            existingCheck,
                            {
                                quantity:
                                    existingCheck.quantity +
                                    d.DeltaQty
                            }
                        )
                    )
                )
            );

            // ======================================
            // LAST ENTRY UPDATE
            // ======================================

            ClearCollect(
                colStockSyncInfo,
                {
                    LastEntryNo:
                        Max(
                            colStockEntries,
                            entryNo
                        )
                }
            );

            // ======================================
            // SAVE LOCAL
            // ======================================

            SaveData(
                colOfflineStock,
                "OfflineStock"
            );

            SaveData(
                colBCStockCheck,
                "BCStockCheck"
            );

            SaveData(
                colStockSyncInfo,
                "StockSyncInfo"
            )
        );

        // ==========================================
        // 5. LAST BATCH
        // ==========================================

        If(
            CountRows(colStockEntries) < 1000,

            Set(
                varStockAutoSync,
                false
            );

            Notify(
                "Stock sync дууслаа | Last Entry: " &
                Text(
                    Coalesce(
                        First(colStockSyncInfo).LastEntryNo,
                        varLastStockEntryNo
                    ),
                    "#,##0"
                ) &
                " | Stock мөр: " &
                Text(
                    CountRows(colOfflineStock),
                    "#,##0"
                ) &
                " | Check мөр: " &
                Text(
                    CountRows(colBCStockCheck),
                    "#,##0"
                ),
                NotificationType.Success
            )
        )
    )
)
)
```

### `ScrSync/tmrStockSync` . **PressedBorderColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrSync/tmrStockSync` . **PressedColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrSync/tmrStockSync` . **PressedFill**  _(Timer@2.1.0)_
```powerfx
Self.Color
```

### `ScrSync/tmrStockSync` . **Repeat**  _(Timer@2.1.0)_
```powerfx
varStockAutoSync
```

### `ScrSync/tmrStockSync` . **Size**  _(Timer@2.1.0)_
```powerfx
(13)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/tmrStockSync` . **Start**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),varStockAutoSync
)
```

### `ScrSync/tmrStockSync` . **Visible**  _(Timer@2.1.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrSync/tmrStockSync` . **Width**  _(Timer@2.1.0)_
```powerfx
(280)*((App.Width/640))
```

### `ScrSync/tmrStockSync` . **X**  _(Timer@2.1.0)_
```powerfx
(360)*((App.Width/640))
```

### `ScrSync/tmrStockSync` . **Y**  _(Timer@2.1.0)_
```powerfx
(1066)*((App.Height/1136))
```

### `ScrSync/tmrItemSync` . **AutoStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrSync/tmrItemSync` . **AutoPause**  _(Timer@2.1.0)_
```powerfx
false
```

### `ScrSync/tmrItemSync` . **BorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrSync/tmrItemSync` . **BorderThickness**  _(Timer@2.1.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/tmrItemSync` . **Color**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/tmrItemSync` . **DisabledBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 70%)
```

### `ScrSync/tmrItemSync` . **DisabledColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 90%)
```

### `ScrSync/tmrItemSync` . **DisabledFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 70%)
```

### `ScrSync/tmrItemSync` . **Duration**  _(Timer@2.1.0)_
```powerfx
700
```

### `ScrSync/tmrItemSync` . **Fill**  _(Timer@2.1.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrSync/tmrItemSync` . **FocusedBorderThickness**  _(Timer@2.1.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/tmrItemSync` . **Font**  _(Timer@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/tmrItemSync` . **Height**  _(Timer@2.1.0)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/tmrItemSync` . **HoverBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrSync/tmrItemSync` . **HoverColor**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/tmrItemSync` . **HoverFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrSync/tmrItemSync` . **OnTimerEnd**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),If(
    varStockAutoSync,

    If(
        !Connection.Connected,

        Set(varStockAutoSync, false);

        Notify(
            "Интернет тасарлаа. Stock sync зогслоо. Өмнөх хадгалсан batch-ууд хэвээр.",
            NotificationType.Warning
        ),

        // ==========================================
        // 1. CURRENT LAST ENTRY
        // ==========================================

        Set(
            varLastStockEntryNo,
            Coalesce(
                First(colStockSyncInfo).LastEntryNo,
                0
            )
        );

        // ==========================================
        // 2. RESET BATCH STATUS
        // ==========================================

        Set(varStockBatchOK, false);
        Set(varStockResponse, Blank());

        // ==========================================
        // 3. GET NEXT BATCH SAFELY
        // ==========================================

        IfError(
            Set(
                varStockResponse,
                PA_GetAllStockOffline.Run(
                    varLastStockEntryNo
                )
            );

            Set(varStockBatchOK, true),

            Set(varStockBatchOK, false);
            Set(varStockAutoSync, false);

            Notify(
                "Stock batch татах үед алдаа гарлаа. Энэ batch local stock-д нэмэгдээгүй.",
                NotificationType.Error
            )
        );

        // ==========================================
        // 4. ONLY PROCESS SUCCESSFUL RESPONSE
        // ==========================================

        If(
            varStockBatchOK,

            ClearCollect(
                colStockEntries,
                ForAll(
                    Table(
                        ParseJSON(
                            Coalesce(
                                varStockResponse.stockjson,
                                "[]"
                            )
                        )
                    ) As r,
                    {
                        entryNo: Value(r.Value.entryNo),
                        itemNo: Text(r.Value.itemNo),
                        locationCode: Text(r.Value.locationCode),
                        quantity: Value(r.Value.quantity)
                    }
                )
            );

            Set(
                varStockBatchNo,
                varStockBatchNo + 1
            );

            // ======================================
            // 5. DATA RECEIVED
            // ======================================

            If(
                CountRows(colStockEntries) > 0,

                // ----------------------------------
                // GROUP ITEM + LOCATION
                // ----------------------------------

                ClearCollect(
                    colStockDelta,
                    AddColumns(
                        GroupBy(
                            colStockEntries,
                            itemNo,
                            locationCode,
                            StockRows
                        ),
                        DeltaQty,
                        Sum(
                            StockRows,
                            quantity
                        )
                    )
                );

                // ----------------------------------
                // LOCAL STOCK UPDATE
                // ----------------------------------

                ForAll(
                    colStockDelta As d,

                    With(
                        {
                            existingStock:
                                LookUp(
                                    colOfflineStock,
                                    itemNo = d.itemNo &&
                                    locationCode = d.locationCode
                                )
                        },

                        If(
                            IsBlank(existingStock),

                            Collect(
                                colOfflineStock,
                                {
                                    itemNo: d.itemNo,
                                    locationCode: d.locationCode,
                                    quantity: d.DeltaQty
                                }
                            ),

                            Patch(
                                colOfflineStock,
                                existingStock,
                                {
                                    quantity:
                                        existingStock.quantity +
                                        d.DeltaQty
                                }
                            )
                        )
                    )
                );

                // ==================================
                // 6. UPDATE LAST ENTRY
                // ==================================

                ClearCollect(
                    colStockSyncInfo,
                    {
                        LastEntryNo:
                            Max(
                                colStockEntries,
                                entryNo
                            )
                    }
                );

                // ==================================
                // 7. SAVE EVERY SUCCESSFUL BATCH
                // ==================================

                SaveData(
                    colOfflineStock,
                    "OfflineStock"
                );

                SaveData(
                    colStockSyncInfo,
                    "StockSyncInfo"
                )
            );

            // ======================================
            // 8. LAST BATCH
            // ======================================

            If(
                CountRows(colStockEntries) < 1000,

                Set(
                    varStockAutoSync,
                    false
                );

                Notify(
                    "Stock sync дууслаа | Last Entry: " &
                    Text(
                        Coalesce(
                            First(colStockSyncInfo).LastEntryNo,
                            varLastStockEntryNo
                        ),
                        "#,##0"
                    ) &
                    " | Stock мөр: " &
                    Text(
                        CountRows(colOfflineStock),
                        "#,##0"
                    ),
                    NotificationType.Success
                )
            )
        )
    )
)
)
```

### `ScrSync/tmrItemSync` . **PressedBorderColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrSync/tmrItemSync` . **PressedColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrSync/tmrItemSync` . **PressedFill**  _(Timer@2.1.0)_
```powerfx
Self.Color
```

### `ScrSync/tmrItemSync` . **Repeat**  _(Timer@2.1.0)_
```powerfx
true
```

### `ScrSync/tmrItemSync` . **Size**  _(Timer@2.1.0)_
```powerfx
(13)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/tmrItemSync` . **Start**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),varItemAutoSync
)
```

### `ScrSync/tmrItemSync` . **Visible**  _(Timer@2.1.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrSync/tmrItemSync` . **Width**  _(Timer@2.1.0)_
```powerfx
(280)*((App.Width/640))
```

### `ScrSync/tmrItemSync` . **X**  _(Timer@2.1.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrSync/tmrItemSync` . **Y**  _(Timer@2.1.0)_
```powerfx
(1066)*((App.Height/1136))
```

### `ScrSync/Button18` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/Button18` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrSync/Button18` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button18` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/Button18` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrSync/Button18` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrSync/Button18` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button18` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/Button18` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/Button18` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrSync/Button18` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/Button18` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrSync/Button18` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varItemAutoSync, false);
Set(varItemBatchNo, 0);
Set(varLastItemNo, "0");

Clear(colOfflineItems);

SaveData(
    colOfflineItems,
    "OfflineItems"
);

ClearCollect(
    colItemSyncInfo,
    {
        LastSyncDate: "2026-08-20T00:00:00Z"
    }
);

SaveData(
    colItemSyncInfo,
    "ItemSyncInfo"
);

Notify(
    "Барааны local cache бүрэн устгагдлаа.",
    NotificationType.Success
)
```

### `ScrSync/Button18` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/Button18` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/Button18` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrSync/Button18` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button18` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button18` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button18` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button18` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(18)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button18` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"ТАТСАН БАРААГ УСТГАХ"
```

### `ScrSync/Button18` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(280)*((App.Width/640))
```

### `ScrSync/Button18` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((App.Width/640))
```

### `ScrSync/Button18` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(822)*((App.Height/1136))
```

### `ScrSync/Button19` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/Button19` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrSync/Button19` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button19` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/Button19` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrSync/Button19` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrSync/Button19` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button19` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/Button19` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/Button19` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrSync/Button19` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrSync/Button19` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrSync/Button19` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Clear(colOfflineStock);

SaveData(
    colOfflineStock,
    "OfflineStock"
);

ClearCollect(
    colStockSyncInfo,
    {
        LastEntryNo: 0
    }
);

SaveData(
    colStockSyncInfo,
    "StockSyncInfo"
);

Clear(colStockEntries);
Clear(colStockDelta);

Set(varLastStockEntryNo, 0);
Set(varStockBatchNo, 0);
Set(varStockAutoSync, false);

Notify(
    "Барааны журналын local cache устгагдлаа. Одоо STOCK SYNC дарж дахин татна уу.",
    NotificationType.Success
)
```

### `ScrSync/Button19` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/Button19` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrSync/Button19` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrSync/Button19` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button19` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button19` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button19` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button19` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(18)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Button19` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"БАРААНЫ ЖУРНАЛ УСТГАХ"
```

### `ScrSync/Button19` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(280)*((App.Width/640))
```

### `ScrSync/Button19` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((App.Width/640))
```

### `ScrSync/Button19` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(924)*((App.Height/1136))
```

### `ScrSync/Label29` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/Label29` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/Label29` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label29` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label29` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/Label29` . **Height**  _(Label@2.5.1)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/Label29` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label29` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label29` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label29` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label29` . **Size**  _(Label@2.5.1)_
```powerfx
(11)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label29` . **Text**  _(Label@2.5.1)_
```powerfx
"BC-д нийт үүссэн items тоогоор БАРААГ ТАТАХ-р UPDATE хийгдэхгүй бол энэ товч дараад дахин татаарай!"
```

### `ScrSync/Label29` . **Width**  _(Label@2.5.1)_
```powerfx
(310)*((App.Width/640))
```

### `ScrSync/Label29` . **X**  _(Label@2.5.1)_
```powerfx
(330)*((App.Width/640))
```

### `ScrSync/Label29` . **Y**  _(Label@2.5.1)_
```powerfx
(822)*((App.Height/1136))
```

### `ScrSync/Label29_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/Label29_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/Label29_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label29_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label29_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/Label29_1` . **Height**  _(Label@2.5.1)_
```powerfx
(70)*((App.Height/1136))
```

### `ScrSync/Label29_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label29_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label29_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label29_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label29_1` . **Size**  _(Label@2.5.1)_
```powerfx
(11)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label29_1` . **Text**  _(Label@2.5.1)_
```powerfx
"Нийт барааны журнал Last Entry No-р STOCK SYNC -р таарахгүй бол ашиглаарай"
```

### `ScrSync/Label29_1` . **Width**  _(Label@2.5.1)_
```powerfx
(310)*((App.Width/640))
```

### `ScrSync/Label29_1` . **X**  _(Label@2.5.1)_
```powerfx
(330)*((App.Width/640))
```

### `ScrSync/Label29_1` . **Y**  _(Label@2.5.1)_
```powerfx
(924)*((App.Height/1136))
```

### `ScrSync/Label24` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/Label24` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/Label24` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label24` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label24` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/Label24` . **Height**  _(Label@2.5.1)_
```powerfx
(55)*((App.Height/1136))
```

### `ScrSync/Label24` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label24` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label24` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label24` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label24` . **Size**  _(Label@2.5.1)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label24` . **Text**  _(Label@2.5.1)_
```powerfx
"ITEM LOCAL: " &
Text(
    CountRows(colOfflineItems),
    "#,##0"
)
```

### `ScrSync/Label24` . **Width**  _(Label@2.5.1)_
```powerfx
(290)*((App.Width/640))
```

### `ScrSync/Label24` . **X**  _(Label@2.5.1)_
```powerfx
(310)*((App.Width/640))
```

### `ScrSync/Label24` . **Y**  _(Label@2.5.1)_
```powerfx
(14)*((App.Height/1136))
```

### `ScrSync/Label32` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrSync/Label32` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrSync/Label32` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label32` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label32` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrSync/Label32` . **Height**  _(Label@2.5.1)_
```powerfx
(74)*((App.Height/1136))
```

### `ScrSync/Label32` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label32` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label32` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrSync/Label32` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrSync/Label32` . **Size**  _(Label@2.5.1)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `ScrSync/Label32` . **Text**  _(Label@2.5.1)_
```powerfx
"STOCK LOCAL: " &
Text(
    CountRows(colOfflineStock),
    "#,##0"
)
```

### `ScrSync/Label32` . **Width**  _(Label@2.5.1)_
```powerfx
(222)*((App.Width/640))
```

### `ScrSync/Label32` . **X**  _(Label@2.5.1)_
```powerfx
(310)*((App.Width/640))
```

### `ScrSync/Label32` . **Y**  _(Label@2.5.1)_
```powerfx
(69)*((App.Height/1136))
```

### `ScrSync/pgDenied1211` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrSync/pgDenied1211` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrSync/pgDenied1211` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrSync/pgDenied1211` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrSync/pgDenied1211` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrSync/pgDenied1211` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrSync/pgDenied1211` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrSync/pgDenied1211` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrSync/pgDenied1211` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrSync/pgDenied1211` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

