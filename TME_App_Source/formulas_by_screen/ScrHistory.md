# ScrHistory — Power Fx formulas

### `ScrHistory` . **Fill**  _(Screen)_
```powerfx
ColorValue("#0B1011")
```

### `ScrHistory` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrHistory` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrHistory` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Set(varFromDate,DateAdd(Today(),-24,TimeUnit.Days));Set(varToDate,Today());Set(varFilterType,"Бүгд");Set(varHistoryArchive,false);Set(varHistoryTrash,false);Set(varHistoryDeleteConfirm,false);If(IsBlank(varHistoryRefreshed) || DateDiff(varHistoryRefreshed,Now(),TimeUnit.Minutes)>=5,If(Connection.Connected && !IsBlank(varCountOwner) && !Coalesce(varCountSaving,false) && !Coalesce(varCountSyncBusy,false) && !Coalesce(varHistoryLoading,false),
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
Set(varHistoryLoading,false)))
)
```

### `ScrHistory` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrHistory/Label15` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Label15` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Label15` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Label15` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Label15` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Label15` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Label15` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrHistory/Label15` . **Height**  _(Label@2.5.1)_
```powerfx
(62)*((App.Height/1136))
```

### `ScrHistory/Label15` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Label15` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Label15` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Label15` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Label15` . **Size**  _(Label@2.5.1)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Label15` . **Text**  _(Label@2.5.1)_
```powerfx
If(varHistoryArchive,"Хуучин төхөөрөмжийн түүх",varHistoryTrash,"Хогийн сав","Тооллогын түүх")
```

### `ScrHistory/Label15` . **Width**  _(Label@2.5.1)_
```powerfx
(262)*((App.Width/640))
```

### `ScrHistory/Label15` . **X**  _(Label@2.5.1)_
```powerfx
(91)*((App.Width/640))
```

### `ScrHistory/Label15` . **Y**  _(Label@2.5.1)_
```powerfx
(29)*((App.Height/1136))
```

### `ScrHistory/Gallery1` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1` . **Fill**  _(Gallery@2.15.0)_
```powerfx
ColorValue("#0B0F0F")
```

### `ScrHistory/Gallery1` . **Height**  _(Gallery@2.15.0)_
```powerfx
(549)*((App.Height/1136))
```

### `ScrHistory/Gallery1` . **Items**  _(Gallery@2.15.0)_
```powerfx
If(varHistoryArchive,Filter(colLegacyInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),Counter=User().FullName && 
    CountDate >= Min(varFromDate, varToDate) &&
    CountDate <
        DateAdd(
            Max(varFromDate, varToDate),
            1,
            TimeUnit.Days
        )
),Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && Coalesce(Archived,false)=varHistoryTrash && 
    CountDate >= Min(varFromDate, varToDate) &&
    CountDate <
        DateAdd(
            Max(varFromDate, varToDate),
            1,
            TimeUnit.Days
        )
))
```

### `ScrHistory/Gallery1` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/Gallery1` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(118)*((App.Height/1136))
```

### `ScrHistory/Gallery1` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrHistory/Gallery1` . **Width**  _(Gallery@2.15.0)_
```powerfx
(640)*((App.Width/640))
```

### `ScrHistory/Gallery1` . **X**  _(Gallery@2.15.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1` . **Y**  _(Gallery@2.15.0)_
```powerfx
(210)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2E6E3")
```

### `ScrHistory/Gallery1/Button8` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Gallery1/Button8` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/Gallery1/Button8` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#0B0F0F")
```

### `ScrHistory/Gallery1/Button8` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/Button8` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - 12)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/Gallery1/Button8` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Gallery1/Button8` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/Gallery1/Button8` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Button8` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Gallery1/Button8` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Gallery1/Button8` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/Gallery1/Button8` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button8` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - 16)*((App.Width/640))
```

### `ScrHistory/Gallery1/Button8` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(8)*((App.Width/640))
```

### `ScrHistory/Gallery1/Button8` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(6)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label5` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1/Label5` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Label5` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#879393")
```

### `ScrHistory/Gallery1/Label5` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Label5` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/Label5` . **Height**  _(Label@2.5.1)_
```powerfx
(14)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label5` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Label5` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label5` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label5` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label5` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label5` . **Size**  _(Label@2.5.1)_
```powerfx
(7)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Label5` . **Text**  _(Label@2.5.1)_
```powerfx
"PCS"
```

### `ScrHistory/Gallery1/Label5` . **Width**  _(Label@2.5.1)_
```powerfx
(90)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label5` . **X**  _(Label@2.5.1)_
```powerfx
(550)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label5` . **Y**  _(Label@2.5.1)_
```powerfx
(45)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label23` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1/Label23` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Label23` . **Color**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrHistory/Gallery1/Label23` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Label23` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/Label23` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrHistory/Gallery1/Label23` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label23` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Label23` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label23` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label23` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label23` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Label23` . **Size**  _(Label@2.5.1)_
```powerfx
(If(
    Len(Text(ThisItem.CountQty)) >= 7,
    11,
    14
))*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Label23` . **Text**  _(Label@2.5.1)_
```powerfx
Text(
    ThisItem.CountQty,
    "#,##0"
)
```

### `ScrHistory/Gallery1/Label23` . **Width**  _(Label@2.5.1)_
```powerfx
(90)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label23` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrHistory/Gallery1/Label23` . **X**  _(Label@2.5.1)_
```powerfx
(550)*((App.Width/640))
```

### `ScrHistory/Gallery1/Label23` . **Y**  _(Label@2.5.1)_
```powerfx
(18)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Title5` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/Gallery1/Title5` . **Color**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrHistory/Gallery1/Title5` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/Title5` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrHistory/Gallery1/Title5` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Title5` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Title5` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Title5` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1/Title5` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1/Title5` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Title5` . **Size**  _(Label@2.5.1)_
```powerfx
(11)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Title5` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemNo
```

### `ScrHistory/Gallery1/Title5` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrHistory/Gallery1/Title5` . **Width**  _(Label@2.5.1)_
```powerfx
(130)*((App.Width/640))
```

### `ScrHistory/Gallery1/Title5` . **X**  _(Label@2.5.1)_
```powerfx
(26)*((App.Width/640))
```

### `ScrHistory/Gallery1/Title5` . **Y**  _(Label@2.5.1)_
```powerfx
(12)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Subtitle2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/Gallery1/Subtitle2` . **Color**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrHistory/Gallery1/Subtitle2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/Subtitle2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `ScrHistory/Gallery1/Subtitle2` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Subtitle2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Subtitle2` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Subtitle2` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1/Subtitle2` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1/Subtitle2` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Subtitle2` . **Size**  _(Label@2.5.1)_
```powerfx
(Max(
    7,
    Min(
        10,
        10 - ((Len(ThisItem.ItemName) - 30) / 20)
    )
))*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Subtitle2` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemName
```

### `ScrHistory/Gallery1/Subtitle2` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrHistory/Gallery1/Subtitle2` . **Width**  _(Label@2.5.1)_
```powerfx
(490)*((App.Width/640))
```

### `ScrHistory/Gallery1/Subtitle2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrHistory/Gallery1/Subtitle2` . **X**  _(Label@2.5.1)_
```powerfx
(26)*((App.Width/640))
```

### `ScrHistory/Gallery1/Subtitle2` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Body1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/Gallery1/Body1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#7F9292")
```

### `ScrHistory/Gallery1/Body1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/Body1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `ScrHistory/Gallery1/Body1` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Body1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Body1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Body1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1/Body1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1/Body1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Body1` . **Size**  _(Label@2.5.1)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Body1` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode
    & "  •  "
    & Text(
        ThisItem.CountDate,
        "[$-en-US]m/d/yyyy h:mm AM/PM"
    )
```

### `ScrHistory/Gallery1/Body1` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrHistory/Gallery1/Body1` . **Width**  _(Label@2.5.1)_
```powerfx
(300)*((App.Width/640))
```

### `ScrHistory/Gallery1/Body1` . **X**  _(Label@2.5.1)_
```powerfx
(26)*((App.Width/640))
```

### `ScrHistory/Gallery1/Body1` . **Y**  _(Label@2.5.1)_
```powerfx
(58)*((App.Height/1136))
```

### `ScrHistory/Gallery1/NextArrow3` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
Self.Tooltip
```

### `ScrHistory/Gallery1/NextArrow3` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1/NextArrow3` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/NextArrow3` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/Gallery1/NextArrow3` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/NextArrow3` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(23)*((App.Height/1136))
```

