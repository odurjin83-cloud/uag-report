# ScrCountHome — Power Fx formulas

### `ScrCountHome` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F3F6F2")
```

### `ScrCountHome` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrCountHome` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrCountHome` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false;If(Connection.Connected && !Coalesce(varStartupSyncRunning,false) &&
    (IsBlank(varAutoDataChecked) || DateDiff(varAutoDataChecked,Now(),TimeUnit.Minutes)>=15),If(Connection.Connected && !Coalesce(varStartupSyncRunning,false),
Set(varStartupSyncRunning,true);
Concurrent(Set(varAutoItemsError,false);
IfError(
    Set(varAutoItemsResponse,PA_GetItemsSnapshot.Run());
    ClearCollect(colAutoItemsV16,ForAll(Table(ParseJSON(Coalesce(varAutoItemsResponse.itemsjson,"[]"))) As r,{number:Text(r.Value.number),displayName:Text(r.Value.displayName),unitOfMeasure:Text(r.Value.unitOfMeasure),itemCategory:Text(r.Value.itemCategory),inventory:Value(r.Value.inventory),unitCost:Value(r.Value.unitCost),unitPrice:Value(r.Value.unitPrice)}));
    If(IsEmpty(colAutoItemsV16),Set(varAutoItemsError,true),
        IfError(SaveData(colAutoItemsV16,"OfflineItems"),Set(varAutoItemsCacheError,true),Set(varAutoItemsCacheError,false));
        ClearCollect(colOfflineItems,colAutoItemsV16);Set(varAutoItemsUpdated,Now());Clear(colAutoItemsV16);Set(varAutoItemsResponse,Blank()));true,
    Set(varAutoItemsError,true);false),
Set(varAutoStockError,false);
IfError(
    Set(varAutoStockResponse,PA_GetStockFromExcel.Run());
    ClearCollect(colAutoStockV16,ForAll(Table(ParseJSON(Coalesce(varAutoStockResponse.stockjson,"[]"))) As r,{itemNo:Text(r.Value.itemNo),locationCode:Text(r.Value.locationCode),quantity:Value(r.Value.quantity)}));
    If(IsEmpty(colAutoStockV16),Set(varAutoStockError,true),
        IfError(SaveData(colAutoStockV16,"OfflineStock"),Set(varAutoStockCacheError,true),Set(varAutoStockCacheError,false));
        ClearCollect(colOfflineStock,colAutoStockV16);Set(varAutoStockUpdated,Now());Clear(colAutoStockV16);Set(varAutoStockResponse,Blank()));true,
    Set(varAutoStockError,true);false),
Set(varAutoBinsError,false);
IfError(
    Set(varAutoBinsResponse,PA_GetAllBinsOffline.Run());
    ClearCollect(colAutoBinsV16,ForAll(Table(ParseJSON(Coalesce(varAutoBinsResponse.binsjson,"[]"))) As r,{itemNo:Text(r.Value.itemNo),locationCode:Text(r.Value.locationCode),binCode:Text(r.Value.binCode)}));
    If(IsEmpty(colAutoBinsV16),Set(varAutoBinsError,true),
        IfError(SaveData(colAutoBinsV16,"OfflineBins"),Set(varAutoBinsCacheError,true),Set(varAutoBinsCacheError,false));
        ClearCollect(colOfflineBins,colAutoBinsV16);Set(varAutoBinsUpdated,Now());Clear(colAutoBinsV16);Set(varAutoBinsResponse,Blank()));true,
    Set(varAutoBinsError,true);false),
If(Connection.Connected && !IsBlank(varCountOwner) && !Coalesce(varCountSaving,false) && !Coalesce(varCountSyncBusy,false) && !Coalesce(varHistoryLoading,false),
Set(varHistoryLoading,true);Set(varHistoryCloudError,false);
IfError(
    Refresh(InventoryCount);
    ClearCollect(colRestoreCloudV16,Filter(InventoryCount,Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)));
    Set(varHistoryCloudLimit,CountRows(colRestoreCloudV16)>=5000);
    ClearCollect(colRestoreRowsV16,ForAll(colRestoreCloudV16 As r,With({_title:If(StartsWith(r.Title,"ARCHIVED:"),Mid(r.Title,10),r.Title)},{
        SyncKey:If(StartsWith(_title,"COUNT:"),Mid(_title,7),"SP-" & Text(r.ID)),
        Title:_title,Archived:StartsWith(r.Title,"ARCHIVED:"),ItemNo:r.ItemNo,ItemName:r.ItemName,LocationCode:Trim(r.LocationCode),
        OpeningBalance:IfError(Value(r.OpeningBalance),Blank()),CountQty:IfError(Value(r.CountQty),Blank()),
        Variance:IfError(Value(r.CountQty)-Value(r.OpeningBalance),Blank()),CountDate:IfError(DateTimeValue(r.CountDate),Blank()),
        Counter:Coalesce(r.Counter,User().FullName),OwnerEmail:varCountOwner,SharePointID:r.ID,Revision:0,SyncError:"",
        Reason:r.Reason,Comment:r.Comment,Resolved:r.Resolved,Synced:true})));
    ClearCollect(colHistoryMergeV16,AddColumns(colOfflineInventory,MergePriority,If(Synced,0,2)));
    Collect(colHistoryMergeV16,AddColumns(colRestoreRowsV16,MergePriority,1));
    ClearCollect(colHistoryMergedV16,ForAll(GroupBy(colHistoryMergeV16,SyncKey,MergeRows) As g,
        Patch(First(SortByColumns(g.MergeRows,"MergePriority",SortOrder.Descending)),{SyncKey:g.SyncKey})));
    ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));
    Set(varHistoryRefreshed,Now());Clear(colRestoreCloudV16);Clear(colRestoreRowsV16);Clear(colHistoryMergeV16);Clear(colHistoryMergedV16);
    If(varCountCacheReady,IfError(If(!varCountDiskSafeV21,Error({Kind:ErrorKind.Validation,Message:"Төхөөрөмжийн эх санг аюулгүй уншаагүй тул дарж бичихгүй."}),
ClearCollect(colCountDiskV21,{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)});
SaveData(colCountDiskV21,varCountCacheKey)),Set(varHistoryCacheError,true),Set(varHistoryCacheError,false)));
    true,
    Set(varHistoryCloudError,true);false);
Set(varHistoryLoading,false)));
Set(varLoadedItemRows,CountRows(colOfflineItems));Set(varLoadedStockRows,CountRows(colOfflineStock));
If(!Coalesce(varDStockBuildingV17,false),
Set(varDStockBuildingV17,true);
IfError(
ClearCollect(colDJoinV17,ForAll(colOfflineItems As i,{JoinNo:i.number,JoinKind:0,JoinCost:i.unitCost,JoinName:i.displayName,JoinUom:i.unitOfMeasure,JoinLocation:"",JoinQty:0}));
Collect(colDJoinV17,ForAll(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),!IsBlank(itemNo) && !IsBlank(locationCode)) As s,{JoinNo:s.itemNo,JoinKind:1,JoinCost:Blank(),JoinName:"",JoinUom:"",JoinLocation:s.locationCode,JoinQty:s.quantity}));
ClearCollect(colDStockBaseV17,Ungroup(ForAll(GroupBy(colDJoinV17,JoinNo,JoinRows) As g,
With({_master:LookUp(g.JoinRows,JoinKind=0)},
{StockRows:ForAll(GroupBy(Filter(g.JoinRows,JoinKind=1),JoinLocation,LocationRows) As l,
{itemNo:g.JoinNo,locationCode:l.JoinLocation,Qty:Sum(l.LocationRows,JoinQty),Cost:_master.JoinCost,ItemName:Coalesce(_master.JoinName,g.JoinNo),Uom:_master.JoinUom})})),StockRows));
Set(varDValue,If(IsEmpty(colDStockBaseV17),Blank(),Sum(colDStockBaseV17,Qty*Cost)));
Set(varDValuationMissing,CountRows(Filter(colDStockBaseV17,IsBlank(Cost))));
Set(varDStockReadyV17,true);Set(varDStockBuiltAtV17,Now());
IfError(SaveData(colDStockBaseV17,"DashboardStockV17"),Set(varDStockCacheErrorV17,true),Set(varDStockCacheErrorV17,false));
Clear(colDJoinV17);true,
Set(varDStockReadyV17,false);Clear(colDJoinV17);false);
Set(varDStockBuildingV17,false));Set(varAutoDataChecked,Now());Set(varStartupSyncRunning,false);
Set(varCountUploadQueue,!IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)))));If(Connection.Connected,Set(varCountUploadQueue,!IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced))))
)
```

