# ScrReport1 — Power Fx formulas

### `ScrReport1` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrReport1` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrReport1` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Clear(colRRaw);Clear(colRLatest);Clear(colRItems);Clear(colRptVariance);Set(varRptMissingReasons,0);Set(varRptIncludeUncounted,App.Width<First(App.SizeBreakpoints).Value);Set(varReportTab,If(App.Width<First(App.SizeBreakpoints).Value,"Хураангуй","Бараагаар"));Set(varRptSettings,false); Set(varRptWarehouse,false); Set(varRptExportDialog,false); Set(varRptPdfPending,false); Set(varRptSending,false);
If(IsBlank(varRptStart),Set(varRptStart,Date(Year(Today()),Month(Today()),1))); If(IsBlank(varRptEnd),Set(varRptEnd,Today()));
If(IsBlank(varReportTab),Set(varReportTab,If(App.Width<First(App.SizeBreakpoints).Value,"Хураангуй","Бараагаар")));
If(Coalesce(varRptFixVersion,0)<>4,Set(varRptInitialized,false);Set(varRptFixVersion,4));
Select(Button10_2);Set(varRptDetail,false);Set(varRptStatus,"Бүгд");Set(varRptSortVariance,false);ClearCollect(colRptSearchItemsV16,{number:""});Clear(colRptSearchItemsV16);Reset(rptSearchV16);Set(mobReportMenu,false)
)
```

### `ScrReport1` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrReport1/rptPrintRootV24` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptPrintRootV24` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending,App.Height*630/700,935*(App.Height/1136))
```