### `ScrHistory/Gallery1/NextArrow3` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronRight
```

### `ScrHistory/Gallery1/NextArrow3` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/NextArrow3` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Height/1136))
```

### `ScrHistory/Gallery1/NextArrow3` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Width/640))
```

### `ScrHistory/Gallery1/NextArrow3` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Width/640))
```

### `ScrHistory/Gallery1/NextArrow3` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Height/1136))
```

### `ScrHistory/Gallery1/NextArrow3` . **Tooltip**  _(Classic/Icon@2.5.0)_
```powerfx
"View item details"
```

### `ScrHistory/Gallery1/NextArrow3` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(50)*((App.Width/640))
```

### `ScrHistory/Gallery1/NextArrow3` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - (Self.Width/((App.Width/640))) - 12)*((App.Width/640))
```

### `ScrHistory/Gallery1/NextArrow3` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(42)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Separator3` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1/Separator3` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Separator3` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#252A2A")
```

### `ScrHistory/Gallery1/Separator3` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Separator3` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Separator3` . **Width**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))))*((App.Width/640))
```

### `ScrHistory/Gallery1/Separator3` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/Gallery1/Separator3` . **Y**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Self.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ScrHistory/Gallery1/Rectangle6` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1/Rectangle6` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Rectangle6` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
If(
    Value(Coalesce(ThisItem.Variance, "0")) = 0,
    ColorValue("#B8FF2C"),
    ColorValue("#FF6B3D")
)
```

### `ScrHistory/Gallery1/Rectangle6` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Rectangle6` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Rectangle6` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
ThisItem.IsSelected
```

### `ScrHistory/Gallery1/Rectangle6` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Gallery1/Rectangle6` . **X**  _(Rectangle@2.3.0)_
```powerfx
(12)*((App.Width/640))
```

### `ScrHistory/Gallery1/Rectangle6` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(18)*((App.Height/1136))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Color**  _(Label@2.5.1)_
```powerfx
With(
    {v: Value(Coalesce(ThisItem.Variance, "0"))},
    If(
        v = 0,
        ColorValue("#B8FF2C"),
        ColorValue("#FF784A")
    )
)
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
With(
    {v: Value(Coalesce(ThisItem.Variance, "0"))},
    If(
        v = 0,
        ColorValue("#233414"),
        ColorValue("#3B2117")
    )
)
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Size**  _(Label@2.5.1)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Text**  _(Label@2.5.1)_
```powerfx
With(
    {v: Value(Coalesce(ThisItem.Variance, "0"))},
    If(
        v = 0,
        "таарсан",
        If(
            v > 0,
            "илүү " & Text(Abs(v)),
            "дутуу " & Text(Abs(v))
        )
    )
)
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(80)*((App.Width/640))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **X**  _(Label@2.5.1)_
```powerfx
(155)*((App.Width/640))
```

### `ScrHistory/Gallery1/lblVarianceStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(13)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#596060")
```

### `ScrHistory/Gallery1/Button9` . **BorderStyle**  _(Classic/Button@2.2.0)_
```powerfx
BorderStyle.Dashed
```

### `ScrHistory/Gallery1/Button9` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#AEBABA")
```

### `ScrHistory/Gallery1/Button9` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/Gallery1/Button9` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrHistory/Gallery1/Button9` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Gallery1/Button9` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(36)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/Gallery1/Button9` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Gallery1/Button9` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/Gallery1/Button9` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varExpandedID = ThisItem.SyncKey,
    Set(varExpandedID, Blank()),
    Set(varExpandedID, ThisItem.SyncKey)
)
```

### `ScrHistory/Gallery1/Button9` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Gallery1/Button9` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Gallery1/Button9` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/Gallery1/Button9` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(9)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Button9` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"+ тайлбар (сонголтоор)"
```

### `ScrHistory/Gallery1/Button9` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
Value(Coalesce(ThisItem.Variance, "0")) <> 0
```

### `ScrHistory/Gallery1/Button9` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(164)*((App.Width/640))
```

### `ScrHistory/Gallery1/Button9` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(26)*((App.Width/640))
```

### `ScrHistory/Gallery1/Button9` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(76)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Rectangle4` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Gallery1/Rectangle4` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Rectangle4` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrHistory/Gallery1/Rectangle4` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Gallery1/Rectangle4` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(100)*((App.Height/1136))
```

### `ScrHistory/Gallery1/Rectangle4` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/Gallery1/Rectangle4` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/Gallery1/Rectangle4` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(150)*((App.Width/640))
```

### `ScrHistory/Gallery1/Rectangle4` . **X**  _(Rectangle@2.3.0)_
```powerfx
(40)*((App.Width/640))
```

### `ScrHistory/Gallery1/Rectangle4` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(18)*((App.Height/1136))
```

### `ScrHistory/Icon14` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Icon14` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Үндсэн нүүр"
```

### `ScrHistory/Icon14` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Icon14` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Icon14` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Icon14` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Icon14` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Height/1136))
```

### `ScrHistory/Icon14` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronLeft
```

### `ScrHistory/Icon14` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate(нүүр)  
```

### `ScrHistory/Icon14` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(30)*((App.Width/640))
```

### `ScrHistory/Icon14` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(31)*((App.Width/640))
```

### `ScrHistory/Icon14` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(59)*((App.Height/1136))
```

### `ScrHistory/Button6` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Button6` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/Button6` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button6` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(99, 139, 44, 1)
```

### `ScrHistory/Button6` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/Button6` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/Button6` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button6` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `ScrHistory/Button6` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Bold
```

### `ScrHistory/Button6` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(48)*((App.Height/1136))
```

### `ScrHistory/Button6` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/Button6` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Button6` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#29483D")
```

### `ScrHistory/Button6` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varHistoryArchive,!varHistoryArchive);Set(varHistoryTrash,false);Set(varExpandedID,Blank());If(varHistoryArchive,Set(varFromDate,Coalesce(Min(Filter(colLegacyInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),Counter=User().FullName),CountDate),Today()));Reset(DatePicker2_1);Notify("Энэ төхөөрөмжийн V15 сангаас таны нэртэй бүртгэлийг зөвхөн уншиж харуулна. Эзэмшигчийг email-аар баталгаажуулаагүй тул тайлан, шинэ синктэй хольж оруулаагүй.",NotificationType.Information))
```

### `ScrHistory/Button6` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button6` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button6` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#345D4F")
```

### `ScrHistory/Button6` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(11,Min(16,Self.Width/Max(10,Len(Self.Text))*1.4))
```

### `ScrHistory/Button6` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varHistoryArchive,"Өөрийн түүх","Хуучин төхөөрөмж")
```

### `ScrHistory/Button6` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(150)*((App.Width/640))
```

### `ScrHistory/Button6` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(472)*((App.Width/640))
```

### `ScrHistory/Button6` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*((App.Height/1136))
```

### `ScrHistory/DatePicker2` . **Visible**  _(Classic/DatePicker@2.6.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/DatePicker2` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/DatePicker2` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/DatePicker2` . **Color**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(204, 204, 204, 1)
```

### `ScrHistory/DatePicker2` . **DefaultDate**  _(Classic/DatePicker@2.6.0)_
```powerfx
varToDate
```

### `ScrHistory/DatePicker2` . **Fill**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/DatePicker2` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/DatePicker2` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/DatePicker2` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrHistory/DatePicker2` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrHistory/DatePicker2` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/DatePicker2` . **OnChange**  _(Classic/DatePicker@2.6.0)_
```powerfx
Set(varToDate, Self.SelectedDate)
```

### `ScrHistory/DatePicker2` . **PaddingBottom**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/DatePicker2` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(12)*((App.Width/640))
```

### `ScrHistory/DatePicker2` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/DatePicker2` . **PaddingTop**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/DatePicker2` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/DatePicker2` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
(145)*((App.Width/640))
```

### `ScrHistory/DatePicker2` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
(218)*((App.Width/640))
```