### `ScrCountHome` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrCountHome/countHomeImage1` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeImage1` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeImage1` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeImage1` . **Height**  _(Image@2.2.3)_
```powerfx
App.Height*0.07
```

### `ScrCountHome/countHomeImage1` . **Image**  _(Image@2.2.3)_
```powerfx
'Buuruljuut logo 3-6-03 2'
```

### `ScrCountHome/countHomeImage1` . **Width**  _(Image@2.2.3)_
```powerfx
App.Width*0.13
```

### `ScrCountHome/countHomeImage1` . **X**  _(Image@2.2.3)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeImage1` . **Y**  _(Image@2.2.3)_
```powerfx
App.Height*0.035
```

### `ScrCountHome/countHomeLabel7` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeLabel7` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrCountHome/countHomeLabel7` . **BorderStyle**  _(Label@2.5.1)_
```powerfx
BorderStyle.None
```

### `ScrCountHome/countHomeLabel7` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeLabel7` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeLabel7` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeLabel7` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrCountHome/countHomeLabel7` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.055
```

### `ScrCountHome/countHomeLabel7` . **Size**  _(Label@2.5.1)_
```powerfx
32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeLabel7` . **Text**  _(Label@2.5.1)_
```powerfx
"Тооллогын төв"
```

### `ScrCountHome/countHomeLabel7` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.74
```

