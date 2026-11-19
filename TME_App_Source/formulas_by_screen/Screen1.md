# Screen1 — Power Fx formulas

### `Screen1` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `Screen1` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `Screen1` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Set(varWView,If(App.Width<First(App.SizeBreakpoints).Value,"stock","overview"));Set(varWFilter,"Бүгд");Set(varWPicker,false);Set(varWBusy,false);Set(varWExport,false);Set(varWItem,Blank());Set(varWChecked,Blank());Set(varWLive,false);Set(varWPhoto,Blank());Clear(colWLedger);Clear(colWLiveBins);
If(!Coalesce(varWInitialized,false),
ClearCollect(colWMinimums,{OwnerEmail:"",ItemNo:"",LocationCode:"",Minimum:0});Clear(colWMinimums);
Set(wMinimumStoreError,"");If(IsBlank(Host.Version),Set(wMinimumStore,"preview"),ClearCollect(colWRestoreMinimums,FirstN(colWMinimums,0));IfError(LoadData(colWRestoreMinimums,"WarehouseMinimumsV6",true);true,Set(wMinimumStoreError,FirstError.Message);Set(wMinimumStore,Switch(FirstError.Kind,ErrorKind.FileNotFound,"ready",ErrorKind.NotSupported,"session","protected"));false,ClearCollect(colWMinimums,colWRestoreMinimums);Set(wMinimumStore,"ready");true);Clear(colWRestoreMinimums));
ClearCollect(colWDrafts,{DraftId:"",OwnerEmail:"",Kind:"",ItemNo:"",ItemName:"",FromLocation:"",ToLocation:"",FromBin:"",ToBin:"",Quantity:0,Uom:"",Reason:"",Recipient:"",Created:Now(),Status:""});Clear(colWDrafts);
Set(wDraftStoreError,"");If(IsBlank(Host.Version),Set(wDraftStore,"preview"),ClearCollect(colWRestoreDrafts,FirstN(colWDrafts,0));IfError(LoadData(colWRestoreDrafts,"WarehouseDraftsV6",true);true,Set(wDraftStoreError,FirstError.Message);Set(wDraftStore,Switch(FirstError.Kind,ErrorKind.FileNotFound,"ready",ErrorKind.NotSupported,"session","protected"));false,ClearCollect(colWDrafts,colWRestoreDrafts);Set(wDraftStore,"ready");true);Clear(colWRestoreDrafts));Set(varWInitialized,true));
If(Connection.Connected && IsEmpty(colWLocationMaster),IfError(ClearCollect(colWLocationMaster,'locations (v2.0)'),Notify("Агуулахын нэрийг онлайн уншиж чадсангүй.",NotificationType.Warning); false, true));
Select(wRebuild)
)
```

### `Screen1` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `Screen1/wRebuild` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wRebuild` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wRebuild` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wRebuild` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wRebuild` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wRebuild` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wRebuild` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wRebuild` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wRebuild` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wRebuild` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wRebuild` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
ClearCollect(colWStock,AddColumns(Filter(colDStockBaseV17,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode)) As s,UnitCost,s.Cost,MinQty,If(IsEmpty(colWMinimums),Blank(),LookUp(colWMinimums,OwnerEmail=User().Email && ItemNo=s.itemNo && LocationCode=s.locationCode,Minimum))));
ClearCollect(colWLocationCodes,ForAll(colOfflineStock As s,{Code:s.locationCode}));
Collect(colWLocationCodes,ForAll(colWLocationMaster As s,{Code:s.Code}));
ClearCollect(colWLocations,AddColumns(DropColumns(GroupBy(Filter(colWLocationCodes,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(Code) & "|") in pgAccess.LocationCode),!IsBlank(Code)),Code,WCodeRows),WCodeRows) As l,LocationName,Coalesce(LookUp(colWLocationMaster,Code=l.Code,Name),l.Code),Amount,Sum(Filter(colWStock,locationCode=l.Code),Qty*UnitCost),SKU,CountRows(Filter(colWStock,locationCode=l.Code)),Shortage,CountRows(Filter(colWStock,locationCode=l.Code && !IsBlank(MinQty) && Qty<MinQty))));
If(IsBlank(LookUp(colWLocations,Code=varWLocation)),Set(varWLocation,First(colWLocations).Code))
```

### `Screen1/wRebuild` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wRebuild` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wRebuild` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wRebuild` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wRebuild` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wRebuild` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wRebuild` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wRebuild` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wRebuild` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wRebuild` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wRebuild` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `Screen1/wRebuild` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wRebuild` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wRebuild` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wReadBC` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wReadBC` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wReadBC` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wReadBC` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wReadBC` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wReadBC` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wReadBC` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wReadBC` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wReadBC` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wReadBC` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wReadBC` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!Connection.Connected,Notify("Интернет холболт алга. Локал үлдэгдэл харагдаж байна.",NotificationType.Warning),
Set(varWBusy,true);Set(varWLive,false);Set(varWChecked,Blank());Clear(colWLedger);Clear(colWLiveBins);
IfError(ClearCollect(colWLedger,Filter('itemLedgerEntries (microsoft/analytics/v1.0)','Item No.'=varWItem && 'Location Code'=varWLocation));
If(CountRows(colWLedger)>=2000,Notify("2000 мөрийн хязгаарт хүрлээ. Дутуу нийлбэрийн оронд локал үлдэгдэл харуулна.",NotificationType.Warning),Set(varWLive,true);Set(varWChecked,Now())),Notify("BC үлдэгдэл уншиж чадсангүй: " & FirstError.Message,NotificationType.Error));
IfError(ClearCollect(colWLiveBins,Filter('warehouseEntries (microsoft/analytics/v1.0)','Item No.'=varWItem && 'Location Code'=varWLocation)),Clear(colWLiveBins); false, true);
If(CountRows(colWLiveBins)>=2000,Clear(colWLiveBins);Notify("Тавиурын мөрийн хязгаарт хүрлээ.",NotificationType.Warning));
Set(varWBusy,false))
```

### `Screen1/wReadBC` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wReadBC` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wReadBC` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wReadBC` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wReadBC` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wReadBC` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wReadBC` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wReadBC` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wReadBC` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wReadBC` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wReadBC` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `Screen1/wReadBC` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wReadBC` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wReadBC` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wOverview` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wOverview` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),varWView<>"transfer" && varWView<>"drafts",varWView="overview"))
```

### `Screen1/wOverview` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width-1128*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2+0*381*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))),(Screen1.Width-366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2)
```

### `Screen1/wOverview` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Screen1.Height-790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))/2
```

### `Screen1/wOverview/overviewClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/overviewClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/overviewClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/overviewClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/overviewClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/overviewClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/overviewClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/overviewClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `Screen1/wOverview/overviewClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/overviewStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/overviewStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/overviewStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#85DFAC")
```

### `Screen1/wOverview/overviewStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/overviewStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/overviewStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/overviewStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/overviewStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `Screen1/wOverview/overviewStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/overviewBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wOverview/overviewBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/overviewBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wOverview/overviewBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wOverview/overviewBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/overviewBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/overviewBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/overviewBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wOverview/overviewBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/overviewBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/overviewBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр',ScreenTransition.Fade)
```

### `Screen1/wOverview/overviewBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/overviewBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/overviewBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wOverview/overviewBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/overviewBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wOverview/overviewBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `Screen1/wOverview/overviewBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/overviewTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/overviewTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/overviewTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/overviewTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/overviewTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/overviewTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/overviewTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/overviewTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/overviewTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/overviewTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Агуулах"
```

### `Screen1/wOverview/overviewTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/overviewTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wOverline` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wOverline` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wOverline` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wOverview/wOverline` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wOverline` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wOverline` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wOverline` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/wOverline` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wOverline` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wOverline` . **Text**  _(Label@2.5.1)_
```powerfx
"02 · WAREHOUSE"
```

### `Screen1/wOverview/wOverline` . **Width**  _(Label@2.5.1)_
```powerfx
(220)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wOverline` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wOverline` . **Y**  _(Label@2.5.1)_
```powerfx
(96)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStat0` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wStat0` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wOverview/wStat0` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(65)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStat0` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat0` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat0` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat0` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat0` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(106)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStat0` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStat0` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(128)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatValue0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wStatValue0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatValue0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wStatValue0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wStatValue0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatValue0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wStatValue0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/wStatValue0` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatValue0` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(28,Self.Height*0.45,Self.Width/Max(8,Len(Self.Text))*1.3))
```

### `Screen1/wOverview/wStatValue0` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:Sum(colWLocations,Amount)},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.##")))
```

### `Screen1/wOverview/wStatValue0` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `Screen1/wOverview/wStatValue0` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatValue0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `Screen1/wOverview/wStatValue0` . **X**  _(Label@2.5.1)_
```powerfx
(28)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatValue0` . **Y**  _(Label@2.5.1)_
```powerfx
(141)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wStatLabel0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatLabel0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wOverview/wStatLabel0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wStatLabel0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatLabel0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wStatLabel0` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel0` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel0` . **Text**  _(Label@2.5.1)_
```powerfx
"Үнэлгээ · локал"
```

### `Screen1/wOverview/wStatLabel0` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatLabel0` . **X**  _(Label@2.5.1)_
```powerfx
(28)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatLabel0` . **Y**  _(Label@2.5.1)_
```powerfx
(173)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStat1` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wStat1` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wOverview/wStat1` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(65)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStat1` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat1` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat1` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat1` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat1` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(106)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStat1` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(129)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStat1` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(128)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatValue1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wStatValue1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatValue1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wStatValue1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wStatValue1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatValue1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wStatValue1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/wStatValue1` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatValue1` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(28,Self.Height*0.45,Self.Width/Max(8,Len(Self.Text))*1.3))
```

### `Screen1/wOverview/wStatValue1` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:CountRows(Distinct(colWStock,itemNo))},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.##")))
```

### `Screen1/wOverview/wStatValue1` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `Screen1/wOverview/wStatValue1` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatValue1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `Screen1/wOverview/wStatValue1` . **X**  _(Label@2.5.1)_
```powerfx
(140)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatValue1` . **Y**  _(Label@2.5.1)_
```powerfx
(141)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wStatLabel1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatLabel1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wOverview/wStatLabel1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wStatLabel1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatLabel1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wStatLabel1` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel1` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel1` . **Text**  _(Label@2.5.1)_
```powerfx
"SKU"
```

### `Screen1/wOverview/wStatLabel1` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatLabel1` . **X**  _(Label@2.5.1)_
```powerfx
(140)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatLabel1` . **Y**  _(Label@2.5.1)_
```powerfx
(173)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStat2` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wStat2` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#251914")
```

### `Screen1/wOverview/wStat2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(65)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStat2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStat2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(106)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStat2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(241)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStat2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(128)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatValue2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wStatValue2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatValue2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wOverview/wStatValue2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wStatValue2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatValue2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wStatValue2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/wStatValue2` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatValue2` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(28,Self.Height*0.45,Self.Width/Max(8,Len(Self.Text))*1.3))
```

### `Screen1/wOverview/wStatValue2` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:CountRows(Filter(colWStock,!IsBlank(MinQty) && Qty<MinQty))},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.##")))
```

### `Screen1/wOverview/wStatValue2` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `Screen1/wOverview/wStatValue2` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatValue2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `Screen1/wOverview/wStatValue2` . **X**  _(Label@2.5.1)_
```powerfx
(252)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatValue2` . **Y**  _(Label@2.5.1)_
```powerfx
(141)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wStatLabel2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatLabel2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wOverview/wStatLabel2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wStatLabel2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wStatLabel2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wStatLabel2` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel2` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wStatLabel2` . **Text**  _(Label@2.5.1)_
```powerfx
"Дутагдалтай"
```

