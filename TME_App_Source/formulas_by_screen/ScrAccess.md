# ScrAccess — Power Fx formulas

### `ScrAccess` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrAccess` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrAccess` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrAccess` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If(IsBlank(varPView),Set(varPView,"welcome"));Set(varPExitConfirm,false);Set(varPExport,false);Set(varPBusy,false);
If(!Coalesce(varPInitialized,false),
ClearCollect(colPPrefs,{OwnerEmail:"",Language:"MN",Completed:false,WarehouseJSON:"[]",CacheReady:false,CacheSavedAt:"",Remind:true});Clear(colPPrefs);
IfError(LoadData(colPPrefs,"AccessPrefsV8",true),Notify("Тохиргоог уншиж чадсангүй.",NotificationType.Warning); false, true);
ClearCollect(colPAudit,{EventId:"",OwnerEmail:"",ActorName:"",ActorEmail:"",OccurredAt:Now(),Module:"",Action:"",Entity:"",BeforeValue:"",AfterValue:"",Result:""});Clear(colPAudit);
IfError(LoadData(colPAudit,"AccessAuditV8",true),Set(varPAuditSaveError,true); false, true);
Set(varPCompleted,Coalesce(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),Completed),false));
Set(varPCacheReady,Coalesce(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),CacheReady),false));
Set(varPCacheSavedAt,Coalesce(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),CacheSavedAt),""));
Set(varPRemind,Coalesce(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),Remind),true));
Set(varHomeLanguage,Coalesce(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),Language),"MN"));
ClearCollect(colPSelected,{Code:""});Clear(colPSelected);
IfError(Collect(colPSelected,ForAll(Table(ParseJSON(Coalesce(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),WarehouseJSON),"[]"))) As w,{Code:Text(w.Value.Code)})),Clear(colPSelected); false, true);
Set(varPCacheKey,Substitute(Substitute(Lower(User().Email),"@","_"),".","_"));
Set(varPAuditFilter,"Бүгд");Set(varPInitialized,true));
ClearCollect(colPLocationCodes,ForAll(Filter(colOfflineStock,!IsBlank(locationCode)),{Code:locationCode}));
If(Connection.Connected && IsEmpty(colPLocationMaster),IfError(ClearCollect(colPLocationMaster,'locations (v2.0)'),Notify("Агуулахын жагсаалтыг онлайн уншиж чадсангүй.",NotificationType.Warning); false, true));
Collect(colPLocationCodes,ForAll(colPLocationMaster,{Code:Code}));Collect(colPLocationCodes,colPSelected);
ClearCollect(colPLocations,AddColumns(DropColumns(GroupBy(Filter(colPLocationCodes,!IsBlank(Code)),Code,PRows),PRows) As w,Name,Coalesce(LookUp(colPLocationMaster,Code=w.Code,Name),w.Code)))
```

### `ScrAccess` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrAccess/pReloadWarehouses` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pReloadWarehouses` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReloadWarehouses` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pReloadWarehouses` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pReloadWarehouses` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReloadWarehouses` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReloadWarehouses` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(1)*((ScrAccess.Height/790))
```

### `ScrAccess/pReloadWarehouses` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pReloadWarehouses` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReloadWarehouses` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pReloadWarehouses` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
ClearCollect(colPLocationCodes,ForAll(Filter(colOfflineStock,!IsBlank(locationCode)),{Code:locationCode}));
If(Connection.Connected,IfError(ClearCollect(colPLocationMaster,'locations (v2.0)'),Notify("Агуулахын жагсаалтыг онлайн уншиж чадсангүй.",NotificationType.Warning); false, true));
Collect(colPLocationCodes,ForAll(colPLocationMaster,{Code:Code}));Collect(colPLocationCodes,colPSelected);
ClearCollect(colPLocations,AddColumns(DropColumns(GroupBy(Filter(colPLocationCodes,!IsBlank(Code)),Code,PRows),PRows) As w,Name,Coalesce(LookUp(colPLocationMaster,Code=w.Code,Name),w.Code)))
```

### `ScrAccess/pReloadWarehouses` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pReloadWarehouses` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pReloadWarehouses` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pReloadWarehouses` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReloadWarehouses` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReloadWarehouses` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReloadWarehouses` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReloadWarehouses` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReloadWarehouses` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReloadWarehouses` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReloadWarehouses` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
false
```

### `ScrAccess/pReloadWarehouses` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(1)*((ScrAccess.Width/366))
```

### `ScrAccess/pReloadWarehouses` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((ScrAccess.Width/366))
```

### `ScrAccess/pReloadWarehouses` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWelcome` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrAccess/pWelcome` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varPView="welcome"
```

### `ScrAccess/pWelcome` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*((ScrAccess.Width/366)))/2
```

### `ScrAccess/pWelcome` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*((ScrAccess.Height/790)))/2
```

### `ScrAccess/pWelcome/pWelcomeGlow` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWelcome/pWelcomeGlow` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWelcome/pWelcomeGlow` . **Height**  _(Image@2.2.3)_
```powerfx
(790)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeGlow` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' width='366' height='790'><defs><radialGradient id='g'><stop stop-color='#51271C'/><stop offset='1' stop-color='#F5F4F1'/></radialGradient></defs><rect width='366' height='790' fill='#F5F4F1'/><ellipse cx='183' cy='410' rx='250' ry='295' fill='url(#g)'/></svg>")
```

### `ScrAccess/pWelcome/pWelcomeGlow` . **Width**  _(Image@2.2.3)_
```powerfx
(366)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeGlow` . **X**  _(Image@2.2.3)_
```powerfx
(0)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeGlow` . **Y**  _(Image@2.2.3)_
```powerfx
(0)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWelcome/pWelcomeClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWelcome/pWelcomeClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Width**  _(Label@2.5.1)_
```powerfx
(90)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLogo` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWelcome/pWelcomeLogo` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWelcome/pWelcomeLogo` . **Height**  _(Image@2.2.3)_
```powerfx
(106)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLogo` . **Image**  _(Image@2.2.3)_
```powerfx
'Buuruljuut logo 3-6-03 2'
```

### `ScrAccess/pWelcome/pWelcomeLogo` . **Width**  _(Image@2.2.3)_
```powerfx
(222)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLogo` . **X**  _(Image@2.2.3)_
```powerfx
(72)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLogo` . **Y**  _(Image@2.2.3)_
```powerfx
(216)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(44)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Self.Width/13,Self.Height/2.8)
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Inventory Management"
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(322)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **X**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(351)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrAccess/pWelcome/pWelcomeSub` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWelcome/pWelcomeSub` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWelcome/pWelcomeSub` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Height**  _(Label@2.5.1)_
```powerfx
(60)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Text**  _(Label@2.5.1)_
```powerfx
Switch(varHomeLanguage,"EN","Inventory, warehouse, search and reports.","中文","盘点、仓库、搜索与报表。","Тооллого, агуулах, хайлт, тайлан — нэг дор.")
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Width**  _(Label@2.5.1)_
```powerfx
(310)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeSub` . **X**  _(Label@2.5.1)_
```powerfx
(28)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeSub` . **Y**  _(Label@2.5.1)_
```powerfx
(408)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pLogin` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWelcome/pLogin` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrAccess/pWelcome/pLogin` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWelcome/pLogin` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pLogin` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pLogin` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pLogin` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pLogin` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWelcome/pLogin` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pLogin` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWelcome/pLogin` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(User().Email),Notify("Power Apps-д Microsoft 365 бүртгэлээрээ нэвтэрнэ үү.",NotificationType.Warning),Set(varPOffline,false);Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Бүртгэлээр үргэлжилсэн",Entity:User().Email,BeforeValue:"",AfterValue:"Microsoft 365 сесс",Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true);Set(varPCompleted,true);Set(varLocationCode,Blank());Set(varWLocation,Blank());Navigate(нүүр,ScreenTransition.Fade))
```

### `ScrAccess/pWelcome/pLogin` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pLogin` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pLogin` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWelcome/pLogin` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pLogin` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWelcome/pLogin` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pLogin` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pLogin` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pLogin` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pLogin` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pLogin` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Switch(varHomeLanguage,"EN","Continue with Microsoft 365","中文","使用 Microsoft 365 继续","Microsoft 365-ээр үргэлжлүүлэх")
```

### `ScrAccess/pWelcome/pLogin` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pLogin` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pLogin` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(587)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pOffline` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWelcome/pOffline` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pOffline` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWelcome/pOffline` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pWelcome/pOffline` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pOffline` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pOffline` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(49)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pOffline` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWelcome/pOffline` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pOffline` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWelcome/pOffline` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(User().Email) || IsEmpty(colOfflineItems),Notify("Энэ бүртгэлээр нэг удаа онлайн нэвтэрч өгөгдлөө татна уу.",NotificationType.Warning),Set(varPOffline,true);Set(varLocationCode,Blank());Set(varWLocation,Blank());Navigate(нүүр,ScreenTransition.None))
```

### `ScrAccess/pWelcome/pOffline` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pOffline` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pOffline` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWelcome/pOffline` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pOffline` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWelcome/pOffline` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pOffline` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pOffline` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pOffline` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pOffline` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pOffline` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Switch(varHomeLanguage,"EN","Continue offline","中文","离线继续","Оффлайн горимоор үргэлжлүүлэх")
```