### `ScrCountHome/countHomeLabel7` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.20
```

### `ScrCountHome/countHomeLabel7` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.035
```

### `ScrCountHome/countHomeImage2` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeImage2` . **BorderStyle**  _(Image@2.2.3)_
```powerfx
BorderStyle.None
```

### `ScrCountHome/countHomeImage2` . **Height**  _(Image@2.2.3)_
```powerfx
87*App.Height/1200
```

### `ScrCountHome/countHomeImage2` . **Image**  _(Image@2.2.3)_
```powerfx
Untitled
```

### `ScrCountHome/countHomeImage2` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/countHomeImage2` . **Width**  _(Image@2.2.3)_
```powerfx
163*App.Width/640
```

### `ScrCountHome/countHomeImage2` . **X**  _(Image@2.2.3)_
```powerfx
459*App.Width/640
```

### `ScrCountHome/countHomeImage2` . **Y**  _(Image@2.2.3)_
```powerfx
17*App.Height/1200
```

### `ScrCountHome/countHomeLabel7_4` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeLabel7_4` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeLabel7_4` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeLabel7_4` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeLabel7_4` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeLabel7_4` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.035
```

### `ScrCountHome/countHomeLabel7_4` . **Size**  _(Label@2.5.1)_
```powerfx
15*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeLabel7_4` . **Text**  _(Label@2.5.1)_
```powerfx
"Бүртгэ · зургаар баталгаажуул · хяна"
```

### `ScrCountHome/countHomeLabel7_4` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.74
```

### `ScrCountHome/countHomeLabel7_4` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.20
```

### `ScrCountHome/countHomeLabel7_4` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.093
```

### `ScrCountHome/countHomeButton2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.12
```

### `ScrCountHome/countHomeButton2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(scrWarehouses,ScreenTransition.Fade)
```

### `ScrCountHome/countHomeButton2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
29*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"＋   Тооллого эхлэх"
```

### `ScrCountHome/countHomeButton2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.92
```

### `ScrCountHome/countHomeButton2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeButton2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.205
```

### `ScrCountHome/countHomeLabel12` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeLabel12` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeLabel12` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeLabel12` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeLabel12` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeLabel12` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.035
```

### `ScrCountHome/countHomeLabel12` . **Size**  _(Label@2.5.1)_
```powerfx
14*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeLabel12` . **Text**  _(Label@2.5.1)_
```powerfx
"АЖЛЫН ХЭСЭГ"
```

### `ScrCountHome/countHomeLabel12` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.92
```

### `ScrCountHome/countHomeLabel12` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeLabel12` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.35
```

### `ScrCountHome/countHomeButton2_1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton2_1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_1` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_1` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_1` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.12
```

### `ScrCountHome/countHomeButton2_1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('Бараа засвар хийх')
```

### `ScrCountHome/countHomeButton2_1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараа засварлах"
```

### `ScrCountHome/countHomeButton2_1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.45
```

### `ScrCountHome/countHomeButton2_1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.51
```

### `ScrCountHome/countHomeButton2_1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.405
```

### `ScrCountHome/countHomeButton2_4` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_4` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_4` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_4` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_4` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_4` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
132*App.Height/1200
```

### `ScrCountHome/countHomeButton2_4` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_4` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('Master Edit')
```

### `ScrCountHome/countHomeButton2_4` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_4` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"✏️ Master Edit"
```

### `ScrCountHome/countHomeButton2_4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/countHomeButton2_4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
225*App.Width/640
```

### `ScrCountHome/countHomeButton2_4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
330*App.Width/640
```

### `ScrCountHome/countHomeButton2_4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
267*App.Height/1200
```

### `ScrCountHome/countHomeButton2_7` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton2_7` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_7` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_7` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_7` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_7` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_7` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FBE7DC")
```