### `Screen1/wOverview/wStatLabel2` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatLabel2` . **X**  _(Label@2.5.1)_
```powerfx
(252)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wStatLabel2` . **Y**  _(Label@2.5.1)_
```powerfx
(173)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationsTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wLocationsTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationsTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wLocationsTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationsTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationsTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wLocationsTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/wLocationsTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationsTitle` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationsTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Бүх агуулах"
```

### `Screen1/wOverview/wLocationsTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(210)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationsTitle` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationsTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(210)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wSync` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wOverview/wSync` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wSync` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wOverview/wSync` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wOverview/wSync` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wSync` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wSync` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(28)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wSync` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wOverview/wSync` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wSync` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wSync` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Notify(If(varStartupSyncRunning,"Мэдээлэл автоматаар шинэчлэгдэж байна…",!Connection.Connected,"Оффлайн — хадгалсан мэдээлэл ашиглаж байна.",varAutoItemsError || varAutoStockError || varAutoBinsError,"Зарим мэдээлэл татагдсангүй. Хадгалсан мэдээлэл хэвээр; нүүр рүү ороход дахин оролдоно.","Автомат шинэчлэлт: " & Text(varAutoDataChecked,"mm.dd hh:mm")) & " | Бараа " & Text(CountRows(colOfflineItems)) & ", үлдэгдэл " & Text(CountRows(colOfflineStock)) & ", тавиур " & Text(CountRows(colOfflineBins)),NotificationType.Information)
```

### `Screen1/wOverview/wSync` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wSync` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wSync` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wOverview/wSync` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wSync` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wOverview/wSync` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wSync` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wSync` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wSync` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wSync` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wSync` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэдээллийн төлөв"
```

### `Screen1/wOverview/wSync` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(76)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wSync` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(270)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wSync` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(210)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wLocationGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(404)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
SortByColumns(Filter(colWLocations,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(Code) & "|") in pgAccess.LocationCode)),"Code",SortOrder.Ascending)
```

### `Screen1/wOverview/wLocationGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
86*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(247)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(ThisItem.Code=varWLocation,ColorValue("#ED5F1C"),ColorValue("#FFFFFF"))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(80)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Code
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Width**  _(Label@2.5.1)_
```powerfx
(210)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **X**  _(Label@2.5.1)_
```powerfx
(15)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationCode` . **Y**  _(Label@2.5.1)_
```powerfx
(12)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Color**  _(Label@2.5.1)_
```powerfx
If(ThisItem.Code=varWLocation,ColorValue("#202225"),ColorValue("#66615B"))
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Height**  _(Label@2.5.1)_
```powerfx
Max(34,Self.Size*2.5)
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(15,Self.Width/Max(15,Len(Self.Text))*2))
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationName
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Width**  _(Label@2.5.1)_
```powerfx
(230)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **X**  _(Label@2.5.1)_
```powerfx
(15)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationName` . **Y**  _(Label@2.5.1)_
```powerfx
(37)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(28,Self.Height*0.45,Self.Width/Max(8,Len(Self.Text))*1.3))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:ThisItem.Amount},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.##")))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **X**  _(Label@2.5.1)_
```powerfx
(228)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationAmount` . **Y**  _(Label@2.5.1)_
```powerfx
(12)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Color**  _(Label@2.5.1)_
```powerfx
If(ThisItem.Code=varWLocation,ColorValue("#202225"),ColorValue("#ED5F1C"))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Shortage & " дутуу"
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **X**  _(Label@2.5.1)_
```powerfx
(229)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationShort` . **Y**  _(Label@2.5.1)_
```powerfx
(39)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(80)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,89,38,0.1)
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWLocation,ThisItem.Code);Set(varWItem,Blank());Set(varWLive,false);Set(varWChecked,Blank());Set(varWPhoto,Blank());Clear(colWLedger);Clear(colWLiveBins);Set(varWView,"stock");Reset(wStockSearch)
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,89,38,0.2)
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationGallery/wLocationHit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationsEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wOverview/wLocationsEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationsEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wOverview/wLocationsEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wOverview/wLocationsEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wLocationsEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wLocationsEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(64)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationsEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wLocationsEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Локал үлдэгдэл алга. Синк хийнэ үү."
```

### `Screen1/wOverview/wLocationsEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(colWStock)
```

### `Screen1/wOverview/wLocationsEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(320)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationsEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(23)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wLocationsEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(330)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wAllLocations` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wOverview/wAllLocations` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wAllLocations` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wOverview/wAllLocations` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wOverview/wAllLocations` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wAllLocations` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wAllLocations` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(28)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wAllLocations` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wOverview/wAllLocations` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wAllLocations` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wAllLocations` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWLocation,Blank());Set(varWItem,Blank());Set(varWLive,false);Set(varWChecked,Blank());Clear(colWLedger);Clear(colWLiveBins);Set(varWView,"stock");Reset(wStockSearch)
```

### `Screen1/wOverview/wAllLocations` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wAllLocations` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wAllLocations` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wOverview/wAllLocations` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wAllLocations` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wOverview/wAllLocations` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wAllLocations` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wAllLocations` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wAllLocations` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wAllLocations` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wAllLocations` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бүх үлдэгдэл"
```

### `Screen1/wOverview/wAllLocations` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(91)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wAllLocations` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(173)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wAllLocations` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(210)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wDraftListOpen` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wOverview/wDraftListOpen` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wDraftListOpen` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wOverview/wDraftListOpen` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wOverview/wDraftListOpen` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wDraftListOpen` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wDraftListOpen` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(42)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wDraftListOpen` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wOverview/wDraftListOpen` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wDraftListOpen` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wDraftListOpen` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWView,"drafts")
```

### `Screen1/wOverview/wDraftListOpen` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wDraftListOpen` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wDraftListOpen` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wOverview/wDraftListOpen` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wDraftListOpen` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wOverview/wDraftListOpen` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wDraftListOpen` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wDraftListOpen` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wDraftListOpen` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wDraftListOpen` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wDraftListOpen` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Ноорог (" & CountRows(Filter(colWDrafts,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(FromLocation) & "|") in pgAccess.LocationCode),OwnerEmail=User().Email)) & ")"
```

### `Screen1/wOverview/wDraftListOpen` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wDraftListOpen` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wDraftListOpen` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(662)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wViewStock` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wOverview/wViewStock` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wOverview/wViewStock` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wOverview/wViewStock` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wViewStock` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wOverview/wViewStock` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wOverview/wViewStock` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wOverview/wViewStock` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wOverview/wViewStock` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wViewStock` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wOverview/wViewStock` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWView,"stock")
```

### `Screen1/wOverview/wViewStock` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wViewStock` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wOverview/wViewStock` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wOverview/wViewStock` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wOverview/wViewStock` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wOverview/wViewStock` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wViewStock` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wViewStock` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wViewStock` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wViewStock` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wOverview/wViewStock` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Coalesce(varWLocation,"Бүх агуулах") & " үлдэгдэл харах →"
```

### `Screen1/wOverview/wViewStock` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wViewStock` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wOverview/wViewStock` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(720)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wStock` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wStock` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),varWView<>"transfer" && varWView<>"drafts",varWView="stock"))
```

### `Screen1/wStock` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wStock` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width-1128*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2+1*381*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))),(Screen1.Width-366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2)
```

### `Screen1/wStock` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Screen1.Height-790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))/2
```

### `Screen1/wStock/stockClock` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true)
```

### `Screen1/wStock/stockClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/stockClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/stockClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/stockClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/stockClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/stockClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/stockClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock/stockClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/stockClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `Screen1/wStock/stockClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wStock/stockClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wStock/stockClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock/stockStatus` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true)
```

### `Screen1/wStock/stockStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/stockStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/stockStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#85DFAC")
```

### `Screen1/wStock/stockStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/stockStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/stockStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/stockStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock/stockStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/stockStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `Screen1/wStock/stockStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wStock/stockStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wStock/stockStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock/stockBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E5E2DD"),ColorValue("#DFE4E1"))
```