### `ScrAccess/pWelcome/pOffline` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pOffline` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pOffline` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(653)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varHomeLanguage="MN",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varHomeLanguage="MN",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(27)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPOldLanguage,varHomeLanguage);Set(varHomeLanguage,"MN");With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);If(varPOldLanguage<>varHomeLanguage,Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Хэл өөрчилсөн",Entity:"Language",BeforeValue:varPOldLanguage,AfterValue:varHomeLanguage,Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"МН"
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(39)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(122)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLang0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(716)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varHomeLanguage="EN",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varHomeLanguage="EN",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(27)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPOldLanguage,varHomeLanguage);Set(varHomeLanguage,"EN");With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);If(varPOldLanguage<>varHomeLanguage,Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Хэл өөрчилсөн",Entity:"Language",BeforeValue:varPOldLanguage,AfterValue:varHomeLanguage,Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"EN"
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(39)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(164)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLang1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(716)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varHomeLanguage="中文",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varHomeLanguage="中文",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(27)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPOldLanguage,varHomeLanguage);Set(varHomeLanguage,"中文");With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);If(varPOldLanguage<>varHomeLanguage,Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Хэл өөрчилсөн",Entity:"Language",BeforeValue:varPOldLanguage,AfterValue:varHomeLanguage,Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"中文"
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(39)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(206)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pWelcomeLang2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(716)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pSessionInfo` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrAccess/pWelcome/pSessionInfo` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWelcome/pSessionInfo` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pSessionInfo` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pWelcome/pSessionInfo` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWelcome/pSessionInfo` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWelcome/pSessionInfo` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWelcome/pSessionInfo` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pSessionInfo` . **Size**  _(Label@2.5.1)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWelcome/pSessionInfo` . **Text**  _(Label@2.5.1)_
```powerfx
"Microsoft 365: " & Coalesce(User().Email,"нэвтрээгүй")
```

### `ScrAccess/pWelcome/pSessionInfo` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pSessionInfo` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWelcome/pSessionInfo` . **Y**  _(Label@2.5.1)_
```powerfx
(756)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWarehouseSetup` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrAccess/pWarehouseSetup` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varPView="warehouses"
```

### `ScrAccess/pWarehouseSetup` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*((ScrAccess.Width/366)))/2
```

### `ScrAccess/pWarehouseSetup` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*((ScrAccess.Height/790)))/2
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(3)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pProgress20` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(60)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(3)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(131)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pProgress21` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(60)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(3)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(241)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pProgress22` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(60)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pStep2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pStep2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pStep2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pStep2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Text**  _(Label@2.5.1)_
```powerfx
"АЛХАМ 2 / 3"
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Width**  _(Label@2.5.1)_
```powerfx
(320)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pStep2` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pStep2` . **Y**  _(Label@2.5.1)_
```powerfx
(84)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Height**  _(Label@2.5.1)_
```powerfx
(67)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Size**  _(Label@2.5.1)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Text**  _(Label@2.5.1)_
```powerfx
Switch(varHomeLanguage,"EN","Which warehouses do you work in?","中文","您在哪些仓库工作？","Аль агуулахад ажилладаг вэ?")
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseQuestion` . **Y**  _(Label@2.5.1)_
```powerfx
(120)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Height**  _(Label@2.5.1)_
```powerfx
(58)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Text**  _(Label@2.5.1)_
```powerfx
"Агуулахаа сонгоно уу. Дараа нь профайлаас өөрчилж болно."
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseIntro` . **Y**  _(Label@2.5.1)_
```powerfx
(199)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(358)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
Filter(SortByColumns(colPLocations,"Code",SortOrder.Ascending),((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(Code) & "|") in pgAccess.LocationCode))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
65*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(268)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
If(ThisItem.Code in colPSelected.Code,ColorValue("#ED5F1C"),ColorValue("#E4E1DC"))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(ThisItem.Code in colPSelected.Code,ColorValue("#2A1A12"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(59)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Size**  _(Label@2.5.1)_
```powerfx
20*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Text**  _(Label@2.5.1)_
```powerfx
If(ThisItem.Code in colPSelected.Code,"✓","○")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Width**  _(Label@2.5.1)_
```powerfx
(32)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **X**  _(Label@2.5.1)_
```powerfx
(15)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCheck` . **Y**  _(Label@2.5.1)_
```powerfx
(14)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Code
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Width**  _(Label@2.5.1)_
```powerfx
(249)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **X**  _(Label@2.5.1)_
```powerfx
(61)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseCode` . **Y**  _(Label@2.5.1)_
```powerfx
(8)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Height**  _(Label@2.5.1)_
```powerfx
(19)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Name
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Width**  _(Label@2.5.1)_
```powerfx
(249)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **X**  _(Label@2.5.1)_
```powerfx
(61)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseName` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(59)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,89,38,0.1)
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(ThisItem.Code in colPSelected.Code,RemoveIf(colPSelected,Code=ThisItem.Code),Collect(colPSelected,{Code:ThisItem.Code}))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pWarehouseGallery/pWarehouseHit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Height**  _(Label@2.5.1)_
```powerfx
(72)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Size**  _(Label@2.5.1)_
```powerfx
13*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Text**  _(Label@2.5.1)_
```powerfx
"Агуулахын жагсаалт алга. Онлайн үед шинэчилнэ үү."
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(colPLocations)
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Width**  _(Label@2.5.1)_
```powerfx
(316)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **X**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pNoWarehouses` . **Y**  _(Label@2.5.1)_
```powerfx
(388)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(36)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(pReloadWarehouses)
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Жагсаалт шинэчлэх"
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pRefreshLocations` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(646)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,If(varPCompleted,"profile","welcome"))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(55)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pSetupBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(718)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*((ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(IsEmpty(colPSelected),Notify("Дор хаяж нэг агуулах сонгоно уу.",NotificationType.Warning),Set(varPView,"ready"))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Үргэлжлүүлэх · " & CountRows(colPSelected) & " агуулах →"
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(262)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(83)*((ScrAccess.Width/366))
```

### `ScrAccess/pWarehouseSetup/pSetupNext` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(718)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pReady` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrAccess/pReady` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*((ScrAccess.Height/790))
```

### `ScrAccess/pReady` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varPView="ready"
```

### `ScrAccess/pReady` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*((ScrAccess.Width/366))
```

### `ScrAccess/pReady` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*((ScrAccess.Width/366)))/2
```

### `ScrAccess/pReady` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*((ScrAccess.Height/790)))/2
```

### `ScrAccess/pReady/pProgress30` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pReady/pProgress30` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pProgress30` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(3)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress30` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress30` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress30` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress30` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress30` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pProgress30` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pProgress30` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(60)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress31` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pReady/pProgress31` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pProgress31` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(3)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress31` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress31` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress31` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress31` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress31` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pProgress31` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(131)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pProgress31` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(60)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress32` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pReady/pProgress32` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pProgress32` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(3)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress32` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress32` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress32` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress32` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
1*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pProgress32` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(104)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pProgress32` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(241)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pProgress32` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(60)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pStep3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pReady/pStep3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pStep3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pStep3` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pReady/pStep3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pStep3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReady/pStep3` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pReady/pStep3` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pStep3` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pStep3` . **Text**  _(Label@2.5.1)_
```powerfx
"АЛХАМ 3 / 3"
```

### `ScrAccess/pReady/pStep3` . **Width**  _(Label@2.5.1)_
```powerfx
(320)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pStep3` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pStep3` . **Y**  _(Label@2.5.1)_
```powerfx
(84)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pReady/pReadyTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pReady/pReadyTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReady/pReadyTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pReady/pReadyTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(55)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyTitle` . **Size**  _(Label@2.5.1)_
```powerfx
26*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyTitle` . **Text**  _(Label@2.5.1)_
```powerfx
Switch(varHomeLanguage,"EN","Ready to start","中文","准备开始","Ажиллахад бэлэн")
```

### `ScrAccess/pReady/pReadyTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyTitle` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(127)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pReady/pReadyCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pReady/pReadyCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(168)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(212)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyUser` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pReady/pReadyUser` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyUser` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyUser` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pReady/pReadyUser` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyUser` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReady/pReadyUser` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pReady/pReadyUser` . **Height**  _(Label@2.5.1)_
```powerfx
(61)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyUser` . **Size**  _(Label@2.5.1)_
```powerfx
13*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyUser` . **Text**  _(Label@2.5.1)_
```powerfx
User().FullName & Char(10) & User().Email
```

### `ScrAccess/pReady/pReadyUser` . **Width**  _(Label@2.5.1)_
```powerfx
(288)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyUser` . **X**  _(Label@2.5.1)_
```powerfx
(39)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyUser` . **Y**  _(Label@2.5.1)_
```powerfx
(229)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyWarehouses` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pReady/pReadyWarehouses` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyWarehouses` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pReadyWarehouses` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pReady/pReadyWarehouses` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyWarehouses` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReady/pReadyWarehouses` . **Height**  _(Label@2.5.1)_
```powerfx
(53)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyWarehouses` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyWarehouses` . **Text**  _(Label@2.5.1)_
```powerfx
Concat(colPSelected,Code,", ")
```

### `ScrAccess/pReady/pReadyWarehouses` . **Width**  _(Label@2.5.1)_
```powerfx
(288)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyWarehouses` . **X**  _(Label@2.5.1)_
```powerfx
(39)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyWarehouses` . **Y**  _(Label@2.5.1)_
```powerfx
(304)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyNotice` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pReady/pReadyNotice` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyNotice` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pReady/pReadyNotice` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pReady/pReadyNotice` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyNotice` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReady/pReadyNotice` . **Height**  _(Label@2.5.1)_
```powerfx
(109)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyNotice` . **Size**  _(Label@2.5.1)_
```powerfx
13*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyNotice` . **Text**  _(Label@2.5.1)_
```powerfx
"Бараа, үлдэгдэл, тавиур онлайн үед автоматаар татагдана. Оффлайн үед хамгийн сүүлд хадгалсан өгөгдлийг ашиглана."
```

### `ScrAccess/pReady/pReadyNotice` . **Width**  _(Label@2.5.1)_
```powerfx
(316)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyNotice` . **X**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyNotice` . **Y**  _(Label@2.5.1)_
```powerfx
(411)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pReady/pReadyBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pReady/pReadyBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pReady/pReadyBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReady/pReadyBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pReady/pReadyBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pReady/pReadyBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"warehouses")
```

### `ScrAccess/pReady/pReadyBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pReady/pReadyBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pReady/pReadyBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pReady/pReadyBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pReadyBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrAccess/pReady/pReadyBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(55)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(718)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyFinish` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pReady/pReadyFinish` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyFinish` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pReady/pReadyFinish` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pReadyFinish` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pReady/pReadyFinish` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pReady/pReadyFinish` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*((ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyFinish` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pReady/pReadyFinish` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyFinish` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pReady/pReadyFinish` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),WarehouseJSON),"[]")<>JSON(colPSelected,JSONFormat.Compact),Set(varPCacheReady,false);Set(varPCacheSavedAt,""));Set(varPCompleted,true);Set(varLocationCode,Blank());Set(varWLocation,Blank());With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Агуулахын тохиргоо хадгалсан",Entity:"Warehouses",BeforeValue:"",AfterValue:Concat(colPSelected,Code,", "),Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true);Navigate('нүүр',ScreenTransition.Fade)
```

### `ScrAccess/pReady/pReadyFinish` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pReady/pReadyFinish` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pReady/pReadyFinish` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pReady/pReadyFinish` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pReady/pReadyFinish` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pReady/pReadyFinish` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyFinish` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyFinish` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyFinish` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyFinish` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pReady/pReadyFinish` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Switch(varHomeLanguage,"EN","Get started →","中文","开始 →","Эхлэх →")
```

### `ScrAccess/pReady/pReadyFinish` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(262)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyFinish` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(83)*((ScrAccess.Width/366))
```

### `ScrAccess/pReady/pReadyFinish` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(718)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),ColorValue("#F5F4F1")
)
```

### `ScrAccess/pProfile` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varPView="profile"
```

### `ScrAccess/pProfile` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*((ScrAccess.Width/366)))/2
```

### `ScrAccess/pProfile` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*((ScrAccess.Height/790)))/2
```

### `ScrAccess/pProfile/pprofileClock` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,true,If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
)
```

### `ScrAccess/pProfile/pprofileClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pprofileClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pprofileClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pprofileClock` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,RGBA(0,0,0,0)
)
```

### `ScrAccess/pProfile/pprofileClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pprofileClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pprofileClock` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(108)*App.Height/720,(20)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pprofileClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileClock` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"",Text(Now(),"hh:mm")
)
```

### `ScrAccess/pProfile/pprofileClock` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(332)*App.Width/360,(85)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pprofileClock` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,(25)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pprofileClock` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(71)*App.Height/720,(22)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pprofileStatus` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pprofileStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pprofileStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pprofileStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#85DFAC")
```

### `ScrAccess/pProfile/pprofileStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pprofileStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pprofileStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pprofileStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `ScrAccess/pProfile/pprofileStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pprofileStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pprofileStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pprofileBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pprofileBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pprofileBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pprofileBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pProfile/pprofileBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pprofileBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pprofileBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pprofileBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pprofileBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pprofileBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр',ScreenTransition.Fade)
```