### `ScrCountHome/countHomeButton2_7` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_7` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_7` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.12
```

### `ScrCountHome/countHomeButton2_7` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_7` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_7` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_7` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPhotoRequestedV28,"");Set(varPhotoReturnV28,"home");Navigate(ScrItemPhotos,ScreenTransition.Fade)
```

### `ScrCountHome/countHomeButton2_7` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_7` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_7` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_7` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_7` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зураг авах · харах"
```

### `ScrCountHome/countHomeButton2_7` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.45
```

### `ScrCountHome/countHomeButton2_7` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeButton2_7` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.405
```

### `ScrCountHome/countHomeButton2_6` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton2_6` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_6` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_6` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_6` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_6` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_6` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_6` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_6` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_6` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.055
```

### `ScrCountHome/countHomeButton2_6` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_6` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_6` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_6` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ITEMS')
```

### `ScrCountHome/countHomeButton2_6` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_6` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_6` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_6` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_6` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Онлайн барааны мэдээлэл →"
```

### `ScrCountHome/countHomeButton2_6` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.92
```

### `ScrCountHome/countHomeButton2_6` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeButton2_6` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.70
```

### `ScrCountHome/countHomeLabel12_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeLabel12_1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeLabel12_1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeLabel12_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeLabel12_1` . **Height**  _(Label@2.5.1)_
```powerfx
38*App.Height/1200
```

### `ScrCountHome/countHomeLabel12_1` . **Size**  _(Label@2.5.1)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeLabel12_1` . **Text**  _(Label@2.5.1)_
```powerfx
"ТАЙЛАН БА ТҮҮХ"
```

### `ScrCountHome/countHomeLabel12_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/countHomeLabel12_1` . **Width**  _(Label@2.5.1)_
```powerfx
580*App.Width/640
```

### `ScrCountHome/countHomeLabel12_1` . **X**  _(Label@2.5.1)_
```powerfx
24*App.Width/640
```

### `ScrCountHome/countHomeLabel12_1` . **Y**  _(Label@2.5.1)_
```powerfx
575*App.Height/1200
```

### `ScrCountHome/countHomeButton2_2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton2_2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_2` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_2` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_2` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.12
```

### `ScrCountHome/countHomeButton2_2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrHistory)  
```

### `ScrCountHome/countHomeButton2_2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллогын түүх"
```

### `ScrCountHome/countHomeButton2_2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.45
```

### `ScrCountHome/countHomeButton2_2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeButton2_2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.55
```

### `ScrCountHome/countHomeButton2_3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton2_3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_3` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_3` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_3` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.12
```

### `ScrCountHome/countHomeButton2_3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrReport1')
```

### `ScrCountHome/countHomeButton2_3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллогын тайлан"
```

### `ScrCountHome/countHomeButton2_3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.45
```

### `ScrCountHome/countHomeButton2_3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.51
```

### `ScrCountHome/countHomeButton2_3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.55
```

### `ScrCountHome/countHomeLabel12_2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeLabel12_2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeLabel12_2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeLabel12_2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeLabel12_2` . **Height**  _(Label@2.5.1)_
```powerfx
57*App.Height/1200
```

### `ScrCountHome/countHomeLabel12_2` . **Size**  _(Label@2.5.1)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeLabel12_2` . **Text**  _(Label@2.5.1)_
```powerfx
"Файл болон санал"
```

### `ScrCountHome/countHomeLabel12_2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/countHomeLabel12_2` . **Width**  _(Label@2.5.1)_
```powerfx
187*App.Width/640
```

### `ScrCountHome/countHomeLabel12_2` . **X**  _(Label@2.5.1)_
```powerfx
82*App.Width/640
```

### `ScrCountHome/countHomeLabel12_2` . **Y**  _(Label@2.5.1)_
```powerfx
754*App.Height/1200
```