### `ScrReport1/rptPrintRootV24` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((!varRptSettings) && !((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending) && varReportTab="Хураангуй"))
```

### `ScrReport1/rptPrintRootV24` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptPrintRootV24` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(250)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
(!varRptSettings) && !(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptPrintRootV24/rptHeader` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Visible**  _(Label@2.5.1)_
```powerfx
!varRptPdfPending
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Width**  _(Label@2.5.1)_
```powerfx
(140)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptClock` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **OnSelect**  _(Label@2.5.1)_
```powerfx
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
Set(varHistoryLoading,false));Select(Button10_2)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Text**  _(Label@2.5.1)_
```powerfx
If(varHistoryLoading,"ТАТАЖ БАЙНА…",!Connection.Connected,"ОФФЛАЙН","ОНЛАЙН ШИНЭЧЛЭХ ↻") & " · " & If(IsBlank(varRRefreshed),"—",Text(varRRefreshed,"hh:mm"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Visible**  _(Label@2.5.1)_
```powerfx
!varRptPdfPending
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Width**  _(Label@2.5.1)_
```powerfx
(230)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **X**  _(Label@2.5.1)_
```powerfx
((Parent.Width/((Min(App.Width,960)/640)))-260)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSync` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр',ScreenTransition.None)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(26)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varRptPdfPending
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(18)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(58)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(34)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(23)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Тооллогын тайлан"
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(530)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **X**  _(Label@2.5.1)_
```powerfx
(62)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(60)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Text**  _(Label@2.5.1)_
```powerfx
Switch(varReportTab,"Бараагаар","Бараа тус бүрийн зөрүү","Гүйцэтгэл","Агуулахаар тоолсон бүтэц","Зөрүү","Топ зөрүүтэй бараа","Өдрийн хураангуй")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(530)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **X**  _(Label@2.5.1)_
```powerfx
(62)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptSubTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(100)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptSettings,true)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Text(dpReportFrom.SelectedDate,"mm.dd") & " → " & Text(dpReportTo.SelectedDate,"mm.dd") & "        " & Text(DateDiff(dpReportFrom.SelectedDate,dpReportTo.SelectedDate,TimeUnit.Days)+1) & " хоног"
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(398)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptDateRange` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(137)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptWarehouse,true)
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(15)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Text(CountRows(colReportWarehouses)) & " агуулах"
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(170)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(442)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/btnWarehouseFilter` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(137)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(596)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(199)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Бараагаар",ColorValue("#FFFFFF"),ColorValue("#BAD0C4"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Бараагаар",ColorValue("#153F30"),ColorValue("#2B5343"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(43)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Бараагаар")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(15)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараагаар"
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(146)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(4)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(4)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Гүйцэтгэл",ColorValue("#FFFFFF"),ColorValue("#BAD0C4"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Гүйцэтгэл",ColorValue("#153F30"),ColorValue("#2B5343"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(43)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Гүйцэтгэл")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(15)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гүйцэтгэл"
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(146)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(151)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(4)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Зөрүү",ColorValue("#FFFFFF"),ColorValue("#BAD0C4"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Зөрүү",ColorValue("#153F30"),ColorValue("#2B5343"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(43)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Зөрүү")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(15)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зөрүү"
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(146)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(298)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(4)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Хураангуй",ColorValue("#FFFFFF"),ColorValue("#BAD0C4"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Хураангуй",ColorValue("#153F30"),ColorValue("#2B5343"))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(43)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Хураангуй")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(15)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хураангуй"
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(146)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(445)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptHeader/rptTabs/rptTab3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(4)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(655)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varReportTab="Хураангуй" && !varRptSettings && !varRptWarehouse
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptPrintRootV24/rptSummary` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(270)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(183)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Text**  _(Label@2.5.1)_
```powerfx
"ТААРСАН ХУВЬ"
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Width**  _(Label@2.5.1)_
```powerfx
(510)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroLabel` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Height**  _(Label@2.5.1)_
```powerfx
(65)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(48)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Text**  _(Label@2.5.1)_
```powerfx
With({n:CountRows(Filter(colRItems,ReportCounted && !ReportInvalid))},If(n=0,"—",Text(CountRows(Filter(colRItems,ReportCounted && !ReportInvalid && ReportVariance=0))/n,"0.0%")))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Width**  _(Label@2.5.1)_
```powerfx
(528)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptHeroValue` . **Y**  _(Label@2.5.1)_
```powerfx
(60)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#D34820")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#D34820")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStatus,"Зөрүүтэй");Set(varReportTab,"Бараагаар")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"зөрүүтэй " & CountRows(colRptVariance)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(180)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMismatchChip` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(137)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStatus,"Таарсан");Set(varReportTab,"Бараагаар")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"таарсан " & CountRows(Filter(colRItems,ReportCounted && !ReportInvalid && ReportVariance=0))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(180)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(222)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryHero/rptMatchedChip` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(137)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(280)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(199)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Text**  _(Label@2.5.1)_
```powerfx
"Тоолсон бараа–агуулах"
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Title` . **Y**  _(Label@2.5.1)_
```powerfx
(17)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Height**  _(Label@2.5.1)_
```powerfx
(41)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(29)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colRLatest),"#,##0")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Width**  _(Label@2.5.1)_
```powerfx
(244)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi0/rptKpi0Value` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(280)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(332)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(199)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Text**  _(Label@2.5.1)_
```powerfx
"Дутуу гарсан мөр"
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Title` . **Y**  _(Label@2.5.1)_
```powerfx
(17)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#B4472A")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Height**  _(Label@2.5.1)_
```powerfx
(41)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(29)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(Filter(colRItems,ReportCounted && !ReportInvalid && ReportVariance<0)),"#,##0")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Width**  _(Label@2.5.1)_
```powerfx
(244)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi1/rptKpi1Value` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(280)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(318)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Text**  _(Label@2.5.1)_
```powerfx
"Илүү гарсан мөр"
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Title` . **Y**  _(Label@2.5.1)_
```powerfx
(17)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Height**  _(Label@2.5.1)_
```powerfx
(41)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(29)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(Filter(colRItems,ReportCounted && !ReportInvalid && ReportVariance>0)),"#,##0")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Width**  _(Label@2.5.1)_
```powerfx
(244)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi2/rptKpi2Value` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(280)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(332)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(318)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Text**  _(Label@2.5.1)_
```powerfx
"Тайлбартай"
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Title` . **Y**  _(Label@2.5.1)_
```powerfx
(17)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Height**  _(Label@2.5.1)_
```powerfx
(41)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(29)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(Filter(colRLatest,!IsBlank(Trim(Coalesce(Comment,""))) || !IsBlank(Trim(Coalesce(Reason,""))))) & "/" & CountRows(colRLatest)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Width**  _(Label@2.5.1)_
```powerfx
(244)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptKpi3/rptKpi3Value` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(106)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(437)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(23)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Сонгосон агуулах"
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(450)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(15)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(colReportWarehouses)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Width**  _(Label@2.5.1)_
```powerfx
(44)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **X**  _(Label@2.5.1)_
```powerfx
(518)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenCount` . **Y**  _(Label@2.5.1)_
```powerfx
(15)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Height**  _(Label@2.5.1)_
```powerfx
(43)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptWarehouse,true)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsEmpty(colReportWarehouses),"Агуулах сонгоогүй",Concat(FirstN(colReportWarehouses,4),code," • ") & If(CountRows(colReportWarehouses)>4,"  +" & Text(CountRows(colReportWarehouses)-4) & " агуулах",""))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Width**  _(Label@2.5.1)_
```powerfx
(538)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptChosen/rptChosenList` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Height**  _(Label@2.5.1)_
```powerfx
(46)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Text**  _(Label@2.5.1)_
```powerfx
"Өөрийн тоолсон бараа–агуулахын хамгийн сүүлийн дүн. Тоолоогүй барааг тусдаа шүүлтээр нээнэ. " & If(varRptCloudError,"Онлайн шинэчлэлт амжилтгүй — төхөөрөмжийн түүхийг харуулж байна.","")
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Width**  _(Label@2.5.1)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptSummary/rptSummaryScope` . **Y**  _(Label@2.5.1)_
```powerfx
(562)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptItems` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptPrintRootV24/rptItems` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending,App.Height*531/700,(App.Height-430*(App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptItems` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varReportTab="Бараагаар" && !varRptSettings && !varRptWarehouse
```

### `ScrReport1/rptPrintRootV24/rptItems` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptPrintRootV24/rptItems` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending,App.Height*97/700,(270)*((App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"БАРАА · " & Text(CountRows(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true))),"#,##0")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsHeading` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width/2
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSortVariance,!varRptSortVariance)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **Text**  _(Label@2.5.1)_
```powerfx
If(varRptSortVariance,"Зөрүү ихээс ↓","Кодоор ↑") & "  ⇅"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width/2-16
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsCols` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width/2
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
Max(80,Parent.Height-130)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
If(varRptSortVariance,SortByColumns(AddColumns(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true)),SortMagnitude,Abs(Coalesce(ReportVariance,0))),"SortMagnitude",SortOrder.Descending,"ItemNo",SortOrder.Ascending),SortByColumns(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true)),"ItemNo",SortOrder.Ascending,"LocationCode",SortOrder.Ascending))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
156
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
Parent.Width-32
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **WrapCount**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,2,1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
122
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
152
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(18)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(18)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(18)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(18)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Parent.TemplateWidth-8
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemNo
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCode` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width-116
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemLocation` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width-100
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(ThisItem.ItemName,LookUp(colOfflineItems,number=ThisItem.ItemNo,displayName),"Нэр бүртгэгдээгүй")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemName` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width-28
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **Text**  _(Label@2.5.1)_
```powerfx
"Үлдэгдэл"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **Width**  _(Label@2.5.1)_
```powerfx
(Parent.Width-28)/3-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap0` . **X**  _(Label@2.5.1)_
```powerfx
14+(Parent.Width-28)*0/3
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:Coalesce(ThisItem.OpeningBalance,0)},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.###")))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **Width**  _(Label@2.5.1)_
```powerfx
(Parent.Width-28)/3-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **X**  _(Label@2.5.1)_
```powerfx
14+(Parent.Width-28)*0/3
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal0` . **Y**  _(Label@2.5.1)_
```powerfx
106
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **Text**  _(Label@2.5.1)_
```powerfx
"Тоолсон"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **Width**  _(Label@2.5.1)_
```powerfx
(Parent.Width-28)/3-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap1` . **X**  _(Label@2.5.1)_
```powerfx
14+(Parent.Width-28)*1/3
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **Text**  _(Label@2.5.1)_
```powerfx
If(ThisItem.ReportCounted,With({v:Coalesce(ThisItem.CountQty,0)},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.###"))),"—")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **Width**  _(Label@2.5.1)_
```powerfx
(Parent.Width-28)/3-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **X**  _(Label@2.5.1)_
```powerfx
14+(Parent.Width-28)*1/3
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal1` . **Y**  _(Label@2.5.1)_
```powerfx
106
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүү"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **Width**  _(Label@2.5.1)_
```powerfx
(Parent.Width-28)/3-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemCap2` . **X**  _(Label@2.5.1)_
```powerfx
14+(Parent.Width-28)*2/3
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **Color**  _(Label@2.5.1)_
```powerfx
If(ThisItem.ReportVariance<0,ColorValue("#D34820"),ColorValue("#2D7F50"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **Text**  _(Label@2.5.1)_
```powerfx
If(!ThisItem.ReportCounted,"Тоолоогүй",ThisItem.ReportInvalid,"Тоо дутуу",If(ThisItem.ReportVariance>0,"+","") & With({v:Coalesce(ThisItem.ReportVariance,0)},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.###"))))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **Width**  _(Label@2.5.1)_
```powerfx
(Parent.Width-28)/3-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **X**  _(Label@2.5.1)_
```powerfx
14+(Parent.Width-28)*2/3
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemsGallery/rptItemCard/rptItemVal2` . **Y**  _(Label@2.5.1)_
```powerfx
106
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(18)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Энэ шүүлтэд тохирох мөр алга. Хайлтаа арилгах эсвэл Бүгдийг сонгоно уу."
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width-32
```

### `ScrReport1/rptPrintRootV24/rptItems/rptItemEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
140
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **AccessibleLabel**  _(Classic/TextInput@2.3.2)_
```powerfx
"Тайлангийн бараа хайх"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#D5DFD9")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **DelayOutput**  _(Classic/TextInput@2.3.2)_
```powerfx
true
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Барааны код, нэр эсвэл агуулах хайх…"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
Clear(colRptSearchItemsV16)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **OnSelect**  _(Classic/TextInput@2.3.2)_
```powerfx
Set(varItem, Blank());
Set(varOpeningBalance, Blank());
Set(varBarcodeText, Blank());
Set(varJustSelected, false);

Set(varNewPicture, Blank());
Set(varItemPicture, Blank());
Set(varPictureResponse, Blank())
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **RadiusBottomLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **RadiusBottomRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **RadiusTopLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **RadiusTopRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptSearchV16` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Width-32
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Бүгд",ColorValue("#FFFFFF"),ColorValue("#153F30"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Бүгд",ColorValue("#153F30"),ColorValue("#E8EEEA"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStatus,"Бүгд");If(varRptIncludeUncounted,Set(varRptIncludeUncounted,false);Select(Button10_2))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тоолсон"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-32)/4-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+(Parent.Width-32)*0/4
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Зөрүүтэй",ColorValue("#FFFFFF"),ColorValue("#153F30"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Зөрүүтэй",ColorValue("#153F30"),ColorValue("#E8EEEA"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStatus,"Зөрүүтэй")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зөрүүтэй"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-32)/4-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+(Parent.Width-32)*1/4
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Таарсан",ColorValue("#FFFFFF"),ColorValue("#153F30"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Таарсан",ColorValue("#153F30"),ColorValue("#E8EEEA"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStatus,"Таарсан")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Таарсан"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-32)/4-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+(Parent.Width-32)*2/4
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Тоолоогүй",ColorValue("#FFFFFF"),ColorValue("#153F30"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStatus="Тоолоогүй",ColorValue("#153F30"),ColorValue("#E8EEEA"))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStatus,"Тоолоогүй");If(!varRptIncludeUncounted,Set(varRptIncludeUncounted,true);Select(Button10_2))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тоолоогүй"
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-32)/4-6
```

### `ScrReport1/rptPrintRootV24/rptItems/rptFilterV16_3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+(Parent.Width-32)*3/4
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending,App.Height*531/700,(655)*((App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varReportTab="Гүйцэтгэл" && !varRptSettings && !varRptWarehouse
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptPrintRootV24/rptPerformance` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending,App.Height*97/700,(270)*((App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(231)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"АГУУЛАХААР ТООЛСОН БҮТЭЦ"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(530)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCompositionTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **BorderThickness**  _(Image@2.2.3)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **FocusedBorderThickness**  _(Image@2.2.3)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **Height**  _(Image@2.2.3)_
```powerfx
(160)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl(varRptDonutSvg)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **PaddingBottom**  _(Image@2.2.3)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **PaddingLeft**  _(Image@2.2.3)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **PaddingRight**  _(Image@2.2.3)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **PaddingTop**  _(Image@2.2.3)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **RadiusBottomLeft**  _(Image@2.2.3)_
```powerfx
(8)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **RadiusBottomRight**  _(Image@2.2.3)_
```powerfx
(8)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **RadiusTopLeft**  _(Image@2.2.3)_
```powerfx
(8)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **RadiusTopRight**  _(Image@2.2.3)_
```powerfx
(8)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **Width**  _(Image@2.2.3)_
```powerfx
(182)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **X**  _(Image@2.2.3)_
```powerfx
(16)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonut` . **Y**  _(Image@2.2.3)_
```powerfx
(54)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Height**  _(Label@2.5.1)_
```powerfx
(35)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(23)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(colRLatest)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Width**  _(Label@2.5.1)_
```powerfx
(117)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **X**  _(Label@2.5.1)_
```powerfx
(48)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutValue` . **Y**  _(Label@2.5.1)_
```powerfx
(112)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(10)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Text**  _(Label@2.5.1)_
```powerfx
"бараа–агуулах"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Width**  _(Label@2.5.1)_
```powerfx
(137)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **X**  _(Label@2.5.1)_
```powerfx
(38)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptDonutUnit` . **Y**  _(Label@2.5.1)_
```powerfx
(147)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **Height**  _(Gallery@2.15.0)_
```powerfx
(157)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **Items**  _(Gallery@2.15.0)_
```powerfx
colRptCategories
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(26)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **Width**  _(Gallery@2.15.0)_
```powerfx
(336)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **X**  _(Gallery@2.15.0)_
```powerfx
(220)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend` . **Y**  _(Gallery@2.15.0)_
```powerfx
(58)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue(Switch(ThisItem.SliceIndex,1,"#153F30",2,"#2D7F50",3,"#5BA97A",4,"#9CCFB0","#D8E8DE"))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Height**  _(Label@2.5.1)_
```powerfx
(23)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Text**  _(Label@2.5.1)_
```powerfx
"●"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Width**  _(Label@2.5.1)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **X**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryDot` . **Y**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Category
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Width**  _(Label@2.5.1)_
```powerfx
(206)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **X**  _(Label@2.5.1)_
```powerfx
(27)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryName` . **Y**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Share,"0") & "%"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Width**  _(Label@2.5.1)_
```powerfx
(65)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **X**  _(Label@2.5.1)_
```powerfx
(250)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptComposition/rptCategoryLegend/rptCategoryShare` . **Y**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(180)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(247)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"АЖИЛТАН"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Width**  _(Label@2.5.1)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleHeading` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(100)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colRptPeople
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(8)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(60)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(63)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(17)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Counter
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Width**  _(Label@2.5.1)_
```powerfx
(428)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **X**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPerson` . **Y**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(18)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Total
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Width**  _(Label@2.5.1)_
```powerfx
(60)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **X**  _(Label@2.5.1)_
```powerfx
(450)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTotal` . **Y**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(7)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(508)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonTrack` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(36)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(7)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(If(CountRows(colRLatest)=0,0,508*ThisItem.Total/CountRows(colRLatest)))*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptPeople/rptPeopleGallery/rptPersonBar` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(36)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(133)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(443)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Гүйцэтгэл"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(19)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Height**  _(Label@2.5.1)_
```powerfx
(39)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(29)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsEmpty(colRStock) || IsEmpty(colRItems),"—",Text(CountRows(colRLatest)/CountRows(colRItems),"0%"))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Width**  _(Label@2.5.1)_
```powerfx
(230)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageVal` . **Y**  _(Label@2.5.1)_
```powerfx
(53)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Давтан тоолсон"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **X**  _(Label@2.5.1)_
```powerfx
(315)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(19)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(29)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(Filter(colRItems,ReportRepeat>1)),"#,##0")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **X**  _(Label@2.5.1)_
```powerfx
(315)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeVal` . **Y**  _(Label@2.5.1)_
```powerfx
(53)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(12)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Text**  _(Label@2.5.1)_
```powerfx
"бараа–агуулахын мөр"
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Width**  _(Label@2.5.1)_
```powerfx
(242)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **X**  _(Label@2.5.1)_
```powerfx
(315)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptTimeHint` . **Y**  _(Label@2.5.1)_
```powerfx
(95)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(7)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(240)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageTrack` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(105)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(7)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(3)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(If(IsEmpty(colRItems) || IsEmpty(colRStock),0,240*CountRows(colRLatest)/CountRows(colRItems)))*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverage/rptCoverageBar` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(105)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Height**  _(Label@2.5.1)_
```powerfx
(54)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Text**  _(Label@2.5.1)_
```powerfx
"Хамралт: төхөөрөмжид татсан үлдэгдэл ба өөрийн тоолсон бараа–агуулах. Түүхэн төлөвлөгөөний хувь биш."
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Width**  _(Label@2.5.1)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptPerformance/rptCoverageHint` . **Y**  _(Label@2.5.1)_
```powerfx
(594)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending,App.Height*531/700,(665)*((App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varReportTab="Зөрүү" && !varRptSettings && !varRptWarehouse
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptPrintRootV24/rptVariance` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending,App.Height*97/700,(270)*((App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(440)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"ТОП ЗӨРҮҮТЭЙ БАРАА"
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(372)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Text**  _(Label@2.5.1)_
```powerfx
"log масштаб"
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Width**  _(Label@2.5.1)_
```powerfx
(130)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **X**  _(Label@2.5.1)_
```powerfx
(430)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptLogScale` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(350)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
FirstN(colRptVariance,6)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(8)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(47)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(64)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemNo & " · " & Coalesce(ThisItem.ItemName,"")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Width**  _(Label@2.5.1)_
```powerfx
(379)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **X**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceItem` . **Y**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(ThisItem.ReportVariance<0,ColorValue("#D34820"),ColorValue("#2D7F50"))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSelectedItem,ThisItem.ItemNo);Set(varRptSelectedLocation,ThisItem.LocationCode);Set(varRptDetail,true)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(15)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Text**  _(Label@2.5.1)_
```powerfx
If(ThisItem.ReportVariance>0,"+","") & With({v:Coalesce(ThisItem.ReportVariance,0)},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.###")))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Width**  _(Label@2.5.1)_
```powerfx
(127)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **X**  _(Label@2.5.1)_
```powerfx
(385)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceQty` . **Y**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(9)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(512)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceTrack` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(31)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(ThisItem.ReportVariance<0,ColorValue("#D34820"),ColorValue("#2D7F50"))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(9)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(If(IsEmpty(colRptVariance),0,512*Log(1+ThisItem.AbsVariance)/Log(1+Max(colRptVariance,AbsVariance))))*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceGallery/rptVarianceBar` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(31)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(17)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүтэй бүртгэл алга"
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(colRptVariance)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceCard/rptVarianceEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(90)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F8F0EC")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(151)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(458)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#D34820")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"АНХААРАХ"
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Width**  _(Label@2.5.1)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningHeading` . **Y**  _(Label@2.5.1)_
```powerfx
(18)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Height**  _(Label@2.5.1)_
```powerfx
(78)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Text**  _(Label@2.5.1)_
```powerfx
"Тайлбаргүй " & varRptMissingReasons & " зөрүүтэй мөр. (+) илүү, (−) дутуу. Барааг сонгож тооллогын түүхийг харна уу."
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Width**  _(Label@2.5.1)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPrintRootV24/rptVariance/rptVarianceWarning/rptWarningBody` . **Y**  _(Label@2.5.1)_
```powerfx
(54)*((App.Height/1136))
```

### `ScrReport1/rptFooter` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(158)*((App.Height/1136))
```

### `ScrReport1/rptFooter` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((!varRptSettings && !varRptWarehouse && !varRptPdfPending) && !(App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending))
```

### `ScrReport1/rptFooter` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptFooter` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrReport1/rptFooter` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Height/((App.Height/1136)))-158)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptExcel` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptExcel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptExcel` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrReport1/rptFooter/rptExcel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptExcel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptExcel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(57)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptExcel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptExcel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptExcel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptExportMode,"CSV");Set(varRptExportDialog,true)
```

### `ScrReport1/rptFooter/rptExcel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptExcel` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptExcel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptExcel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptExcel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptExcel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(17*(Min(App.Width,960)/640),21*(App.Height/1136))
```

### `ScrReport1/rptFooter/rptExcel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"CSV · мэйл"
```

### `ScrReport1/rptFooter/rptExcel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
125*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptExcel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
22*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptExcel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(15)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptPdf` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptPdf` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptPdf` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrReport1/rptFooter/rptPdf` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptPdf` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptPdf` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(57)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptPdf` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptPdf` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptPdf` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Бараагаар",Set(varRptExportMode,"CSV"),Set(varRptExportMode,"PDF"));Set(varRptExportDialog,true)
```

### `ScrReport1/rptFooter/rptPdf` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptPdf` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptPdf` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptPdf` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptPdf` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptPdf` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(17*(Min(App.Width,960)/640),21*(App.Height/1136))
```

### `ScrReport1/rptFooter/rptPdf` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Бараагаар","CSV","PDF")
```

### `ScrReport1/rptFooter/rptPdf` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
125*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptPdf` . **X**  _(Classic/Button@2.2.0)_
```powerfx
157*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptPdf` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(15)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptPptV24` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptPptV24` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptPptV24` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrReport1/rptFooter/rptPptV24` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptPptV24` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptPptV24` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(57)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptPptV24` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptPptV24` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptPptV24` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!IsBlank(varRptPptUrlV24),Launch(varRptPptUrlV24),Set(varRptExportMode,"PPTX");Set(varRptExportDialog,true))
```

### `ScrReport1/rptFooter/rptPptV24` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptPptV24` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptPptV24` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptPptV24` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptPptV24` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptPptV24` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(17*(Min(App.Width,960)/640),21*(App.Height/1136))
```

### `ScrReport1/rptFooter/rptPptV24` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(!IsBlank(varRptPptUrlV24),"PPTX нээх","PowerPoint")
```

### `ScrReport1/rptFooter/rptPptV24` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
"Сонгосон хугацааны графиктай PowerPoint тайлан"
```

### `ScrReport1/rptFooter/rptPptV24` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
124*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptPptV24` . **X**  _(Classic/Button@2.2.0)_
```powerfx
292*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptPptV24` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(15)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptMail` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptMail` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptMail` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrReport1/rptFooter/rptMail` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptFooter/rptMail` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptMail` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(57)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptMail` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptMail` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptFooter/rptMail` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptExportMode,If(varReportTab="Бараагаар","CSV","PDF"));Set(varRptExportDialog,true)
```

### `ScrReport1/rptFooter/rptMail` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptMail` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptMail` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptMail` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptMail` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptMail` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(17*(Min(App.Width,960)/640),21*(App.Height/1136))
```

### `ScrReport1/rptFooter/rptMail` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэйл + хавсралт"
```

### `ScrReport1/rptFooter/rptMail` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
192*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptMail` . **X**  _(Classic/Button@2.2.0)_
```powerfx
426*(Min(App.Width,960)/640)
```

### `ScrReport1/rptFooter/rptMail` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(15)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptNav0` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNav0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptNav0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNav0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(73)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptNav0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNav0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(scrWarehouses,ScreenTransition.None)
```

### `ScrReport1/rptFooter/rptNav0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav0` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptNav0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptNav0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNav0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(82)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Тооллого эхлэх"
```

### `ScrReport1/rptFooter/rptNavIcon0` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavIcon0` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNavIcon0` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavIcon0` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Scan
```

### `ScrReport1/rptFooter/rptNavIcon0` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate(scrWarehouses,ScreenTransition.None)
```

### `ScrReport1/rptFooter/rptNavIcon0` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon0` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(88)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrReport1/rptFooter/rptNavLabel0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavLabel0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavLabel0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Navigate(scrWarehouses,ScreenTransition.None)
```

### `ScrReport1/rptFooter/rptNavLabel0` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Text**  _(Label@2.5.1)_
```powerfx
"Скан"
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Width**  _(Label@2.5.1)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **X**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel0` . **Y**  _(Label@2.5.1)_
```powerfx
(127)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptNav1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNav1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptNav1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNav1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(73)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptNav1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNav1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrHistory,ScreenTransition.None)
```

### `ScrReport1/rptFooter/rptNav1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptNav1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptNav1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNav1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(82)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Тооллогын түүх"
```

### `ScrReport1/rptFooter/rptNavIcon1` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavIcon1` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNavIcon1` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavIcon1` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.History
```

### `ScrReport1/rptFooter/rptNavIcon1` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate(ScrHistory,ScreenTransition.None)
```

### `ScrReport1/rptFooter/rptNavIcon1` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(224)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon1` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(88)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrReport1/rptFooter/rptNavLabel1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavLabel1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavLabel1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Navigate(ScrHistory,ScreenTransition.None)
```

### `ScrReport1/rptFooter/rptNavLabel1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Text**  _(Label@2.5.1)_
```powerfx
"Түүх"
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Width**  _(Label@2.5.1)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **X**  _(Label@2.5.1)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel1` . **Y**  _(Label@2.5.1)_
```powerfx
(127)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptNav2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptFooter/rptNav2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptNav2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNav2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(73)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptNav2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptFooter/rptNav2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptSettings,false)
```

### `ScrReport1/rptFooter/rptNav2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptNav2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptNav2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNav2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(320)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(82)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavIcon2` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptFooter/rptNavIcon2` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavIcon2` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.TrendingUpwards
```

### `ScrReport1/rptFooter/rptNavIcon2` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(varRptSettings,false)
```

### `ScrReport1/rptFooter/rptNavIcon2` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(384)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon2` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(88)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrReport1/rptFooter/rptNavLabel2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavLabel2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavLabel2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSettings,false)
```

### `ScrReport1/rptFooter/rptNavLabel2` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Text**  _(Label@2.5.1)_
```powerfx
"Тайлан"
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Width**  _(Label@2.5.1)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **X**  _(Label@2.5.1)_
```powerfx
(320)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel2` . **Y**  _(Label@2.5.1)_
```powerfx
(127)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptFooter/rptNav3` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNav3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptFooter/rptNav3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNav3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(73)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptFooter/rptNav3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNav3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptSettings,true)
```

### `ScrReport1/rptFooter/rptNav3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav3` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptFooter/rptNav3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptFooter/rptNav3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptFooter/rptNav3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNav3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNav3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(480)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNav3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(82)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavIcon3` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNavIcon3` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavIcon3` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Settings
```

### `ScrReport1/rptFooter/rptNavIcon3` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(varRptSettings,true)
```