### `Screen1/wStock/stockBack` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,1,0)
```

### `Screen1/wStock/stockBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#1E2124"),ColorValue("#202225"))
```

### `Screen1/wStock/stockBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wStock/stockBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#FFFFFF"))
```

### `Screen1/wStock/stockBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/stockBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/stockBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,35*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(39)*(Screen1.Height/790),(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/stockBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wStock/stockBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/stockBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wStock/stockBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWView,"overview")
```

### `Screen1/wStock/stockBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/stockBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/stockBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wStock/stockBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/stockBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wStock/stockBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,18*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/stockBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,18*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/stockBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,18*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/stockBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,18*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/stockBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),22*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/stockBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Coalesce(varWLocation,"Бүгд") & "  ⌄","‹")
```

### `Screen1/wStock/stockBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,85*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(118)*(Screen1.Width/366),(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/stockBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,264*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(231)*(Screen1.Width/366),(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/stockBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(16)*(Screen1.Height/790),(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/stockTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/stockTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/stockTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#1E2124"),ColorValue("#202225"))
```

### `Screen1/wStock/stockTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/stockTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/stockTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/stockTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Semibold)
```

### `Screen1/wStock/stockTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,44*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(45)*(Screen1.Height/790),(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/stockTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,23*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,22*Min(Screen1.Width/366,Screen1.Height/790),20*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/stockTitle` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Агуулах","Үлдэгдэл")
```

### `Screen1/wStock/stockTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,210*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(170)*(Screen1.Width/366),(275)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/stockTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(17)*(Screen1.Width/366),(66)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/stockTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(13)*(Screen1.Height/790),(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockScope` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,true,If(App.Width<First(App.SizeBreakpoints).Value,false,true))
```

### `Screen1/wStock/wStockScope` . **BorderColor**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E5E2DD"),RGBA(131, 24, 75, 1))
```

### `Screen1/wStock/wStockScope` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,1,(0)*(Min(App.Width/640,App.Height/1136)))
```

### `Screen1/wStock/wStockScope` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wStock/wStockScope` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,RGBA(0,0,0,0))
```

### `Screen1/wStock/wStockScope` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockScope` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockScope` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,90*Screen1.Height/790,(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockScope` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wStockScope` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"",Coalesce(varWLocation,"Бүх агуулах") & " · локал snapshot")
```

### `Screen1/wStock/wStockScope` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,366*Screen1.Width/366,(280)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockScope` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Screen1.Width/366,(65)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockScope` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,700*Screen1.Height/790,(88)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockSearch` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E5E2DD"),ColorValue("#E4E1DC"))
```

### `Screen1/wStock/wStockSearch` . **BorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,1,1)
```

### `Screen1/wStock/wStockSearch` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wStockSearch` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
Coalesce(varWScanned,"")
```

### `Screen1/wStock/wStockSearch` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wStock/wStockSearch` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockSearch` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockSearch` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,44*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(46)*(Screen1.Height/790),(47)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockSearch` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Код, нэр, 中文, тавиур…","Код, нэр, 中文, тавиур...")
```

### `Screen1/wStock/wStockSearch` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockSearch` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wStock/wStockSearch` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wStockSearch` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,39*Screen1.Width/366,12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockSearch` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wStock/wStockSearch` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wStockSearch` . **RadiusBottomLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),12)
```

### `Screen1/wStock/wStockSearch` . **RadiusBottomRight**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),12)
```

### `Screen1/wStock/wStockSearch` . **RadiusTopLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),12)
```

### `Screen1/wStock/wStockSearch` . **RadiusTopRight**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),12)
```

### `Screen1/wStock/wStockSearch` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wStockSearch` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,332*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(278)*(Screen1.Width/366),(277)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockSearch` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(17)*(Screen1.Width/366),(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockSearch` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,146*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(158)*(Screen1.Height/790),(120)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockScanner` . **BorderFillColor**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#ED5F1C"))
```

### `Screen1/wStock/wStockScanner` . **FillColor**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#ED5F1C"))
```

### `Screen1/wStock/wStockScanner` . **FontSize**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,19*Min(Screen1.Width/366,Screen1.Height/790),10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockScanner` . **Height**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(46)*(Screen1.Height/790),(47)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockScanner` . **OnScan**  _(BarcodeReader@1.0.25)_
```powerfx
Set(varWScanned,First(Self.Barcodes).Value);Reset(wStockSearch)
```

### `Screen1/wStock/wStockScanner` . **Text**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"⌕","Scan")
```

### `Screen1/wStock/wStockScanner` . **TextColor**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#68615C"),ColorValue("#202225"))
```

### `Screen1/wStock/wStockScanner` . **Width**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,32*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(48)*(Screen1.Width/366),(49)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockScanner` . **X**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,21*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(301)*(Screen1.Width/366),(300)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockScanner` . **Y**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,149*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(158)*(Screen1.Height/790),(120)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E5E2DD"),ColorValue("#DFE4E1"))
```

### `Screen1/wStock/wFilter0` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,1,0)
```

### `Screen1/wStock/wFilter0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varWFilter="Бүгд",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `Screen1/wStock/wFilter0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wStock/wFilter0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varWFilter="Бүгд",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `Screen1/wStock/wFilter0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wFilter0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wFilter0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,34*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(34)*(Screen1.Height/790),(30)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wStock/wFilter0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wFilter0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wStock/wFilter0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWFilter,"Бүгд")
```

### `Screen1/wStock/wFilter0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wFilter0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wFilter0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wStock/wFilter0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wFilter0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wStock/wFilter0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бүгд"
```

### `Screen1/wStock/wFilter0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,53*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(52)*(Screen1.Width/366),(57)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wFilter0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(17)*(Screen1.Width/366),(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wFilter0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,202*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(217)*(Screen1.Height/790),(180)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E5E2DD"),ColorValue("#DFE4E1"))
```

### `Screen1/wStock/wFilter1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,1,0)
```

### `Screen1/wStock/wFilter1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varWFilter="Дутагдалтай",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `Screen1/wStock/wFilter1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wStock/wFilter1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varWFilter="Дутагдалтай",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `Screen1/wStock/wFilter1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wFilter1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wFilter1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,34*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(34)*(Screen1.Height/790),(30)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wStock/wFilter1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wFilter1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wStock/wFilter1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWFilter,"Дутагдалтай")
```

### `Screen1/wStock/wFilter1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wFilter1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wFilter1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wStock/wFilter1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wFilter1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wStock/wFilter1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Дутагдалтай · " & CountIf(Filter(colWStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),IsBlank(varWLocation) || locationCode=varWLocation),!IsBlank(MinQty) && Qty<MinQty),"Дутагдалтай")
```

### `Screen1/wStock/wFilter1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,127*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(139)*(Screen1.Width/366),(100)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wFilter1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,149*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(163)*(Screen1.Width/366),(80)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wFilter1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,202*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(217)*(Screen1.Height/790),(180)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E5E2DD"),ColorValue("#DFE4E1"))
```

### `Screen1/wStock/wFilter2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,1,0)
```

### `Screen1/wStock/wFilter2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varWFilter="Хэвийн",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `Screen1/wStock/wFilter2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wStock/wFilter2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varWFilter="Хэвийн",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `Screen1/wStock/wFilter2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wFilter2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wFilter2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,34*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(34)*(Screen1.Height/790),(30)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wStock/wFilter2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wFilter2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wStock/wFilter2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWFilter,"Хэвийн")
```

### `Screen1/wStock/wFilter2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wFilter2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wFilter2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wStock/wFilter2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wFilter2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wStock/wFilter2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wFilter2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Screen1.Width/366,Screen1.Height/790),10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wFilter2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хэвийн"
```

### `Screen1/wStock/wFilter2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,63*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(78)*(Screen1.Width/366),(76)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wFilter2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,78*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(77)*(Screen1.Width/366),(186)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wFilter2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,202*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(217)*(Screen1.Height/790),(180)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,452*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(446)*(Screen1.Height/790),(473)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
Filter(colWStock As s,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(s.locationCode) & "|") in pgAccess.LocationCode),(IsBlank(varWLocation) || s.locationCode=varWLocation) && (IsBlank(Trim(wStockSearch.Text)) || Lower(Trim(wStockSearch.Text)) in Lower(s.itemNo & " " & s.ItemName) || !IsBlank(LookUp(colOfflineBins,itemNo=s.itemNo && locationCode=s.locationCode && Lower(Trim(wStockSearch.Text)) in Lower(binCode),binCode))) && (varWFilter="Бүгд" || (varWFilter="Дутагдалтай" && !IsBlank(s.MinQty) && s.Qty<s.MinQty) || (varWFilter="Хэвийн" && !IsBlank(s.MinQty) && s.Qty>=s.MinQty)))
```

### `Screen1/wStock/wStockGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,5*Screen1.Height/790,6*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,89*Screen1.Height/790,88*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,344*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(344)*(Screen1.Width/366),(344)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(11)*(Screen1.Width/366),(11)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,244*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(260)*(Screen1.Height/790),(221)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,1,0)
```

### `Screen1/wStock/wStockGallery/wStockCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E5E2DD"),ColorValue("#E4E1DC"))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wStock/wStockGallery/wStockCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,84*Screen1.Height/790,(82)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,332*Screen1.Width/366,(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Screen1.Width/366,(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockGallery/wStockCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Screen1.Height/790,(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#EEECE8"),ColorValue("#E4E1DC"))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,5*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(5)*(Screen1.Height/790),(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,2*Min(Screen1.Width/366,Screen1.Height/790),10*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,2*Min(Screen1.Width/366,Screen1.Height/790),10*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,2*Min(Screen1.Width/366,Screen1.Height/790),10*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,2*Min(Screen1.Width/366,Screen1.Height/790),10*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,303*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(306)*(Screen1.Width/366),(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(13)*(Screen1.Width/366),(12)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockThumb` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,66*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(65)*(Screen1.Height/790),(14)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockGallery/wStockName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockName` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#1E2124"),ColorValue("#202225"))
```

### `Screen1/wStock/wStockGallery/wStockName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery/wStockName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockGallery/wStockName` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wStock/wStockGallery/wStockName` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,29*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(28)*(Screen1.Height/790),(27)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockName` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),11*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockName` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemName
```

### `Screen1/wStock/wStockGallery/wStockName` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,222*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(220)*(Screen1.Width/366),(183)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockName` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(13)*(Screen1.Width/366),(61)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockName` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(8)*(Screen1.Height/790),(10)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockGallery/wStockCode` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#68615C"),If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#656463"),ColorValue("#66615B")))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery/wStockCode` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(21)*(Screen1.Height/790),(18)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Screen1.Width/366,Screen1.Height/790),9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,With({r:ThisItem},With({b:LookUp(colOfflineBins,itemNo=r.itemNo && locationCode=r.locationCode,binCode)},r.itemNo & " · " & r.locationCode & If(IsBlank(b),""," · " & b))),If(App.Width<First(App.SizeBreakpoints).Value,ThisItem.itemNo & " · " & ThisItem.locationCode,ThisItem.itemNo))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,221*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(229)*(Screen1.Width/366),(177)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(13)*(Screen1.Width/366),(61)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockCode` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(38)*(Screen1.Height/790),(37)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true)
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.locationCode & " · " & Coalesce(LookUp(colOfflineBins,itemNo=ThisItem.itemNo && locationCode=ThisItem.locationCode,binCode),"—")
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Width**  _(Label@2.5.1)_
```powerfx
(230)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **X**  _(Label@2.5.1)_
```powerfx
(61)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wStock/wStockGallery/wStockLocation` . **Y**  _(Label@2.5.1)_
```powerfx
(61)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Align**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Right,Align.Left)
```

### `Screen1/wStock/wStockGallery/wStockQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockGallery/wStockQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#1E2124"),ColorValue("#202225"))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery/wStockQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockGallery/wStockQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,29*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(28)*(Screen1.Height/790),(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),Max(10,Min(20,Self.Width/Max(8,Len(Self.Text))*1.2))))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Qty,If(Mod(ThisItem.Qty,1)=0,"#,##0","#,##0.###")) & " " & ThisItem.Uom
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,80*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(88)*(Screen1.Width/366),(74)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `Screen1/wStock/wStockGallery/wStockQty` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,237*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(232)*(Screen1.Width/366),(245)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockQty` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(8)*(Screen1.Height/790),(14)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Semibold,FontWeight.Normal)
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Align**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Right,Align.Left)
```