### `ScrAccess/pProfile/pprofileBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pprofileBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pprofileBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pprofileBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pprofileBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pprofileBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrAccess/pProfile/pprofileBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pprofileBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pprofileBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pprofileTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pprofileTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pprofileTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pprofileTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pprofileTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pprofileTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pprofileTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Semibold
)
```

### `ScrAccess/pProfile/pprofileTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(48)*App.Height/720,(38)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pprofileTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Min(App.Width/360,App.Height/720),20*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pprofileTitle` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Би","Профайл"
)
```

### `ScrAccess/pProfile/pprofileTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(220)*App.Width/360,(275)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pprofileTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,(66)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pprofileTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(10)*App.Height/720,(51)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pAvatar` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pAvatar` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#994019"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pAvatar` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pAvatar` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#FFF0E5"),ColorValue("#ED5F1C")
)
```

### `ScrAccess/pProfile/pAvatar` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pAvatar` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pAvatar` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(50)*App.Height/720,(69)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pAvatar` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pAvatar` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pAvatar` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pAvatar` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pAvatar` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pAvatar` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pAvatar` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pAvatar` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pAvatar` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pAvatar` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pAvatar` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pAvatar` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pAvatar` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(App.Width/360,App.Height/720),24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pAvatar` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Upper(Left(User().FullName,2))
```

### `ScrAccess/pProfile/pAvatar` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(50)*App.Width/360,(69)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pAvatar` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(29)*App.Width/360,(21)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pAvatar` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(98)*App.Height/720,(106)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pUserName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pUserName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pUserName` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pUserName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pUserName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pUserName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pUserName` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pProfile/pUserName` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(32)*App.Height/720,(33)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pUserName` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(App.Width/360,App.Height/720),21*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pUserName` . **Text**  _(Label@2.5.1)_
```powerfx
User().FullName
```

### `ScrAccess/pProfile/pUserName` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(240)*App.Width/360,(240)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pUserName` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(89)*App.Width/360,(104)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pUserName` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(83)*App.Height/720,(108)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pUserEmail` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pUserEmail` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pUserEmail` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#66615B")
)
```

### `ScrAccess/pProfile/pUserEmail` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pUserEmail` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pUserEmail` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pUserEmail` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(25)*App.Height/720,(23)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pUserEmail` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pUserEmail` . **Text**  _(Label@2.5.1)_
```powerfx
User().Email
```

### `ScrAccess/pProfile/pUserEmail` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(242)*App.Width/360,(240)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pUserEmail` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(89)*App.Width/360,(104)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pUserEmail` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(113)*App.Height/720,(147)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pRoleStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pRoleStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pRoleStatus` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#ED5F1C")
)
```

### `ScrAccess/pProfile/pRoleStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#FFF0E5"),RGBA(0,0,0,0)
)
```

### `ScrAccess/pProfile/pRoleStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pRoleStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pRoleStatus` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(28)*App.Height/720,(23)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pRoleStatus` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(App.Width/360,App.Height/720),10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pRoleStatus` . **Text**  _(Label@2.5.1)_
```powerfx
If(Lower(User().Email)="od.u@tme.mn","Админ",pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()),Switch(pgAccess.Role.Value,"Counter","Нярав","Supervisor","Ахлагч","Auditor","Аудитор","Admin","Админ","Хуудасны эрхтэй"),"Эрх холбогдоогүй") & If(App.Width<First(App.SizeBreakpoints).Value && !IsEmpty(Filter(colPSelected,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(Code) & "|") in pgAccess.LocationCode))),"  ·  " & Concat(Filter(colPSelected,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(Code) & "|") in pgAccess.LocationCode)),Code,", "),"")
```

### `ScrAccess/pProfile/pRoleStatus` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(230)*App.Width/360,(240)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pRoleStatus` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(89)*App.Width/360,(104)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pRoleStatus` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(140)*App.Height/720,(174)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pStatCard0` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatCard0` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pStatCard0` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#FFFFFF")
)
```

### `ScrAccess/pProfile/pStatCard0` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(108)*App.Height/720,(66)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pStatCard0` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard0` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard0` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard0` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard0` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(332)*App.Width/360,(106)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pStatCard0` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,(17)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pStatCard0` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(71)*App.Height/720,(215)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pStatValue0` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatValue0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pStatValue0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatValue0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pStatValue0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pStatValue0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatValue0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pStatValue0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pProfile/pStatValue0` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue0` . **Size**  _(Label@2.5.1)_
```powerfx
19*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue0` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(Filter(colOfflineInventory,!Coalesce(Archived,false) && OwnerEmail=varCountOwner && CountDate>=Date(Year(Today()),Month(Today()),1)))
```

### `ScrAccess/pProfile/pStatValue0` . **Width**  _(Label@2.5.1)_
```powerfx
(81)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatValue0` . **X**  _(Label@2.5.1)_
```powerfx
(30)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatValue0` . **Y**  _(Label@2.5.1)_
```powerfx
(226)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel0` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatLabel0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pStatLabel0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatLabel0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pProfile/pStatLabel0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pStatLabel0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatLabel0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pStatLabel0` . **Height**  _(Label@2.5.1)_
```powerfx
(17)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel0` . **Size**  _(Label@2.5.1)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel0` . **Text**  _(Label@2.5.1)_
```powerfx
"энэ сард тоолсон"
```

### `ScrAccess/pProfile/pStatLabel0` . **Width**  _(Label@2.5.1)_
```powerfx
(82)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatLabel0` . **X**  _(Label@2.5.1)_
```powerfx
(30)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatLabel0` . **Y**  _(Label@2.5.1)_
```powerfx
(256)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard1` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatCard1` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pStatCard1` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pProfile/pStatCard1` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(66)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard1` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard1` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard1` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard1` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard1` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(106)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatCard1` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(130)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatCard1` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(215)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue1` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatValue1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pStatValue1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatValue1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pStatValue1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pStatValue1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatValue1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pStatValue1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pProfile/pStatValue1` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue1` . **Size**  _(Label@2.5.1)_
```powerfx
19*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue1` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced))
```

### `ScrAccess/pProfile/pStatValue1` . **Width**  _(Label@2.5.1)_
```powerfx
(81)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatValue1` . **X**  _(Label@2.5.1)_
```powerfx
(143)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatValue1` . **Y**  _(Label@2.5.1)_
```powerfx
(226)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel1` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatLabel1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pStatLabel1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatLabel1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pProfile/pStatLabel1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pStatLabel1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatLabel1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pStatLabel1` . **Height**  _(Label@2.5.1)_
```powerfx
(17)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel1` . **Size**  _(Label@2.5.1)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel1` . **Text**  _(Label@2.5.1)_
```powerfx
"илгээгээгүй"
```