### `ScrReport1/rptFooter/rptNavIcon3` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(544)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavIcon3` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(88)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrReport1/rptFooter/rptNavLabel3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptFooter/rptNavLabel3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptFooter/rptNavLabel3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSettings,true)
```

### `ScrReport1/rptFooter/rptNavLabel3` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Text**  _(Label@2.5.1)_
```powerfx
"Тохиргоо"
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Width**  _(Label@2.5.1)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **X**  _(Label@2.5.1)_
```powerfx
(480)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptFooter/rptNavLabel3` . **Y**  _(Label@2.5.1)_
```powerfx
(127)*((App.Height/1136))
```

### `ScrReport1/rptSettings` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptSettings` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ScrReport1/rptSettings` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varRptSettings)
```

### `ScrReport1/rptSettings` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptSettings` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrReport1/rptSettings` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(125)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Width/((Min(App.Width,960)/640))))*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(24)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Тайлангийн тохиргоо"
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(58)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Text**  _(Label@2.5.1)_
```powerfx
"хугацаа · агуулах · төрөл"
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Width**  _(Label@2.5.1)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptSettingsHeader/rptSettingsSubtitle` . **Y**  _(Label@2.5.1)_
```powerfx
(97)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptDateCard` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(163)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(148)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"ХУГАЦАА"
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptDateTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(18)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStart=Date(Year(Today()),Month(Today()),1) && varRptEnd=Today(),ColorValue("#FFFFFF"),ColorValue("#86968F"))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStart=Date(Year(Today()),Month(Today()),1) && varRptEnd=Today(),ColorValue("#153F30"),ColorValue("#E9EEEB"))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStart,Date(Year(Today()),Month(Today()),1));Set(varRptEnd,Today());Reset(dpReportFrom);Reset(dpReportTo);Select(Button10_2)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ сар"
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(122)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(53)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStart=DateAdd(Today(),-6,TimeUnit.Days) && varRptEnd=Today(),ColorValue("#FFFFFF"),ColorValue("#86968F"))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStart=DateAdd(Today(),-6,TimeUnit.Days) && varRptEnd=Today(),ColorValue("#153F30"),ColorValue("#E9EEEB"))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStart,DateAdd(Today(),-6,TimeUnit.Days));Set(varRptEnd,Today());Reset(dpReportFrom);Reset(dpReportTo);Select(Button10_2)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"7 хоног"
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(122)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(156)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(53)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStart=Today() && varRptEnd=Today(),ColorValue("#FFFFFF"),ColorValue("#86968F"))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptStart=Today() && varRptEnd=Today(),ColorValue("#153F30"),ColorValue("#E9EEEB"))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptStart,Today());Set(varRptEnd,Today());Reset(dpReportFrom);Reset(dpReportTo);Select(Button10_2)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Өнөөдөр"
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(122)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(288)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(53)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptCustomDates,true)
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Сонгох"
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(122)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(420)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/rptPreset3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(53)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(If(Coalesce(varRptCustomDates,false),1,0))*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Color**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **DefaultDate**  _(Classic/DatePicker@2.6.0)_
```powerfx
varRptStart
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Fill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Format**  _(Classic/DatePicker@2.6.0)_
```powerfx
"yyyy.mm.dd"
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
(38)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **OnChange**  _(Classic/DatePicker@2.6.0)_
```powerfx
Set(varRptStart,Self.SelectedDate);Select(Button10_2)
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **PaddingBottom**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **PaddingTop**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
Max(12,(17)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
(250)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportFrom` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
(111)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(If(Coalesce(varRptCustomDates,false),1,0))*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Color**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **DefaultDate**  _(Classic/DatePicker@2.6.0)_
```powerfx
varRptEnd
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Fill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Format**  _(Classic/DatePicker@2.6.0)_
```powerfx
"yyyy.mm.dd"
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
(38)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **OnChange**  _(Classic/DatePicker@2.6.0)_
```powerfx
Set(varRptEnd,Self.SelectedDate);Select(Button10_2)
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **PaddingBottom**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **PaddingTop**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
Max(12,(17)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
(250)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
(310)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptDateCard/dpReportTo` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
(111)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(422)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(329)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"АГУУЛАХ"
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(360)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(colReportWarehouses) & " агуулах"
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Width**  _(Label@2.5.1)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **X**  _(Label@2.5.1)_
```powerfx
(399)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptWarehouseCount` . **Y**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(341)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colRptWarehouses
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(8)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(548)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(18)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(63)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **BorderColor**  _(Classic/CheckBox@2.1.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **BorderThickness**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **CheckboxBackgroundFill**  _(Classic/CheckBox@2.1.0)_
```powerfx
If(Self.Value,ColorValue("#2D7F50"),ColorValue("#FFFFFF"))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **CheckboxBorderColor**  _(Classic/CheckBox@2.1.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **CheckmarkFill**  _(Classic/CheckBox@2.1.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Color**  _(Classic/CheckBox@2.1.0)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Default**  _(Classic/CheckBox@2.1.0)_
```powerfx
ThisItem.Code in colReportWarehouses.code
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **FocusedBorderThickness**  _(Classic/CheckBox@2.1.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Font**  _(Classic/CheckBox@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **FontWeight**  _(Classic/CheckBox@2.1.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Height**  _(Classic/CheckBox@2.1.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **HoverColor**  _(Classic/CheckBox@2.1.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **OnCheck**  _(Classic/CheckBox@2.1.0)_
```powerfx
If(!(ThisItem.Code in colReportWarehouses.code),Collect(colReportWarehouses,{code:ThisItem.Code}))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **OnUncheck**  _(Classic/CheckBox@2.1.0)_
```powerfx
RemoveIf(colReportWarehouses,code=ThisItem.Code)
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **PaddingBottom**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **PaddingLeft**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **PaddingRight**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **PaddingTop**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Size**  _(Classic/CheckBox@2.1.0)_
```powerfx
Max(12,(17)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Text**  _(Classic/CheckBox@2.1.0)_
```powerfx
ThisItem.Code
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Width**  _(Classic/CheckBox@2.1.0)_
```powerfx
((Parent.TemplateWidth/((Min(App.Width,960)/640)))-8)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **X**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptWarehouseCard/rptSettingsWarehouseGallery/rptSettingsWarehouseCheck` . **Y**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptTypeCard` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(165)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(769)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"ТАЙЛАНГИЙН ТӨРӨЛ"
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(536)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptTypeTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(18)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Бараагаар",ColorValue("#FFFFFF"),ColorValue("#86968F"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Бараагаар",ColorValue("#153F30"),ColorValue("#FFFFFF"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Бараагаар")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараагаар"
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(152)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(58)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Гүйцэтгэл",ColorValue("#FFFFFF"),ColorValue("#86968F"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Гүйцэтгэл",ColorValue("#153F30"),ColorValue("#FFFFFF"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Гүйцэтгэл")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гүйцэтгэл"
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(152)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(188)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(58)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Зөрүү",ColorValue("#FFFFFF"),ColorValue("#86968F"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Зөрүү",ColorValue("#153F30"),ColorValue("#FFFFFF"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Зөрүү")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зөрүү"
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(152)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(352)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(58)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Хураангуй",ColorValue("#FFFFFF"),ColorValue("#86968F"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Хураангуй",ColorValue("#153F30"),ColorValue("#FFFFFF"))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Хураангуй")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хураангуй"
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(152)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptTypeCard/rptType3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(106)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSettings/rptApply` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptApply` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSettings/rptApply` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSettings/rptApply` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptApply` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(77)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSettings/rptApply` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptApply` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSettings/rptApply` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(dpReportFrom.SelectedDate>dpReportTo.SelectedDate,Notify("Огнооны муж буруу байна.",NotificationType.Warning),Select(Button10_2);Set(varRptSettings,false))
```

### `ScrReport1/rptSettings/rptApply` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptApply` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptApply` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSettings/rptApply` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSettings/rptApply` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSettings/rptApply` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptApply` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(22)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptApply` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тайлан харах                         ›"
```

### `ScrReport1/rptSettings/rptApply` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(596)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptApply` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(22)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptApply` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
((Parent.Height/((App.Height/1136)))-136)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptUser` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSettings/rptUser` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptUser` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSettings/rptUser` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSettings/rptUser` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSettings/rptUser` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSettings/rptUser` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptUser` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptUser` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptUser` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptUser` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSettings/rptUser` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(12)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSettings/rptUser` . **Text**  _(Label@2.5.1)_
```powerfx
User().Email & " · өөрийн тооллого"
```

### `ScrReport1/rptSettings/rptUser` . **Width**  _(Label@2.5.1)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptUser` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSettings/rptUser` . **Y**  _(Label@2.5.1)_
```powerfx
((Parent.Height/((App.Height/1136)))-43)*((App.Height/1136))
```

### `ScrReport1/rptShade` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptShade` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptShade` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
RGBA(10,28,20,0.5)
```

### `ScrReport1/rptShade` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ScrReport1/rptShade` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptShade` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptShade` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptShade` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptShade` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varRptWarehouse)
```

### `ScrReport1/rptShade` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Width/((Min(App.Width,960)/640))))*((Min(App.Width,960)/640))
```

### `ScrReport1/rptShade` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptShade` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSheet` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSheet` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptSheet` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(570)*((App.Height/1136))
```

### `ScrReport1/rptSheet` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(28)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(28)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(28)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(28)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varRptWarehouse)
```

### `ScrReport1/rptSheet` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width,960)
```

### `ScrReport1/rptSheet` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrReport1/rptSheet` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Height/((App.Height/1136)))-570)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSheet/rptSheetTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSheet/rptSheetTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSheet/rptSheetTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(36)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,(23)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Агуулах сонгох"
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(400)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*((App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F6F8F7")
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(Button10_2);Set(varRptWarehouse,false)
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(16)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"болсон"
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(120)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(492)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/btnWarehouseDone` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(21)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSheet/rptSelectAll` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSheet/rptSelectAll` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSheet/rptSelectAll` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptSheet/rptSelectAll` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSheet/rptSelectAll` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSheet/rptSelectAll` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSheet/rptSelectAll` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptSheet/rptSelectAll` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
ClearCollect(colReportWarehouses,ForAll(colRptWarehouses,{code:Code}))
```

### `ScrReport1/rptSheet/rptSelectAll` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectAll` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectAll` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSheet/rptSelectAll` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSheet/rptSelectAll` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSheet/rptSelectAll` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectAll` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSheet/rptSelectAll` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"бүгдийг"
```

### `ScrReport1/rptSheet/rptSelectAll` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(120)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectAll` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectAll` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(78)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSheet/rptSelectNone` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSheet/rptSelectNone` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptSheet/rptSelectNone` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptSheet/rptSelectNone` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSheet/rptSelectNone` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptSheet/rptSelectNone` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptSheet/rptSelectNone` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E9EEEB")
```

### `ScrReport1/rptSheet/rptSelectNone` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Clear(colReportWarehouses)
```

### `ScrReport1/rptSheet/rptSelectNone` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectNone` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectNone` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptSheet/rptSelectNone` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSheet/rptSelectNone` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptSheet/rptSelectNone` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSelectNone` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(14)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSheet/rptSelectNone` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"цэвэрлэх"
```

### `ScrReport1/rptSheet/rptSelectNone` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(130)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectNone` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(160)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSelectNone` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(78)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSheet/rptSheetCard` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSheet/rptSheetCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(398)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(20)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(584)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(28)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(139)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(372)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colRptWarehouses
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(8)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(48)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(548)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(18)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(12)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **BorderColor**  _(Classic/CheckBox@2.1.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **BorderThickness**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **CheckboxBackgroundFill**  _(Classic/CheckBox@2.1.0)_
```powerfx
If(Self.Value,ColorValue("#2D7F50"),ColorValue("#FFFFFF"))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **CheckboxBorderColor**  _(Classic/CheckBox@2.1.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **CheckmarkFill**  _(Classic/CheckBox@2.1.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Color**  _(Classic/CheckBox@2.1.0)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Default**  _(Classic/CheckBox@2.1.0)_
```powerfx
ThisItem.Code in colReportWarehouses.code
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **FocusedBorderThickness**  _(Classic/CheckBox@2.1.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Font**  _(Classic/CheckBox@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **FontWeight**  _(Classic/CheckBox@2.1.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Height**  _(Classic/CheckBox@2.1.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **HoverColor**  _(Classic/CheckBox@2.1.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **OnCheck**  _(Classic/CheckBox@2.1.0)_
```powerfx
If(!(ThisItem.Code in colReportWarehouses.code),Collect(colReportWarehouses,{code:ThisItem.Code}))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **OnUncheck**  _(Classic/CheckBox@2.1.0)_
```powerfx
RemoveIf(colReportWarehouses,code=ThisItem.Code)
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **PaddingBottom**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **PaddingLeft**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **PaddingRight**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **PaddingTop**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Size**  _(Classic/CheckBox@2.1.0)_
```powerfx
Max(12,(17)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Text**  _(Classic/CheckBox@2.1.0)_
```powerfx
ThisItem.Code
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Width**  _(Classic/CheckBox@2.1.0)_
```powerfx
((Parent.TemplateWidth/((Min(App.Width,960)/640)))-8)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **X**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptSheet/rptSheetCard/rptSheetGallery/rptSheetCheck` . **Y**  _(Classic/CheckBox@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/Button10_2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/Button10_2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/Button10_2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/Button10_2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/Button10_2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/Button10_2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/Button10_2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/Button10_2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ScrReport1/Button10_2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/Button10_2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/Button10_2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/Button10_2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptPptUrlV24,Blank());Set(varRptCloudError,Coalesce(varHistoryCloudError,false));Set(varRptCloudLimit,Coalesce(varHistoryCloudLimit,false));ClearCollect(colRptSource,AddColumns(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Coalesce(Archived,false)),RptPriority,1));
ClearCollect(colRptWarehouseCodes,ForAll(Distinct(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),!IsBlank(locationCode)),locationCode) As w,{Code:Trim(w.Value)}));
Collect(colRptWarehouseCodes,ForAll(colRptSource As w,{Code:Trim(w.LocationCode)}));
ClearCollect(colRptWarehouses,SortByColumns(DropColumns(GroupBy(Filter(colRptWarehouseCodes,!IsBlank(Code)),Code,WarehouseRows),WarehouseRows),"Code",SortOrder.Ascending));
If(!Coalesce(varRptInitialized,false),ClearCollect(colReportWarehouses,ForAll(colRptWarehouses As w,{code:w.Code}));Set(varRptInitialized,true));
RemoveIf(colReportWarehouses,IsBlank(code) || !(code in colRptWarehouses.Code));
If(varRptCloudError,Notify("Онлайн тооллогыг уншиж чадсангүй. Төхөөрөмжийн бүртгэлийг харуулж байна.",NotificationType.Warning));
Set(varRInvalidDates, IsBlank(dpReportFrom.SelectedDate) || IsBlank(dpReportTo.SelectedDate) || dpReportFrom.SelectedDate > dpReportTo.SelectedDate);
Clear(colRRaw); Clear(colRLatest); Clear(colRStock); Clear(colRItems);
If(varRInvalidDates,
    Notify("Эхлэх болон дуусах огноогоо зөв сонгоно уу.", NotificationType.Warning),
    ClearCollect(colRRaw, Filter(colRptSource,
        OwnerEmail=varCountOwner && !IsBlank(ItemNo) &&
        CountDate >= dpReportFrom.SelectedDate && CountDate < DateAdd(dpReportTo.SelectedDate,1,TimeUnit.Days) &&
        (LocationCode in colReportWarehouses.code)));
    ClearCollect(colRLatest, ForAll(GroupBy(colRRaw, ItemNo, LocationCode, ReportHistory) As g,
        Patch(First(SortByColumns(g.ReportHistory,"CountDate",SortOrder.Descending,"RptPriority",SortOrder.Descending,"SyncKey",SortOrder.Descending)),
            {ItemNo:g.ItemNo, LocationCode:g.LocationCode,ReportHistoryCount:CountRows(g.ReportHistory)})));
    If(Coalesce(varRptIncludeUncounted,false),ClearCollect(colRStock, Filter(AddColumns(GroupBy(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),
        !IsBlank(itemNo) && (locationCode in colReportWarehouses.code)),
        itemNo, locationCode, ReportStockRows), ReportStockQty, Sum(ReportStockRows,quantity)), ReportStockQty <> 0)));
    ClearCollect(colRItemCandidatesV16, ForAll(colRLatest As r,
        {ItemNo:r.ItemNo, ItemName:r.ItemName, LocationCode:r.LocationCode,
         OpeningBalance:r.OpeningBalance, CountQty:r.CountQty,
         ReportVariance:r.CountQty-r.OpeningBalance, ReportCounted:true,ReportPriority:1,
         CountDate:r.CountDate, Counter:r.Counter, Reason:r.Reason, Comment:r.Comment,
         ReportInvalid:IsBlank(r.CountQty) || IsBlank(r.OpeningBalance),
         ReportRepeat:r.ReportHistoryCount}));
    Collect(colRItemCandidatesV16, ForAll(colRStock As s,
        {ItemNo:s.itemNo, ItemName:"", LocationCode:s.locationCode,
         OpeningBalance:s.ReportStockQty, CountQty:Blank(), ReportVariance:Blank(), ReportCounted:false,ReportPriority:0,
         CountDate:Blank(), Counter:"", Reason:"", Comment:"", ReportInvalid:false, ReportRepeat:0}));
    ClearCollect(colRItems,ForAll(GroupBy(colRItemCandidatesV16,ItemNo,LocationCode,ReportCandidates) As g,
        Patch(First(SortByColumns(g.ReportCandidates,"ReportPriority",SortOrder.Descending)),{ItemNo:g.ItemNo,LocationCode:g.LocationCode})));
    Set(varRRefreshed,Now())
);
ClearCollect(colRptVariance, SortByColumns(AddColumns(Filter(colRItems,ReportCounted && !ReportInvalid && ReportVariance<>0),AbsVariance,Abs(ReportVariance)),"AbsVariance",SortOrder.Descending));
ClearCollect(colRptCategoryRaw,SortByColumns(AddColumns(GroupBy(AddColumns(colRLatest As r,RCategory,Coalesce(r.LocationCode,"Байршилгүй")),RCategory,RCategoryRows),Total,CountRows(RCategoryRows)),"Total",SortOrder.Descending));
ClearCollect(colRptCategoryTop,ForAll(FirstN(colRptCategoryRaw,4),{Category:RCategory,Total:Total}));
If(CountRows(colRptCategoryRaw)>4,Collect(colRptCategoryTop,{Category:"Бусад агуулах",Total:Sum(colRptCategoryRaw,Total)-Sum(colRptCategoryTop,Total)}));
ClearCollect(colRptCategories,ForAll(Sequence(CountRows(colRptCategoryTop)) As s,With({r:Last(FirstN(colRptCategoryTop,s.Value))},{Category:r.Category,Total:r.Total,SliceIndex:s.Value,Share:If(CountRows(colRLatest)>0,r.Total/CountRows(colRLatest)*100,0),Offset:If(CountRows(colRLatest)>0,Sum(FirstN(colRptCategoryTop,s.Value-1),Total)/CountRows(colRLatest)*100,0)})));
ClearCollect(colRptPeople,AddColumns(GroupBy(ForAll(colRLatest As own,Patch(own,{Counter:If(own.OwnerEmail=varCountOwner,User().FullName,own.Counter)})),Counter,RPersonRows),Total,CountRows(RPersonRows)));
Set(varRptDonutSvg,"<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220' viewBox='0 0 220 220'><circle cx='110' cy='110' r='76' fill='none' stroke='#E9EEEB' stroke-width='30'/>" & Concat(colRptCategories,"<circle cx='110' cy='110' r='76' pathLength='100' fill='none' stroke='" & Switch(SliceIndex,1,"#153F30",2,"#2D7F50",3,"#5BA97A",4,"#9CCFB0","#D8E8DE") & "' stroke-width='30' stroke-dasharray='" & Text(Share,"0.0000","en-US") & " 100' stroke-dashoffset='" & Text(-Offset,"0.0000","en-US") & "' transform='rotate(-90 110 110)'/>") & "</svg>");
Set(varRptMissingReasons,CountRows(Filter(colRptVariance,IsBlank(Trim(Coalesce(Reason,""))) && IsBlank(Trim(Coalesce(Comment,""))))));Clear(colRItemCandidatesV16);Clear(colRptWarehouseCodes)
```

### `ScrReport1/Button10_2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/Button10_2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/Button10_2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/Button10_2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/Button10_2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/Button10_2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/Button10_2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/Button10_2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/Button10_2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/Button10_2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/Button10_2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/Button10_2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(18)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/Button10_2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Шинэчлэх"
```

### `ScrReport1/Button10_2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrReport1/Button10_2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(1)*((Min(App.Width,960)/640))
```

### `ScrReport1/Button10_2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/Button10_2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptExportShade` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptExportShade` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportShade` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
RGBA(10,28,20,0.5)
```

### `ScrReport1/rptExportShade` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ScrReport1/rptExportShade` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportShade` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportShade` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportShade` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportShade` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varRptExportDialog)
```

### `ScrReport1/rptExportShade` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
((Parent.Width/((Min(App.Width,960)/640))))*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportShade` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportShade` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptExportModal` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptExportModal` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptExportModal` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Height*0.90,440*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrReport1/rptExportModal` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varRptExportDialog)
```

### `ScrReport1/rptExportModal` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width*0.92,680*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrReport1/rptExportModal` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrReport1/rptExportModal` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(App.Height-Self.Height)/2
```

### `ScrReport1/rptExportModal/rptExportTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptExportModal/rptExportTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptExportModal/rptExportTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptExportModal/rptExportTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.14
```

### `ScrReport1/rptExportModal/rptExportTitle` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportTitle` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportTitle` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportTitle` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/24,Parent.Height/17)
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Text**  _(Label@2.5.1)_
```powerfx
If(varRptExportMode="PPTX","Тооллогын PowerPoint тайлан","Тооллогын тайлан - " & varReportTab & " · " & varRptExportMode)
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrReport1/rptExportModal/rptExportTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrReport1/rptExportModal/rptExportTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.05
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.44
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Text**  _(Label@2.5.1)_
```powerfx
If(varRptExportMode="PPTX","Сонгосон хугацаа, агуулах, шүүлтэд тохирох өөрийн тооллогоор 6 слайд үүсгэнэ. График, явц, зөрүү, товч навигац, Fade эффекттэй. Мэйлд хавсаргаж, OneDrive-аас нээж татна.",varRptExportMode="PDF","Харагдаж буй графиктай тайлан PDF хавсралт болно.","Шүүлтэд тохирох бүх мөр CSV хавсралт болно.") & Char(10) & User().Email
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrReport1/rptExportModal/rptExportExplanation` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.23
```

### `ScrReport1/rptExportModal/rptExportCancel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptExportModal/rptExportCancel` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptExportModal/rptExportCancel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptExportModal/rptExportCancel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrReport1/rptExportModal/rptExportCancel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptExportModal/rptExportCancel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptExportModal/rptExportCancel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptExportModal/rptExportCancel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptExportDialog,false)
```

### `ScrReport1/rptExportModal/rptExportCancel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptExportModal/rptExportCancel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptExportModal/rptExportCancel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptExportModal/rptExportCancel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Болих"
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.29
```

### `ScrReport1/rptExportModal/rptExportCancel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.06
```

### `ScrReport1/rptExportModal/rptExportCancel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptExportMode="PPTX",If(varRptSending || varRptPdfPending,Notify("Тайлан бэлтгэж байна…",NotificationType.Information),!Connection.Connected,Notify("PowerPoint үүсгэхэд интернет шаардлагатай.",NotificationType.Warning),varRptCloudLimit || varRInvalidDates,Notify("Огноо эсвэл тайлангийн мөрийн хязгаарыг шалгана уу.",NotificationType.Warning),With({_ppt:Filter(colRRaw As h,h.OwnerEmail=varCountOwner && !Coalesce(h.Archived,false) && !IsBlank(h.CountQty) && !IsBlank(h.OpeningBalance) && !IsBlank(LookUp(If(varRptSortVariance,SortByColumns(AddColumns(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true)),SortMagnitude,Abs(Coalesce(ReportVariance,0))),"SortMagnitude",SortOrder.Descending,"ItemNo",SortOrder.Ascending),SortByColumns(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true)),"ItemNo",SortOrder.Ascending,"LocationCode",SortOrder.Ascending)),ItemNo=h.ItemNo && LocationCode=h.LocationCode && ReportCounted && !ReportInvalid)))},If(IsEmpty(_ppt),Notify("Шүүлтэд тохирох тооллого алга.",NotificationType.Information),Set(varRptSending,true);Set(varRptExportDialog,false);Set(varRptPptUrlV24,Blank());Set(varRptPptResultV24,{result:""});IfError(Set(varRptPptResultV24,PA_ExportInventoryCSV.Run(JSON(Table({From:Text(dpReportFrom.SelectedDate,"yyyy-mm-dd"),To:Text(dpReportTo.SelectedDate,"yyyy-mm-dd"),User:User().FullName,Email:Lower(User().Email),Generated:Text(Now(),"yyyy-mm-dd hh:mm:ss"),Rows:ForAll(_ppt As r,{ItemNo:r.ItemNo,ItemName:r.ItemName,LocationCode:r.LocationCode,CountDateText:Text(r.CountDate,"yyyy-mm-dd hh:mm:ss"),CountQty:r.CountQty,OpeningBalance:r.OpeningBalance,Counter:r.Counter,RecordKey:r.SyncKey,OwnerEmail:r.OwnerEmail,Archived:false})}),JSONFormat.Compact),User().Email,"[PPTX] Тооллогын тайлан " & Text(dpReportFrom.SelectedDate,"yyyy-mm-dd") & " - " & Text(dpReportTo.SelectedDate,"yyyy-mm-dd"),"<h2>Тооллогын PowerPoint тайлан</h2><p>Хэрэглэгч: " & Substitute(Substitute(Substitute(Coalesce(User().FullName,""),"&","&amp;"),"<","&lt;"),">","&gt;") & " · " & User().Email & "</p><p>Хугацаа: " & Text(dpReportFrom.SelectedDate,"yyyy-mm-dd") & " — " & Text(dpReportTo.SelectedDate,"yyyy-mm-dd") & "</p><p>Хуудас: Тооллогын тайлан · PowerPoint</p><p>Шүүлт: " & Substitute(Substitute(Substitute(Coalesce(varRptStatus & " · " & rptSearchV16.Text,""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Нийт хадгалсан мөр: " & CountRows(_ppt) & "</p><p>Агуулахын тоо: " & CountRows(Distinct(_ppt,LocationCode)) & "</p><p>График, хураангуй, хугацааны явц, зөрүү, навигацтай 6 слайд хавсаргав.</p>"));Set(varRptPptUrlV24,If(IsBlankOrError(varRptPptResultV24.result),Blank(),If(StartsWith(varRptPptResultV24.result,"https://"),varRptPptResultV24.result,Blank()))),Notify("PowerPoint үүсгэхэд алдаа: " & FirstError.Message,NotificationType.Error),If(IsBlankOrError(varRptPptUrlV24),Notify("PowerPoint үүссэн баталгаа ирсэнгүй. Холболтоо шалгаад дахин оролдоно уу.",NotificationType.Error),Notify("PowerPoint мэйлд хавсаргалаа. PPTX нээх товчоор мөн үзэж татаж болно.",NotificationType.Success)));Set(varRptSending,false)))),If(varRptSending || varRptPdfPending,Notify("Тайлан бэлтгэж байна…",NotificationType.Information),!Connection.Connected,Notify("Интернет холболт алга.",NotificationType.Warning),varRptCloudLimit,Notify("Мөрийн хязгаараас шалтгаалсан дутуу тайланг илгээхгүй.",NotificationType.Warning),varRInvalidDates,Notify("Огнооны дарааллыг шалгана уу.",NotificationType.Warning),With({_rows:If(varReportTab="Бараагаар",If(varRptSortVariance,SortByColumns(AddColumns(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true)),SortMagnitude,Abs(Coalesce(ReportVariance,0))),"SortMagnitude",SortOrder.Descending,"ItemNo",SortOrder.Ascending),SortByColumns(Filter(colRItems,
    (IsBlank(Trim(rptSearchV16.Text)) || Trim(rptSearchV16.Text) in ItemNo || Trim(rptSearchV16.Text) in ItemName || ItemNo in colRptSearchItemsV16.number || Trim(rptSearchV16.Text) in LocationCode) &&
    Switch(varRptStatus,"Зөрүүтэй",ReportCounted && !ReportInvalid && ReportVariance<>0,
        "Таарсан",ReportCounted && !ReportInvalid && ReportVariance=0,"Тоолоогүй",!ReportCounted,true)),"ItemNo",SortOrder.Ascending,"LocationCode",SortOrder.Ascending)),colRLatest)},If(IsEmpty(_rows),Notify("Илгээх мөр алга.",NotificationType.Information),Set(varRptAttachmentNameV23,"Тооллогын тайлан - " & varReportTab & " " & Text(dpReportFrom.SelectedDate,"yyyy-mm-dd") & " - " & Text(dpReportTo.SelectedDate,"yyyy-mm-dd"));Set(varRptSummaryV23,"<h2>" & Substitute(Substitute(Substitute(Coalesce("Тооллогын тайлан - " & varReportTab,""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</h2><p>Хэрэглэгч: " & Substitute(Substitute(Substitute(Coalesce(User().FullName,""),"&","&amp;"),"<","&lt;"),">","&gt;") & " · " & Substitute(Substitute(Substitute(Coalesce(User().Email,""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Хугацаа: " & Text(dpReportFrom.SelectedDate,"yyyy-mm-dd") & " — " & Text(dpReportTo.SelectedDate,"yyyy-mm-dd") & "</p><p>Хуудас: " & Substitute(Substitute(Substitute(Coalesce("Тооллогын тайлан · " & varReportTab,""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Шүүлт: " & Substitute(Substitute(Substitute(Coalesce(varRptStatus & " · Хайлт: " & Coalesce(rptSearchV16.Text,""),""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Нийт мөр: " & CountRows(_rows) & "</p><p>Таарсан: " & CountRows(Filter(_rows,!IsBlank(CountQty) && CountQty=OpeningBalance)) & " · Дутуу: " & CountRows(Filter(_rows,!IsBlank(CountQty) && CountQty<OpeningBalance)) & " · Илүү: " & CountRows(Filter(_rows,!IsBlank(CountQty) && CountQty>OpeningBalance)) & "</p><p>Агуулахын тоо: " & CountRows(Distinct(_rows,LocationCode)) & "</p><p>Дэлгэрэнгүй тайланг хавсралтаас үзнэ үү.</p>");Set(varRptExportDialog,false);Set(varRptSending,true);If(varRptExportMode="PDF",Set(varRptPdfPending,true),IfError(Set(varRptMailResult,PA_ExportInventoryCSV.Run(JSON(ForAll(_rows As r,{'Огноо':If(IsBlank(r.CountDate),"",Text(r.CountDate,"yyyy-mm-dd hh:mm:ss")),'Барааны код':If(IsMatch(r.ItemNo,"[0-9]+"),"=" & Char(34) & r.ItemNo & Char(34),With({s:Coalesce(r.ItemNo,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s))),'Барааны нэр':With({s:Coalesce(r.ItemName,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Агуулах':With({s:Coalesce(r.LocationCode,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Үлдэгдэл':r.OpeningBalance,'Тоолсон':r.CountQty,'Зөрүү':If(IsBlank(r.CountQty),Blank(),r.CountQty-r.OpeningBalance),'Тоологч':With({s:Coalesce(r.Counter,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Шалтгаан':With({s:Coalesce(r.Reason,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Тайлбар':With({s:Coalesce(r.Comment,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s))}),JSONFormat.Compact),User().Email,"[CSV2] " & varRptAttachmentNameV23,varRptSummaryV23)),Notify("Илгээхэд алдаа: " & FirstError.Message,NotificationType.Error),Notify("Хураангуй болон CSV хавсралтыг өөрийн мэйлд илгээлээ.",NotificationType.Success));Set(varRptSending,false))))))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Өөрийн мэйлд илгээх"
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.56
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.38
```

### `ScrReport1/rptExportModal/rptExportConfirm` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrReport1/rptPdfTimer` . **OnTimerStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrReport1/rptPdfTimer` . **AutoStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrReport1/rptPdfTimer` . **AutoPause**  _(Timer@2.1.0)_
```powerfx
false
```

### `ScrReport1/rptPdfTimer` . **BorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrReport1/rptPdfTimer` . **BorderThickness**  _(Timer@2.1.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPdfTimer` . **Color**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrReport1/rptPdfTimer` . **DisabledBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 70%)
```

### `ScrReport1/rptPdfTimer` . **DisabledColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 90%)
```

### `ScrReport1/rptPdfTimer` . **DisabledFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 70%)
```

### `ScrReport1/rptPdfTimer` . **Duration**  _(Timer@2.1.0)_
```powerfx
500
```

### `ScrReport1/rptPdfTimer` . **Fill**  _(Timer@2.1.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrReport1/rptPdfTimer` . **FocusedBorderThickness**  _(Timer@2.1.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrReport1/rptPdfTimer` . **Font**  _(Timer@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptPdfTimer` . **Height**  _(Timer@2.1.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ScrReport1/rptPdfTimer` . **HoverBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptPdfTimer` . **HoverColor**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrReport1/rptPdfTimer` . **HoverFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrReport1/rptPdfTimer` . **OnTimerEnd**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),IfError(Set(varRptPdfFile,PDF(rptPrintRootV24,{Size:"A4",Orientation:"Portrait",ExpandContainers:false}));If(IsBlank(varRptPdfFile),Error({Kind:ErrorKind.Validation,Message:"PDF файл үүссэнгүй."}),PA_ExportInventoryCSV.Run(JSON(Table({PdfDataUri:Substitute(JSON(varRptPdfFile,JSONFormat.IncludeBinaryData),Char(34),"")}),JSONFormat.Compact),User().Email,"[PDF] " & varRptAttachmentNameV23,varRptSummaryV23)),Notify("PDF үүсгэх эсвэл илгээхэд алдаа: " & FirstError.Message,NotificationType.Error),Notify("Хураангуй болон графиктай PDF тайланг илгээлээ.",NotificationType.Success));Set(varRptPdfPending,false);Set(varRptSending,false);Set(varRptPdfFile,Blank())
)
```

### `ScrReport1/rptPdfTimer` . **PressedBorderColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPdfTimer` . **PressedColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptPdfTimer` . **PressedFill**  _(Timer@2.1.0)_
```powerfx
Self.Color
```

### `ScrReport1/rptPdfTimer` . **Reset**  _(Timer@2.1.0)_
```powerfx
!varRptPdfPending
```

### `ScrReport1/rptPdfTimer` . **Size**  _(Timer@2.1.0)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrReport1/rptPdfTimer` . **Start**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),varRptPdfPending
)
```

### `ScrReport1/rptPdfTimer` . **Visible**  _(Timer@2.1.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrReport1/rptPdfTimer` . **Width**  _(Timer@2.1.0)_
```powerfx
(1)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPdfTimer` . **X**  _(Timer@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrReport1/rptPdfTimer` . **Y**  _(Timer@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailShadeV16` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptDetailShadeV16` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailShadeV16` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
RGBA(8,24,17,0.48)
```

### `ScrReport1/rptDetailShadeV16` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
App.Height
```

### `ScrReport1/rptDetailShadeV16` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailShadeV16` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailShadeV16` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailShadeV16` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailShadeV16` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varRptDetail)
```

### `ScrReport1/rptDetailShadeV16` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
App.Width
```

### `ScrReport1/rptDetailV16` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptDetailV16` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptDetailV16` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Height-24,720)
```

### `ScrReport1/rptDetailV16` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varRptDetail)
```

### `ScrReport1/rptDetailV16` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width-24,680)
```

### `ScrReport1/rptDetailV16` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrReport1/rptDetailV16` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(App.Height-Self.Height)/2
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **Text**  _(Label@2.5.1)_
```powerfx
varRptSelectedItem & " / " & varRptSelectedLocation
```

### `ScrReport1/rptDetailV16/rptDetailTitleV16` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width-84
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptDetail,false)
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"✕"
```

### `ScrReport1/rptDetailV16/rptDetailCloseV16` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width-60
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **Height**  _(Label@2.5.1)_
```powerfx
132
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:LookUp(colRItems,ItemNo=varRptSelectedItem && LocationCode=varRptSelectedLocation)},
Coalesce(r.ItemName,LookUp(colOfflineItems,number=varRptSelectedItem,displayName),"Нэргүй") & Char(10) &
If(!r.ReportCounted,"Тооллого бүртгэгдээгүй", "Үлдэгдэл: " & Text(r.OpeningBalance,If(Mod(r.OpeningBalance,1)=0,"#,##0","#,##0.###")) & "    Тоолсон: " & Text(r.CountQty,If(Mod(r.CountQty,1)=0,"#,##0","#,##0.###")) & Char(10) &
"Зөрүү: " & If(r.ReportVariance>0,"+","") & Text(r.ReportVariance,If(Mod(r.ReportVariance,1)=0,"#,##0","#,##0.###")) & "    Бүртгэл: " & Text(r.ReportRepeat) & Char(10) &
"Сүүлийн тооллого: " & Text(r.CountDate,"yyyy.mm.dd hh:mm")))
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrReport1/rptDetailV16/rptDetailInfoV16` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width-40
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **Text**  _(Label@2.5.1)_
```powerfx
"СОНГОСОН ХУГАЦААНЫ ТООЛЛОГЫН ТҮҮХ"
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width-40
```

### `ScrReport1/rptDetailV16/rptDetailHistoryTitleV16` . **Y**  _(Label@2.5.1)_
```powerfx
204
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **Height**  _(Gallery@2.15.0)_
```powerfx
Max(80,Parent.Height-260)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **Items**  _(Gallery@2.15.0)_
```powerfx
SortByColumns(Filter(colRRaw,ItemNo=varRptSelectedItem && LocationCode=varRptSelectedLocation),"CountDate",SortOrder.Descending)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
106
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **Width**  _(Gallery@2.15.0)_
```powerfx
Parent.Width-40
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16` . **Y**  _(Gallery@2.15.0)_
```powerfx
240
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#102D25")
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.CountDate,"mm.dd hh:mm") & "  •  Тоолсон " & Text(ThisItem.CountQty,If(Mod(ThisItem.CountQty,1)=0,"#,##0","#,##0.###")) & Char(10) &
Coalesce(ThisItem.Counter,"") & "  •  " & If(ThisItem.Synced,"SharePoint-д хадгалсан","Илгээгдээгүй") & Char(10) &
Coalesce(ThisItem.Reason,"") & If(!IsBlank(ThisItem.Comment)," — " & ThisItem.Comment,"")
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrReport1/rptDetailV16/rptDetailHistoryV16/rptDetailHistoryRowV16` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-20
```

### `ScrReport1/mobRBody` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*0/360
```

### `ScrReport1/mobRBody` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*0/700
```

### `ScrReport1/mobRBody` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*360/360
```

### `ScrReport1/mobRBody` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*700/700
```

### `ScrReport1/mobRBody` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRBody` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRBody` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 360 700'><rect x='0' y='0' width='360' height='700' fill='#F5F4F1' stroke='#F5F4F1' rx='0'/><rect x='14' y='103' width='332' height='155' fill='#FFFFFF' stroke='#E5E2DD' rx='15'/><rect x='14' y='267' width='332' height='51' fill='#FFF7E9' stroke='#F4B86D' rx='15'/></svg>")
```

### `ScrReport1/mobRBody` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrReport1/mobRCountTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*30/360
```

### `ScrReport1/mobRCountTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*118/700
```

### `ScrReport1/mobRCountTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*177/360
```

### `ScrReport1/mobRCountTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*25/700
```

### `ScrReport1/mobRCountTitle` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRCountTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobRCountTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRCountTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRCountTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Таарсан хувь"
```

### `ScrReport1/mobRCountTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobRCountTitle` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRCountTitle` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRCountTotal` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*208/360
```

### `ScrReport1/mobRCountTotal` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*118/700
```

### `ScrReport1/mobRCountTotal` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*121/360
```

### `ScrReport1/mobRCountTotal` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*25/700
```

### `ScrReport1/mobRCountTotal` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRCountTotal` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobRCountTotal` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRCountTotal` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRCountTotal` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colRLatest),"#,##0") & " мөр"
```

### `ScrReport1/mobRCountTotal` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobRCountTotal` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/mobRCountTotal` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRCountPct` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobRCountPct` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*145/700
```

### `ScrReport1/mobRCountPct` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*303/360
```

### `ScrReport1/mobRCountPct` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*52/700
```

### `ScrReport1/mobRCountPct` . **Size**  _(Label@2.5.1)_
```powerfx
37*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRCountPct` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRCountPct` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRCountPct` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRCountPct` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountIf(colRItems,ReportCounted && !ReportInvalid)=0,"—",Text(100*CountIf(colRItems,ReportCounted && !ReportInvalid && ReportVariance=0)/Max(1,CountIf(colRItems,ReportCounted && !ReportInvalid)),"0.0") & "%")
```

### `ScrReport1/mobRCountPct` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRCountPct` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRCountPct` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRBarBase` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*(30+300*(0))/360
```

### `ScrReport1/mobRBarBase` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*202/700
```

### `ScrReport1/mobRBarBase` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*300/360*(1)
```

### `ScrReport1/mobRBarBase` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*8/700
```

### `ScrReport1/mobRBarBase` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrReport1/mobRBarBase` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRBarBase` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRBarMatch` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*(30+300*(0))/360
```

### `ScrReport1/mobRBarMatch` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*202/700
```

### `ScrReport1/mobRBarMatch` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*300/360*(CountIf(colRItems,ReportCounted && !ReportInvalid && ReportVariance=0)/Max(1,CountRows(colRItems)))
```

### `ScrReport1/mobRBarMatch` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*8/700
```

### `ScrReport1/mobRBarMatch` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrReport1/mobRBarMatch` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#139D50")
```

### `ScrReport1/mobRBarMatch` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRBarVariance` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*(30+300*(CountIf(colRItems,ReportCounted && !ReportInvalid && ReportVariance=0)/Max(1,CountRows(colRItems))))/360
```

### `ScrReport1/mobRBarVariance` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*202/700
```

### `ScrReport1/mobRBarVariance` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*300/360*(CountRows(colRptVariance)/Max(1,CountRows(colRItems)))
```

### `ScrReport1/mobRBarVariance` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*8/700
```

### `ScrReport1/mobRBarVariance` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrReport1/mobRBarVariance` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#F4A415")
```

### `ScrReport1/mobRBarVariance` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRMatch` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*30/360
```

### `ScrReport1/mobRMatch` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*219/700
```

### `ScrReport1/mobRMatch` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*99/360
```

### `ScrReport1/mobRMatch` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*25/700
```

### `ScrReport1/mobRMatch` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRMatch` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#139D50")
```

### `ScrReport1/mobRMatch` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRMatch` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRMatch` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountIf(colRItems,ReportCounted && !ReportInvalid && ReportVariance=0)) & " таарсан"
```

### `ScrReport1/mobRMatch` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRMatch` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRMatch` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRVariance` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*136/360
```

### `ScrReport1/mobRVariance` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*219/700
```

### `ScrReport1/mobRVariance` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*105/360
```

### `ScrReport1/mobRVariance` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*25/700
```

### `ScrReport1/mobRVariance` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRVariance` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A85309")
```

### `ScrReport1/mobRVariance` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRVariance` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRVariance` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(colRptVariance) & " зөрүүтэй"
```

### `ScrReport1/mobRVariance` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRVariance` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRVariance` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobROther` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*248/360
```

### `ScrReport1/mobROther` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*219/700
```

### `ScrReport1/mobROther` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*84/360
```

### `ScrReport1/mobROther` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*25/700
```

### `ScrReport1/mobROther` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobROther` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobROther` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobROther` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobROther` . **Text**  _(Label@2.5.1)_
```powerfx
If(varRptIncludeUncounted,CountIf(colRItems,!ReportCounted) & " тоолоогүй","")
```

### `ScrReport1/mobROther` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobROther` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobROther` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRWarn` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*24/360
```

### `ScrReport1/mobRWarn` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*272/700
```

### `ScrReport1/mobRWarn` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*310/360
```

### `ScrReport1/mobRWarn` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*40/700
```

### `ScrReport1/mobRWarn` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRWarn` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#914512")
```

### `ScrReport1/mobRWarn` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRWarn` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRWarn` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsEmpty(colRLatest),"Сонгосон хугацаанд тооллого алга",varRptMissingReasons>0,"⚠ " & varRptMissingReasons & " зөрүүтэй мөр тайлбаргүй","Зөрүүний тайлбар бүрэн")
```

### `ScrReport1/mobRWarn` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobRWarn` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRWarn` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRTop` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*15/360
```

### `ScrReport1/mobRTop` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*326/700
```

### `ScrReport1/mobRTop` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*328/360
```

### `ScrReport1/mobRTop` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*25/700
```

### `ScrReport1/mobRTop` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRTop` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobRTop` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRTop` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй")
```

### `ScrReport1/mobRTop` . **Text**  _(Label@2.5.1)_
```powerfx
"Топ зөрүүтэй бараа"
```

### `ScrReport1/mobRTop` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRTop` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRTop` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRRow0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*14/360
```

### `ScrReport1/mobRRow0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*358/700
```

### `ScrReport1/mobRRow0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*332/360
```

### `ScrReport1/mobRRow0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*65/700
```

### `ScrReport1/mobRRow0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRRow0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRRow0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRRow0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRRow0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRRow0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>0))
```

### `ScrReport1/mobRRow0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Last(FirstN(colRptVariance,1))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRRow0` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRRow0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRRow0` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,1)).ItemName,Last(FirstN(colRptVariance,1)).ItemNo)
```

### `ScrReport1/mobRName0` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobRName0` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*363/700
```

### `ScrReport1/mobRName0` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*239/360
```

### `ScrReport1/mobRName0` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*30/700
```

### `ScrReport1/mobRName0` . **Size**  _(Label@2.5.1)_
```powerfx
14*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRName0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRName0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRName0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>0))
```

### `ScrReport1/mobRName0` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,1)).ItemName,Last(FirstN(colRptVariance,1)).ItemNo)
```

### `ScrReport1/mobRName0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRName0` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRName0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRName0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,1))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRName0` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,1)).ItemName,Last(FirstN(colRptVariance,1)).ItemNo)
```

### `ScrReport1/mobRDiff0` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*271/360
```

### `ScrReport1/mobRDiff0` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*363/700
```

### `ScrReport1/mobRDiff0` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*58/360
```

### `ScrReport1/mobRDiff0` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*30/700
```

### `ScrReport1/mobRDiff0` . **Size**  _(Label@2.5.1)_
```powerfx
15*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRDiff0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRDiff0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRDiff0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>0))
```

### `ScrReport1/mobRDiff0` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colRptVariance,1)).ReportVariance,"+#,##0.##;-#,##0.##;0")
```

### `ScrReport1/mobRDiff0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRDiff0` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/mobRDiff0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRDiff0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,1))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRDiff0` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colRptVariance,1)).ReportVariance,"+#,##0.##;-#,##0.##;0")
```

### `ScrReport1/mobRPlace0` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobRPlace0` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*392/700
```

### `ScrReport1/mobRPlace0` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*301/360
```

### `ScrReport1/mobRPlace0` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*24/700
```

### `ScrReport1/mobRPlace0` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRPlace0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobRPlace0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRPlace0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>0))
```

### `ScrReport1/mobRPlace0` . **Text**  _(Label@2.5.1)_
```powerfx
Last(FirstN(colRptVariance,1)).LocationCode & " · " & Coalesce(Last(FirstN(colRptVariance,1)).Reason,Last(FirstN(colRptVariance,1)).Comment,"Тайлбаргүй")
```

### `ScrReport1/mobRPlace0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobRPlace0` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRPlace0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRPlace0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,1))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRPlace0` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Last(FirstN(colRptVariance,1)).LocationCode & " · " & Coalesce(Last(FirstN(colRptVariance,1)).Reason,Last(FirstN(colRptVariance,1)).Comment,"Тайлбаргүй")
```

### `ScrReport1/mobRRow1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*14/360
```

### `ScrReport1/mobRRow1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*431/700
```

### `ScrReport1/mobRRow1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*332/360
```

### `ScrReport1/mobRRow1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*65/700
```

### `ScrReport1/mobRRow1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRRow1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRRow1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRRow1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRRow1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRRow1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>1))
```

### `ScrReport1/mobRRow1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Last(FirstN(colRptVariance,2))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRRow1` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRRow1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRRow1` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,2)).ItemName,Last(FirstN(colRptVariance,2)).ItemNo)
```

### `ScrReport1/mobRName1` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobRName1` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*436/700
```

### `ScrReport1/mobRName1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*239/360
```

### `ScrReport1/mobRName1` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*30/700
```