### `ScrCountHome/countHomeButton2_8` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton2_8` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_8` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_8` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_8` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_8` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_8` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_8` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_8` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_8` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.05
```

### `ScrCountHome/countHomeButton2_8` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_8` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_8` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_8` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Notify(If(varStartupSyncRunning,"Мэдээлэл автоматаар шинэчлэгдэж байна…",!Connection.Connected,"Оффлайн — хадгалсан мэдээлэл ашиглаж байна.",varAutoItemsError || varAutoStockError || varAutoBinsError,"Зарим мэдээлэл татагдсангүй. Хадгалсан мэдээлэл хэвээр; дараагийн автомат шинэчлэлтээр дахин оролдоно.","Автомат шинэчлэлт: " & Text(varAutoDataChecked,"mm.dd hh:mm")) & " | Бараа " & Text(CountRows(colOfflineItems)) & ", үлдэгдэл " & Text(CountRows(colOfflineStock)) & ", тавиур " & Text(CountRows(colOfflineBins)),NotificationType.Information)
```

### `ScrCountHome/countHomeButton2_8` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_8` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_8` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_8` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_8` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэдээллийн төлөв"
```

### `ScrCountHome/countHomeButton2_8` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.45
```

### `ScrCountHome/countHomeButton2_8` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeButton2_8` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.845
```

### `ScrCountHome/countHomeButton2_5` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton2_5` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_5` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton2_5` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton2_5` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton2_5` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_5` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton2_5` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton2_5` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
48*App.Height/1200
```

### `ScrCountHome/countHomeButton2_5` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton2_5` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton2_5` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton2_5` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('IMPORT')
```

### `ScrCountHome/countHomeButton2_5` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton2_5` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton2_5` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton2_5` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton2_5` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"📦 IMPORT FILE"
```

### `ScrCountHome/countHomeButton2_5` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/countHomeButton2_5` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
233*App.Width/640
```

### `ScrCountHome/countHomeButton2_5` . **X**  _(Classic/Button@2.2.0)_
```powerfx
330*App.Width/640
```

### `ScrCountHome/countHomeButton2_5` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
803*App.Height/1200
```

### `ScrCountHome/countHomeButton5_2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton5_2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton5_2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton5_2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeButton5_2` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton5_2` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton5_2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton5_2` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton5_2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton5_2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.05
```

### `ScrCountHome/countHomeButton5_2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton5_2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton5_2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton5_2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Launch("mailto:" & User().Email & "?subject=Toollogo%20app%20feedback")
```

### `ScrCountHome/countHomeButton5_2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton5_2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton5_2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton5_2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton5_2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Санал · тусламж"
```

### `ScrCountHome/countHomeButton5_2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.45
```

### `ScrCountHome/countHomeButton5_2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.51
```

### `ScrCountHome/countHomeButton5_2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.845
```

### `ScrCountHome/countHomeButton5` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeButton5` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeButton5` . **BorderStyle**  _(Classic/Button@2.2.0)_
```powerfx
BorderStyle.None
```

### `ScrCountHome/countHomeButton5` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton5` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(151, 0, 0, 1)
```

### `ScrCountHome/countHomeButton5` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeButton5` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeButton5` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Connection.Connected && varCountCacheReady && !Coalesce(varCountSyncBusy,false) && !IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrCountHome/countHomeButton5` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton5` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeButton5` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeButton5` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.06
```

### `ScrCountHome/countHomeButton5` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeButton5` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeButton5` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeButton5` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
// V27 durable upload: CountKeyV27 is unique in SharePoint.
If(Connection.Connected && varCountCacheReady &&
 !Coalesce(varCountSyncBusy,false) && !Coalesce(varCountSaving,false) &&
 !Coalesce(varHistoryLoading,false) && varCountOwner=Lower(Trim(User().Email)) &&
 !IsBlank(varCountOwner) && !IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)) &&
 (IsBlank(varCountRetryAtV27) || Now()>=varCountRetryAtV27),