### `Screen1/wStock/wStockGallery/wStockMin` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockGallery/wStockMin` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(ThisItem.Qty<ThisItem.MinQty,ColorValue("#B65409"),ColorValue("#098547")),If(IsBlank(ThisItem.MinQty),ColorValue("#66615B"),ThisItem.Qty<ThisItem.MinQty,ColorValue("#ED5F1C"),ColorValue("#85DFAC")))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery/wStockMin` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(21)*(Screen1.Height/790),(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Screen1.Width/366,Screen1.Height/790),8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(IsBlank(ThisItem.MinQty),"","мин " & Text(ThisItem.MinQty)),If(IsBlank(ThisItem.MinQty),"мин —",ThisItem.Qty<ThisItem.MinQty,"мин " & Text(ThisItem.MinQty),"хэвийн"))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,78*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(74)*(Screen1.Width/366),(77)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,239*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(245)*(Screen1.Width/366),(243)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wStockGallery/wStockMin` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(38)*(Screen1.Height/790),(42)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wStock/wStockGallery/wStockHit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wStockGallery/wStockHit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wStock/wStockGallery/wStockHit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockGallery/wStockHit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockGallery/wStockHit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,84*Screen1.Height/790,(82)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wStock/wStockGallery/wStockHit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wStockGallery/wStockHit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,89,38,0.08)
```

### `Screen1/wStock/wStockGallery/wStockHit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWItem,ThisItem.itemNo);Set(varWLocation,ThisItem.locationCode);Set(varWChecked,Blank());Set(varWLive,false);Set(varWPhoto,Blank());Clear(colWLiveBins);Clear(colWLedger);Set(varWView,"detail");Reset(wMinimumInput)
```

### `Screen1/wStock/wStockGallery/wStockHit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wStock/wStockGallery/wStockHit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wStockGallery/wStockHit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,89,38,0.15)
```

### `Screen1/wStock/wStockGallery/wStockHit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,332*Screen1.Width/366,(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Screen1.Width/366,(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockGallery/wStockHit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Screen1.Height/790,(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **X**  _(Label@2.5.1)_
```powerfx
14*Screen1.Width/366
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **Y**  _(Label@2.5.1)_
```powerfx
66*Screen1.Height/790
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **Width**  _(Label@2.5.1)_
```powerfx
303*Screen1.Width/366*If(ThisItem.MinQty>0,Max(0,Min(1,ThisItem.Qty/ThisItem.MinQty)),0)
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **Height**  _(Label@2.5.1)_
```powerfx
(5)*(Screen1.Height/790)
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **Fill**  _(Label@2.5.1)_
```powerfx
If(ThisItem.Qty<ThisItem.MinQty,ColorValue("#F59D00"),ColorValue("#10A05A"))
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && !IsBlank(ThisItem.MinQty) && ThisItem.MinQty>0
```

### `Screen1/wStock/wStockGallery/mobileStockLevel` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(wStockHit)
```

### `Screen1/wStock/wStockEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wStock/wStockEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wStock/wStockEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wStock/wStockEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wStockEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wStockEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(60)*(Screen1.Height/790),(52)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wStockEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wStockEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Шүүлтүүрт тохирох бараа алга."
```

### `Screen1/wStock/wStockEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(wStockGallery.AllItems)
```

### `Screen1/wStock/wStockEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(326)*(Screen1.Width/366),(313)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockEmpty` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(20)*(Screen1.Width/366),(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))
```

### `Screen1/wStock/wStockEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(282)*(Screen1.Height/790),(350)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))
```

### `Screen1/wStock/wExcel` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Excel, мэйл","")
```

### `Screen1/wStock/wExcel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wStock/wExcel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#1E2124"),ColorValue("#202225"))
```

### `Screen1/wStock/wExcel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wStock/wExcel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#FFFFFF")))
```

### `Screen1/wStock/wExcel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wExcel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wExcel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,34*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(37)*(Screen1.Height/790),(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wExcel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wStock/wExcel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wExcel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wStock/wExcel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWExport,true)
```

### `Screen1/wStock/wExcel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wExcel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wExcel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wStock/wExcel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wExcel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wStock/wExcel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wExcel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wExcel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wExcel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wStock/wExcel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Screen1.Width/366,Screen1.Height/790),10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wExcel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"⋯",If(App.Width<First(App.SizeBreakpoints).Value,"···","Excel · мэйл"))
```

### `Screen1/wStock/wExcel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,39*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(40)*(Screen1.Width/366),(109)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wExcel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,310*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(309)*(Screen1.Width/366),(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wExcel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,202*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(215)*(Screen1.Height/790),(720)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wShortRequest` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wStock/wShortRequest` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#202225")))
```

### `Screen1/wStock/wShortRequest` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wStock/wShortRequest` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#EF601B"),ColorValue("#ED5F1C"))
```

### `Screen1/wStock/wShortRequest` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wStock/wShortRequest` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wStock/wShortRequest` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,55*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(54)*(Screen1.Height/790),(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/wShortRequest` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wStock/wShortRequest` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wShortRequest` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wStock/wShortRequest` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
ClearCollect(colPAuditDraftKeys,colWDrafts.DraftId);If(IsEmpty(Filter(colWStock,locationCode=varWLocation && !IsBlank(MinQty) && Qty<MinQty)),Notify("Минимумтай, дутагдалтай бараа алга.",NotificationType.Information),Set(varWBatchId,Text(GUID()));ForAll(Filter(colWStock,locationCode=varWLocation && !IsBlank(MinQty) && Qty<MinQty) As r,Collect(colWDrafts,{DraftId:varWBatchId & "-" & r.itemNo,OwnerEmail:User().Email,Kind:"Request",ItemNo:r.itemNo,ItemName:r.ItemName,FromLocation:r.locationCode,ToLocation:"",FromBin:"",ToBin:"",Quantity:r.MinQty-r.Qty,Uom:r.Uom,Reason:"Минимумын дутагдал",Recipient:"",Created:Now(),Status:"Draft"}));If(wDraftStore="ready",IfError(SaveData(colWDrafts,"WarehouseDraftsV6");true,Set(wDraftStoreError,FirstError.Message);Notify("Ноорог энэ удаагийн сессэд байна. Төхөөрөмжид хадгалахад алдаа гарлаа. " & wDraftStoreError,NotificationType.Warning);false,Set(wDraftStoreError,"");true),wDraftStore="preview",Notify("Ноорог Studio-ийн энэ сессэд хадгалагдлаа.",NotificationType.Information),wDraftStore="session",Notify("Ноорог энэ сессэд хадгалагдлаа. Энэ төхөөрөмжийн тоглуулагч локал хадгалалтыг дэмжихгүй байна.",NotificationType.Warning),Notify("Ноорог энэ сессэд байна. Өмнөх кэшийг уншихад гарсан алдаа: " & wDraftStoreError,NotificationType.Warning));Set(varWView,"drafts"));ForAll(Filter(colWDrafts,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(FromLocation) & "|") in pgAccess.LocationCode),!(DraftId in colPAuditDraftKeys.DraftId) && OwnerEmail=User().Email) As a,Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:a.Created,Module:"Агуулах",Action:"Шаардах ноорог үүсгэсэн",Entity:a.ItemNo & " / " & a.FromLocation,BeforeValue:"",AfterValue:Text(a.Quantity) & " " & a.Uom,Result:"Локал ноорог"}));If(!IsBlank(Host.Version),IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true))
```

### `Screen1/wStock/wShortRequest` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wShortRequest` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wStock/wShortRequest` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wStock/wShortRequest` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wStock/wShortRequest` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wStock/wShortRequest` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wShortRequest` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wShortRequest` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wShortRequest` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790))))
```

### `Screen1/wStock/wShortRequest` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Screen1.Width/366,Screen1.Height/790),If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Screen1.Width/366,Screen1.Height/790),10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))))
```

### `Screen1/wStock/wShortRequest` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Дутагдлаар шаардах ноорог · " & CountIf(Filter(colWStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),IsBlank(varWLocation) || locationCode=varWLocation),!IsBlank(MinQty) && Qty<MinQty),"Дутагдлаар ноорог үүсгэх")
```

### `Screen1/wStock/wShortRequest` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,332*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(332)*(Screen1.Width/366),(215)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wShortRequest` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Screen1.Width/366,If(App.Width<First(App.SizeBreakpoints).Value,(17)*(Screen1.Width/366),(134)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))))
```

### `Screen1/wStock/wShortRequest` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,716*Screen1.Height/790,If(App.Width<First(App.SizeBreakpoints).Value,(719)*(Screen1.Height/790),(720)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))))
```

### `Screen1/wStock/mobileStockKpi0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Screen1.Width/366,(17)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Screen1.Height/790,(74)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,106*Screen1.Width/366,(104)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,68*Screen1.Height/790,(71)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `Screen1/wStock/mobileStockKpi0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `Screen1/wStock/mobileStockKpi0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `Screen1/wStock/mobileStockKpi0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `Screen1/wStock/mobileStockKpi0` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
DisplayMode.View
```

### `Screen1/wStock/mobileStockKpi0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E8E5E1")
```

### `Screen1/wStock/mobileStockKpi0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi0Caption` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Screen1.Width/366,(27)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,71*Screen1.Height/790,(81)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,88*Screen1.Width/366,(88)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,21*Screen1.Height/790,(22)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Screen1.Width/366,Screen1.Height/790),10*Min(Screen1.Width/366,Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#68615C"),ColorValue("#1E2124"))
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"SKU","Нэр төрөл")
```

### `Screen1/wStock/mobileStockKpi0Caption` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `Screen1/wStock/mobileStockKpi0Caption` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi0Value` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Screen1.Width/366,(27)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi0Value` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,91*Screen1.Height/790,(103)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0Value` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,94*Screen1.Width/366,(88)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi0Value` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,33*Screen1.Height/790,(33)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0Value` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,19*Min(Screen1.Width/366,Screen1.Height/790),18*Min(Screen1.Width/366,Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi0Value` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#1E2124"))
```

### `Screen1/wStock/mobileStockKpi0Value` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `Screen1/wStock/mobileStockKpi0Value` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(Distinct(Filter(colWStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),IsBlank(varWLocation) || locationCode=varWLocation),itemNo)),"#,##0")
```

### `Screen1/wStock/mobileStockKpi0Value` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `Screen1/wStock/mobileStockKpi0Value` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,130*Screen1.Width/366,(131)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Screen1.Height/790,(74)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,106*Screen1.Width/366,(104)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,68*Screen1.Height/790,(71)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `Screen1/wStock/mobileStockKpi1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF6E6")
```

### `Screen1/wStock/mobileStockKpi1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `Screen1/wStock/mobileStockKpi1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `Screen1/wStock/mobileStockKpi1` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
DisplayMode.View
```

### `Screen1/wStock/mobileStockKpi1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFC15C")
```

### `Screen1/wStock/mobileStockKpi1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi1Caption` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,141*Screen1.Width/366,(141)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,71*Screen1.Height/790,(81)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,88*Screen1.Width/366,(88)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,21*Screen1.Height/790,(22)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Screen1.Width/366,Screen1.Height/790),10*Min(Screen1.Width/366,Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#B65409"),ColorValue("#1E2124"))
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Text**  _(Label@2.5.1)_
```powerfx
"Дутагдалтай"
```

### `Screen1/wStock/mobileStockKpi1Caption` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `Screen1/wStock/mobileStockKpi1Caption` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi1Value` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,141*Screen1.Width/366,(141)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi1Value` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,91*Screen1.Height/790,(103)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1Value` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,94*Screen1.Width/366,(88)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi1Value` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,33*Screen1.Height/790,(33)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1Value` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,19*Min(Screen1.Width/366,Screen1.Height/790),18*Min(Screen1.Width/366,Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi1Value` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#B65409"),ColorValue("#1E2124"))
```

### `Screen1/wStock/mobileStockKpi1Value` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `Screen1/wStock/mobileStockKpi1Value` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountIf(Filter(colWStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),IsBlank(varWLocation) || locationCode=varWLocation),!IsBlank(MinQty) && Qty<MinQty),"#,##0")
```

### `Screen1/wStock/mobileStockKpi1Value` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `Screen1/wStock/mobileStockKpi1Value` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,243*Screen1.Width/366,(245)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Screen1.Height/790,(74)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,106*Screen1.Width/366,(104)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,68*Screen1.Height/790,(71)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `Screen1/wStock/mobileStockKpi2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `Screen1/wStock/mobileStockKpi2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Screen1.Width/366,Screen1.Height/790),10)
```

### `Screen1/wStock/mobileStockKpi2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `Screen1/wStock/mobileStockKpi2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `Screen1/wStock/mobileStockKpi2` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
DisplayMode.View
```

### `Screen1/wStock/mobileStockKpi2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E8E5E1")
```

### `Screen1/wStock/mobileStockKpi2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi2Caption` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,254*Screen1.Width/366,(255)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,71*Screen1.Height/790,(81)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,88*Screen1.Width/366,(88)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,21*Screen1.Height/790,(22)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Screen1.Width/366,Screen1.Height/790),10*Min(Screen1.Width/366,Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#68615C"),ColorValue("#1E2124"))
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Text**  _(Label@2.5.1)_
```powerfx
"Үнэлгээ"
```

### `Screen1/wStock/mobileStockKpi2Caption` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `Screen1/wStock/mobileStockKpi2Caption` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wStock/mobileStockKpi2Value` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,254*Screen1.Width/366,(255)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi2Value` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,91*Screen1.Height/790,(103)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2Value` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,94*Screen1.Width/366,(88)*(Screen1.Width/366))
```

### `Screen1/wStock/mobileStockKpi2Value` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,33*Screen1.Height/790,(33)*(Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2Value` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,19*Min(Screen1.Width/366,Screen1.Height/790),18*Min(Screen1.Width/366,Screen1.Height/790))
```

### `Screen1/wStock/mobileStockKpi2Value` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#1E2124"))
```

### `Screen1/wStock/mobileStockKpi2Value` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `Screen1/wStock/mobileStockKpi2Value` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:Sum(Filter(colWStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),IsBlank(varWLocation) || locationCode=varWLocation),Qty*UnitCost)},If(Abs(v)>=1000000000,"₮" & Text(v/1000000000,"0.0") & "B",Abs(v)>=1000000,"₮" & Text(v/1000000,"0.0") & "M","₮" & Text(v,"#,##0")))
```

### `Screen1/wStock/mobileStockKpi2Value` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `Screen1/wStock/mobileStockKpi2Value` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value
```