### `ScrReport1/mobRName1` . **Size**  _(Label@2.5.1)_
```powerfx
14*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRName1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRName1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRName1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>1))
```

### `ScrReport1/mobRName1` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,2)).ItemName,Last(FirstN(colRptVariance,2)).ItemNo)
```

### `ScrReport1/mobRName1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRName1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRName1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRName1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,2))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRName1` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,2)).ItemName,Last(FirstN(colRptVariance,2)).ItemNo)
```

### `ScrReport1/mobRDiff1` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*271/360
```

### `ScrReport1/mobRDiff1` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*436/700
```

### `ScrReport1/mobRDiff1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*58/360
```

### `ScrReport1/mobRDiff1` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*30/700
```

### `ScrReport1/mobRDiff1` . **Size**  _(Label@2.5.1)_
```powerfx
15*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRDiff1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRDiff1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRDiff1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>1))
```

### `ScrReport1/mobRDiff1` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colRptVariance,2)).ReportVariance,"+#,##0.##;-#,##0.##;0")
```

### `ScrReport1/mobRDiff1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRDiff1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/mobRDiff1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRDiff1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,2))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRDiff1` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colRptVariance,2)).ReportVariance,"+#,##0.##;-#,##0.##;0")
```

### `ScrReport1/mobRPlace1` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobRPlace1` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*465/700
```

### `ScrReport1/mobRPlace1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*301/360
```

### `ScrReport1/mobRPlace1` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*24/700
```