### `ScrHistory/DatePicker2` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
(91)*((App.Height/1136))
```

### `ScrHistory/DatePicker2_1` . **Visible**  _(Classic/DatePicker@2.6.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/DatePicker2_1` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/DatePicker2_1` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/DatePicker2_1` . **Color**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(204, 204, 204, 1)
```

### `ScrHistory/DatePicker2_1` . **DefaultDate**  _(Classic/DatePicker@2.6.0)_
```powerfx
varFromDate
```

### `ScrHistory/DatePicker2_1` . **Fill**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/DatePicker2_1` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/DatePicker2_1` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/DatePicker2_1` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ScrHistory/DatePicker2_1` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrHistory/DatePicker2_1` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/DatePicker2_1` . **OnChange**  _(Classic/DatePicker@2.6.0)_
```powerfx
Set(varFromDate, Self.SelectedDate)
```

### `ScrHistory/DatePicker2_1` . **PaddingBottom**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/DatePicker2_1` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(12)*((App.Width/640))
```

### `ScrHistory/DatePicker2_1` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/DatePicker2_1` . **PaddingTop**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/DatePicker2_1` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/DatePicker2_1` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
(145)*((App.Width/640))
```

### `ScrHistory/DatePicker2_1` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
(72)*((App.Width/640))
```

### `ScrHistory/DatePicker2_1` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
(89)*((App.Height/1136))
```

### `ScrHistory/Button7` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Button7` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/Button7` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varFilterType = "Бүгд",
    RGBA(20,20,15,1),      // идэвхтэй үед — хар
    RGBA(230,210,220,1)    // идэвхгүй үед — өмнөх цайвар өнгө
)
```

### `ScrHistory/Button7` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/Button7` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varFilterType = "Бүгд",
    RGBA(255,255,255,1),
    RGBA(80,20,45,1)  // одоогийн maroon өнгө
)
```

### `ScrHistory/Button7` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `ScrHistory/Button7` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(55)*((App.Height/1136))
```

### `ScrHistory/Button7` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/Button7` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Button7` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#29483D")
```

### `ScrHistory/Button7` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
// Бүгд
Set(varFilterType, "Бүгд")
```

### `ScrHistory/Button7` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button7` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button7` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#345D4F")
```

### `ScrHistory/Button7` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(11,Min(16,Self.Width/Max(10,Len(Self.Text))*1.4))
```

### `ScrHistory/Button7` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бүгд"
```

### `ScrHistory/Button7` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(100)*((App.Width/640))
```

### `ScrHistory/Button7` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((App.Width/640))
```

### `ScrHistory/Button7` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(147)*((App.Height/1136))
```

### `ScrHistory/Button7_1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Button7_1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/Button7_1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varFilterType = "Зөрүүтэй",
    RGBA(20,20,15,1),      // идэвхтэй үед — хар
    RGBA(230,210,220,1)    // идэвхгүй үед — өмнөх цайвар өнгө
)
```

### `ScrHistory/Button7_1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/Button7_1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varFilterType = "Зөрүүтэй",
    RGBA(255,255,255,1),
    RGBA(80,20,45,1)
)
```

### `ScrHistory/Button7_1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Button7_1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(55)*((App.Height/1136))
```

### `ScrHistory/Button7_1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/Button7_1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Button7_1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/Button7_1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
// Зөрүүтэй
Set(varFilterType, "Зөрүүтэй")
```

### `ScrHistory/Button7_1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Button7_1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Button7_1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Button7_1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Button7_1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button7_1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button7_1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/Button7_1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зөрүүтэй"
```

### `ScrHistory/Button7_1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(108)*((App.Width/640))
```

### `ScrHistory/Button7_1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(150)*((App.Width/640))
```

### `ScrHistory/Button7_1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(147)*((App.Height/1136))
```

### `ScrHistory/Button7_2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Button7_2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/Button7_2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varFilterType = "Таарсан",
    RGBA(20,20,15,1),      // идэвхтэй үед — хар
    RGBA(230,210,220,1)    // идэвхгүй үед — өмнөх цайвар өнгө
)
```

### `ScrHistory/Button7_2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/Button7_2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varFilterType = "Таарсан",
    RGBA(255,255,255,1),
    RGBA(80,20,45,1)
)
```

### `ScrHistory/Button7_2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Button7_2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(55)*((App.Height/1136))
```

### `ScrHistory/Button7_2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/Button7_2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Button7_2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/Button7_2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
// Таарсан
Set(varFilterType, "Таарсан")
```

### `ScrHistory/Button7_2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Button7_2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Button7_2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Button7_2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Button7_2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button7_2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/Button7_2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/Button7_2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Button7_2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Таарсан"
```

### `ScrHistory/Button7_2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(107)*((App.Width/640))
```

### `ScrHistory/Button7_2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(266)*((App.Width/640))
```

### `ScrHistory/Button7_2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(147)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/galHistoryFlex` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex` . **Height**  _(Gallery@2.15.0)_
```powerfx
Max(120,App.Height-380*App.Height/1136)
```

### `ScrHistory/galHistoryFlex` . **Items**  _(Gallery@2.15.0)_
```powerfx
If(varHistoryArchive,SortByColumns(
    Filter(colLegacyInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),Counter=User().FullName && 

        DateValue(CountDate) >= DatePicker2_1.SelectedDate &&
        DateValue(CountDate) <= DatePicker2.SelectedDate &&

        (
            varFilterType = "Бүгд" ||

            (
                varFilterType = "Зөрүүтэй" &&
                Variance <> 0
            ) ||

            (
                varFilterType = "Таарсан" &&
                Variance = 0
            )
        )
    ),
    "CountDate",
    SortOrder.Descending
),SortByColumns(
    Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && Coalesce(Archived,false)=varHistoryTrash && 

        DateValue(CountDate) >= DatePicker2_1.SelectedDate &&
        DateValue(CountDate) <= DatePicker2.SelectedDate &&

        (
            varFilterType = "Бүгд" ||

            (
                varFilterType = "Зөрүүтэй" &&
                Variance <> 0
            ) ||

            (
                varFilterType = "Таарсан" &&
                Variance = 0
            )
        )
    ),
    "CountDate",
    SortOrder.Descending
))
```

### `ScrHistory/galHistoryFlex` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
180*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex` . **Width**  _(Gallery@2.15.0)_
```powerfx
App.Width-32*App.Width/640
```

### `ScrHistory/galHistoryFlex` . **X**  _(Gallery@2.15.0)_
```powerfx
16*App.Width/640
```

### `ScrHistory/galHistoryFlex` . **Y**  _(Gallery@2.15.0)_
```powerfx
280*App.Height/1136
```

### `ScrHistory/galHistoryFlex/Button11` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#394141")
```

### `ScrHistory/galHistoryFlex/Button11` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button11` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button11` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#151A1A")
```

### `ScrHistory/galHistoryFlex/Button11` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button11` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(145)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button11` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button11` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button11` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Button11` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button11` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button11` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button11` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button11` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Button11` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - 52)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button11` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(26)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button11` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
180*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2E6E3")
```