### `Screen1/wDetail` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDetail` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wDetail` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),varWView<>"transfer" && varWView<>"drafts",varWView="detail"))
```

### `Screen1/wDetail` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width-1128*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2+2*381*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))),(Screen1.Width-366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2)
```

### `Screen1/wDetail` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Screen1.Height-790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))/2
```

### `Screen1/wDetail/detailClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/detailClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/detailClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/detailClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/detailClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/detailClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/detailClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/detailClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `Screen1/wDetail/detailClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/detailStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/detailStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/detailStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#85DFAC")
```

### `Screen1/wDetail/detailStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/detailStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/detailStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/detailStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/detailStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailStatus` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varWChecked),"ЛОКАЛ", "BC " & Text(varWChecked,"hh:mm"))
```

### `Screen1/wDetail/detailStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/detailBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDetail/detailBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/detailBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDetail/detailBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/detailBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/detailBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/detailBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/detailBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDetail/detailBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/detailBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/detailBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWView,"stock")
```

### `Screen1/wDetail/detailBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/detailBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/detailBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDetail/detailBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/detailBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/detailBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `Screen1/wDetail/detailBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/detailTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/detailTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/detailTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/detailTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/detailTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/detailTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/detailTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/detailTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/detailTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/detailTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Барааны дэлгэрэнгүй"
```

### `Screen1/wDetail/detailTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/detailTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wPhotoBackground` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wPhotoBackground` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wPhotoBackground` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(125)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wPhotoBackground` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wPhotoBackground` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wPhotoBackground` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wPhotoBackground` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wPhotoBackground` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wPhotoBackground` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wPhotoBackground` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(108)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wItemPhoto` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wItemPhoto` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wItemPhoto` . **Height**  _(Image@2.2.3)_
```powerfx
(125)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wItemPhoto` . **Image**  _(Image@2.2.3)_
```powerfx
varWPhoto
```

### `Screen1/wDetail/wItemPhoto` . **Width**  _(Image@2.2.3)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wItemPhoto` . **X**  _(Image@2.2.3)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wItemPhoto` . **Y**  _(Image@2.2.3)_
```powerfx
(108)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wLoadPhoto` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDetail/wLoadPhoto` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wLoadPhoto` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDetail/wLoadPhoto` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wLoadPhoto` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wLoadPhoto` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wLoadPhoto` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wLoadPhoto` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDetail/wLoadPhoto` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wLoadPhoto` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wLoadPhoto` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!Connection.Connected,Notify("Зураг татахад интернет хэрэгтэй.",NotificationType.Warning),IfError(Set(varWPhoto,'PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo...'.Run(varWItem).picture),Notify("Зургийг уншиж чадсангүй.",NotificationType.Warning)))
```

### `Screen1/wDetail/wLoadPhoto` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wLoadPhoto` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wLoadPhoto` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDetail/wLoadPhoto` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wLoadPhoto` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wLoadPhoto` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wLoadPhoto` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wLoadPhoto` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wLoadPhoto` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wLoadPhoto` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wLoadPhoto` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зураг харах"
```

### `Screen1/wDetail/wLoadPhoto` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
IsBlank(varWPhoto) && !IsBlank(varWItem)
```

### `Screen1/wDetail/wLoadPhoto` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(158)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wLoadPhoto` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(104)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wLoadPhoto` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(151)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailCode` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailCode` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailCode` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wDetailCode` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailCode` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailCode` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailCode` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wDetailCode` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailCode` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailCode` . **Text**  _(Label@2.5.1)_
```powerfx
varWItem
```

### `Screen1/wDetail/wDetailCode` . **Width**  _(Label@2.5.1)_
```powerfx
(313)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailCode` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailCode` . **Y**  _(Label@2.5.1)_
```powerfx
(244)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailName` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wDetailName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailName` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wDetailName` . **Height**  _(Label@2.5.1)_
```powerfx
(43)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailName` . **Size**  _(Label@2.5.1)_
```powerfx
19*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailName` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(LookUp(colOfflineItems,number=varWItem,displayName),varWItem)
```

### `Screen1/wDetail/wDetailName` . **Width**  _(Label@2.5.1)_
```powerfx
(326)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailName` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailName` . **Y**  _(Label@2.5.1)_
```powerfx
(267)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpis` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wDetailKpis` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wDetailKpis` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(76)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpis` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpis` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpis` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpis` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpis` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpis` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpis` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(322)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailKpiLabel0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailKpiLabel0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Text**  _(Label@2.5.1)_
```powerfx
"Нийт үлдэгдэл"
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Width**  _(Label@2.5.1)_
```powerfx
(97)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiLabel0` . **X**  _(Label@2.5.1)_
```powerfx
(31)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiLabel0` . **Y**  _(Label@2.5.1)_
```powerfx
(334)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailKpiVal0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiVal0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wDetailKpiVal0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailKpiVal0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiVal0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailKpiVal0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wDetailKpiVal0` . **Height**  _(Label@2.5.1)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal0` . **Size**  _(Label@2.5.1)_
```powerfx
23*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal0` . **Text**  _(Label@2.5.1)_
```powerfx
Text(If(varWLive,Sum(colWLedger,Quantity),LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,Qty)),"#,##0.###")
```

### `Screen1/wDetail/wDetailKpiVal0` . **Width**  _(Label@2.5.1)_
```powerfx
(97)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiVal0` . **X**  _(Label@2.5.1)_
```powerfx
(31)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiVal0` . **Y**  _(Label@2.5.1)_
```powerfx
(356)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailKpiLabel1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailKpiLabel1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Text**  _(Label@2.5.1)_
```powerfx
"Минимум"
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Width**  _(Label@2.5.1)_
```powerfx
(97)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiLabel1` . **X**  _(Label@2.5.1)_
```powerfx
(137)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiLabel1` . **Y**  _(Label@2.5.1)_
```powerfx
(334)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailKpiVal1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiVal1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wDetailKpiVal1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailKpiVal1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiVal1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailKpiVal1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wDetailKpiVal1` . **Height**  _(Label@2.5.1)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal1` . **Size**  _(Label@2.5.1)_
```powerfx
23*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal1` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(Text(LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,MinQty)),"—")
```

### `Screen1/wDetail/wDetailKpiVal1` . **Width**  _(Label@2.5.1)_
```powerfx
(97)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiVal1` . **X**  _(Label@2.5.1)_
```powerfx
(137)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiVal1` . **Y**  _(Label@2.5.1)_
```powerfx
(356)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailKpiLabel2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailKpiLabel2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Text**  _(Label@2.5.1)_
```powerfx
"30 хоног зарлага"
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Width**  _(Label@2.5.1)_
```powerfx
(97)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiLabel2` . **X**  _(Label@2.5.1)_
```powerfx
(243)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiLabel2` . **Y**  _(Label@2.5.1)_
```powerfx
(334)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wDetailKpiVal2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiVal2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wDetailKpiVal2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wDetailKpiVal2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wDetailKpiVal2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wDetailKpiVal2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wDetailKpiVal2` . **Height**  _(Label@2.5.1)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal2` . **Size**  _(Label@2.5.1)_
```powerfx
23*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wDetailKpiVal2` . **Text**  _(Label@2.5.1)_
```powerfx
If(varWLive,Text(-Sum(Filter(colWLedger,Quantity<0 && IfError(DateValue('Posting Date'),Date(1900,1,1))>=DateAdd(Today(),-30,TimeUnit.Days)),Quantity)),"—")
```

### `Screen1/wDetail/wDetailKpiVal2` . **Width**  _(Label@2.5.1)_
```powerfx
(97)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiVal2` . **X**  _(Label@2.5.1)_
```powerfx
(243)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wDetailKpiVal2` . **Y**  _(Label@2.5.1)_
```powerfx
(356)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMinimumInput` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wMinimumInput` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wMinimumInput` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
Text(LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,MinQty))
```

### `Screen1/wDetail/wMinimumInput` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wMinimumInput` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMinimumInput` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wMinimumInput` . **Format**  _(Classic/TextInput@2.3.2)_
```powerfx
TextFormat.Number
```

### `Screen1/wDetail/wMinimumInput` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(35)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMinimumInput` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Минимум"
```

### `Screen1/wDetail/wMinimumInput` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wMinimumInput` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wDetail/wMinimumInput` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wMinimumInput` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMinimumInput` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wDetail/wMinimumInput` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wMinimumInput` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wMinimumInput` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(91)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMinimumInput` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMinimumInput` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(408)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wSaveMinimum` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDetail/wSaveMinimum` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wSaveMinimum` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDetail/wSaveMinimum` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(varWItem),DisplayMode.Disabled,DisplayMode.Edit)
```

### `Screen1/wDetail/wSaveMinimum` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wSaveMinimum` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wSaveMinimum` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wSaveMinimum` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(35)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wSaveMinimum` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDetail/wSaveMinimum` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wSaveMinimum` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wSaveMinimum` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPAuditMinimumBefore,JSON(Filter(colWMinimums,OwnerEmail=User().Email && ItemNo=varWItem && LocationCode=varWLocation),JSONFormat.Compact));With({v:IfError(Value(wMinimumInput.Text),Blank())},If(IsBlank(varWItem) || IsBlank(v) || v<0,Notify("Минимумд 0 буюу түүнээс их тоо оруулна уу.",NotificationType.Warning),RemoveIf(colWMinimums,OwnerEmail=User().Email && ItemNo=varWItem && LocationCode=varWLocation);Collect(colWMinimums,{OwnerEmail:User().Email,ItemNo:varWItem,LocationCode:varWLocation,Minimum:v});If(wMinimumStore="ready",IfError(SaveData(colWMinimums,"WarehouseMinimumsV6");true,Set(wMinimumStoreError,FirstError.Message);Notify("Доод үлдэгдэл энэ удаагийн сессэд байна. Төхөөрөмжид хадгалахад алдаа гарлаа. " & wMinimumStoreError,NotificationType.Warning);false,Set(wMinimumStoreError,"");true),wMinimumStore="preview",Notify("Доод үлдэгдэл Studio-ийн энэ сессэд хадгалагдлаа.",NotificationType.Information),wMinimumStore="session",Notify("Доод үлдэгдэл энэ сессэд хадгалагдлаа. Энэ төхөөрөмжийн тоглуулагч локал хадгалалтыг дэмжихгүй байна.",NotificationType.Warning),Notify("Доод үлдэгдэл энэ сессэд байна. Өмнөх кэшийг уншихад гарсан алдаа: " & wMinimumStoreError,NotificationType.Warning));Select(wRebuild)));If(varPAuditMinimumBefore<>JSON(Filter(colWMinimums,OwnerEmail=User().Email && ItemNo=varWItem && LocationCode=varWLocation),JSONFormat.Compact),Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Агуулах",Action:"Минимум өөрчилсөн",Entity:varWItem & " / " & varWLocation,BeforeValue:varPAuditMinimumBefore,AfterValue:JSON(Filter(colWMinimums,OwnerEmail=User().Email && ItemNo=varWItem && LocationCode=varWLocation),JSONFormat.Compact),Result:"Локал өөрчлөлт"});If(!IsBlank(Host.Version),IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true)))
```

### `Screen1/wDetail/wSaveMinimum` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wSaveMinimum` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wSaveMinimum` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDetail/wSaveMinimum` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wSaveMinimum` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wSaveMinimum` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wSaveMinimum` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wSaveMinimum` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wSaveMinimum` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wSaveMinimum` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wSaveMinimum` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мин хадгалах"
```

### `Screen1/wDetail/wSaveMinimum` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(111)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wSaveMinimum` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(115)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wSaveMinimum` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(408)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wRefreshDetail` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDetail/wRefreshDetail` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wRefreshDetail` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDetail/wRefreshDetail` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varWBusy || IsBlank(varWItem),DisplayMode.Disabled,DisplayMode.Edit)
```

### `Screen1/wDetail/wRefreshDetail` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wRefreshDetail` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wRefreshDetail` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wRefreshDetail` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(35)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wRefreshDetail` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDetail/wRefreshDetail` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wRefreshDetail` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wRefreshDetail` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(wReadBC)
```

### `Screen1/wDetail/wRefreshDetail` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wRefreshDetail` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wRefreshDetail` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDetail/wRefreshDetail` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wRefreshDetail` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wRefreshDetail` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRefreshDetail` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRefreshDetail` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRefreshDetail` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRefreshDetail` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRefreshDetail` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"BC шинэчлэх"
```

### `Screen1/wDetail/wRefreshDetail` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(116)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wRefreshDetail` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(233)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wRefreshDetail` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(408)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBinTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wBinTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBinTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wBinTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wBinTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBinTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wBinTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wBinTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBinTitle` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wBinTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Байрлалаар"
```

### `Screen1/wDetail/wBinTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(200)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBinTitle` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBinTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(454)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wBins` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wBins` . **Height**  _(Gallery@2.15.0)_
```powerfx
(79)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins` . **Items**  _(Gallery@2.15.0)_
```powerfx
AddColumns(GroupBy(ForAll(colWLiveBins As b,{BinCode:b.'Bin Code',BinQuantity:b.qtyBase}),BinCode,WBinRows),BinQty,Sum(WBinRows,BinQuantity))
```

### `Screen1/wDetail/wBins` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wBins` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
34*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins` . **Y**  _(Gallery@2.15.0)_
```powerfx
(481)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wBins/wBinCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wBins/wBinCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(30)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins/wBinCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins/wBinCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wBins/wBinName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBins/wBinName` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wBins/wBinName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wBins/wBinName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBins/wBinName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wBins/wBinName` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wBins/wBinName` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinName` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinName` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.BinCode
```

### `Screen1/wDetail/wBins/wBinName` . **Width**  _(Label@2.5.1)_
```powerfx
(237)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins/wBinName` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins/wBinName` . **Y**  _(Label@2.5.1)_
```powerfx
(3)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wBins/wBinQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBins/wBinQty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wBins/wBinQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wBins/wBinQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBins/wBinQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wBins/wBinQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wBins/wBinQty` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBins/wBinQty` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(28,Self.Height*0.45,Self.Width/Max(8,Len(Self.Text))*1.3))
```

### `Screen1/wDetail/wBins/wBinQty` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:ThisItem.BinQty},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.##")))
```