### `ScrAccess/pProfile/pStatLabel1` . **Width**  _(Label@2.5.1)_
```powerfx
(82)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatLabel1` . **X**  _(Label@2.5.1)_
```powerfx
(143)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatLabel1` . **Y**  _(Label@2.5.1)_
```powerfx
(256)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard2` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatCard2` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pStatCard2` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pProfile/pStatCard2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(66)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatCard2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(106)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatCard2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(243)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatCard2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(215)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue2` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatValue2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pStatValue2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatValue2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pStatValue2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pStatValue2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatValue2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pStatValue2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pProfile/pStatValue2` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue2` . **Size**  _(Label@2.5.1)_
```powerfx
19*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatValue2` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(colPSelected)
```

### `ScrAccess/pProfile/pStatValue2` . **Width**  _(Label@2.5.1)_
```powerfx
(81)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatValue2` . **X**  _(Label@2.5.1)_
```powerfx
(256)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatValue2` . **Y**  _(Label@2.5.1)_
```powerfx
(226)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel2` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pStatLabel2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pStatLabel2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatLabel2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pProfile/pStatLabel2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pStatLabel2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pStatLabel2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pStatLabel2` . **Height**  _(Label@2.5.1)_
```powerfx
(17)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel2` . **Size**  _(Label@2.5.1)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pStatLabel2` . **Text**  _(Label@2.5.1)_
```powerfx
"агуулах"
```

### `ScrAccess/pProfile/pStatLabel2` . **Width**  _(Label@2.5.1)_
```powerfx
(82)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatLabel2` . **X**  _(Label@2.5.1)_
```powerfx
(256)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pStatLabel2` . **Y**  _(Label@2.5.1)_
```powerfx
(256)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pSettingsCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pSettingsCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#FFFFFF")
)
```

### `ScrAccess/pProfile/pSettingsCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(141)*App.Height/720,(177)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pSettingsCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pSettingsCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pSettingsCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pSettingsCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pSettingsCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(332)*App.Width/360,(332)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pSettingsCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,(17)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pSettingsCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(193)*App.Height/720,(310)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pLanguageCaption` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pLanguageCaption` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pLanguageCaption` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pLanguageCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,RGBA(0,0,0,0)
)
```

### `ScrAccess/pProfile/pLanguageCaption` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pLanguageCaption` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pLanguageCaption` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pProfile/pLanguageCaption` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(40)*App.Height/720,(28)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pLanguageCaption` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(App.Width/360,App.Height/720),12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pLanguageCaption` . **Text**  _(Label@2.5.1)_
```powerfx
Switch(varHomeLanguage,"EN","Language","中文","语言","Хэл")
```

### `ScrAccess/pProfile/pLanguageCaption` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(110)*App.Width/360,(112)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pLanguageCaption` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(24)*App.Width/360,(31)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pLanguageCaption` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(242)*App.Height/720,(324)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pProfileLang0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),If(varHomeLanguage="MN",ColorValue("#F5F4F1"),ColorValue("#66615B"))
)
```

### `ScrAccess/pProfile/pProfileLang0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pProfileLang0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(varHomeLanguage="MN",ColorValue("#FFF0E5"),ColorValue("#F5F4F1")),If(varHomeLanguage="MN",ColorValue("#202225"),ColorValue("#FFFFFF"))
)
```

### `ScrAccess/pProfile/pProfileLang0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pProfileLang0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(31)*App.Height/720,(27)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pProfileLang0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileLang0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pProfileLang0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPOldLanguage,varHomeLanguage);Set(varHomeLanguage,"MN");With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);If(varPOldLanguage<>varHomeLanguage,Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Хэл өөрчилсөн",Entity:"Language",BeforeValue:varPOldLanguage,AfterValue:varHomeLanguage,Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true))
```

### `ScrAccess/pProfile/pProfileLang0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pProfileLang0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileLang0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pProfileLang0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"МН"
```

### `ScrAccess/pProfile/pProfileLang0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(44)*App.Width/360,(39)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileLang0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(195)*App.Width/360,(216)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileLang0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(247)*App.Height/720,(324)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pProfileLang1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),If(varHomeLanguage="EN",ColorValue("#F5F4F1"),ColorValue("#66615B"))
)
```

### `ScrAccess/pProfile/pProfileLang1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pProfileLang1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(varHomeLanguage="EN",ColorValue("#FFF0E5"),ColorValue("#F5F4F1")),If(varHomeLanguage="EN",ColorValue("#202225"),ColorValue("#FFFFFF"))
)
```

### `ScrAccess/pProfile/pProfileLang1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pProfileLang1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(31)*App.Height/720,(27)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pProfileLang1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileLang1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pProfileLang1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPOldLanguage,varHomeLanguage);Set(varHomeLanguage,"EN");With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);If(varPOldLanguage<>varHomeLanguage,Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Хэл өөрчилсөн",Entity:"Language",BeforeValue:varPOldLanguage,AfterValue:varHomeLanguage,Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true))
```

### `ScrAccess/pProfile/pProfileLang1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pProfileLang1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileLang1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pProfileLang1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"EN"
```

### `ScrAccess/pProfile/pProfileLang1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(44)*App.Width/360,(39)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileLang1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(241)*App.Width/360,(258)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileLang1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(247)*App.Height/720,(324)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pProfileLang2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),If(varHomeLanguage="中文",ColorValue("#F5F4F1"),ColorValue("#66615B"))
)
```

### `ScrAccess/pProfile/pProfileLang2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pProfileLang2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(varHomeLanguage="中文",ColorValue("#FFF0E5"),ColorValue("#F5F4F1")),If(varHomeLanguage="中文",ColorValue("#202225"),ColorValue("#FFFFFF"))
)
```

### `ScrAccess/pProfile/pProfileLang2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pProfileLang2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(31)*App.Height/720,(27)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pProfileLang2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileLang2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pProfileLang2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPOldLanguage,varHomeLanguage);Set(varHomeLanguage,"中文");With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);If(varPOldLanguage<>varHomeLanguage,Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Хэл өөрчилсөн",Entity:"Language",BeforeValue:varPOldLanguage,AfterValue:varHomeLanguage,Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true))
```

### `ScrAccess/pProfile/pProfileLang2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileLang2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pProfileLang2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileLang2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pProfileLang2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileLang2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileLang2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"中文"
```

### `ScrAccess/pProfile/pProfileLang2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(44)*App.Width/360,(39)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileLang2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(287)*App.Width/360,(300)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileLang2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(247)*App.Height/720,(324)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Left,Align.Center
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pMyWarehouses` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pMyWarehouses` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#FFFFFF")
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pMyWarehouses` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pMyWarehouses` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(43)*App.Height/720,(37)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pMyWarehouses` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pMyWarehouses` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pMyWarehouses` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"warehouses")
```

### `ScrAccess/pProfile/pMyWarehouses` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pMyWarehouses` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pMyWarehouses` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pMyWarehouses` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pMyWarehouses` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pMyWarehouses` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pMyWarehouses` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pMyWarehouses` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pMyWarehouses` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pMyWarehouses` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(App.Width/360,App.Height/720),11*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Миний агуулах     " & Coalesce(Concat(Filter(colPSelected,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(Code) & "|") in pgAccess.LocationCode)),Code,", "),"Сонгох") & "  ›","Миний агуулах    " & CountRows(colPSelected) & "  ›"
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(316)*App.Width/360,(308)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(22)*App.Width/360,(29)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pMyWarehouses` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(196)*App.Height/720,(364)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pPrinter` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Left,Align.Center
)
```

### `ScrAccess/pProfile/pPrinter` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pPrinter` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#66615B")
)
```

### `ScrAccess/pProfile/pPrinter` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pPrinter` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#FFFFFF")
)
```

### `ScrAccess/pProfile/pPrinter` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pPrinter` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pPrinter` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(42)*App.Height/720,(32)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pPrinter` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pPrinter` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pPrinter` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pPrinter` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Notify("Принтерийн холболт одоогоор бэлэн биш.",NotificationType.Information)
```

### `ScrAccess/pProfile/pPrinter` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pPrinter` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pPrinter` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pPrinter` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pPrinter` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pPrinter` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pPrinter` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pPrinter` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pPrinter` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pPrinter` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(App.Width/360,App.Height/720),10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pPrinter` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Баркод принтер · холбогдоогүй"
```

### `ScrAccess/pProfile/pPrinter` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(316)*App.Width/360,(308)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pPrinter` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(22)*App.Width/360,(29)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pPrinter` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(286)*App.Height/720,(406)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pReminders` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pReminders` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pReminders` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pReminders` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pReminders` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pProfile/pReminders` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pReminders` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pReminders` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(32)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pReminders` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pReminders` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pReminders` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pReminders` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPRemind,!varPRemind);With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Синк сануулга өөрчилсөн",Entity:"Remind",BeforeValue:"",AfterValue:Text(varPRemind),Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true)
```

### `ScrAccess/pProfile/pReminders` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pReminders` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pReminders` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pReminders` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pReminders` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pReminders` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pReminders` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pReminders` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pReminders` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pReminders` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pReminders` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Синк сануулга     " & If(varPRemind,"Асаалттай","Унтраалттай")
```

### `ScrAccess/pProfile/pReminders` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(308)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pReminders` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(29)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pReminders` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(445)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOfflineCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pOfflineCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#FFFFFF")
)
```