### `ScrReport1/mobRPlace1` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRPlace1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobRPlace1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRPlace1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>1))
```

### `ScrReport1/mobRPlace1` . **Text**  _(Label@2.5.1)_
```powerfx
Last(FirstN(colRptVariance,2)).LocationCode & " · " & Coalesce(Last(FirstN(colRptVariance,2)).Reason,Last(FirstN(colRptVariance,2)).Comment,"Тайлбаргүй")
```

### `ScrReport1/mobRPlace1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobRPlace1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRPlace1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRPlace1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,2))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRPlace1` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Last(FirstN(colRptVariance,2)).LocationCode & " · " & Coalesce(Last(FirstN(colRptVariance,2)).Reason,Last(FirstN(colRptVariance,2)).Comment,"Тайлбаргүй")
```

### `ScrReport1/mobRRow2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*14/360
```

### `ScrReport1/mobRRow2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*504/700
```

### `ScrReport1/mobRRow2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*332/360
```

### `ScrReport1/mobRRow2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*65/700
```

### `ScrReport1/mobRRow2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRRow2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRRow2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRRow2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRRow2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRRow2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>2))
```

### `ScrReport1/mobRRow2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Last(FirstN(colRptVariance,3))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRRow2` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRRow2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRRow2` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,3)).ItemName,Last(FirstN(colRptVariance,3)).ItemNo)
```

### `ScrReport1/mobRName2` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobRName2` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*509/700
```

### `ScrReport1/mobRName2` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*239/360
```