### `Screen1/wDetail/wBins/wBinQty` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `Screen1/wDetail/wBins/wBinQty` . **Width**  _(Label@2.5.1)_
```powerfx
(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins/wBinQty` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `Screen1/wDetail/wBins/wBinQty` . **X**  _(Label@2.5.1)_
```powerfx
(265)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBins/wBinQty` . **Y**  _(Label@2.5.1)_
```powerfx
(3)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBinEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wBinEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBinEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wDetail/wBinEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wBinEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wBinEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wBinEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(42)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wBinEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wBinEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Тавиурын тоо авахын тулд BC шинэчилнэ."
```

### `Screen1/wDetail/wBinEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(colWLiveBins)
```

### `Screen1/wDetail/wBinEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(321)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBinEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wBinEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(491)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovementTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wMovementTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovementTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wMovementTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wMovementTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovementTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wMovementTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wMovementTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(23)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovementTitle` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wMovementTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хөдөлгөөн"
```

### `Screen1/wDetail/wMovementTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(220)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovementTitle` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovementTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(569)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wMovements` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wMovements` . **Height**  _(Gallery@2.15.0)_
```powerfx
(96)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements` . **Items**  _(Gallery@2.15.0)_
```powerfx
Sort(colWLedger,'Entry No.',SortOrder.Descending)
```

### `Screen1/wDetail/wMovements` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wMovements` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
44*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements` . **Y**  _(Gallery@2.15.0)_
```powerfx
(599)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementType` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wMovements/wMovementType` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovements/wMovementType` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wMovements/wMovementType` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wMovements/wMovementType` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovements/wMovementType` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wMovements/wMovementType` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wMovements/wMovementType` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementType` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementType` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.'Entry Type' & " · " & ThisItem.'Document No.'
```

### `Screen1/wDetail/wMovements/wMovementType` . **Width**  _(Label@2.5.1)_
```powerfx
(248)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements/wMovementType` . **X**  _(Label@2.5.1)_
```powerfx
(10)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements/wMovementType` . **Y**  _(Label@2.5.1)_
```powerfx
(1)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementDate` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wMovements/wMovementDate` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wMovements/wMovementDate` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.'Posting Date')
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Width**  _(Label@2.5.1)_
```powerfx
(220)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements/wMovementDate` . **X**  _(Label@2.5.1)_
```powerfx
(10)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements/wMovementDate` . **Y**  _(Label@2.5.1)_
```powerfx
(26)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDetail/wMovements/wMovementQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(ThisItem.Quantity<0,ColorValue("#ED5F1C"),ColorValue("#85DFAC"))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDetail/wMovements/wMovementQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wMovements/wMovementQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(28,Self.Height*0.45,Self.Width/Max(8,Len(Self.Text))*1.3))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Text**  _(Label@2.5.1)_
```powerfx
With({v:ThisItem.Quantity},Text(v,If(Mod(v,1)=0,"#,##0","#,##0.##")))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Width**  _(Label@2.5.1)_
```powerfx
(61)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `Screen1/wDetail/wMovements/wMovementQty` . **X**  _(Label@2.5.1)_
```powerfx
(260)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wMovements/wMovementQty` . **Y**  _(Label@2.5.1)_
```powerfx
(8)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wTransfer` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDetail/wTransfer` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wTransfer` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDetail/wTransfer` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(varWItem),DisplayMode.Disabled,DisplayMode.Edit)
```

### `Screen1/wDetail/wTransfer` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDetail/wTransfer` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wTransfer` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wTransfer` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wTransfer` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDetail/wTransfer` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wTransfer` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wTransfer` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWDestination,Blank());Set(varWKind,"Transfer");Set(varWDraftId,Text(GUID()));Set(varWAvailable,If(varWLive,Sum(colWLedger,Quantity),LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,Qty)));Set(varWQty,Min(1,Max(0,If(varWLive,Sum(colWLedger,Quantity),LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,Qty)))));Set(varWView,"transfer");Reset(wDestination);Reset(wFromBin);Reset(wToBin);Reset(wReason);Reset(wRecipient);Reset(wQuantity)
```

### `Screen1/wDetail/wTransfer` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wTransfer` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wTransfer` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDetail/wTransfer` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wTransfer` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wTransfer` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wTransfer` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wTransfer` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wTransfer` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wTransfer` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wTransfer` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Шилжүүлэх"
```

### `Screen1/wDetail/wTransfer` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(162)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wTransfer` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wTransfer` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(720)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wRequest` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDetail/wRequest` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wRequest` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDetail/wRequest` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(varWItem),DisplayMode.Disabled,DisplayMode.Edit)
```

### `Screen1/wDetail/wRequest` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wRequest` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDetail/wRequest` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDetail/wRequest` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDetail/wRequest` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDetail/wRequest` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wRequest` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDetail/wRequest` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWDestination,Blank());Set(varWKind,"Request");Set(varWDraftId,Text(GUID()));Set(varWAvailable,If(varWLive,Sum(colWLedger,Quantity),LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,Qty)));Set(varWQty,Max(1,Coalesce(LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,MinQty),0)-Coalesce(If(varWLive,Sum(colWLedger,Quantity),LookUp(colWStock,itemNo=varWItem && locationCode=varWLocation,Qty)),0)));Set(varWView,"transfer");Reset(wDestination);Reset(wFromBin);Reset(wToBin);Reset(wReason);Reset(wRecipient);Reset(wQuantity)
```

### `Screen1/wDetail/wRequest` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wRequest` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDetail/wRequest` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDetail/wRequest` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDetail/wRequest` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDetail/wRequest` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRequest` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRequest` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRequest` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRequest` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDetail/wRequest` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Шаардах"
```

### `Screen1/wDetail/wRequest` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(162)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wRequest` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(187)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDetail/wRequest` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(720)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wTransferPane` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wTransferPane` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varWView="transfer")
```

### `Screen1/wTransferPane` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2
```

### `Screen1/wTransferPane` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Screen1.Height-790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))/2
```

### `Screen1/wTransferPane/transferClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/transferClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/transferClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/transferClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/transferClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/transferClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/transferClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `Screen1/wTransferPane/transferClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/transferStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/transferStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#85DFAC")
```

### `Screen1/wTransferPane/transferStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/transferStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/transferStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/transferStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `Screen1/wTransferPane/transferStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wTransferPane/transferBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/transferBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wTransferPane/transferBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/transferBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/transferBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/transferBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wTransferPane/transferBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/transferBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/transferBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWView,"detail")
```

### `Screen1/wTransferPane/transferBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/transferBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/transferBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wTransferPane/transferBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/transferBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wTransferPane/transferBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `Screen1/wTransferPane/transferBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/transferTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/transferTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/transferTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/transferTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/transferTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/transferTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wTransferPane/transferTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/transferTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Шилжүүлэг / шаардах"
```

### `Screen1/wTransferPane/transferTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/transferTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wDraftStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wDraftStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wDraftStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wTransferPane/wDraftStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/wDraftStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wDraftStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wDraftStatus` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wTransferPane/wDraftStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wDraftStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wDraftStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"НООРОГ · BC руу постлохгүй"
```

### `Screen1/wTransferPane/wDraftStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wDraftStatus` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wDraftStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(94)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wFromCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wFromCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(66)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(130)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCaption` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wFromCaption` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wFromCaption` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wTransferPane/wFromCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/wFromCaption` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wFromCaption` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wFromCaption` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCaption` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromCaption` . **Text**  _(Label@2.5.1)_
```powerfx
"Хаанаас / хүсэлт гаргасан агуулах"
```

### `Screen1/wTransferPane/wFromCaption` . **Width**  _(Label@2.5.1)_
```powerfx
(298)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromCaption` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromCaption` . **Y**  _(Label@2.5.1)_
```powerfx
(140)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromValue` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wFromValue` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wFromValue` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wFromValue` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/wFromValue` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wFromValue` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wFromValue` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wTransferPane/wFromValue` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromValue` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromValue` . **Text**  _(Label@2.5.1)_
```powerfx
varWLocation & " · " & Text(varWAvailable,"#,##0.###") & " байна"
```

### `Screen1/wTransferPane/wFromValue` . **Width**  _(Label@2.5.1)_
```powerfx
(298)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromValue` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromValue` . **Y**  _(Label@2.5.1)_
```powerfx
(164)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wDestination` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wDestination` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wDestination` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
Coalesce(varWDestination,"")
```

### `Screen1/wTransferPane/wDestination` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wDestination` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wDestination` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wDestination` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(48)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wDestination` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Хаашаа — агуулах сонгох"
```

### `Screen1/wTransferPane/wDestination` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wDestination` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wTransferPane/wDestination` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wDestination` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wDestination` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wTransferPane/wDestination` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wDestination` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wDestination` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(285)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wDestination` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wDestination` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(207)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wChooseDestination` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wTransferPane/wChooseDestination` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wChooseDestination` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wTransferPane/wChooseDestination` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wChooseDestination` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wChooseDestination` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wChooseDestination` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(48)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wChooseDestination` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wTransferPane/wChooseDestination` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wChooseDestination` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wChooseDestination` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWPicker,true)
```

### `Screen1/wTransferPane/wChooseDestination` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wChooseDestination` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wChooseDestination` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wTransferPane/wChooseDestination` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wChooseDestination` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wTransferPane/wChooseDestination` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wChooseDestination` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wChooseDestination` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wChooseDestination` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wChooseDestination` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
16*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wChooseDestination` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"⌄"
```