### `ScrHistory/galHistoryFlex/Button8_1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button8_1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button8_1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#192225")
```

### `ScrHistory/galHistoryFlex/Button8_1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button8_1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
180*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button8_1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button8_1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#233330")
```

### `ScrHistory/galHistoryFlex/Button8_1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Button8_1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button8_1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button8_1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#29483D")
```

### `ScrHistory/galHistoryFlex/Button8_1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.TemplateWidth
```

### `ScrHistory/galHistoryFlex/Button8_1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button8_1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Color**  _(Label@2.5.1)_
```powerfx
With(
    {v: Value(Coalesce(ThisItem.Variance, "0"))},
    If(
        v = 0,
        ColorValue("#B8FF2C"),
        ColorValue("#FF784A")
    )
)
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Fill**  _(Label@2.5.1)_
```powerfx
With(
    {v: Value(Coalesce(ThisItem.Variance, "0"))},
    If(
        v = 0,
        ColorValue("#233414"),
        ColorValue("#3B2117")
    )
)
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Size**  _(Label@2.5.1)_
```powerfx
(11)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Text**  _(Label@2.5.1)_
```powerfx
With(
    {
        v: Coalesce(ThisItem.Variance, 0)
    },
    If(
        v = 0,
        "таарсан",
        If(
            v > 0,
            "илүү " & Text(Abs(v), "#,##0"),
            "дутуу " & Text(Abs(v), "#,##0")
        )
    )
)
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Width**  _(Label@2.5.1)_
```powerfx
(110)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **X**  _(Label@2.5.1)_
```powerfx
(14)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/lblVarianceStatus_1` . **Y**  _(Label@2.5.1)_
```powerfx
(82)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#596060")
```

### `ScrHistory/galHistoryFlex/Button9_1` . **BorderStyle**  _(Classic/Button@2.2.0)_
```powerfx
BorderStyle.Dashed
```

### `ScrHistory/galHistoryFlex/Button9_1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4F7F6")
```

### `ScrHistory/galHistoryFlex/Button9_1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#263734")
```

### `ScrHistory/galHistoryFlex/Button9_1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
36*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button9_1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button9_1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button9_1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varExpandedID = ThisItem.SyncKey,

    Set(varExpandedID, Blank()),

    Set(varExpandedID, ThisItem.SyncKey);

    Set(
        varReason,
        If(
            IsBlank(ThisItem.Reason),
            Blank(),
            ThisItem.Reason
        )
    )
)
```

### `ScrHistory/galHistoryFlex/Button9_1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button9_1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button9_1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button9_1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(11)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"+ тайлбар"
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
Value(Coalesce(ThisItem.Variance, "0")) <> 0
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(104)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button9_1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(106)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(11)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
If(
    varExpandedID = ThisItem.SyncKey,
    255,
    If(
        !IsBlank(ThisItem.Reason) || !IsBlank(ThisItem.Comment),
        125,
        104
    )
)
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **X**  _(Rectangle@2.3.0)_
```powerfx
(40)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Rectangle4_1` . **Y**  _(Rectangle@2.3.0)_
```powerfx
336*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
If(
    Value(Coalesce(ThisItem.Variance, "0")) = 0,
    ColorValue("#B8FF2C"),
    ColorValue("#FF6B3D")
)
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
false
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **X**  _(Rectangle@2.3.0)_
```powerfx
(32)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Rectangle6_1` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(38)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#252A2A")
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **Width**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))))*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Separator3_1` . **Y**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Self.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
Self.Tooltip
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(23)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronRight
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **Tooltip**  _(Classic/Icon@2.5.0)_
```powerfx
"View item details"
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
false
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(50)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - (Self.Width/((App.Width/640))) - 12)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/NextArrow3_1` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(42)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/galHistoryFlex/Body1_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A4B3AE")
```

### `ScrHistory/galHistoryFlex/Body1_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Body1_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `ScrHistory/galHistoryFlex/Body1_1` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Body1_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode
    & "  •  "
    & Text(
        DateTimeValue(ThisItem.CountDate, "en-US"),
        "[$-en-US]m/d/yyyy h:mm AM/PM"
    )
```

### `ScrHistory/galHistoryFlex/Body1_1` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrHistory/galHistoryFlex/Body1_1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-28*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **X**  _(Label@2.5.1)_
```powerfx
(14)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Body1_1` . **Y**  _(Label@2.5.1)_
```powerfx
(64)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#F4F7F6")
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemName
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Tooltip**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemName
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-28*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **X**  _(Label@2.5.1)_
```powerfx
(14)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Subtitle2_1` . **Y**  _(Label@2.5.1)_
```powerfx
(38)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/galHistoryFlex/Title5_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#F4F7F6")
```

### `ScrHistory/galHistoryFlex/Title5_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Title5_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrHistory/galHistoryFlex/Title5_1` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Title5_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **Size**  _(Label@2.5.1)_
```powerfx
(15)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemNo
```

### `ScrHistory/galHistoryFlex/Title5_1` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrHistory/galHistoryFlex/Title5_1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-180*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **X**  _(Label@2.5.1)_
```powerfx
(14)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Title5_1` . **Y**  _(Label@2.5.1)_
```powerfx
(10)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/Label23_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#F4F7F6")
```

### `ScrHistory/galHistoryFlex/Label23_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Label23_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Label23_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Size**  _(Label@2.5.1)_
```powerfx
Min(18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640)),Self.Width/Max(8,Len(Self.Text))*1.05)
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.CountQty,If(Mod(ThisItem.CountQty,1)=0,"#,##0","#,##0.###"))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Width**  _(Label@2.5.1)_
```powerfx
144*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrHistory/galHistoryFlex/Label23_1` . **X**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-160*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label23_1` . **Y**  _(Label@2.5.1)_
```powerfx
(10)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/Label5_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#879393")
```

### `ScrHistory/galHistoryFlex/Label5_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Height**  _(Label@2.5.1)_
```powerfx
Max(20,20*App.Height/1136)
```

### `ScrHistory/galHistoryFlex/Label5_1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Label5_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,10*Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Text**  _(Label@2.5.1)_
```powerfx
If(varHistoryArchive,"Хуучин",ThisItem.Synced,"Хадгалсан","Илгээгээгүй")
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Visible**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Width**  _(Label@2.5.1)_
```powerfx
(90)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **X**  _(Label@2.5.1)_
```powerfx
(542)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label5_1` . **Y**  _(Label@2.5.1)_
```powerfx
(45)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/galHistoryFlex/Button12` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    Color.White,
    ColorValue("#D0D6D4")
)
```

### `ScrHistory/galHistoryFlex/Button12` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button12` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    ColorValue("#E14B0A"),
    ColorValue("#3A4240")
)
```

### `ScrHistory/galHistoryFlex/Button12` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button12` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Normal
```

### `ScrHistory/galHistoryFlex/Button12` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button12` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button12` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button12` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReason, "Хэмжилтийн зөрүү")
```

### `ScrHistory/galHistoryFlex/Button12` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button12` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button12` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button12` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(9)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button12` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хэмжилтийн зөрүү"
```

### `ScrHistory/galHistoryFlex/Button12` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Button12` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(105)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button12` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(36)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button12` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
188*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button13` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/galHistoryFlex/Button13` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    Color.White,
    ColorValue("#D0D6D4")
)
```

### `ScrHistory/galHistoryFlex/Button13` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button13` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    ColorValue("#E14B0A"),
    ColorValue("#3A4240")
)
```

### `ScrHistory/galHistoryFlex/Button13` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button13` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Normal
```

### `ScrHistory/galHistoryFlex/Button13` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button13` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button13` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button13` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReason, "Гэмтэлтэй")
```

### `ScrHistory/galHistoryFlex/Button13` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button13` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button13` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button13` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(9)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button13` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гэмтэлтэй"
```

### `ScrHistory/galHistoryFlex/Button13` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Button13` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(80)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button13` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(146)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button13` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
188*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button14` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/galHistoryFlex/Button14` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    Color.White,
    ColorValue("#D0D6D4")
)
```

### `ScrHistory/galHistoryFlex/Button14` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button14` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    ColorValue("#E14B0A"),
    ColorValue("#3A4240")
)
```

### `ScrHistory/galHistoryFlex/Button14` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button14` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Normal
```

### `ScrHistory/galHistoryFlex/Button14` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button14` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button14` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button14` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReason, "Бичиг баримтгүй")
```

### `ScrHistory/galHistoryFlex/Button14` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button14` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button14` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button14` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(9)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button14` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бичиг баримтгүй"
```

### `ScrHistory/galHistoryFlex/Button14` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Button14` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(110)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button14` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(231)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button14` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
188*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button15` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/galHistoryFlex/Button15` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    Color.White,
    ColorValue("#D0D6D4")
)
```

### `ScrHistory/galHistoryFlex/Button15` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button15` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(
    varReason = Self.Text,
    ColorValue("#E14B0A"),
    ColorValue("#3A4240")
)
```

### `ScrHistory/galHistoryFlex/Button15` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button15` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Normal
```

### `ScrHistory/galHistoryFlex/Button15` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button15` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button15` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button15` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varReason, "Байршил өөр")
```

### `ScrHistory/galHistoryFlex/Button15` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button15` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button15` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button15` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(9)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button15` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Байршил өөр"
```

### `ScrHistory/galHistoryFlex/Button15` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Button15` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(95)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button15` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(36)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button15` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
216*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/TextInput1` . **BorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
Coalesce(ThisItem.Comment, "")
```

### `ScrHistory/galHistoryFlex/TextInput1` . **DelayOutput**  _(Classic/TextInput@2.3.2)_
```powerfx
true
```