Set(varCountSyncBusy,true);
IfError(
ClearCollect(colToSync,FirstN(SortByColumns(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced),"SyncError",SortOrder.Ascending),25));
If(!IsEmpty(colToSync),
ForAll(colToSync As rec,
    IfError(
        With({_existing:With({_rowID:rec.SharePointID,_rowTitle:rec.Title,_archivedTitle:"ARCHIVED:" & rec.Title,_oldCounter:User().FullName},If(_rowID>0,With({_byID:LookUp(InventoryCount,ID=_rowID)},If(_byID.Counter=varCountOwner || (_byID.Counter=_oldCounter && _byID.'Created By'.Email=varCountOwner),_byID,Blank())),Coalesce(LookUp(InventoryCount,CountKeyV27=rec.SyncKey && Counter=varCountOwner),LookUp(InventoryCount,Title=_rowTitle && Counter=varCountOwner),LookUp(InventoryCount,Title=_archivedTitle && Counter=varCountOwner))))},
            With({_saved:Patch(InventoryCount,If(IsBlank(_existing.ID),Defaults(InventoryCount),_existing),{
                CountKeyV27:rec.SyncKey,Title:If(Coalesce(rec.Archived,false),"ARCHIVED:" & rec.Title,rec.Title),ItemNo:rec.ItemNo,ItemName:rec.ItemName,LocationCode:rec.LocationCode,
                OpeningBalance:rec.OpeningBalance,CountQty:rec.CountQty,Variance:rec.CountQty-rec.OpeningBalance,
                CountDate:rec.CountDate,Counter:rec.OwnerEmail,Reason:rec.Reason,Comment:rec.Comment,Resolved:rec.Resolved})},
                If(IsBlank(_saved.ID),Error({Kind:ErrorKind.Validation,Message:"Сервер мөрийн ID баталгаажуулсангүй."}),
                    Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=rec.SyncKey && OwnerEmail=varCountOwner),
                        {SharePointID:_saved.ID,SyncError:"",Synced:LookUp(colOfflineInventory,SyncKey=rec.SyncKey,Revision)=rec.Revision}));
                true
            )
        ),
        Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=rec.SyncKey && OwnerEmail=varCountOwner),
            {Synced:false,SyncError:FirstError.Message});false
    )
);
);
IfError(
 If(!varCountDiskSafeV21,Error({Kind:ErrorKind.Validation,Message:"Эх хадгалалтыг аюулгүй уншаагүй байна."}),
 ClearCollect(colCountDiskV21,{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)});
 SaveData(colCountDiskV21,varCountCacheKey)),
 Set(varCountStorageError,FirstError.Message),Set(varCountStorageError,""));
Set(varCountRemainingV27,CountRows(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)));
If(!IsEmpty(Filter(colToSync As q,!IsBlank(LookUp(colOfflineInventory,SyncKey=q.SyncKey,SyncError)))),
 Set(varCountRetryCountV27,Min(5,Coalesce(varCountRetryCountV27,0)+1));
 Set(varCountRetryAtV27,DateAdd(Now(),Min(300,15*Power(2,varCountRetryCountV27-1)),TimeUnit.Seconds)),
 Set(varCountRetryCountV27,0);Set(varCountRetryAtV27,Now()));
Set(varCountUploadQueue,varCountRemainingV27>0),
 Set(varCountStorageError,FirstError.Message);
 Set(varCountRetryAtV27,DateAdd(Now(),60,TimeUnit.Seconds)));
Set(varCountSyncBusy,false))
```

### `ScrCountHome/countHomeButton5` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeButton5` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeButton5` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeButton5` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeButton5` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountSyncBusy,"Автоматаар илгээж байна…",!Connection.Connected,"Оффлайн · илгээх " & CountRows(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)) & " мөр",IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)),"SharePoint-д илгээгдсэн · тооллого хадгалагдсан","Автоматаар илгээх " & CountRows(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)) & " мөр")
```

### `ScrCountHome/countHomeButton5` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.92
```

### `ScrCountHome/countHomeButton5` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeButton5` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.77
```

### `ScrCountHome/countHomeLabel7_2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeLabel7_2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeLabel7_2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeLabel7_2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeLabel7_2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeLabel7_2` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.035
```

### `ScrCountHome/countHomeLabel7_2` . **Size**  _(Label@2.5.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeLabel7_2` . **Text**  _(Label@2.5.1)_
```powerfx
User().FullName & "  ·  " & Text(Today(),"mm.dd")
```

### `ScrCountHome/countHomeLabel7_2` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.92
```

### `ScrCountHome/countHomeLabel7_2` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeLabel7_2` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.15
```

### `ScrCountHome/countHomeImage3` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeImage3` . **Height**  _(Image@2.2.3)_
```powerfx
112*App.Height/1200
```

### `ScrCountHome/countHomeImage3` . **Image**  _(Image@2.2.3)_
```powerfx
'911787850'
```