### `Screen1/wTransferPane/wChooseDestination` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(42)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wChooseDestination` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(307)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wChooseDestination` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(207)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wTransferItem` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wTransferItem` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wTransferItem` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wTransferItem` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/wTransferItem` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wTransferItem` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wTransferItem` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wTransferPane/wTransferItem` . **Height**  _(Label@2.5.1)_
```powerfx
(45)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wTransferItem` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wTransferItem` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(LookUp(colOfflineItems,number=varWItem,displayName),varWItem) & " · " & varWItem
```

### `Screen1/wTransferPane/wTransferItem` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wTransferItem` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wTransferItem` . **Y**  _(Label@2.5.1)_
```powerfx
(269)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wQuantityLabel` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wQuantityLabel` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wQuantityLabel` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wTransferPane/wQuantityLabel` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/wQuantityLabel` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wQuantityLabel` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wQuantityLabel` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wQuantityLabel` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wQuantityLabel` . **Text**  _(Label@2.5.1)_
```powerfx
"Шилжүүлэх / шаардах тоо"
```

### `Screen1/wTransferPane/wQuantityLabel` . **Width**  _(Label@2.5.1)_
```powerfx
(244)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wQuantityLabel` . **X**  _(Label@2.5.1)_
```powerfx
(61)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wQuantityLabel` . **Y**  _(Label@2.5.1)_
```powerfx
(331)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wMinus` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wTransferPane/wMinus` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wMinus` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wTransferPane/wMinus` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wMinus` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wMinus` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wMinus` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(52)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wMinus` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wTransferPane/wMinus` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wMinus` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wMinus` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWQty,Max(0,IfError(Value(wQuantity.Text),0)-1));Reset(wQuantity)
```

### `Screen1/wTransferPane/wMinus` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wMinus` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wMinus` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wTransferPane/wMinus` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wMinus` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wTransferPane/wMinus` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wMinus` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wMinus` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wMinus` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wMinus` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
23*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wMinus` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"−"
```

### `Screen1/wTransferPane/wMinus` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(52)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wMinus` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(34)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wMinus` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(372)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wQuantity` . **Align**  _(Classic/TextInput@2.3.2)_
```powerfx
Align.Center
```

### `Screen1/wTransferPane/wQuantity` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wQuantity` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wQuantity` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
Text(varWQty)
```

### `Screen1/wTransferPane/wQuantity` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wQuantity` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wQuantity` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wQuantity` . **Format**  _(Classic/TextInput@2.3.2)_
```powerfx
TextFormat.Number
```

### `Screen1/wTransferPane/wQuantity` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(69)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wQuantity` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Тоо"
```

### `Screen1/wTransferPane/wQuantity` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wQuantity` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wTransferPane/wQuantity` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wQuantity` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wQuantity` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wTransferPane/wQuantity` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wQuantity` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
34*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wQuantity` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(157)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wQuantity` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(105)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wQuantity` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(363)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPlus` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wTransferPane/wPlus` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wPlus` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wTransferPane/wPlus` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wPlus` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wPlus` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wPlus` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(52)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPlus` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wTransferPane/wPlus` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wPlus` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wPlus` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWQty,IfError(Value(wQuantity.Text),0)+1);Reset(wQuantity)
```

### `Screen1/wTransferPane/wPlus` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wPlus` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wPlus` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wTransferPane/wPlus` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wPlus` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wTransferPane/wPlus` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPlus` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPlus` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPlus` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPlus` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
23*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPlus` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"+"
```

### `Screen1/wTransferPane/wPlus` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(52)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wPlus` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(282)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wPlus` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(372)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromBin` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wFromBin` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wFromBin` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wFromBin` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wFromBin` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wFromBin` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(40)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromBin` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Эхлэх тавиур (сонголт)"
```

### `Screen1/wTransferPane/wFromBin` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wFromBin` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wTransferPane/wFromBin` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wFromBin` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromBin` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wTransferPane/wFromBin` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wFromBin` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wFromBin` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(161)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromBin` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wFromBin` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(451)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wToBin` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wToBin` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wToBin` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wToBin` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wToBin` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wToBin` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(40)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wToBin` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Хүрэх тавиур (сонголт)"
```

### `Screen1/wTransferPane/wToBin` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wToBin` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wTransferPane/wToBin` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wToBin` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wToBin` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wTransferPane/wToBin` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wToBin` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wToBin` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(161)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wToBin` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(188)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wToBin` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(451)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wReason` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wReason` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wReason` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wReason` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wReason` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wReason` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(45)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wReason` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Шалтгаан"
```

### `Screen1/wTransferPane/wReason` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wReason` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wTransferPane/wReason` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wReason` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wReason` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wTransferPane/wReason` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wReason` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wReason` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wReason` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wReason` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(509)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wRecipient` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wRecipient` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wRecipient` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wTransferPane/wRecipient` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wRecipient` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wRecipient` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(45)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wRecipient` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Хүлээн авагч"
```

### `Screen1/wTransferPane/wRecipient` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wRecipient` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `Screen1/wTransferPane/wRecipient` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wRecipient` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wRecipient` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `Screen1/wTransferPane/wRecipient` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wRecipient` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wRecipient` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wRecipient` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wRecipient` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(564)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPrinter` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wTransferPane/wPrinter` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wPrinter` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wTransferPane/wPrinter` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wTransferPane/wPrinter` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wPrinter` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wPrinter` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPrinter` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wPrinter` . **Text**  _(Label@2.5.1)_
```powerfx
"Баркод хэвлэх · принтер холбогдоогүй"
```

### `Screen1/wTransferPane/wPrinter` . **Width**  _(Label@2.5.1)_
```powerfx
(316)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wPrinter` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wPrinter` . **Y**  _(Label@2.5.1)_
```powerfx
(624)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wSaveDraft` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wTransferPane/wSaveDraft` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wSaveDraft` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wTransferPane/wSaveDraft` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varWBusy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `Screen1/wTransferPane/wSaveDraft` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wTransferPane/wSaveDraft` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wTransferPane/wSaveDraft` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wTransferPane/wSaveDraft` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wTransferPane/wSaveDraft` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wTransferPane/wSaveDraft` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wSaveDraft` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wTransferPane/wSaveDraft` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPAuditDraftBefore,JSON(Filter(colWDrafts,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(FromLocation) & "|") in pgAccess.LocationCode),DraftId=varWDraftId && OwnerEmail=User().Email),JSONFormat.Compact));With({v:IfError(Value(wQuantity.Text),Blank()),dest:Trim(wDestination.Text)},
If(IsBlank(varWItem) || IsBlank(varWLocation),Notify("Бараа, эхлэх агуулах сонгоно уу.",NotificationType.Warning),
IsBlank(v) || v<=0,Notify("Тоо 0-ээс их байх ёстой.",NotificationType.Warning),
varWKind="Transfer" && (IsBlank(dest) || IsBlank(LookUp(colWLocations,Code=dest,Code)) || dest=varWLocation),Notify("Өөр хүрэх агуулах сонгоно уу.",NotificationType.Warning),
varWKind="Transfer" && v>Max(0,Coalesce(varWAvailable,0)),Notify("Шилжүүлэх тоо харагдаж буй үлдэгдлээс их байна.",NotificationType.Warning),
IsBlank(Trim(wReason.Text)) || IsBlank(Trim(wRecipient.Text)),Notify("Шалтгаан болон хүлээн авагчийг бөглөнө үү.",NotificationType.Warning),
Set(varWBusy,true);
With({r:{DraftId:varWDraftId,OwnerEmail:User().Email,Kind:varWKind,ItemNo:varWItem,ItemName:Coalesce(LookUp(colOfflineItems,number=varWItem,displayName),varWItem),FromLocation:varWLocation,ToLocation:dest,FromBin:Trim(wFromBin.Text),ToBin:Trim(wToBin.Text),Quantity:v,Uom:LookUp(colOfflineItems,number=varWItem,unitOfMeasure),Reason:Trim(wReason.Text),Recipient:Trim(wRecipient.Text),Created:Now(),Status:"Draft"}},
If(IsBlank(LookUp(colWDrafts,DraftId=varWDraftId,DraftId)),Collect(colWDrafts,r),Patch(colWDrafts,LookUp(colWDrafts,DraftId=varWDraftId),r)));
If(wDraftStore="ready",IfError(SaveData(colWDrafts,"WarehouseDraftsV6");true,Set(wDraftStoreError,FirstError.Message);Notify("Ноорог энэ удаагийн сессэд байна. Төхөөрөмжид хадгалахад алдаа гарлаа. " & wDraftStoreError,NotificationType.Warning);false,Set(wDraftStoreError,"");Notify("Ноорог төхөөрөмжид хадгалагдлаа.",NotificationType.Success);true),wDraftStore="preview",Notify("Ноорог Studio-ийн энэ сессэд хадгалагдлаа.",NotificationType.Information),wDraftStore="session",Notify("Ноорог энэ сессэд хадгалагдлаа. Энэ төхөөрөмжийн тоглуулагч локал хадгалалтыг дэмжихгүй байна.",NotificationType.Warning),Notify("Ноорог энэ сессэд байна. Өмнөх кэшийг уншихад гарсан алдаа: " & wDraftStoreError,NotificationType.Warning));
Set(varWBusy,false);Set(varWView,"drafts")));If(varPAuditDraftBefore<>JSON(Filter(colWDrafts,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(FromLocation) & "|") in pgAccess.LocationCode),DraftId=varWDraftId && OwnerEmail=User().Email),JSONFormat.Compact),Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Агуулах",Action:"Ноорог шинэчилсэн",Entity:varWDraftId,BeforeValue:varPAuditDraftBefore,AfterValue:JSON(Filter(colWDrafts,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(FromLocation) & "|") in pgAccess.LocationCode),DraftId=varWDraftId && OwnerEmail=User().Email),JSONFormat.Compact),Result:"Локал өөрчлөлт"});If(!IsBlank(Host.Version),IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true)))
```

### `Screen1/wTransferPane/wSaveDraft` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wSaveDraft` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wTransferPane/wSaveDraft` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wTransferPane/wSaveDraft` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wTransferPane/wSaveDraft` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wTransferPane/wSaveDraft` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wSaveDraft` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wSaveDraft` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wSaveDraft` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wSaveDraft` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wTransferPane/wSaveDraft` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Ноорог хадгалах →"
```

### `Screen1/wTransferPane/wSaveDraft` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wSaveDraft` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wTransferPane/wSaveDraft` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(720)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDraftPane` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wDraftPane` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varWView="drafts")
```

### `Screen1/wDraftPane` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2
```

### `Screen1/wDraftPane` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Screen1.Height-790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))/2
```

### `Screen1/wDraftPane/draftsClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/draftsClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/draftsClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/draftsClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/draftsClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/draftsClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/draftsClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `Screen1/wDraftPane/draftsClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/draftsStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/draftsStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#85DFAC")
```

### `Screen1/wDraftPane/draftsStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/draftsStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/draftsStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/draftsStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `Screen1/wDraftPane/draftsStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDraftPane/draftsBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/draftsBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDraftPane/draftsBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDraftPane/draftsBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/draftsBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/draftsBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDraftPane/draftsBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/draftsBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDraftPane/draftsBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWView,"overview")
```