### `ScrAccess/pProfile/pOfflineCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(159)*App.Height/720,(163)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pOfflineCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOfflineCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOfflineCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOfflineCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOfflineCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(332)*App.Width/360,(332)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pOfflineCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,(17)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pOfflineCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(382)*App.Height/720,(504)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pOfflineTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pOfflineTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pOfflineTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#66615B")
)
```

### `ScrAccess/pProfile/pOfflineTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pOfflineTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pOfflineTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pOfflineTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(32)*App.Height/720,(23)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pOfflineTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pOfflineTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"ОФФЛАЙН ӨГӨГДӨЛ"
```

### `ScrAccess/pProfile/pOfflineTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(325)*App.Width/360,(306)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pOfflineTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(15)*App.Width/360,(31)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pOfflineTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(345)*App.Height/720,(519)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pOfflineCounts` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pOfflineCounts` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pOfflineCounts` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pOfflineCounts` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pOfflineCounts` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pOfflineCounts` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pOfflineCounts` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pOfflineCounts` . **Height**  _(Label@2.5.1)_
```powerfx
(43)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOfflineCounts` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOfflineCounts` . **Text**  _(Label@2.5.1)_
```powerfx
"Бараа " & CountRows(colOfflineItems) & " · Үлдэгдэл " & CountRows(colOfflineStock) & " · Тооллого " & CountRows(Filter(colOfflineInventory,!Coalesce(Archived,false) && OwnerEmail=varCountOwner))
```

### `ScrAccess/pProfile/pOfflineCounts` . **Width**  _(Label@2.5.1)_
```powerfx
(306)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pOfflineCounts` . **X**  _(Label@2.5.1)_
```powerfx
(31)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pOfflineCounts` . **Y**  _(Label@2.5.1)_
```powerfx
(550)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pCacheSave` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pCacheSave` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pCacheSave` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pCacheSave` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPBusy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrAccess/pProfile/pCacheSave` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#ED5F1C")
)
```

### `ScrAccess/pProfile/pCacheSave` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pCacheSave` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pCacheSave` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(38)*App.Height/720,(40)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pCacheSave` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pCacheSave` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pCacheSave` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pCacheSave` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(IsEmpty(colPSelected),Notify("Эхлээд агуулахаа сонгоно уу.",NotificationType.Warning),IsEmpty(colOfflineItems),Notify("Барааны мэдээлэл автоматаар татагдаж байна. Интернет холболт болон мэдээллийн төлөвийг шалгана уу.",NotificationType.Warning),
Set(varPBusy,true);Set(varPCacheReady,false);
ClearCollect(colPScopedStock,Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode) && locationCode in colPSelected.Code));
ClearCollect(colPScopedItems,Filter(colOfflineItems,number in colPScopedStock.itemNo));
ClearCollect(colPScopedBins,Filter(colOfflineBins,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode) && locationCode in colPSelected.Code));
If(IsEmpty(colPScopedItems),Notify("Сонгосон агуулахын мэдээлэл одоогоор алга. Автомат шинэчлэлт дуусахыг хүлээнэ үү.",NotificationType.Warning),IfError(SaveData(colPScopedStock,"PStockV8_" & varPCacheKey);SaveData(colPScopedItems,"PItemsV8_" & varPCacheKey);SaveData(colPScopedBins,"PBinsV8_" & varPCacheKey);Set(varPCacheReady,true);Set(varPCacheSavedAt,Text(Now(),"yyyy.mm.dd hh:mm"));With({r:{OwnerEmail:Lower(User().Email),Language:varHomeLanguage,Completed:Coalesce(varPCompleted,false),WarehouseJSON:JSON(colPSelected,JSONFormat.Compact),CacheReady:Coalesce(varPCacheReady,false),CacheSavedAt:Coalesce(varPCacheSavedAt,""),Remind:Coalesce(varPRemind,true)}},If(IsBlank(LookUp(colPPrefs,OwnerEmail=Lower(User().Email),OwnerEmail)),Collect(colPPrefs,r),Patch(colPPrefs,LookUp(colPPrefs,OwnerEmail=Lower(User().Email)),r)));
IfError(SaveData(colPPrefs,"AccessPrefsV8"),Notify("Тохиргоо зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Warning); false, true);Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Систем",Action:"Оффлайн snapshot хадгалсан",Entity:"Cache",BeforeValue:"",AfterValue:Text(CountRows(colPScopedItems)) & " бараа / " & CountRows(colPScopedStock) & " үлдэгдэл",Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true);Notify("Сонгосон агуулахын өгөгдөл төхөөрөмжид хадгалагдлаа.",NotificationType.Success),Notify("Оффлайн хадгалалт амжилтгүй: " & FirstError.Message,NotificationType.Error)));Set(varPBusy,false))
```

### `ScrAccess/pProfile/pCacheSave` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pCacheSave` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pCacheSave` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pCacheSave` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pCacheSave` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pCacheSave` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pCacheSave` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pCacheSave` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pCacheSave` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pCacheSave` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pCacheSave` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Оффлайн хадгалах"
```

### `ScrAccess/pProfile/pCacheSave` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(160)*App.Width/360,(169)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pCacheSave` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,(29)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pCacheSave` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(596)*App.Height/720,(608)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pOpenSync` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pOpenSync` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pOpenSync` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pOpenSync` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pOpenSync` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pProfile/pOpenSync` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pOpenSync` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pOpenSync` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOpenSync` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pOpenSync` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pOpenSync` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pOpenSync` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Notify(If(varStartupSyncRunning,"Мэдээлэл автоматаар шинэчлэгдэж байна…",!Connection.Connected,"Оффлайн — хадгалсан мэдээлэл ашиглаж байна.",varAutoItemsError || varAutoStockError || varAutoBinsError,"Зарим мэдээлэл татагдсангүй. Хадгалсан мэдээлэл хэвээр; нүүр рүү ороход дахин оролдоно.","Автомат шинэчлэлт: " & Text(varAutoDataChecked,"mm.dd hh:mm")) & " | Бараа " & Text(CountRows(colOfflineItems)) & ", үлдэгдэл " & Text(CountRows(colOfflineStock)) & ", тавиур " & Text(CountRows(colOfflineBins)),NotificationType.Information)
```

### `ScrAccess/pProfile/pOpenSync` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pOpenSync` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pOpenSync` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pOpenSync` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pOpenSync` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pOpenSync` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOpenSync` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOpenSync` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOpenSync` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOpenSync` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pOpenSync` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэдээллийн төлөв"
```

### `ScrAccess/pProfile/pOpenSync` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(131)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pOpenSync` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(206)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pOpenSync` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(608)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Visible**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,true
)
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Height**  _(Label@2.5.1)_
```powerfx
(29)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Size**  _(Label@2.5.1)_
```powerfx
Max(11,11*Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Text**  _(Label@2.5.1)_
```powerfx
If(varStartupSyncRunning,"Мэдээллийг автоматаар шинэчилж байна…",!Connection.Connected,"Оффлайн · хадгалсан өгөгдөл",varAutoItemsError || varAutoStockError || varAutoBinsError,"Зарим таталт амжилтгүй · өмнөх өгөгдөл хэвээр","Автомат шинэчлэлт · " & Text(varAutoDataChecked,"mm.dd hh:mm"))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Width**  _(Label@2.5.1)_
```powerfx
(316)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **X**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Width/366))
```

### `ScrAccess/pProfile/pAutoSyncInfo` . **Y**  _(Label@2.5.1)_
```powerfx
(677)*((ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileAudit` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Left,Align.Center
)
```

### `ScrAccess/pProfile/pProfileAudit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pProfileAudit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#AD4516"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pProfileAudit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pProfileAudit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),ColorValue("#FFFFFF")
)
```

### `ScrAccess/pProfile/pProfileAudit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pProfileAudit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pProfileAudit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(39)*App.Height/720,(48)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileAudit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pProfileAudit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileAudit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pProfileAudit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"audit")
```

### `ScrAccess/pProfile/pProfileAudit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileAudit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileAudit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pProfileAudit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileAudit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pProfileAudit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileAudit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileAudit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileAudit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileAudit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(App.Width/360,App.Height/720),10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileAudit` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Аудитын түүх"
```

### `ScrAccess/pProfile/pProfileAudit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(140)*App.Width/360,(130)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileAudit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,(17)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileAudit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(550)*App.Height/720,(726)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileExit` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Right,Align.Center
)
```

### `ScrAccess/pProfile/pProfileExit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pProfile/pProfileExit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#202225")
)
```

### `ScrAccess/pProfile/pProfileExit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pProfile/pProfileExit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),ColorValue("#321316")
)
```

### `ScrAccess/pProfile/pProfileExit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pProfile/pProfileExit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pProfile/pProfileExit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(39)*App.Height/720,(48)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileExit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pProfile/pProfileExit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileExit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pProfile/pProfileExit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPExitConfirm,true)
```

### `ScrAccess/pProfile/pProfileExit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileExit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pProfile/pProfileExit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pProfile/pProfileExit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pProfile/pProfileExit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pProfile/pProfileExit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileExit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileExit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileExit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pProfile/pProfileExit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(App.Width/360,App.Height/720),10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
)
```

### `ScrAccess/pProfile/pProfileExit` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гарах"
```

### `ScrAccess/pProfile/pProfileExit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(81)*App.Width/360,(60)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileExit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(264)*App.Width/360,(289)*((ScrAccess.Width/366))
)
```

### `ScrAccess/pProfile/pProfileExit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(550)*App.Height/720,(726)*((ScrAccess.Height/790))
)
```

### `ScrAccess/pAudit` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrAccess/pAudit` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varPView="audit"
```

### `ScrAccess/pAudit` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*((ScrAccess.Width/366)))/2
```

### `ScrAccess/pAudit` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*((ScrAccess.Height/790)))/2
```

### `ScrAccess/pAudit/pauditClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pauditClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pauditClock` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pauditClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pauditClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pauditClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pauditClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `ScrAccess/pAudit/pauditClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pauditStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pauditStatus` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#85DFAC")
```