### `ScrCountHome/countHomeImage3` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/countHomeImage3` . **Width**  _(Image@2.2.3)_
```powerfx
216*App.Width/640
```

### `ScrCountHome/countHomeImage3` . **X**  _(Image@2.2.3)_
```powerfx
60*App.Width/640
```

### `ScrCountHome/countHomeImage3` . **Y**  _(Image@2.2.3)_
```powerfx
1024*App.Height/1200
```

### `ScrCountHome/countHomeLabel7_3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCountHome/countHomeLabel7_3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeLabel7_3` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeLabel7_3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeLabel7_3` . **Height**  _(Label@2.5.1)_
```powerfx
36*App.Height/1200
```

### `ScrCountHome/countHomeLabel7_3` . **Size**  _(Label@2.5.1)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeLabel7_3` . **Text**  _(Label@2.5.1)_
```powerfx
"Огноо: " & Text(Today(),"yyyy-mm-dd")
```

### `ScrCountHome/countHomeLabel7_3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/countHomeLabel7_3` . **Width**  _(Label@2.5.1)_
```powerfx
592*App.Width/640
```

### `ScrCountHome/countHomeLabel7_3` . **X**  _(Label@2.5.1)_
```powerfx
24*App.Width/640
```

### `ScrCountHome/countHomeLabel7_3` . **Y**  _(Label@2.5.1)_
```powerfx
1005*App.Height/1200
```

### `ScrCountHome/countHomeBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCountHome/countHomeBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrCountHome/countHomeBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCountHome/countHomeBack` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrCountHome/countHomeBack` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrCountHome/countHomeBack` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCountHome/countHomeBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCountHome/countHomeBack` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrCountHome/countHomeBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/countHomeBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.055
```

### `ScrCountHome/countHomeBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/countHomeBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrCountHome/countHomeBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrCountHome/countHomeBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(нүүр,ScreenTransition.Fade)
```

### `ScrCountHome/countHomeBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCountHome/countHomeBack` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCountHome/countHomeBack` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCountHome/countHomeBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCountHome/countHomeBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/countHomeBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/countHomeBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrCountHome/countHomeBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
19*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrCountHome/countHomeBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹ Үндсэн нүүр"
```

### `ScrCountHome/countHomeBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.92
```

### `ScrCountHome/countHomeBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrCountHome/countHomeBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.925
```

### `ScrCountHome/uploadQueueV16_10` . **OnTimerStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrCountHome/uploadQueueV16_10` . **AutoPause**  _(Timer@2.1.0)_
```powerfx
false
```

### `ScrCountHome/uploadQueueV16_10` . **AutoStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),true
)
```

### `ScrCountHome/uploadQueueV16_10` . **BorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrCountHome/uploadQueueV16_10` . **BorderThickness**  _(Timer@2.1.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrCountHome/uploadQueueV16_10` . **Color**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrCountHome/uploadQueueV16_10` . **DisabledBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 70%)
```

### `ScrCountHome/uploadQueueV16_10` . **DisabledColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 90%)
```