### `ScrReport1/mobRName2` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*30/700
```

### `ScrReport1/mobRName2` . **Size**  _(Label@2.5.1)_
```powerfx
14*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRName2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRName2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRName2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>2))
```

### `ScrReport1/mobRName2` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,3)).ItemName,Last(FirstN(colRptVariance,3)).ItemNo)
```

### `ScrReport1/mobRName2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRName2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRName2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRName2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,3))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRName2` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Coalesce(Last(FirstN(colRptVariance,3)).ItemName,Last(FirstN(colRptVariance,3)).ItemNo)
```

### `ScrReport1/mobRDiff2` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*271/360
```

### `ScrReport1/mobRDiff2` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*509/700
```

### `ScrReport1/mobRDiff2` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*58/360
```

### `ScrReport1/mobRDiff2` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*30/700
```

### `ScrReport1/mobRDiff2` . **Size**  _(Label@2.5.1)_
```powerfx
15*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRDiff2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRDiff2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRDiff2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>2))
```

### `ScrReport1/mobRDiff2` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colRptVariance,3)).ReportVariance,"+#,##0.##;-#,##0.##;0")
```

### `ScrReport1/mobRDiff2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRDiff2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrReport1/mobRDiff2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRDiff2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,3))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRDiff2` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colRptVariance,3)).ReportVariance,"+#,##0.##;-#,##0.##;0")
```

### `ScrReport1/mobRPlace2` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobRPlace2` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*538/700
```

### `ScrReport1/mobRPlace2` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*301/360
```