### `ScrHistory/galHistoryFlex/TextInput1` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/TextInput1` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(38)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"""Зөрүүний тайлбар..."""
```

### `ScrHistory/galHistoryFlex/TextInput1` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/TextInput1` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ScrHistory/galHistoryFlex/TextInput1` . **RadiusBottomLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **RadiusBottomRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **RadiusTopLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **RadiusTopRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
(9)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/TextInput1` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - 72)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(36)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/TextInput1` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
250*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button16` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/galHistoryFlex/Button16` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button16` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button16` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varCountSaving,false) || Coalesce(varCountSyncBusy,false) || Coalesce(varHistoryLoading,false) || varHistoryArchive || varHistoryTrash || (!varCountCacheReady && !Connection.Connected),DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrHistory/galHistoryFlex/Button16` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrHistory/galHistoryFlex/Button16` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button16` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(24)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button16` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button16` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button16` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varCountSaving,false) || Coalesce(varCountSyncBusy,false) || Coalesce(varHistoryLoading,false) || IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)) || varHistoryArchive || varHistoryTrash || ThisItem.OwnerEmail<>varCountOwner,
 Notify("Энэ бүртгэлийг одоо өөрчлөх боломжгүй.",NotificationType.Warning),
 Set(varCountSaving,true);Set(varHistorySavedV22,false);Set(varHistoryCloudOnlyV22,false);Set(varHistoryActionErrorV22,"");
 ClearCollect(colHistoryNoteBeforeV22,Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),SyncKey=ThisItem.SyncKey && OwnerEmail=varCountOwner));
 With({_before:First(colHistoryNoteBeforeV22)},
 If(IsBlank(_before.SyncKey),Notify("Бүртгэл олдсонгүй.",NotificationType.Error),
 Patch(colOfflineInventory,_before,{Reason:"",Comment:"",Resolved:false},{Synced:false,Revision:Coalesce(_before.Revision,0)+1});
 IfError(If(!varCountDiskSafeV21,Error({Kind:ErrorKind.Validation,Message:"Төхөөрөмжийн эх санг аюулгүй уншаагүй тул дарж бичихгүй."}),
ClearCollect(colCountDiskV21,{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)});
SaveData(colCountDiskV21,varCountCacheKey)),
 Set(varCountCacheReady,false);Set(varCountStorageError,FirstError.Message);false,
 Set(varCountCacheReady,true);Set(varCountStorageError,"");Set(varHistorySavedV22,true);true);
 If(!varHistorySavedV22 && Connection.Connected,
 IfError(If(!_before.Synced,Error({Kind:ErrorKind.Validation,Message:"Энэ мөрийн өмнөх өөрчлөлт серверт илгээгдээгүй байна. Оффлайн хадгалалтыг сэргээж дахин оролдоно уу."}),With({_id:_before.SharePointID,_title:_before.Title,_archived:"ARCHIVED:" & _before.Title},
 With({_server:If(_id>0,LookUp(InventoryCount,ID=_id),Coalesce(LookUp(InventoryCount,Title=_title && Counter=varCountOwner),LookUp(InventoryCount,Title=_archived && Counter=varCountOwner)))},
 If(IsBlank(_server.ID),Error({Kind:ErrorKind.NotFound,Message:"Серверийн эх мөр олдсонгүй. Төхөөрөмжийн хадгалалтыг сэргээж дахин оролдоно уу."}),
 !(_server.Counter=varCountOwner || (_server.Counter=User().FullName && _server.'Created By'.Email=varCountOwner)),
 Error({Kind:ErrorKind.Validation,Message:"Энэ бүртгэлийн эзэмшигч тохирохгүй байна."}),
 With({_ack:Patch(InventoryCount,_server,{Reason:"",Comment:"",Resolved:false})},
 If(IsBlank(_ack.ID),Error({Kind:ErrorKind.Validation,Message:"Сервер өөрчлөлтийг баталгаажуулсангүй."}),
 Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=_before.SyncKey && OwnerEmail=varCountOwner),
 {SharePointID:_ack.ID,Synced:true,SyncError:""});true)))))),
 Set(varHistoryActionErrorV22,FirstError.Message);false,
 Set(varHistorySavedV22,true);Set(varHistoryCloudOnlyV22,true);true));
 If(varHistorySavedV22,
 Set(varExpandedID,Blank());Set(varReason,Blank());Reset(TextInput1);
 Notify(If(varHistoryCloudOnlyV22,"Тайлбарыг SharePoint-д хадгаллаа. Оффлайн хуулбар шинэчлэгдээгүй.","Тайлбарыг төхөөрөмжид хадгаллаа."),If(varHistoryCloudOnlyV22,NotificationType.Warning,NotificationType.Success)),
 Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=_before.SyncKey && OwnerEmail=varCountOwner),_before);
 Notify("Өөрчлөлт хадгалагдсангүй. " & Coalesce(varHistoryActionErrorV22,varCountStorageError),NotificationType.Error))));
 Clear(colHistoryNoteBeforeV22);
 Set(varCountUploadQueue,varCountCacheReady && Connection.Connected && !IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)));
 Set(varCountSaving,false))
```

### `ScrHistory/galHistoryFlex/Button16` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button16` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button16` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button16` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button16` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тайлбар арилгах"
```

### `ScrHistory/galHistoryFlex/Button16` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Button16` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
120*App.Width/640
```

### `ScrHistory/galHistoryFlex/Button16` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.TemplateWidth-230*App.Width/640
```

### `ScrHistory/galHistoryFlex/Button16` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
298*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button17` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/galHistoryFlex/Button17` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#162000")
```

### `ScrHistory/galHistoryFlex/Button17` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/Button17` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varCountSaving,false) || Coalesce(varCountSyncBusy,false) || Coalesce(varHistoryLoading,false) || varHistoryArchive || varHistoryTrash || (!varCountCacheReady && !Connection.Connected),DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrHistory/galHistoryFlex/Button17` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrHistory/galHistoryFlex/Button17` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Button17` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(28)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/Button17` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/Button17` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/galHistoryFlex/Button17` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varCountSaving,false) || Coalesce(varCountSyncBusy,false) || Coalesce(varHistoryLoading,false) || IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)) || varHistoryArchive || varHistoryTrash || ThisItem.OwnerEmail<>varCountOwner,
 Notify("Энэ бүртгэлийг одоо өөрчлөх боломжгүй.",NotificationType.Warning),
 Set(varCountSaving,true);Set(varHistorySavedV22,false);Set(varHistoryCloudOnlyV22,false);Set(varHistoryActionErrorV22,"");
 ClearCollect(colHistoryNoteBeforeV22,Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),SyncKey=ThisItem.SyncKey && OwnerEmail=varCountOwner));
 With({_before:First(colHistoryNoteBeforeV22)},
 If(IsBlank(_before.SyncKey),Notify("Бүртгэл олдсонгүй.",NotificationType.Error),
 Patch(colOfflineInventory,_before,{Reason:Coalesce(varReason,""),Comment:TextInput1.Text,Resolved:true},{Synced:false,Revision:Coalesce(_before.Revision,0)+1});
 IfError(If(!varCountDiskSafeV21,Error({Kind:ErrorKind.Validation,Message:"Төхөөрөмжийн эх санг аюулгүй уншаагүй тул дарж бичихгүй."}),
ClearCollect(colCountDiskV21,{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)});
SaveData(colCountDiskV21,varCountCacheKey)),
 Set(varCountCacheReady,false);Set(varCountStorageError,FirstError.Message);false,
 Set(varCountCacheReady,true);Set(varCountStorageError,"");Set(varHistorySavedV22,true);true);
 If(!varHistorySavedV22 && Connection.Connected,
 IfError(If(!_before.Synced,Error({Kind:ErrorKind.Validation,Message:"Энэ мөрийн өмнөх өөрчлөлт серверт илгээгдээгүй байна. Оффлайн хадгалалтыг сэргээж дахин оролдоно уу."}),With({_id:_before.SharePointID,_title:_before.Title,_archived:"ARCHIVED:" & _before.Title},
 With({_server:If(_id>0,LookUp(InventoryCount,ID=_id),Coalesce(LookUp(InventoryCount,Title=_title && Counter=varCountOwner),LookUp(InventoryCount,Title=_archived && Counter=varCountOwner)))},
 If(IsBlank(_server.ID),Error({Kind:ErrorKind.NotFound,Message:"Серверийн эх мөр олдсонгүй. Төхөөрөмжийн хадгалалтыг сэргээж дахин оролдоно уу."}),
 !(_server.Counter=varCountOwner || (_server.Counter=User().FullName && _server.'Created By'.Email=varCountOwner)),
 Error({Kind:ErrorKind.Validation,Message:"Энэ бүртгэлийн эзэмшигч тохирохгүй байна."}),
 With({_ack:Patch(InventoryCount,_server,{Reason:Coalesce(varReason,""),Comment:TextInput1.Text,Resolved:true})},
 If(IsBlank(_ack.ID),Error({Kind:ErrorKind.Validation,Message:"Сервер өөрчлөлтийг баталгаажуулсангүй."}),
 Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=_before.SyncKey && OwnerEmail=varCountOwner),
 {SharePointID:_ack.ID,Synced:true,SyncError:""});true)))))),
 Set(varHistoryActionErrorV22,FirstError.Message);false,
 Set(varHistorySavedV22,true);Set(varHistoryCloudOnlyV22,true);true));
 If(varHistorySavedV22,
 Set(varExpandedID,Blank());Set(varReason,Blank());Reset(TextInput1);
 Notify(If(varHistoryCloudOnlyV22,"Тайлбарыг SharePoint-д хадгаллаа. Оффлайн хуулбар шинэчлэгдээгүй.","Тайлбарыг төхөөрөмжид хадгаллаа."),If(varHistoryCloudOnlyV22,NotificationType.Warning,NotificationType.Success)),
 Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=_before.SyncKey && OwnerEmail=varCountOwner),_before);
 Notify("Өөрчлөлт хадгалагдсангүй. " & Coalesce(varHistoryActionErrorV22,varCountStorageError),NotificationType.Error))));
 Clear(colHistoryNoteBeforeV22);
 Set(varCountUploadQueue,varCountCacheReady && Connection.Connected && !IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)));
 Set(varCountSaving,false))