### `Screen1/wDraftPane/draftsBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDraftPane/draftsBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDraftPane/draftsBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDraftPane/draftsBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/draftsBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDraftPane/draftsBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `Screen1/wDraftPane/draftsBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/draftsTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/draftsTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/draftsTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/draftsTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/draftsTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/draftsTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDraftPane/draftsTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/draftsTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хадгалсан ноорог"
```

### `Screen1/wDraftPane/draftsTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/draftsTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Height**  _(Label@2.5.1)_
```powerfx
(37)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Text**  _(Label@2.5.1)_
```powerfx
Switch(wDraftStore,"preview","Studio · нооргууд энэ сессэд хадгалагдана.","session","Энэ тоглуулагчид нооргууд зөвхөн сессэд хадгалагдана.","protected","Өмнөх нооргуудыг уншиж чадсангүй. Шинэ ноорог энэ сессэд хадгалагдана.",If(!IsBlank(wDraftStoreError),"Төхөөрөмжид хадгалах үед алдаа гарсан · сессийн нооргууд","Зөвхөн энэ төхөөрөмж · BC руу илгээгээгүй"))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftDisclaimer` . **Y**  _(Label@2.5.1)_
```powerfx
(104)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/wDraftGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/wDraftGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(480)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
SortByColumns(Filter(colWDrafts,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(FromLocation) & "|") in pgAccess.LocationCode),OwnerEmail=User().Email),"Created",SortOrder.Descending)
```

### `Screen1/wDraftPane/wDraftGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/wDraftGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
119*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(159)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(111)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ItemName & " · " & Text(ThisItem.Quantity)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Width**  _(Label@2.5.1)_
```powerfx
(305)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftItem` . **Y**  _(Label@2.5.1)_
```powerfx
(11)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.FromLocation & " → " & ThisItem.ToLocation & " · " & If(ThisItem.Kind="Transfer","Шилжүүлэг","Шаардах")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Width**  _(Label@2.5.1)_
```powerfx
(305)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftPath` . **Y**  _(Label@2.5.1)_
```powerfx
(40)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Reason & " · " & ThisItem.Recipient
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Width**  _(Label@2.5.1)_
```powerfx
(305)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftReason` . **Y**  _(Label@2.5.1)_
```powerfx
(66)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Created,"yyyy.mm.dd hh:mm")
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Width**  _(Label@2.5.1)_
```powerfx
(305)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wDraftGallery/wDraftDate` . **Y**  _(Label@2.5.1)_
```powerfx
(89)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wBackOverview` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wDraftPane/wBackOverview` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wDraftPane/wBackOverview` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wDraftPane/wBackOverview` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/wBackOverview` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wDraftPane/wBackOverview` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wDraftPane/wBackOverview` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wDraftPane/wBackOverview` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wDraftPane/wBackOverview` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/wBackOverview` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wDraftPane/wBackOverview` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWView,"overview")
```

### `Screen1/wDraftPane/wBackOverview` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDraftPane/wBackOverview` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wDraftPane/wBackOverview` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wDraftPane/wBackOverview` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wDraftPane/wBackOverview` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wDraftPane/wBackOverview` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wBackOverview` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wBackOverview` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wBackOverview` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wBackOverview` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wDraftPane/wBackOverview` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах руу буцах"
```

### `Screen1/wDraftPane/wBackOverview` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wBackOverview` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wDraftPane/wBackOverview` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(720)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wPicker` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `Screen1/wPicker` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(790)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varWPicker)
```

### `Screen1/wPicker` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(366)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366))))/2
```

### `Screen1/wPicker` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790))))/2
```

### `Screen1/wPicker/wPickerTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wPicker/wPickerTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wPicker/wPickerTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wPicker/wPickerTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wPicker/wPickerTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wPicker/wPickerTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wPicker/wPickerTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wPicker/wPickerTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(40)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хүрэх агуулах"
```

### `Screen1/wPicker/wPickerTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(260)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wPickerTitle` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wPickerTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(63)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerClose` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wPicker/wPickerClose` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wPicker/wPickerClose` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wPicker/wPickerClose` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wPicker/wPickerClose` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wPicker/wPickerClose` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wPicker/wPickerClose` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerClose` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wPicker/wPickerClose` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wPicker/wPickerClose` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wPicker/wPickerClose` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWPicker,false)
```

### `Screen1/wPicker/wPickerClose` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wPicker/wPickerClose` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wPicker/wPickerClose` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wPicker/wPickerClose` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wPicker/wPickerClose` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wPicker/wPickerClose` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerClose` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerClose` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerClose` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerClose` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
21*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wPickerClose` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"×"
```

### `Screen1/wPicker/wPickerClose` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(43)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wPickerClose` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(302)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wPickerClose` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(63)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wPicker/wDestinationGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wPicker/wDestinationGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(537)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
Filter(colWLocations,Code<>varWLocation)
```

### `Screen1/wPicker/wDestinationGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wPicker/wDestinationGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
65*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wDestinationGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wDestinationGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(137)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(59)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWDestination,ThisItem.Code);Reset(wDestination);Set(varWPicker,false)
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
ThisItem.Code & " · " & ThisItem.LocationName
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Width/1128),(Screen1.Width/366)))
```

### `Screen1/wPicker/wDestinationGallery/wDestinationRow` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((Screen1.Width>=First(App.SizeBreakpoints).Value && Screen1.Width>Screen1.Height),(Screen1.Height/790),(Screen1.Height/790)))
```

### `Screen1/wExportModal` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wExportModal` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wExportModal` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Height*0.90,440*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `Screen1/wExportModal` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varWExport)
```

### `Screen1/wExportModal` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width*0.92,680*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `Screen1/wExportModal` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `Screen1/wExportModal` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(App.Height-Self.Height)/2
```

### `Screen1/wExportModal/wExportTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wExportModal/wExportTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wExportModal/wExportTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wExportModal/wExportTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wExportModal/wExportTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wExportModal/wExportTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wExportModal/wExportTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `Screen1/wExportModal/wExportTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.14
```

### `Screen1/wExportModal/wExportTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/24,Parent.Height/17)
```

### `Screen1/wExportModal/wExportTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Excel-д нээх CSV"
```

### `Screen1/wExportModal/wExportTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `Screen1/wExportModal/wExportTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `Screen1/wExportModal/wExportTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.05
```

### `Screen1/wExportModal/wExportText` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Screen1/wExportModal/wExportText` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wExportModal/wExportText` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `Screen1/wExportModal/wExportText` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `Screen1/wExportModal/wExportText` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wExportModal/wExportText` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wExportModal/wExportText` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.44
```

### `Screen1/wExportModal/wExportText` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `Screen1/wExportModal/wExportText` . **Text**  _(Label@2.5.1)_
```powerfx
"Одоо шүүсэн үлдэгдлийг өөрийн мэйлд илгээнэ." & Char(10) & User().Email
```

### `Screen1/wExportModal/wExportText` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `Screen1/wExportModal/wExportText` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `Screen1/wExportModal/wExportText` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.23
```

### `Screen1/wExportModal/wExportCancel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wExportModal/wExportCancel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wExportModal/wExportCancel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wExportModal/wExportCancel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `Screen1/wExportModal/wExportCancel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wExportModal/wExportCancel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wExportModal/wExportCancel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `Screen1/wExportModal/wExportCancel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wExportModal/wExportCancel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wExportModal/wExportCancel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wExportModal/wExportCancel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWExport,false)
```

### `Screen1/wExportModal/wExportCancel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wExportModal/wExportCancel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wExportModal/wExportCancel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wExportModal/wExportCancel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wExportModal/wExportCancel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wExportModal/wExportCancel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportCancel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportCancel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportCancel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportCancel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `Screen1/wExportModal/wExportCancel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Болих"
```

### `Screen1/wExportModal/wExportCancel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.29
```

### `Screen1/wExportModal/wExportCancel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.06
```

### `Screen1/wExportModal/wExportCancel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `Screen1/wExportModal/wExportSend` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `Screen1/wExportModal/wExportSend` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wExportModal/wExportSend` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `Screen1/wExportModal/wExportSend` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varWBusy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `Screen1/wExportModal/wExportSend` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wExportModal/wExportSend` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `Screen1/wExportModal/wExportSend` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `Screen1/wExportModal/wExportSend` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `Screen1/wExportModal/wExportSend` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `Screen1/wExportModal/wExportSend` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wExportModal/wExportSend` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `Screen1/wExportModal/wExportSend` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!Connection.Connected,Notify("Интернет холболт алга.",NotificationType.Warning),IsEmpty(wStockGallery.AllItems),Notify("Илгээх мөр алга.",NotificationType.Warning),Set(varWBusy,true);IfError(PA_ExportInventoryCSV.Run(JSON(ForAll(Filter(colWStock As s,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(s.locationCode) & "|") in pgAccess.LocationCode),(IsBlank(varWLocation) || s.locationCode=varWLocation) && (IsBlank(Trim(wStockSearch.Text)) || Lower(Trim(wStockSearch.Text)) in Lower(s.itemNo & " " & s.ItemName) || !IsBlank(LookUp(colOfflineBins,itemNo=s.itemNo && locationCode=s.locationCode && Lower(Trim(wStockSearch.Text)) in Lower(binCode),binCode))) && (varWFilter="Бүгд" || (varWFilter="Дутагдалтай" && !IsBlank(s.MinQty) && s.Qty<s.MinQty) || (varWFilter="Хэвийн" && !IsBlank(s.MinQty) && s.Qty>=s.MinQty))) As r,{ItemNo:r.itemNo,ItemName:r.ItemName,LocationCode:r.locationCode,OpeningBalance:r.Qty,CountQty:Blank(),Variance:Blank(),Counter:User().FullName,CountDate:Now(),Reason:"Үлдэгдэл · локал snapshot",Comment:"Минимум: " & Coalesce(Text(r.MinQty),"—")}),JSONFormat.Compact),User().Email,"[CSV] Агуулахын үлдэгдэл " & Coalesce(varWLocation,"Бүгд") & " " & Text(Today(),"yyyy-mm-dd"),"<h2>Агуулахын үлдэгдэл</h2><p>Хэрэглэгч: " & User().FullName & " · " & User().Email & "</p><p>Хуудас: Агуулах · Үлдэгдэл</p><p>Огноо: " & Text(Now(),"yyyy-mm-dd hh:mm") & "</p><p>Шүүлт: " & Coalesce(varWLocation,"Бүгд") & " · " & varWFilter & "</p><p>Үлдэгдлийн CSV хавсралт. Тоолсон тоо болон зөрүүгийн багана хамаарахгүй.</p>");Notify("CSV илгээх хүсэлт гүйцэтгэлээ.",NotificationType.Success);Set(varWExport,false),Notify("Илгээхэд алдаа: " & FirstError.Message,NotificationType.Error));Set(varWBusy,false))
```

### `Screen1/wExportModal/wExportSend` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wExportModal/wExportSend` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `Screen1/wExportModal/wExportSend` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `Screen1/wExportModal/wExportSend` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/wExportModal/wExportSend` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `Screen1/wExportModal/wExportSend` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportSend` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportSend` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportSend` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(Screen1.Width>=First(App.SizeBreakpoints).Value,Min(Screen1.Width/1128,Screen1.Height/790),Min(Screen1.Width/366,Screen1.Height/790)))
```

### `Screen1/wExportModal/wExportSend` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `Screen1/wExportModal/wExportSend` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Илгээх"
```

### `Screen1/wExportModal/wExportSend` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.56
```

### `Screen1/wExportModal/wExportSend` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.38
```

### `Screen1/wExportModal/wExportSend` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `Screen1/pgDenied1229` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `Screen1/pgDenied1229` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `Screen1/pgDenied1229` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `Screen1/pgDenied1229` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `Screen1/pgDenied1229` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Screen1/pgDenied1229` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `Screen1/pgDenied1229` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `Screen1/pgDenied1229` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `Screen1/pgDenied1229` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `Screen1/pgDenied1229` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