### `ScrAccess/pAudit/pauditStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pauditStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pauditStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pauditStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `ScrAccess/pAudit/pauditStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit/pauditBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pauditBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pAudit/pauditBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pAudit/pauditBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pauditBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pauditBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pAudit/pauditBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pauditBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pAudit/pauditBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile")
```

### `ScrAccess/pAudit/pauditBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pauditBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pauditBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pAudit/pauditBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pauditBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pauditBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrAccess/pAudit/pauditBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pauditTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pauditTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pauditTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pauditTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pauditTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pauditTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pAudit/pauditTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pauditTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Аудитын түүх"
```

### `ScrAccess/pAudit/pauditTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pauditTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Height**  _(Label@2.5.1)_
```powerfx
(24)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Text**  _(Label@2.5.1)_
```powerfx
"Энэ төхөөрөмж · серверийн аудит биш"
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditDisclaimer` . **Y**  _(Label@2.5.1)_
```powerfx
(102)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit/pAuditFilter0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Бүгд",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pAudit/pAuditFilter0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pAudit/pAuditFilter0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Бүгд",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pAudit/pAuditFilter0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditFilter0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pAudit/pAuditFilter0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pAudit/pAuditFilter0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPAuditFilter,"Бүгд")
```

### `ScrAccess/pAudit/pAuditFilter0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pAudit/pAuditFilter0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditFilter0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бүгд"
```

### `ScrAccess/pAudit/pAuditFilter0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(63)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(142)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit/pAuditFilter1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Тооллого",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pAudit/pAuditFilter1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pAudit/pAuditFilter1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Тооллого",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pAudit/pAuditFilter1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditFilter1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pAudit/pAuditFilter1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pAudit/pAuditFilter1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPAuditFilter,"Тооллого")
```

### `ScrAccess/pAudit/pAuditFilter1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pAudit/pAuditFilter1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditFilter1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллого"
```

### `ScrAccess/pAudit/pAuditFilter1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(63)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(84)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(142)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit/pAuditFilter2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Агуулах",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pAudit/pAuditFilter2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pAudit/pAuditFilter2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Агуулах",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pAudit/pAuditFilter2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditFilter2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pAudit/pAuditFilter2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pAudit/pAuditFilter2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPAuditFilter,"Агуулах")
```

### `ScrAccess/pAudit/pAuditFilter2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pAudit/pAuditFilter2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditFilter2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrAccess/pAudit/pAuditFilter2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(63)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(151)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(142)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit/pAuditFilter3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Бараа",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pAudit/pAuditFilter3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pAudit/pAuditFilter3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Бараа",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pAudit/pAuditFilter3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditFilter3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pAudit/pAuditFilter3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pAudit/pAuditFilter3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPAuditFilter,"Бараа")
```

### `ScrAccess/pAudit/pAuditFilter3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pAudit/pAuditFilter3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditFilter3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараа"
```

### `ScrAccess/pAudit/pAuditFilter3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(63)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(218)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(142)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter4` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit/pAuditFilter4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Хэрэглэгч",ColorValue("#F5F4F1"),ColorValue("#66615B"))
```

### `ScrAccess/pAudit/pAuditFilter4` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pAudit/pAuditFilter4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varPAuditFilter="Хэрэглэгч",ColorValue("#202225"),ColorValue("#FFFFFF"))
```

### `ScrAccess/pAudit/pAuditFilter4` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter4` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditFilter4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter4` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pAudit/pAuditFilter4` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pAudit/pAuditFilter4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPAuditFilter,"Хэрэглэгч")
```

### `ScrAccess/pAudit/pAuditFilter4` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter4` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFilter4` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pAudit/pAuditFilter4` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFilter4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditFilter4` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter4` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter4` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter4` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFilter4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хэрэглэгч"
```

### `ScrAccess/pAudit/pAuditFilter4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(63)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(285)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFilter4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(142)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFrom` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrAccess/pAudit/pAuditFrom` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(If(Coalesce(varRptCustomDates,false),1,0))*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFrom` . **Color**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditFrom` . **DefaultDate**  _(Classic/DatePicker@2.6.0)_
```powerfx
DateAdd(Today(),-30,TimeUnit.Days)
```

### `ScrAccess/pAudit/pAuditFrom` . **Fill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pAudit/pAuditFrom` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFrom` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditFrom` . **Format**  _(Classic/DatePicker@2.6.0)_
```powerfx
"yyyy.mm.dd"
```

### `ScrAccess/pAudit/pAuditFrom` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
(37)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFrom` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pAudit/pAuditFrom` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrAccess/pAudit/pAuditFrom` . **InputTextPlaceholder**  _(Classic/DatePicker@2.6.0)_
```powerfx
"Огноо"
```

### `ScrAccess/pAudit/pAuditFrom` . **PaddingBottom**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFrom` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrAccess/pAudit/pAuditFrom` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrAccess/pAudit/pAuditFrom` . **PaddingTop**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditFrom` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditFrom` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
(161)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFrom` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
(17)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditFrom` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
(186)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditTo` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrAccess/pAudit/pAuditTo` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(If(Coalesce(varRptCustomDates,false),1,0))*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditTo` . **Color**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditTo` . **Fill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pAudit/pAuditTo` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditTo` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditTo` . **Format**  _(Classic/DatePicker@2.6.0)_
```powerfx
"yyyy.mm.dd"
```

### `ScrAccess/pAudit/pAuditTo` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
(37)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditTo` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pAudit/pAuditTo` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#2D7F50")
```

### `ScrAccess/pAudit/pAuditTo` . **InputTextPlaceholder**  _(Classic/DatePicker@2.6.0)_
```powerfx
"Огноо"
```

### `ScrAccess/pAudit/pAuditTo` . **PaddingBottom**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditTo` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrAccess/pAudit/pAuditTo` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrAccess/pAudit/pAuditTo` . **PaddingTop**  _(Classic/DatePicker@2.6.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditTo` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditTo` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
(161)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditTo` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
(188)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditTo` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
(186)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(413)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
SortByColumns(Filter(colPAudit,OwnerEmail=Lower(User().Email) && (varPAuditFilter="Бүгд" || Module=varPAuditFilter) && OccurredAt>=pAuditFrom.SelectedDate && OccurredAt<DateAdd(pAuditTo.SelectedDate,1,TimeUnit.Days)),"OccurredAt",SortOrder.Descending)
```

### `ScrAccess/pAudit/pAuditGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
96*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(244)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Text**  _(Label@2.5.1)_
```powerfx
"●"
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Width**  _(Label@2.5.1)_
```powerfx
(18)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **X**  _(Label@2.5.1)_
```powerfx
(7)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditDot` . **Y**  _(Label@2.5.1)_
```powerfx
(4)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Size**  _(Label@2.5.1)_
```powerfx
11*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.ActorName & " · " & ThisItem.Action
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Width**  _(Label@2.5.1)_
```powerfx
(287)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **X**  _(Label@2.5.1)_
```powerfx
(29)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditActor` . **Y**  _(Label@2.5.1)_
```powerfx
(4)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Size**  _(Label@2.5.1)_
```powerfx
8*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.OccurredAt,"mm.dd hh:mm")
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Width**  _(Label@2.5.1)_
```powerfx
(287)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **X**  _(Label@2.5.1)_
```powerfx
(29)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditTime` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Height**  _(Label@2.5.1)_
```powerfx
(33)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Entity & " · " & ThisItem.BeforeValue & If(!IsBlank(ThisItem.BeforeValue)," → ","") & ThisItem.AfterValue
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Width**  _(Label@2.5.1)_
```powerfx
(287)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **X**  _(Label@2.5.1)_
```powerfx
(29)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditGallery/pAuditChange` . **Y**  _(Label@2.5.1)_
```powerfx
(56)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pAudit/pAuditEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(83)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
13*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Сонгосон хугацаанд локал үйлдэл бүртгэгдээгүй."
```

### `ScrAccess/pAudit/pAuditEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(pAuditGallery.AllItems)
```

### `ScrAccess/pAudit/pAuditEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(312)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(27)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(347)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Text**  _(Label@2.5.1)_
```powerfx
If(varPAuditSaveError,"Зарим түүх зөвхөн санах ойд байна.","Зөвхөн энэ хувилбарт бүртгэсэн локал үйлдэл харагдана.")
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Width**  _(Label@2.5.1)_
```powerfx
(316)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **X**  _(Label@2.5.1)_
```powerfx
(25)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditSaveWarning` . **Y**  _(Label@2.5.1)_
```powerfx
(673)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditExport` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pAudit/pAuditExport` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrAccess/pAudit/pAuditExport` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pAudit/pAuditExport` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditExport` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pAudit/pAuditExport` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pAudit/pAuditExport` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(48)*((ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditExport` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pAudit/pAuditExport` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditExport` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pAudit/pAuditExport` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPExport,true)
```

### `ScrAccess/pAudit/pAuditExport` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditExport` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pAudit/pAuditExport` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pAudit/pAuditExport` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pAudit/pAuditExport` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pAudit/pAuditExport` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditExport` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditExport` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditExport` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditExport` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pAudit/pAuditExport` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэйлээр тайлан авах"
```

### `ScrAccess/pAudit/pAuditExport` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditExport` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*((ScrAccess.Width/366))
```

### `ScrAccess/pAudit/pAuditExport` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(726)*((ScrAccess.Height/790))
```

### `ScrAccess/pExportModal` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pExportModal` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pExportModal` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Height*0.90,440*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrAccess/pExportModal` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varPExport
```

### `ScrAccess/pExportModal` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width*0.92,680*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrAccess/pExportModal` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrAccess/pExportModal` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(App.Height-Self.Height)/2
```

### `ScrAccess/pExportModal/pExportTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pExportModal/pExportTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExportModal/pExportTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pExportTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pExportModal/pExportTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExportModal/pExportTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExportModal/pExportTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pExportModal/pExportTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.14
```

### `ScrAccess/pExportModal/pExportTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/24,Parent.Height/17)
```

### `ScrAccess/pExportModal/pExportTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Локал аудитын тайлан"
```

### `ScrAccess/pExportModal/pExportTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrAccess/pExportModal/pExportTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrAccess/pExportModal/pExportTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.05
```

### `ScrAccess/pExportModal/pAuditRecipient` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
User().Email
```