```

### `ScrHistory/galHistoryFlex/Button17` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button17` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/Button17` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ScrHistory/galHistoryFlex/Button17` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(9)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Button17` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Болсон"
```

### `ScrHistory/galHistoryFlex/Button17` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
varExpandedID = ThisItem.SyncKey
```

### `ScrHistory/galHistoryFlex/Button17` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(75)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button17` . **X**  _(Classic/Button@2.2.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - 105)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Button17` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
298*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label11` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/galHistoryFlex/Label11` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label11` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#FF6B3D")
```

### `ScrHistory/galHistoryFlex/Label11` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label11` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/Label11` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label11` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ScrHistory/galHistoryFlex/Label11` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label11` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label11` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label11` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/Label11` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label11` . **Text**  _(Label@2.5.1)_
```powerfx

Coalesce(ThisItem.Reason, "") &
If(
    !IsBlank(ThisItem.Comment),
    "   " & ThisItem.Comment,
    ""
)
```

### `ScrHistory/galHistoryFlex/Label11` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `ScrHistory/galHistoryFlex/Label11` . **Visible**  _(Label@2.5.1)_
```powerfx
!IsBlank(ThisItem.Reason) || !IsBlank(ThisItem.Comment)
```

### `ScrHistory/galHistoryFlex/Label11` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-144*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label11` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrHistory/galHistoryFlex/Label11` . **X**  _(Label@2.5.1)_
```powerfx
(130)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/Label11` . **Y**  _(Label@2.5.1)_
```powerfx
(84)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#596060")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **BorderStyle**  _(Classic/Button@2.2.0)_
```powerfx
BorderStyle.Dashed
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFB8AC")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A4B3AE")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242829")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varCountSaving,false) || Coalesce(varCountSyncBusy,false) || Coalesce(varHistoryLoading,false) || (!varCountCacheReady && !Connection.Connected),DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#392427")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
36*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#553033")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
ClearCollect(colHistoryDeleteV16,ThisItem);Set(varHistoryDeleteMode,If(varHistoryTrash,"restore","delete"));Set(varHistoryDeleteConfirm,true);SetFocus(hDeleteCancelV16)
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#6C343A")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(11)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varHistoryTrash,"Сэргээх","Хогийн сав")
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varHistoryArchive
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
144*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.TemplateWidth-160*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/galHistoryFlex/hDeleteRowV16` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(106)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `ScrHistory/Icon2` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Icon2` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Тооллогын түүхийг CSV хавсралттай өөрийн мэйлд илгээх"
```

### `ScrHistory/Icon2` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Icon2` . **BorderStyle**  _(Classic/Icon@2.5.0)_
```powerfx
BorderStyle.None
```

### `ScrHistory/Icon2` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Icon2` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `ScrHistory/Icon2` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/Icon2` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Icon2` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Mail
```

### `ScrHistory/Icon2` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
If(varHistoryMailSendingV18,Notify("Тайлан илгээж байна…",NotificationType.Information),!Connection.Connected,Notify("Интернет холболт шаардлагатай.",NotificationType.Warning),DatePicker2_1.SelectedDate>DatePicker2.SelectedDate,Notify("Огнооны дарааллыг шалгана уу.",NotificationType.Warning),With({_rows:Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Coalesce(Archived,false) && CountDate>=DatePicker2_1.SelectedDate && CountDate<DateAdd(DatePicker2.SelectedDate,1,TimeUnit.Days) && Switch(varFilterType,"Зөрүүтэй",CountQty<>OpeningBalance,"Таарсан",CountQty=OpeningBalance,true))},If(IsEmpty(_rows),Notify("Илгээх мөр алга.",NotificationType.Information),Set(varHistoryMailSendingV18,true);IfError(Set(varMailResult,PA_ExportInventoryCSV.Run(JSON(ForAll(_rows As r,{'Огноо':If(IsBlank(r.CountDate),"",Text(r.CountDate,"yyyy-mm-dd hh:mm:ss")),'Барааны код':If(IsMatch(r.ItemNo,"[0-9]+"),"=" & Char(34) & r.ItemNo & Char(34),With({s:Coalesce(r.ItemNo,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s))),'Барааны нэр':With({s:Coalesce(r.ItemName,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Агуулах':With({s:Coalesce(r.LocationCode,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Үлдэгдэл':r.OpeningBalance,'Тоолсон':r.CountQty,'Зөрүү':If(IsBlank(r.CountQty),Blank(),r.CountQty-r.OpeningBalance),'Тоологч':With({s:Coalesce(r.Counter,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Шалтгаан':With({s:Coalesce(r.Reason,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Тайлбар':With({s:Coalesce(r.Comment,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s))}),JSONFormat.Compact),User().Email,"[CSV2] " & "Тооллогын түүх " & Text(DatePicker2_1.SelectedDate,"yyyy-mm-dd") & " - " & Text(DatePicker2.SelectedDate,"yyyy-mm-dd"),"<h2>" & Substitute(Substitute(Substitute(Coalesce("Тооллогын түүх",""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</h2><p>Хэрэглэгч: " & Substitute(Substitute(Substitute(Coalesce(User().FullName,""),"&","&amp;"),"<","&lt;"),">","&gt;") & " · " & Substitute(Substitute(Substitute(Coalesce(User().Email,""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Хугацаа: " & Text(DatePicker2_1.SelectedDate,"yyyy-mm-dd") & " — " & Text(DatePicker2.SelectedDate,"yyyy-mm-dd") & "</p><p>Хуудас: " & Substitute(Substitute(Substitute(Coalesce("Түүх · сонгосон хугацааны бүртгэлүүд",""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Шүүлт: " & Substitute(Substitute(Substitute(Coalesce(varFilterType,""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Нийт мөр: " & CountRows(_rows) & "</p><p>Таарсан: " & CountRows(Filter(_rows,!IsBlank(CountQty) && CountQty=OpeningBalance)) & " · Дутуу: " & CountRows(Filter(_rows,!IsBlank(CountQty) && CountQty<OpeningBalance)) & " · Илүү: " & CountRows(Filter(_rows,!IsBlank(CountQty) && CountQty>OpeningBalance)) & "</p><p>Агуулахын тоо: " & CountRows(Distinct(_rows,LocationCode)) & "</p><p>Дэлгэрэнгүй тайланг хавсралтаас үзнэ үү.</p>")),Notify("Илгээхэд алдаа: " & FirstError.Message,NotificationType.Error),Notify("Түүхийн хураангуй болон CSV хавсралтыг өөрийн мэйлд илгээлээ.",NotificationType.Success));Set(varHistoryMailSendingV18,false))))
```

### `ScrHistory/Icon2` . **Tooltip**  _(Classic/Icon@2.5.0)_
```powerfx
"Түүхийн хураангуй + CSV хавсралт"
```

### `ScrHistory/Icon2` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
App.Width-64
```

### `ScrHistory/Icon2` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
32*App.Height/1136
```

### `ScrHistory/Icon3` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Icon3` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Тооллого эхлэх"
```

### `ScrHistory/Icon3` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Icon3` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Icon3` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Icon3` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/Icon3` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Icon3` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Height/1136))
```

### `ScrHistory/Icon3` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.BackArrow
```

### `ScrHistory/Icon3` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate('scrWarehouses')
```

### `ScrHistory/Icon3` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Width/640))
```

### `ScrHistory/Icon3` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(112)*((App.Width/640))
```

### `ScrHistory/Icon3` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(1058)*((App.Height/1136))
```