### `ScrReport1/mobRPlace2` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*24/700
```

### `ScrReport1/mobRPlace2` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRPlace2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobRPlace2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRPlace2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (CountRows(colRptVariance)>2))
```

### `ScrReport1/mobRPlace2` . **Text**  _(Label@2.5.1)_
```powerfx
Last(FirstN(colRptVariance,3)).LocationCode & " · " & Coalesce(Last(FirstN(colRptVariance,3)).Reason,Last(FirstN(colRptVariance,3)).Comment,"Тайлбаргүй")
```

### `ScrReport1/mobRPlace2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobRPlace2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRPlace2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRPlace2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colRptVariance,3))},Set(varRptSelectedItem,r.ItemNo);Set(varRptSelectedLocation,r.LocationCode);Set(varRptDetail,true))
```

### `ScrReport1/mobRPlace2` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Last(FirstN(colRptVariance,3)).LocationCode & " · " & Coalesce(Last(FirstN(colRptVariance,3)).Reason,Last(FirstN(colRptVariance,3)).Comment,"Тайлбаргүй")
```

### `ScrReport1/mobREmpty` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrReport1/mobREmpty` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*366/700
```

### `ScrReport1/mobREmpty` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*301/360
```

### `ScrReport1/mobREmpty` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*48/700
```

### `ScrReport1/mobREmpty` . **Size**  _(Label@2.5.1)_
```powerfx
13*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobREmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobREmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobREmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending && varReportTab="Хураангуй") && (IsEmpty(colRptVariance)))
```

### `ScrReport1/mobREmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүтэй бараа бүртгэгдээгүй"
```

### `ScrReport1/mobREmpty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobREmpty` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobREmpty` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRHeader` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0/360
```