### `ScrAccess/pExportModal/pAuditRecipient` . **DisplayMode**  _(Classic/TextInput@2.3.2)_
```powerfx
DisplayMode.View
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pExportModal/pAuditRecipient` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Height*0.13
```

### `ScrAccess/pExportModal/pAuditRecipient` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Хүлээн авагч@tme.mn"
```

### `ScrAccess/pExportModal/pAuditRecipient` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pExportModal/pAuditRecipient` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ScrAccess/pExportModal/pAuditRecipient` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExportModal/pAuditRecipient` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*((ScrAccess.Width/366))
```

### `ScrAccess/pExportModal/pAuditRecipient` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `ScrAccess/pExportModal/pAuditRecipient` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Width*0.88
```

### `ScrAccess/pExportModal/pAuditRecipient` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Width*0.06
```

### `ScrAccess/pExportModal/pAuditRecipient` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Height*0.24
```

### `ScrAccess/pExportModal/pExportHelp` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pExportModal/pExportHelp` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExportModal/pExportHelp` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pExportModal/pExportHelp` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pExportModal/pExportHelp` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExportModal/pExportHelp` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExportModal/pExportHelp` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.25
```

### `ScrAccess/pExportModal/pExportHelp` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `ScrAccess/pExportModal/pExportHelp` . **Text**  _(Label@2.5.1)_
```powerfx
"Хураангуй мэйлд үлдэж, шүүсэн үйлдлүүд CSV хавсралтаар очно."
```

### `ScrAccess/pExportModal/pExportHelp` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrAccess/pExportModal/pExportHelp` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrAccess/pExportModal/pExportHelp` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.42
```