### `ScrHistory/Label25` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/Label25` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/Label25` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Label25` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/Label25` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Label25` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/Label25` . **Height**  _(Label@2.5.1)_
```powerfx
(64)*((App.Height/1136))
```

### `ScrHistory/Label25` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Label25` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Label25` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/Label25` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/Label25` . **Size**  _(Label@2.5.1)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/Label25` . **Text**  _(Label@2.5.1)_
```powerfx
"Тооллого буцах"
```

### `ScrHistory/Label25` . **Width**  _(Label@2.5.1)_
```powerfx
(436)*((App.Width/640))
```

### `ScrHistory/Label25` . **X**  _(Label@2.5.1)_
```powerfx
(204)*((App.Width/640))
```

### `ScrHistory/Label25` . **Y**  _(Label@2.5.1)_
```powerfx
(1058)*((App.Height/1136))
```

### `ScrHistory/hTrashV16` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/hTrashV16` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/hTrashV16` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hTrashV16` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(99, 139, 44, 1)
```

### `ScrHistory/hTrashV16` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/hTrashV16` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/hTrashV16` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hTrashV16` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `ScrHistory/hTrashV16` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Bold
```

### `ScrHistory/hTrashV16` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
40*App.Height/1136
```

### `ScrHistory/hTrashV16` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/hTrashV16` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/hTrashV16` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#29483D")
```

### `ScrHistory/hTrashV16` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varHistoryTrash,!varHistoryTrash);Set(varHistoryArchive,false);Set(varExpandedID,Blank())
```

### `ScrHistory/hTrashV16` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/hTrashV16` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/hTrashV16` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#345D4F")
```

### `ScrHistory/hTrashV16` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(11,Min(16,Self.Width/Max(10,Len(Self.Text))*1.4))
```

### `ScrHistory/hTrashV16` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varHistoryTrash,"← Өөрийн түүх","Хогийн сав")
```

### `ScrHistory/hTrashV16` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
170*App.Width/640
```

### `ScrHistory/hTrashV16` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16*App.Width/640
```

### `ScrHistory/hTrashV16` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
205*App.Height/1136
```

### `ScrHistory/hCleanV16` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/hCleanV16` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hCleanV16` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(99, 139, 44, 1)
```

### `ScrHistory/hCleanV16` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/hCleanV16` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountSyncBusy || varCountSaving || varHistoryLoading || (!varCountCacheReady && !Connection.Connected),DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrHistory/hCleanV16` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `ScrHistory/hCleanV16` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hCleanV16` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `ScrHistory/hCleanV16` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Bold
```

### `ScrHistory/hCleanV16` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
40*App.Height/1136
```

### `ScrHistory/hCleanV16` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/hCleanV16` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/hCleanV16` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#29483D")
```

### `ScrHistory/hCleanV16` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
ClearCollect(colHistoryDeleteV16,If(varHistoryArchive,SortByColumns(
    Filter(colLegacyInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),Counter=User().FullName && 

        DateValue(CountDate) >= DatePicker2_1.SelectedDate &&
        DateValue(CountDate) <= DatePicker2.SelectedDate &&

        (
            varFilterType = "Бүгд" ||

            (
                varFilterType = "Зөрүүтэй" &&
                Variance <> 0
            ) ||

            (
                varFilterType = "Таарсан" &&
                Variance = 0
            )
        )
    ),
    "CountDate",
    SortOrder.Descending
),SortByColumns(
    Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && Coalesce(Archived,false)=varHistoryTrash && 

        DateValue(CountDate) >= DatePicker2_1.SelectedDate &&
        DateValue(CountDate) <= DatePicker2.SelectedDate &&

        (
            varFilterType = "Бүгд" ||

            (
                varFilterType = "Зөрүүтэй" &&
                Variance <> 0
            ) ||

            (
                varFilterType = "Таарсан" &&
                Variance = 0
            )
        )
    ),
    "CountDate",
    SortOrder.Descending
)));Set(varHistoryDeleteMode,If(varHistoryTrash,"restore","delete"));Set(varHistoryDeleteConfirm,!IsEmpty(colHistoryDeleteV16))
```

### `ScrHistory/hCleanV16` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/hCleanV16` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/hCleanV16` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#345D4F")
```

### `ScrHistory/hCleanV16` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Max(11,Min(16,Self.Width/Max(10,Len(Self.Text))*1.4))
```

### `ScrHistory/hCleanV16` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varHistoryTrash,"Шүүсэн мөрүүдийг сэргээх","Шүүсэн мөрүүдийг цэвэрлэх")
```

### `ScrHistory/hCleanV16` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (!varHistoryArchive)
```

### `ScrHistory/hCleanV16` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
420*App.Width/640
```

### `ScrHistory/hCleanV16` . **X**  _(Classic/Button@2.2.0)_
```powerfx
200*App.Width/640
```

### `ScrHistory/hCleanV16` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
205*App.Height/1136
```

### `ScrHistory/hHistoryStateV16` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrHistory/hHistoryStateV16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/hHistoryStateV16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hHistoryStateV16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrHistory/hHistoryStateV16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrHistory/hHistoryStateV16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hHistoryStateV16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/hHistoryStateV16` . **Height**  _(Label@2.5.1)_
```powerfx
28*App.Height/1136
```

### `ScrHistory/hHistoryStateV16` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/hHistoryStateV16` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrHistory/hHistoryStateV16` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrHistory/hHistoryStateV16` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/hHistoryStateV16` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,10*App.Width/640)
```

### `ScrHistory/hHistoryStateV16` . **Text**  _(Label@2.5.1)_
```powerfx
If(!varCountCacheReady,"Төхөөрөмжийн хадгалалт бэлэн биш · " & varCountStorageError,If(varHistoryArchive,"Хуучин локал сан · зөвхөн унших",varHistoryLoading,"Өөрийн түүхийг татаж байна…",varHistoryCloudLimit,"Онлайн түүх 5,000 мөрийн хязгаар хүрсэн; зарим мөр дутуу байж болно",varHistoryCloudError,"Онлайн түүх татагдсангүй · локал түүх хадгалагдсан",varHistoryCacheError,"Түүх онлайн уншигдсан · төхөөрөмжид хадгалах боломжгүй",varHistoryTrash,"Хогийн сав дахь мөрийг буцааж сэргээж болно","Түүх синк хийсний дараа ч төхөөрөмж дээр үлдэнэ"))
```

### `ScrHistory/hHistoryStateV16` . **Tooltip**  _(Label@2.5.1)_
```powerfx
If(!varCountCacheReady,"Оффлайн хадгалалт бэлэн биш. Интернеттэй үед сервер баталгаажуулсан өөрчлөлт хийгдэнэ. " & varCountStorageError,"")
```

### `ScrHistory/hHistoryStateV16` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width-32
```

### `ScrHistory/hHistoryStateV16` . **X**  _(Label@2.5.1)_
```powerfx
16*App.Width/640
```

### `ScrHistory/hHistoryStateV16` . **Y**  _(Label@2.5.1)_
```powerfx
249*App.Height/1136
```

### `ScrHistory/hDeleteShadeV16` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrHistory/hDeleteShadeV16` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteShadeV16` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
RGBA(8,24,17,0.48)
```

### `ScrHistory/hDeleteShadeV16` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
App.Height
```

### `ScrHistory/hDeleteShadeV16` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteShadeV16` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteShadeV16` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteShadeV16` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteShadeV16` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varHistoryDeleteConfirm)
```

### `ScrHistory/hDeleteShadeV16` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
App.Width
```