### `ScrReport1/mobRHeader` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0/700
```

### `ScrReport1/mobRHeader` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*360/360
```

### `ScrReport1/mobRHeader` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*95/700
```

### `ScrReport1/mobRHeader` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrReport1/mobRHeader` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrReport1/mobRHeader` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*12/360
```

### `ScrReport1/mobRBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*7/700
```

### `ScrReport1/mobRBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*33/360
```

### `ScrReport1/mobRBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*34/700
```

### `ScrReport1/mobRBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
20*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrReport1/mobRBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Back()
```

### `ScrReport1/mobRBack` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRBack` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
"Буцах"
```

### `ScrReport1/mobRTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*54/360
```

### `ScrReport1/mobRTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*2/700
```

### `ScrReport1/mobRTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*249/360
```

### `ScrReport1/mobRTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*27/700
```

### `ScrReport1/mobRTitle` . **Size**  _(Label@2.5.1)_
```powerfx
18*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Тооллогын тайлан"
```

### `ScrReport1/mobRTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRTitle` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRTitle` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRRange` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*54/360
```

### `ScrReport1/mobRRange` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*29/700
```

### `ScrReport1/mobRRange` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*248/360
```

### `ScrReport1/mobRRange` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*18/700
```

### `ScrReport1/mobRRange` . **Size**  _(Label@2.5.1)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRRange` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrReport1/mobRRange` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrReport1/mobRRange` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRRange` . **Text**  _(Label@2.5.1)_
```powerfx
Text(varRptStart,"mm.dd") & "–" & Text(varRptEnd,"mm.dd") & " · " & Concat(FirstN(colReportWarehouses,3),code,", ")
```

### `ScrReport1/mobRRange` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrReport1/mobRRange` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrReport1/mobRRange` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrReport1/mobRRange` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varRptSettings,true)
```

### `ScrReport1/mobRRange` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Text(varRptStart,"mm.dd") & "–" & Text(varRptEnd,"mm.dd") & " · " & Concat(FirstN(colReportWarehouses,3),code,", ")
```

### `ScrReport1/mobRMore` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*312/360
```

### `ScrReport1/mobRMore` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*7/700
```

### `ScrReport1/mobRMore` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*35/360
```

### `ScrReport1/mobRMore` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*35/700
```

### `ScrReport1/mobRMore` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
18*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRMore` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRMore` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRMore` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRMore` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRMore` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRMore` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"⋯"
```

### `ScrReport1/mobRMore` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobReportMenu,!mobReportMenu)
```

### `ScrReport1/mobRMore` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRMore` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRMore` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
"Тайлангийн үйлдэл"
```

### `ScrReport1/mobRTab0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*14/360
```

### `ScrReport1/mobRTab0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*55/700
```

### `ScrReport1/mobRTab0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*109/360
```

### `ScrReport1/mobRTab0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*34/700
```

### `ScrReport1/mobRTab0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRTab0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRTab0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Хураангуй",Color.White,ColorValue("#EFEDE9"))
```

### `ScrReport1/mobRTab0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRTab0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRTab0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRTab0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хураангуй"
```

### `ScrReport1/mobRTab0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Хураангуй")
```

### `ScrReport1/mobRTab0` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRTab0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRTab1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*125/360
```

### `ScrReport1/mobRTab1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*55/700
```

### `ScrReport1/mobRTab1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*109/360
```

### `ScrReport1/mobRTab1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*34/700
```

### `ScrReport1/mobRTab1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRTab1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRTab1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Бараагаар",Color.White,ColorValue("#EFEDE9"))
```

### `ScrReport1/mobRTab1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRTab1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRTab1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRTab1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараагаар"
```

### `ScrReport1/mobRTab1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Бараагаар")
```

### `ScrReport1/mobRTab1` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRTab1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRTab2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*236/360
```

### `ScrReport1/mobRTab2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*55/700
```

### `ScrReport1/mobRTab2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*109/360
```

### `ScrReport1/mobRTab2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*34/700
```

### `ScrReport1/mobRTab2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRTab2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRTab2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varReportTab="Зөрүү",Color.White,ColorValue("#EFEDE9"))
```

### `ScrReport1/mobRTab2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRTab2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRTab2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRTab2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зөрүү"
```

### `ScrReport1/mobRTab2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReportTab,"Зөрүү")
```

### `ScrReport1/mobRTab2` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRTab2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRFoot` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0/360
```

### `ScrReport1/mobRFoot` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*630/700
```

### `ScrReport1/mobRFoot` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*360/360
```

### `ScrReport1/mobRFoot` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*70/700
```

### `ScrReport1/mobRFoot` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrReport1/mobRFoot` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRFoot` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRCsv` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*13/360
```

### `ScrReport1/mobRCsv` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*641/700
```

### `ScrReport1/mobRCsv` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*100/360
```

### `ScrReport1/mobRCsv` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*46/700
```

### `ScrReport1/mobRCsv` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRCsv` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobRCsv` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRCsv` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRCsv` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRCsv` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRCsv` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"CSV"
```

### `ScrReport1/mobRCsv` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptExportMode,"CSV");Set(varRptExportDialog,true)
```

### `ScrReport1/mobRCsv` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRCsv` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobRMail` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*122/360
```

### `ScrReport1/mobRMail` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*641/700
```

### `ScrReport1/mobRMail` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*225/360
```

### `ScrReport1/mobRMail` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*46/700
```

### `ScrReport1/mobRMail` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobRMail` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobRMail` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EF601B")
```

### `ScrReport1/mobRMail` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobRMail` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobRMail` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending)
```

### `ScrReport1/mobRMail` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэйлээр илгээх"
```

### `ScrReport1/mobRMail` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varRptExportMode,If(varReportTab="Бараагаар","CSV","PDF"));Set(varRptExportDialog,true)
```

### `ScrReport1/mobRMail` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobRMail` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobROption0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*162/360
```

### `ScrReport1/mobROption0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*47/700
```

### `ScrReport1/mobROption0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*184/360
```

### `ScrReport1/mobROption0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*40/700
```

### `ScrReport1/mobROption0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobROption0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobROption0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobROption0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobROption0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobROption0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending) && (mobReportMenu))
```

### `ScrReport1/mobROption0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тохиргоо"
```

### `ScrReport1/mobROption0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobReportMenu,false);Set(varRptSettings,true)
```

### `ScrReport1/mobROption0` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobROption0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobROption1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*162/360
```

### `ScrReport1/mobROption1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*89/700
```

### `ScrReport1/mobROption1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*184/360
```

### `ScrReport1/mobROption1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*40/700
```

### `ScrReport1/mobROption1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobROption1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobROption1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobROption1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobROption1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobROption1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending) && (mobReportMenu))
```

### `ScrReport1/mobROption1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гүйцэтгэл"
```

### `ScrReport1/mobROption1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobReportMenu,false);Set(varReportTab,"Гүйцэтгэл")
```

### `ScrReport1/mobROption1` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobROption1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobROption2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*162/360
```

### `ScrReport1/mobROption2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*131/700
```

### `ScrReport1/mobROption2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*184/360
```

### `ScrReport1/mobROption2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*40/700
```

### `ScrReport1/mobROption2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobROption2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobROption2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobROption2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobROption2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobROption2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending) && (mobReportMenu && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrReport1/mobROption2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Түүх"
```

### `ScrReport1/mobROption2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobReportMenu,false);Navigate(ScrHistory)
```

### `ScrReport1/mobROption2` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobROption2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobROption3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*162/360
```

### `ScrReport1/mobROption3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*173/700
```

### `ScrReport1/mobROption3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*184/360
```

### `ScrReport1/mobROption3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*40/700
```

### `ScrReport1/mobROption3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobROption3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobROption3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobROption3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobROption3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobROption3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending) && (mobReportMenu))
```

### `ScrReport1/mobROption3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"PDF / CSV"
```

### `ScrReport1/mobROption3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobReportMenu,false);If(varReportTab="Бараагаар",Set(varRptExportMode,"CSV"),Set(varRptExportMode,"PDF"));Set(varRptExportDialog,true)
```

### `ScrReport1/mobROption3` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobROption3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/mobROption4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*162/360
```

### `ScrReport1/mobROption4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*215/700
```

### `ScrReport1/mobROption4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*184/360
```

### `ScrReport1/mobROption4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*40/700
```

### `ScrReport1/mobROption4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrReport1/mobROption4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrReport1/mobROption4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrReport1/mobROption4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/mobROption4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/mobROption4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && !varRptSettings && !varRptWarehouse && !varRptExportDialog && !varRptDetail && !varRptPdfPending) && (mobReportMenu))
```

### `ScrReport1/mobROption4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"PowerPoint"
```

### `ScrReport1/mobROption4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobReportMenu,false);If(!IsBlank(varRptPptUrlV24),Launch(varRptPptUrlV24),Set(varRptExportMode,"PPTX");Set(varRptExportDialog,true))
```

### `ScrReport1/mobROption4` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrReport1/mobROption4` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrReport1/pgDenied977` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrReport1/pgDenied977` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrReport1/pgDenied977` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrReport1/pgDenied977` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrReport1/pgDenied977` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrReport1/pgDenied977` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrReport1/pgDenied977` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrReport1/pgDenied977` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrReport1/pgDenied977` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrReport1/pgDenied977` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