### `ScrAccess/pExportModal/pExportCancel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pExportModal/pExportCancel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pExportCancel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pExportModal/pExportCancel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pExportModal/pExportCancel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExportModal/pExportCancel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExportModal/pExportCancel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrAccess/pExportModal/pExportCancel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pExportModal/pExportCancel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pExportCancel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pExportModal/pExportCancel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPExport,false)
```

### `ScrAccess/pExportModal/pExportCancel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExportModal/pExportCancel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExportModal/pExportCancel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pExportModal/pExportCancel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pExportCancel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pExportModal/pExportCancel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportCancel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportCancel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportCancel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportCancel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrAccess/pExportModal/pExportCancel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Болих"
```

### `ScrAccess/pExportModal/pExportCancel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.29
```

### `ScrAccess/pExportModal/pExportCancel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.06
```

### `ScrAccess/pExportModal/pExportCancel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrAccess/pExportModal/pExportSend` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pExportModal/pExportSend` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pExportSend` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pExportModal/pExportSend` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPBusy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrAccess/pExportModal/pExportSend` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pExportModal/pExportSend` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExportModal/pExportSend` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExportModal/pExportSend` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrAccess/pExportModal/pExportSend` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pExportModal/pExportSend` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pExportSend` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pExportModal/pExportSend` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(varPBusy,Notify("Тайлан илгээж байна…",NotificationType.Information),!Connection.Connected,Notify("Интернет холболт алга.",NotificationType.Warning),With({_rows:Filter(colPAudit,OwnerEmail=Lower(User().Email) && (varPAuditFilter="Бүгд" || Module=varPAuditFilter) && OccurredAt>=pAuditFrom.SelectedDate && OccurredAt<DateAdd(pAuditTo.SelectedDate,1,TimeUnit.Days))},If(IsEmpty(_rows),Notify("Илгээх түүх алга.",NotificationType.Warning),Set(varPBusy,true);IfError(PA_ExportInventoryCSV.Run(JSON(ForAll(_rows As r,{'Огноо':Text(r.OccurredAt,"yyyy-mm-dd hh:mm:ss"),'Хэрэглэгч':With({s:Coalesce(r.ActorName,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Модуль':With({s:Coalesce(r.Module,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Үйлдэл':With({s:Coalesce(r.Action,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Бүртгэл':With({s:Coalesce(r.Entity,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Өмнө':With({s:Coalesce(r.BeforeValue,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Дараа':With({s:Coalesce(r.AfterValue,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s))}),JSONFormat.Compact),User().Email,"[CSV2] Локал аудитын түүх " & Text(pAuditFrom.SelectedDate,"yyyy-mm-dd") & " - " & Text(pAuditTo.SelectedDate,"yyyy-mm-dd"),"<h2>Локал аудитын түүх</h2><p>Хэрэглэгч: " & Substitute(Substitute(Substitute(Coalesce(User().FullName,""),"&","&amp;"),"<","&lt;"),">","&gt;") & " · " & User().Email & "</p><p>Хуудас: Профайл · Аудитын түүх</p><p>Хугацаа: " & Text(pAuditFrom.SelectedDate,"yyyy-mm-dd") & " — " & Text(pAuditTo.SelectedDate,"yyyy-mm-dd") & "</p><p>Шүүлт: " & Substitute(Substitute(Substitute(Coalesce(varPAuditFilter,""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</p><p>Нийт мөр: " & CountRows(_rows) & "</p><p>Энэ нь төхөөрөмжийн локал үйлдлийн түүх. Дэлгэрэнгүй CSV хавсралтад бий.</p>"),Notify("Илгээхэд алдаа: " & FirstError.Message,NotificationType.Error),Set(varPExport,false);Notify("Хураангуй болон аудитын CSV хавсралтыг илгээлээ.",NotificationType.Success));Set(varPBusy,false))))
```

### `ScrAccess/pExportModal/pExportSend` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExportModal/pExportSend` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExportModal/pExportSend` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pExportModal/pExportSend` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExportModal/pExportSend` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pExportModal/pExportSend` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportSend` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportSend` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportSend` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExportModal/pExportSend` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrAccess/pExportModal/pExportSend` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Илгээх"
```

### `ScrAccess/pExportModal/pExportSend` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.56
```

### `ScrAccess/pExportModal/pExportSend` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.38
```

### `ScrAccess/pExportModal/pExportSend` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrAccess/pExitModal` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pExitModal` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pExitModal` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(255)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
varPExitConfirm
```

### `ScrAccess/pExitModal` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(366)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*((ScrAccess.Width/366)))/2
```

### `ScrAccess/pExitModal` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-255*((ScrAccess.Height/790)))/2
```

### `ScrAccess/pExitModal/pExitTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pExitModal/pExitTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExitModal/pExitTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExitModal/pExitTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pExitModal/pExitTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExitModal/pExitTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExitModal/pExitTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrAccess/pExitModal/pExitTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(45)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Power Apps-ээс гарах уу?"
```

### `ScrAccess/pExitModal/pExitTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(322)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitTitle` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(23)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitWarning` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrAccess/pExitModal/pExitWarning` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExitModal/pExitWarning` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#66615B")
```

### `ScrAccess/pExitModal/pExitWarning` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrAccess/pExitModal/pExitWarning` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExitModal/pExitWarning` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExitModal/pExitWarning` . **Height**  _(Label@2.5.1)_
```powerfx
(67)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitWarning` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitWarning` . **Text**  _(Label@2.5.1)_
```powerfx
"Илгээгээгүй тооллого: " & CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced)) & ". Локал өгөгдлийг устгахгүй."
```

### `ScrAccess/pExitModal/pExitWarning` . **Width**  _(Label@2.5.1)_
```powerfx
(322)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitWarning` . **X**  _(Label@2.5.1)_
```powerfx
(22)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitWarning` . **Y**  _(Label@2.5.1)_
```powerfx
(85)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitCancel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pExitModal/pExitCancel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExitModal/pExitCancel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pExitModal/pExitCancel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrAccess/pExitModal/pExitCancel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExitModal/pExitCancel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExitModal/pExitCancel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitCancel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pExitModal/pExitCancel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExitModal/pExitCancel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pExitModal/pExitCancel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPExitConfirm,false)
```

### `ScrAccess/pExitModal/pExitCancel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExitModal/pExitCancel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExitModal/pExitCancel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pExitModal/pExitCancel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExitModal/pExitCancel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pExitModal/pExitCancel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitCancel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitCancel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitCancel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitCancel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitCancel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Буцах"
```

### `ScrAccess/pExitModal/pExitCancel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(145)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitCancel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(22)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitCancel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(179)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#321316")
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*((ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Collect(colPAudit,{EventId:Text(GUID()),OwnerEmail:Lower(User().Email),ActorName:User().FullName,ActorEmail:User().Email,OccurredAt:Now(),Module:"Хэрэглэгч",Action:"Гарах хүсэлт өгсөн",Entity:User().Email,BeforeValue:"",AfterValue:"",Result:"Локал өөрчлөлт"});IfError(SaveData(colPAudit,"AccessAuditV8"),Set(varPAuditSaveError,true); false, true);Exit(true)
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(ScrAccess.Width/366,ScrAccess.Height/790))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гарах"
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(164)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(180)*((ScrAccess.Width/366))
```

### `ScrAccess/pExitModal/pExitConfirmButton` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(179)*((ScrAccess.Height/790))
```

### `ScrAccess/pgOpenAdminMe` . **AccessibleLabel**  _(Classic/Button@2.2.0)_
```powerfx
"Админ · Хэрэглэгч ба эрх"
```

### `ScrAccess/pgOpenAdminMe` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(180)*App.Width/360,Parent.Width-130
)
```

### `ScrAccess/pgOpenAdminMe` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(varPView="profile",(596)*App.Height/720,App.Height-48),Parent.Height-48
)
```

### `ScrAccess/pgOpenAdminMe` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(166)*App.Width/360,124
)
```

### `ScrAccess/pgOpenAdminMe` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(38)*App.Height/720,42
)
```

### `ScrAccess/pgOpenAdminMe` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),12
)
```

### `ScrAccess/pgOpenAdminMe` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),Color.White
)
```

### `ScrAccess/pgOpenAdminMe` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#202225")
)
```

### `ScrAccess/pgOpenAdminMe` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrAccess/pgOpenAdminMe` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrAccess/pgOpenAdminMe` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Админ · Эрх"
```

### `ScrAccess/pgOpenAdminMe` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrPageAdmin,ScreenTransition.Fade)
```

### `ScrAccess/pgOpenAdminMe` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (!varPExitConfirm && !varPExport),(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))
)
```

### `ScrAccess/pgMenuEntry` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(true) && (!varPExitConfirm && !varPExport),true
)
```

### `ScrAccess/pgMenuEntry` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(228)*App.Width/360,8
)
```

### `ScrAccess/pgMenuEntry` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(varPView="profile",(13)*App.Height/720,App.Height-48),Parent.Height-48
)
```

### `ScrAccess/pgMenuEntry` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(116)*App.Width/360,124
)
```

### `ScrAccess/pgMenuEntry` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(38)*App.Height/720,42
)
```

### `ScrAccess/pgMenuEntry` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),14
)
```

### `ScrAccess/pgMenuEntry` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),Color.White
)
```

### `ScrAccess/pgMenuEntry` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#202225")
)
```

### `ScrAccess/pgMenuEntry` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrAccess/pgMenuEntry` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrAccess/pgMenuEntry` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Миний хуудсууд"
```

### `ScrAccess/pgMenuEntry` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrPageMenu,ScreenTransition.Fade)
```

### `ScrAccess/phoneProfileStockRows` . **X**  _(Label@2.5.1)_
```powerfx
(28)*App.Width/360
```

### `ScrAccess/phoneProfileStockRows` . **Y**  _(Label@2.5.1)_
```powerfx
(389)*App.Height/720
```

### `ScrAccess/phoneProfileStockRows` . **Width**  _(Label@2.5.1)_
```powerfx
(207)*App.Width/360
```

### `ScrAccess/phoneProfileStockRows` . **Height**  _(Label@2.5.1)_
```powerfx
(95)*App.Height/720
```

### `ScrAccess/phoneProfileStockRows` . **Size**  _(Label@2.5.1)_
```powerfx
13*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileStockRows` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/phoneProfileStockRows` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrAccess/phoneProfileStockRows` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport)
```

### `ScrAccess/phoneProfileStockRows` . **Text**  _(Label@2.5.1)_
```powerfx
"Бараа" & Char(10) & "Үлдэгдлийн мөр" & Char(10) & "Илгээгээгүй тооллого"
```

### `ScrAccess/phoneProfileStockRows` . **LineHeight**  _(Label@2.5.1)_
```powerfx
1.6
```

### `ScrAccess/phoneProfileStockValues` . **X**  _(Label@2.5.1)_
```powerfx
(239)*App.Width/360
```

### `ScrAccess/phoneProfileStockValues` . **Y**  _(Label@2.5.1)_
```powerfx
(389)*App.Height/720
```

### `ScrAccess/phoneProfileStockValues` . **Width**  _(Label@2.5.1)_
```powerfx
(92)*App.Width/360
```

### `ScrAccess/phoneProfileStockValues` . **Height**  _(Label@2.5.1)_
```powerfx
(95)*App.Height/720
```

### `ScrAccess/phoneProfileStockValues` . **Size**  _(Label@2.5.1)_
```powerfx
13*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileStockValues` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/phoneProfileStockValues` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrAccess/phoneProfileStockValues` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport)
```

### `ScrAccess/phoneProfileStockValues` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(Distinct(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode)),itemNo)),"#,##0") & Char(10) & Text(CountRows(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode))),"#,##0") & Char(10) & Text(CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced && ((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode))))
```

### `ScrAccess/phoneProfileStockValues` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrAccess/phoneProfileStockValues` . **LineHeight**  _(Label@2.5.1)_
```powerfx
1.6
```

### `ScrAccess/phoneProfileSync` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(27)*App.Width/360
```

### `ScrAccess/phoneProfileSync` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(485)*App.Height/720
```

### `ScrAccess/phoneProfileSync` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(306)*App.Width/360
```

### `ScrAccess/phoneProfileSync` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(44)*App.Height/720
```

### `ScrAccess/phoneProfileSync` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileSync` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrAccess/phoneProfileSync` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/phoneProfileSync` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrAccess/phoneProfileSync` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrAccess/phoneProfileSync` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrAccess/phoneProfileSync` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!Connection.Connected,Notify("Интернет холболтоо шалгана уу.",NotificationType.Warning),Set(varAutoDataChecked,Blank());false;If(Connection.Connected && !Coalesce(varStartupSyncRunning,false) &&
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

### `ScrAccess/phoneProfileSync` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varStartupSyncRunning,"Шинэчилж байна…","⟳   Бүгдийг синк хийх")
```

### `ScrAccess/phoneProfileSync` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varStartupSyncRunning,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrAccess/phoneProfileHome` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(9)*App.Width/360
```

### `ScrAccess/phoneProfileHome` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(657)*App.Height/720
```

### `ScrAccess/phoneProfileHome` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(61)*App.Width/360
```

### `ScrAccess/phoneProfileHome` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(52)*App.Height/720
```

### `ScrAccess/phoneProfileHome` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileHome` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/phoneProfileHome` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrAccess/phoneProfileHome` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrAccess/phoneProfileHome` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrAccess/phoneProfileHome` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|home|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrAccess/phoneProfileHome` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр',ScreenTransition.Fade)
```

### `ScrAccess/phoneProfileHome` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"⌂" & Char(10) & "Нүүр"
```

### `ScrAccess/phoneProfileStore` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(78)*App.Width/360
```

### `ScrAccess/phoneProfileStore` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(657)*App.Height/720
```

### `ScrAccess/phoneProfileStore` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(61)*App.Width/360
```

### `ScrAccess/phoneProfileStore` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(52)*App.Height/720
```

### `ScrAccess/phoneProfileStore` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileStore` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/phoneProfileStore` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrAccess/phoneProfileStore` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrAccess/phoneProfileStore` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrAccess/phoneProfileStore` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrAccess/phoneProfileStore` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(Screen1,ScreenTransition.Fade)
```

### `ScrAccess/phoneProfileStore` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"▤" & Char(10) & "Агуулах"
```

### `ScrAccess/phoneProfileScan` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(151)*App.Width/360
```

### `ScrAccess/phoneProfileScan` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(646)*App.Height/720
```

### `ScrAccess/phoneProfileScan` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(58)*App.Width/360
```

### `ScrAccess/phoneProfileScan` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(60)*App.Height/720
```

### `ScrAccess/phoneProfileScan` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileScan` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrAccess/phoneProfileScan` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F15D18")
```

### `ScrAccess/phoneProfileScan` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrAccess/phoneProfileScan` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrAccess/phoneProfileScan` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrAccess/phoneProfileScan` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(scrWarehouses,ScreenTransition.Fade)
```

### `ScrAccess/phoneProfileScan` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"▥" & Char(10) & "Scan"
```

### `ScrAccess/phoneProfileDash` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(219)*App.Width/360
```

### `ScrAccess/phoneProfileDash` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(657)*App.Height/720
```

### `ScrAccess/phoneProfileDash` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(74)*App.Width/360
```

### `ScrAccess/phoneProfileDash` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(52)*App.Height/720
```

### `ScrAccess/phoneProfileDash` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileDash` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrAccess/phoneProfileDash` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrAccess/phoneProfileDash` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrAccess/phoneProfileDash` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrAccess/phoneProfileDash` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrAccess/phoneProfileDash` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrDashboard,ScreenTransition.Fade)
```

### `ScrAccess/phoneProfileDash` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"▥" & Char(10) & "Dashboard"
```

### `ScrAccess/phoneProfileMe` . **X**  _(Label@2.5.1)_
```powerfx
(298)*App.Width/360
```

### `ScrAccess/phoneProfileMe` . **Y**  _(Label@2.5.1)_
```powerfx
(657)*App.Height/720
```

### `ScrAccess/phoneProfileMe` . **Width**  _(Label@2.5.1)_
```powerfx
(53)*App.Width/360
```

### `ScrAccess/phoneProfileMe` . **Height**  _(Label@2.5.1)_
```powerfx
(52)*App.Height/720
```

### `ScrAccess/phoneProfileMe` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `ScrAccess/phoneProfileMe` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#AD4516")
```

### `ScrAccess/phoneProfileMe` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrAccess/phoneProfileMe` . **Visible**  _(Label@2.5.1)_
```powerfx
App.Width<First(App.SizeBreakpoints).Value && (varPView="profile" && !varPExitConfirm && !varPExport)
```

### `ScrAccess/phoneProfileMe` . **Text**  _(Label@2.5.1)_
```powerfx
"♙" & Char(10) & "Би"
```

### `ScrAccess/phoneProfileMe` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