### `ScrCountHome/uploadQueueV16_10` . **DisabledFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 70%)
```

### `ScrCountHome/uploadQueueV16_10` . **Duration**  _(Timer@2.1.0)_
```powerfx
5000
```

### `ScrCountHome/uploadQueueV16_10` . **Fill**  _(Timer@2.1.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrCountHome/uploadQueueV16_10` . **FocusedBorderThickness**  _(Timer@2.1.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrCountHome/uploadQueueV16_10` . **Font**  _(Timer@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCountHome/uploadQueueV16_10` . **HoverBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCountHome/uploadQueueV16_10` . **HoverColor**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrCountHome/uploadQueueV16_10` . **HoverFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrCountHome/uploadQueueV16_10` . **OnTimerEnd**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),// V27 durable upload: CountKeyV27 is unique in SharePoint.
If(Connection.Connected && varCountCacheReady &&
 !Coalesce(varCountSyncBusy,false) && !Coalesce(varCountSaving,false) &&
 !Coalesce(varHistoryLoading,false) && varCountOwner=Lower(Trim(User().Email)) &&
 !IsBlank(varCountOwner) && !IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)) &&
 (IsBlank(varCountRetryAtV27) || Now()>=varCountRetryAtV27),
Set(varCountSyncBusy,true);
IfError(
ClearCollect(colToSync,FirstN(SortByColumns(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced),"SyncError",SortOrder.Ascending),25));
If(!IsEmpty(colToSync),
ForAll(colToSync As rec,
    IfError(
        With({_existing:With({_rowID:rec.SharePointID,_rowTitle:rec.Title,_archivedTitle:"ARCHIVED:" & rec.Title,_oldCounter:User().FullName},If(_rowID>0,With({_byID:LookUp(InventoryCount,ID=_rowID)},If(_byID.Counter=varCountOwner || (_byID.Counter=_oldCounter && _byID.'Created By'.Email=varCountOwner),_byID,Blank())),Coalesce(LookUp(InventoryCount,CountKeyV27=rec.SyncKey && Counter=varCountOwner),LookUp(InventoryCount,Title=_rowTitle && Counter=varCountOwner),LookUp(InventoryCount,Title=_archivedTitle && Counter=varCountOwner))))},
            With({_saved:Patch(InventoryCount,If(IsBlank(_existing.ID),Defaults(InventoryCount),_existing),{
                CountKeyV27:rec.SyncKey,Title:If(Coalesce(rec.Archived,false),"ARCHIVED:" & rec.Title,rec.Title),ItemNo:rec.ItemNo,ItemName:rec.ItemName,LocationCode:rec.LocationCode,
                OpeningBalance:rec.OpeningBalance,CountQty:rec.CountQty,Variance:rec.CountQty-rec.OpeningBalance,
                CountDate:rec.CountDate,Counter:rec.OwnerEmail,Reason:rec.Reason,Comment:rec.Comment,Resolved:rec.Resolved})},
                If(IsBlank(_saved.ID),Error({Kind:ErrorKind.Validation,Message:"Сервер мөрийн ID баталгаажуулсангүй."}),
                    Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=rec.SyncKey && OwnerEmail=varCountOwner),
                        {SharePointID:_saved.ID,SyncError:"",Synced:LookUp(colOfflineInventory,SyncKey=rec.SyncKey,Revision)=rec.Revision}));
                true
            )
        ),
        Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=rec.SyncKey && OwnerEmail=varCountOwner),
            {Synced:false,SyncError:FirstError.Message});false
    )
);
);
IfError(
 If(!varCountDiskSafeV21,Error({Kind:ErrorKind.Validation,Message:"Эх хадгалалтыг аюулгүй уншаагүй байна."}),
 ClearCollect(colCountDiskV21,{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)});
 SaveData(colCountDiskV21,varCountCacheKey)),
 Set(varCountStorageError,FirstError.Message),Set(varCountStorageError,""));
Set(varCountRemainingV27,CountRows(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)));
If(!IsEmpty(Filter(colToSync As q,!IsBlank(LookUp(colOfflineInventory,SyncKey=q.SyncKey,SyncError)))),
 Set(varCountRetryCountV27,Min(5,Coalesce(varCountRetryCountV27,0)+1));
 Set(varCountRetryAtV27,DateAdd(Now(),Min(300,15*Power(2,varCountRetryCountV27-1)),TimeUnit.Seconds)),
 Set(varCountRetryCountV27,0);Set(varCountRetryAtV27,Now()));
Set(varCountUploadQueue,varCountRemainingV27>0),
 Set(varCountStorageError,FirstError.Message);
 Set(varCountRetryAtV27,DateAdd(Now(),60,TimeUnit.Seconds)));
Set(varCountSyncBusy,false))

)
```

### `ScrCountHome/uploadQueueV16_10` . **PressedBorderColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/uploadQueueV16_10` . **PressedColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrCountHome/uploadQueueV16_10` . **PressedFill**  _(Timer@2.1.0)_
```powerfx
Self.Color
```

### `ScrCountHome/uploadQueueV16_10` . **Repeat**  _(Timer@2.1.0)_
```powerfx
true
```

### `ScrCountHome/uploadQueueV16_10` . **Reset**  _(Timer@2.1.0)_
```powerfx
!varRptPdfPending
```

### `ScrCountHome/uploadQueueV16_10` . **Size**  _(Timer@2.1.0)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrCountHome/uploadQueueV16_10` . **Start**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Connection.Connected && varCountCacheReady
)
```

### `ScrCountHome/uploadQueueV16_10` . **Visible**  _(Timer@2.1.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCountHome/pgDenied290` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrCountHome/pgDenied290` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrCountHome/pgDenied290` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrCountHome/pgDenied290` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCountHome/pgDenied290` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCountHome/pgDenied290` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCountHome/pgDenied290` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCountHome/pgDenied290` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrCountHome/pgDenied290` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrCountHome/pgDenied290` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