### `ScrHistory/hDeleteModalV16` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrHistory/hDeleteModalV16` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(1)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrHistory/hDeleteModalV16` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Height*0.9,440*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrHistory/hDeleteModalV16` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(22)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varHistoryDeleteConfirm)
```

### `ScrHistory/hDeleteModalV16` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width*0.92,680*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrHistory/hDeleteModalV16` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrHistory/hDeleteModalV16` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(App.Height-Self.Height)/2
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#153F30")
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.14
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/24,Parent.Height/17)
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Text**  _(Label@2.5.1)_
```powerfx
If(varHistoryDeleteMode="restore","Тооллого сэргээх","Тооллого цэвэрлэх")
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrHistory/hDeleteModalV16/hDeleteTitleV16` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.05
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#86968F")
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.46
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colHistoryDeleteV16),"#,##0") & " мөр" & Char(10) & If(varHistoryDeleteMode="restore","Эдгээр мөр өөрийн түүх, тайланд дахин харагдана.","Эдгээр мөр Хогийн сав руу шилжинэ. Тайлангийн дүнд орохгүй. Дараа нь сэргээж болно.") & Char(10) & "Зөвхөн таны сонгосон мөрүүдэд үйлчилнэ. BC баримтыг өөрчлөхгүй."
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrHistory/hDeleteModalV16/hDeleteInfoV16` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.23
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#153F30")
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varHistoryDeleteConfirm,false)
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Болих"
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.29
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.06
```

### `ScrHistory/hDeleteModalV16/hDeleteCancelV16` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountSyncBusy || varCountSaving || varHistoryLoading,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#B5E755")
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(varCountSaving,false) || Coalesce(varCountSyncBusy,false) || Coalesce(varHistoryLoading,false) || IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Хадгалалт дуусахыг хүлээнэ үү.",NotificationType.Information),
 Set(varCountSaving,true);Set(varHistoryDiskSavedV22,false);Set(varHistoryActionErrorV22,"");
 ClearCollect(colHistoryActionV22,ForAll(FirstN(Filter(colHistoryDeleteV16,OwnerEmail=varCountOwner),25) As selected,
 LookUp(colOfflineInventory,SyncKey=selected.SyncKey && OwnerEmail=varCountOwner)));
 Clear(colHistoryActionResultV22);
 ForAll(Filter(colHistoryActionV22,!IsBlank(SyncKey)) As old,
 Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=old.SyncKey && OwnerEmail=varCountOwner),
 {Archived:varHistoryDeleteMode="delete",Revision:Coalesce(old.Revision,0)+1,Synced:false,SyncError:""}));
 IfError(If(!varCountDiskSafeV21,Error({Kind:ErrorKind.Validation,Message:"Төхөөрөмжийн эх санг аюулгүй уншаагүй тул дарж бичихгүй."}),
ClearCollect(colCountDiskV21,{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)});
SaveData(colCountDiskV21,varCountCacheKey)),
 Set(varCountCacheReady,false);Set(varCountStorageError,FirstError.Message);false,
 Set(varCountCacheReady,true);Set(varCountStorageError,"");Set(varHistoryDiskSavedV22,true);true);
 If(varHistoryDiskSavedV22,
 ForAll(Filter(colHistoryActionV22,!IsBlank(SyncKey)) As old,Collect(colHistoryActionResultV22,{SyncKey:old.SyncKey,Success:true,Message:""})),
 ForAll(Filter(colHistoryActionV22,!IsBlank(SyncKey)) As _before,
 IfError(If(!Connection.Connected,Error({Kind:ErrorKind.Network,Message:"Интернет холболт алга байна."}),If(!_before.Synced,Error({Kind:ErrorKind.Validation,Message:"Энэ мөрийн өмнөх өөрчлөлт серверт илгээгдээгүй байна. Оффлайн хадгалалтыг сэргээж дахин оролдоно уу."}),With({_id:_before.SharePointID,_title:_before.Title,_archived:"ARCHIVED:" & _before.Title},
 With({_server:If(_id>0,LookUp(InventoryCount,ID=_id),Coalesce(LookUp(InventoryCount,Title=_title && Counter=varCountOwner),LookUp(InventoryCount,Title=_archived && Counter=varCountOwner)))},
 If(IsBlank(_server.ID),Error({Kind:ErrorKind.NotFound,Message:"Серверийн эх мөр олдсонгүй. Төхөөрөмжийн хадгалалтыг сэргээж дахин оролдоно уу."}),
 !(_server.Counter=varCountOwner || (_server.Counter=User().FullName && _server.'Created By'.Email=varCountOwner)),
 Error({Kind:ErrorKind.Validation,Message:"Энэ бүртгэлийн эзэмшигч тохирохгүй байна."}),
 With({_ack:Patch(InventoryCount,_server,{Title:If(varHistoryDeleteMode="delete","ARCHIVED:" & _before.Title,_before.Title)})},
 If(IsBlank(_ack.ID),Error({Kind:ErrorKind.Validation,Message:"Сервер өөрчлөлтийг баталгаажуулсангүй."}),
 Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=_before.SyncKey && OwnerEmail=varCountOwner),
 {SharePointID:_ack.ID,Synced:true,SyncError:""});true))))))),
 Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=_before.SyncKey && OwnerEmail=varCountOwner),_before);
 Collect(colHistoryActionResultV22,{SyncKey:_before.SyncKey,Success:false,Message:FirstError.Message});false,
 Collect(colHistoryActionResultV22,{SyncKey:_before.SyncKey,Success:true,Message:""});true)));
 RemoveIf(colHistoryDeleteV16,SyncKey in Filter(colHistoryActionResultV22,Success).SyncKey);
 Set(varExpandedID,Blank());Set(varHistoryDeleteConfirm,!IsEmpty(colHistoryDeleteV16));
 Notify("Амжилттай: " & CountRows(Filter(colHistoryActionResultV22,Success)) & " · Үлдсэн: " & CountRows(colHistoryDeleteV16) &
 If(varHistoryDiskSavedV22," · төхөөрөмжид хадгалсан"," · SharePoint баталгаажуулсан, оффлайн хуулбар шинэчлэгдээгүй") &
 If(!IsEmpty(Filter(colHistoryActionResultV22,!Success)),". " & First(Filter(colHistoryActionResultV22,!Success)).Message,""),
 If(!IsEmpty(Filter(colHistoryActionResultV22,!Success)),NotificationType.Error,If(varHistoryDiskSavedV22,NotificationType.Success,NotificationType.Warning)));
 Clear(colHistoryActionV22);
 Set(varCountUploadQueue,varCountCacheReady && Connection.Connected && !IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)));
 Set(varCountSaving,false))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((Min(App.Width,960)/640))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(colHistoryDeleteV16)>25,"Дараагийн 25 мөр",If(varHistoryDeleteMode="restore","Сэргээх","Хогийн сав руу"))
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.56
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.38
```

### `ScrHistory/hDeleteModalV16/hDeleteConfirmV16` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrHistory/uploadQueueV16_12` . **OnTimerStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrHistory/uploadQueueV16_12` . **AutoPause**  _(Timer@2.1.0)_
```powerfx
false
```

### `ScrHistory/uploadQueueV16_12` . **AutoStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),true
)
```

### `ScrHistory/uploadQueueV16_12` . **BorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrHistory/uploadQueueV16_12` . **BorderThickness**  _(Timer@2.1.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/uploadQueueV16_12` . **Color**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/uploadQueueV16_12` . **DisabledBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 70%)
```

### `ScrHistory/uploadQueueV16_12` . **DisabledColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 90%)
```

### `ScrHistory/uploadQueueV16_12` . **DisabledFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 70%)
```

### `ScrHistory/uploadQueueV16_12` . **Duration**  _(Timer@2.1.0)_
```powerfx
5000
```

### `ScrHistory/uploadQueueV16_12` . **Fill**  _(Timer@2.1.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrHistory/uploadQueueV16_12` . **FocusedBorderThickness**  _(Timer@2.1.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrHistory/uploadQueueV16_12` . **Font**  _(Timer@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrHistory/uploadQueueV16_12` . **HoverBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrHistory/uploadQueueV16_12` . **HoverColor**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrHistory/uploadQueueV16_12` . **HoverFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrHistory/uploadQueueV16_12` . **OnTimerEnd**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),// V27 durable upload: CountKeyV27 is unique in SharePoint.
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

### `ScrHistory/uploadQueueV16_12` . **PressedBorderColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrHistory/uploadQueueV16_12` . **PressedColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrHistory/uploadQueueV16_12` . **PressedFill**  _(Timer@2.1.0)_
```powerfx
Self.Color
```

### `ScrHistory/uploadQueueV16_12` . **Repeat**  _(Timer@2.1.0)_
```powerfx
true
```

### `ScrHistory/uploadQueueV16_12` . **Reset**  _(Timer@2.1.0)_
```powerfx
!varRptPdfPending
```

### `ScrHistory/uploadQueueV16_12` . **Size**  _(Timer@2.1.0)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrHistory/uploadQueueV16_12` . **Start**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Connection.Connected && varCountCacheReady
)
```

### `ScrHistory/uploadQueueV16_12` . **Visible**  _(Timer@2.1.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrHistory/pgDenied550` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrHistory/pgDenied550` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrHistory/pgDenied550` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrHistory/pgDenied550` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrHistory/pgDenied550` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrHistory/pgDenied550` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrHistory/pgDenied550` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrHistory/pgDenied550` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrHistory/pgDenied550` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrHistory/pgDenied550` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

