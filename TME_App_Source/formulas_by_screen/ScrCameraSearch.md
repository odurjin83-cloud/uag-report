# ScrCameraSearch — Power Fx formulas

### `ScrCameraSearch` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrCameraSearch` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrCameraSearch` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrCameraSearch` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Set(varCView,"search");Set(varCOnlyStock,false);Set(varCQuery,"");Set(varCItem,"");Set(varCPhoto,Blank());Set(varCNewPhoto,Blank());Set(varCZoom,1);Set(varCLoading,false);
If(!Coalesce(varCInitialized,false),
ClearCollect(colCPhotos,{PhotoId:"",OwnerEmail:"",ItemNo:"",ImageData:"",Created:Now()});Clear(colCPhotos);
IfError(LoadData(colCPhotos,"CameraPhotosV12",true),Notify("Локал зургийг уншиж чадсангүй.",NotificationType.Warning);false,true);
Set(varCInitialized,true));
Reset(cSearch)
)
```

### `ScrCameraSearch` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrCameraSearch/cLoad` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cLoad` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cLoad` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCameraSearch/cLoad` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCameraSearch/cLoad` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cLoad` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cLoad` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cLoad` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,1,1)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cLoad` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCameraSearch/cLoad` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrCameraSearch/cLoad` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cLoad` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCLoading,true);Set(varCPhoto,Blank());Set(varCNewPhoto,Blank());Set(varCZoom,1);Reset(cTakePhoto);Reset(cPickPhoto);
If(Connection.Connected,IfError(Set(varCPhoto,'PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo...'.Run(varCItem).picture),Notify("Серверийн зураг татагдсангүй. Локал зургаа сонгож болно.",NotificationType.Warning)));
Set(varCLoading,false);Set(varCView,"detail")
```

### `ScrCameraSearch/cLoad` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cLoad` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cLoad` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cLoad` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cLoad` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCameraSearch/cLoad` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cLoad` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrCameraSearch/cLoad` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cLoad` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrCameraSearch/cLoad` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,1,1)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cLoad` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0,0)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cLoad` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0,0)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCameraSearch/cBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCameraSearch/cBack` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCameraSearch/cBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,42,38)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCameraSearch/cBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrCameraSearch/cBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(varCView="search",Navigate(нүүр,ScreenTransition.Fade),Set(varCView,"search"))
```

### `ScrCameraSearch/cBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cBack` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cBack` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCameraSearch/cBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrCameraSearch/cBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrCameraSearch/cBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,40,36)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24,18)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,22,24)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCameraSearch/cTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,42,42)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cTitle` . **Size**  _(Label@2.5.1)_
```powerfx
21*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Камер ба хайлт"
```

### `ScrCameraSearch/cTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,470,278)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,80,66)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,22,23)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cSub` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCameraSearch/cSub` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cSub` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSub` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#969DA8")
```

### `ScrCameraSearch/cSub` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cSub` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSub` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cSub` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cSub` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24,24)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cSub` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cSub` . **Text**  _(Label@2.5.1)_
```powerfx
"Барааны код · нэр · зураг"
```

### `ScrCameraSearch/cSub` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610,320)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cSub` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,26,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cSub` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,78,71)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cSearch` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrCameraSearch/cSearch` . **BorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSearch` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cSearch` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
varCQuery
```

### `ScrCameraSearch/cSearch` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cSearch` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSearch` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cSearch` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48,46)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cSearch` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Код эсвэл нэрээр хайх…"
```

### `ScrCameraSearch/cSearch` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cSearch` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ScrCameraSearch/cSearch` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrCameraSearch/cSearch` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrCameraSearch/cSearch` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrCameraSearch/cSearch` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrCameraSearch/cSearch` . **RadiusBottomLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSearch` . **RadiusBottomRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSearch` . **RadiusTopLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSearch` . **RadiusTopRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSearch` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cSearch` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail"))
```

### `ScrCameraSearch/cSearch` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,618,270)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cSearch` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,26,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cSearch` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,117,165)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cClear` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cClear` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cClear` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCameraSearch/cClear` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCameraSearch/cClear` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cClear` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cClear` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cClear` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48,46)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cClear` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCameraSearch/cClear` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrCameraSearch/cClear` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cClear` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCQuery,"");Reset(cSearch)
```

### `ScrCameraSearch/cClear` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cClear` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cClear` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cClear` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cClear` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCameraSearch/cClear` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cClear` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrCameraSearch/cClear` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cClear` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"×"
```

### `ScrCameraSearch/cClear` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail"))
```

### `ScrCameraSearch/cClear` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,98,44)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cClear` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,656,300)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cClear` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,117,165)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cStock` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cStock` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cStock` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCameraSearch/cStock` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCameraSearch/cStock` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cStock` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cStock` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cStock` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,36,34)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cStock` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCameraSearch/cStock` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrCameraSearch/cStock` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cStock` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCOnlyStock,!varCOnlyStock)
```

### `ScrCameraSearch/cStock` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cStock` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cStock` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cStock` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cStock` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCameraSearch/cStock` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cStock` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrCameraSearch/cStock` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cStock` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бэлэн"
```

### `ScrCameraSearch/cStock` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail"))
```

### `ScrCameraSearch/cStock` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,105,100)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cStock` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,26,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cStock` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,178,222)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cStockState` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cStockState` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cStockState` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#969DA8")
```

### `ScrCameraSearch/cStockState` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cStockState` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cStockState` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cStockState` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cStockState` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,30,30)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cStockState` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cStockState` . **Text**  _(Label@2.5.1)_
```powerfx
If(varCOnlyStock,"Зөвхөн үлдэгдэлтэй","Бүх бараа")
```

### `ScrCameraSearch/cStockState` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail"))
```

### `ScrCameraSearch/cStockState` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,460,212)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cStockState` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,147,132)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cStockState` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,180,224)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cBarcode` . **BorderThickness**  _(BarcodeReader@1.0.25)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cBarcode` . **FillColor**  _(BarcodeReader@1.0.25)_
```powerfx
RGBA(99, 139, 44, 1)
```

### `ScrCameraSearch/cBarcode` . **Height**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,43,43)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cBarcode` . **OnScan**  _(BarcodeReader@1.0.25)_
```powerfx
Set(varCQuery,Text(First(Self.Barcodes).Value));Reset(cSearch);If(IsBlank(LookUp(colOfflineItems,number=varCQuery,number)),Notify("Локал жагсаалтад код олдсонгүй. Синк эсвэл нэрээр хайлт хийнэ үү.",NotificationType.Warning),Set(varCItem,varCQuery);Select(cLoad))
```

### `ScrCameraSearch/cBarcode` . **Text**  _(BarcodeReader@1.0.25)_
```powerfx
"Баркод скан"
```

### `ScrCameraSearch/cBarcode` . **Visible**  _(BarcodeReader@1.0.25)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail"))
```

### `ScrCameraSearch/cBarcode` . **Width**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,143,224)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cBarcode` . **X**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,459,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cBarcode` . **Y**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,23,108)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cResults` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cResults` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cResults` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cResults` . **Height**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,563,452)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cResults` . **Items**  _(Gallery@2.15.0)_
```powerfx
Filter(colOfflineItems As i,!IsBlank(i.number) && (IsBlank(Trim(cSearch.Text)) || Lower(Trim(cSearch.Text)) in Lower(i.number) || Lower(Trim(cSearch.Text)) in Lower(i.displayName)) && (!varCOnlyStock || Sum(Filter(colOfflineStock,itemNo=i.number),quantity)>0))
```

### `ScrCameraSearch/cResults` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cResults` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cResults` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
92*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cResults` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail"))
```

### `ScrCameraSearch/cResults` . **Width**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,728,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cResults` . **X**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,26,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cResults` . **Y**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,227,272)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cResults/cResultRow` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrCameraSearch/cResults/cResultRow` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cResults/cResultRow` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cResults/cResultRow` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCameraSearch/cResults/cResultRow` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCameraSearch/cResults/cResultRow` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cResults/cResultRow` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cResults/cResultRow` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cResults/cResultRow` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
86*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cResults/cResultRow` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCameraSearch/cResults/cResultRow` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrCameraSearch/cResults/cResultRow` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cResults/cResultRow` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCItem,ThisItem.number);Select(cLoad)
```

### `ScrCameraSearch/cResults/cResultRow` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cResults/cResultRow` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cResults/cResultRow` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cResults/cResultRow` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cResults/cResultRow` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCameraSearch/cResults/cResultRow` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cResults/cResultRow` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrCameraSearch/cResults/cResultRow` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cResults/cResultRow` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cResults/cResultRow` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cResults/cResultRow` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cResults/cResultRow` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cResults/cResultRow` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
ThisItem.number & Char(10) & ThisItem.displayName & Char(10) & "Үлдэгдэл: " & Text(Sum(Filter(colOfflineStock,itemNo=ThisItem.number),quantity),"#,##0.###")
```

### `ScrCameraSearch/cResults/cResultRow` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.TemplateWidth
```

### `ScrCameraSearch/cEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#969DA8")
```

### `ScrCameraSearch/cEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cEmpty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,100,100)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Бараа олдсонгүй. Өгөгдлөө синк хийж, код эсвэл нэрээр хайна уу."
```

### `ScrCameraSearch/cEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail")) && IsEmpty(cResults.AllItems))
```

### `ScrCameraSearch/cEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,620,296)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cEmpty` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,80,35)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,390,350)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cLocalNote` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cLocalNote` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cLocalNote` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#969DA8")
```

### `ScrCameraSearch/cLocalNote` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cLocalNote` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cLocalNote` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cLocalNote` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cLocalNote` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,22,30)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cLocalNote` . **Size**  _(Label@2.5.1)_
```powerfx
9*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cLocalNote` . **Text**  _(Label@2.5.1)_
```powerfx
"Үлдэгдэл: төхөөрөмжид синк хийсэн өгөгдөл"
```

### `ScrCameraSearch/cLocalNote` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((varCView="search") || (App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height && varCView="detail"))
```

### `ScrCameraSearch/cLocalNote` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,728,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cLocalNote` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,26,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cLocalNote` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,791,740)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotoCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cPhotoCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cPhotoCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,330,273)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotoCard` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cPhotoCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,366,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhotoCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhotoCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,100,161)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cItemTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cItemTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cItemTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cItemTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cItemTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cItemTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cItemTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cItemTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,64,48)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cItemTitle` . **Size**  _(Label@2.5.1)_
```powerfx
13*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cItemTitle` . **Text**  _(Label@2.5.1)_
```powerfx
varCItem & Char(10) & Coalesce(LookUp(colOfflineItems,number=varCItem,displayName),"")
```

### `ScrCameraSearch/cItemTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cItemTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,366,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cItemTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cItemTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,23,106)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhoto` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cPhoto` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(215, 223, 240, 1)
```

### `ScrCameraSearch/cPhoto` . **Height**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,314,261)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhoto` . **Image**  _(Image@2.2.3)_
```powerfx
Coalesce(varCNewPhoto,varCPhoto)
```

### `ScrCameraSearch/cPhoto` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
If(varCZoom>1,ImagePosition.Fill,ImagePosition.Fit)
```

### `ScrCameraSearch/cPhoto` . **OnSelect**  _(Image@2.2.3)_
```powerfx
Set(varCZoom,If(varCZoom=1,2,1))
```

### `ScrCameraSearch/cPhoto` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cPhoto` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,350,310)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhoto` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,796,28)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhoto` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,108,167)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cNoPhoto` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cNoPhoto` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cNoPhoto` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#969DA8")
```

### `ScrCameraSearch/cNoPhoto` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cNoPhoto` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cNoPhoto` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cNoPhoto` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cNoPhoto` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,80,80)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cNoPhoto` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cNoPhoto` . **Text**  _(Label@2.5.1)_
```powerfx
If(varCLoading,"Зураг татаж байна…","Зураг байхгүй. Доорх товчоор зураг авна уу.")
```

### `ScrCameraSearch/cNoPhoto` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail" && IsBlank(varCPhoto) && IsBlank(varCNewPhoto))
```

### `ScrCameraSearch/cNoPhoto` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,300,266)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cNoPhoto` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,819,50)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cNoPhoto` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,216,257)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cZoom` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cZoom` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cZoom` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCameraSearch/cZoom` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varRptSending || varRptPdfPending,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCameraSearch/cZoom` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cZoom` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cZoom` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cZoom` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,34,34)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cZoom` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCameraSearch/cZoom` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrCameraSearch/cZoom` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cZoom` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCZoom,If(varCZoom=1,2,1))
```

### `ScrCameraSearch/cZoom` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cZoom` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cZoom` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cZoom` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cZoom` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCameraSearch/cZoom` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cZoom` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrCameraSearch/cZoom` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cZoom` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"⤢"
```

### `ScrCameraSearch/cZoom` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cZoom` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48,48)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cZoom` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,1094,285)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cZoom` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,385,391)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cImageState` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cImageState` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cImageState` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#969DA8")
```

### `ScrCameraSearch/cImageState` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cImageState` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cImageState` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cImageState` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cImageState` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,25,24)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cImageState` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cImageState` . **Text**  _(Label@2.5.1)_
```powerfx
If(!IsBlank(varCNewPhoto),"Шинэ зураг · хадгалаагүй","Зураг · " & If(varCZoom>1,"дүүргэж харах","бүтнээр харах"))
```

### `ScrCameraSearch/cImageState` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cImageState` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,366,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cImageState` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cImageState` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,440,438)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotos` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cPhotos` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cPhotos` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cPhotos` . **Height**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,64,64)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotos` . **Items**  _(Gallery@2.15.0)_
```powerfx
Filter(colCPhotos,ItemNo=varCItem && OwnerEmail=Lower(User().Email))
```

### `ScrCameraSearch/cPhotos` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cPhotos` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
74*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhotos` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cPhotos` . **Width**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,366,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhotos` . **X**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhotos` . **Y**  _(Gallery@2.15.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,475,470)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotos/cThumb` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cPhotos/cThumb` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(215, 223, 240, 1)
```

### `ScrCameraSearch/cPhotos/cThumb` . **Height**  _(Image@2.2.3)_
```powerfx
58*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotos/cThumb` . **Image**  _(Image@2.2.3)_
```powerfx
ThisItem.ImageData
```

### `ScrCameraSearch/cPhotos/cThumb` . **OnSelect**  _(Image@2.2.3)_
```powerfx
Set(varCPhoto,ThisItem.ImageData);Set(varCNewPhoto,Blank())
```

### `ScrCameraSearch/cPhotos/cThumb` . **Width**  _(Image@2.2.3)_
```powerfx
66*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cStockInfo` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cStockInfo` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cStockInfo` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cStockInfo` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cStockInfo` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cStockInfo` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cStockInfo` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cStockInfo` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,58,58)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cStockInfo` . **Size**  _(Label@2.5.1)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cStockInfo` . **Text**  _(Label@2.5.1)_
```powerfx
"Үлдэгдэл: " & Text(Sum(Filter(colOfflineStock,itemNo=varCItem),quantity),"#,##0.###") & Char(10) & "Агуулах: " & Concat(Distinct(Filter(colOfflineStock,itemNo=varCItem),locationCode),Value,", ")
```

### `ScrCameraSearch/cStockInfo` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cStockInfo` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,366,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cStockInfo` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cStockInfo` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,550,544)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cTakePhoto` . **Align**  _(AddMedia@2.2.1)_
```powerfx
Align.Right
```

### `ScrCameraSearch/cTakePhoto` . **BorderColor**  _(AddMedia@2.2.1)_
```powerfx
RGBA(111,73,224,1)
```

### `ScrCameraSearch/cTakePhoto` . **BorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cTakePhoto` . **ChangePictureText**  _(AddMedia@2.2.1)_
```powerfx
"Зураг авах"
```

### `ScrCameraSearch/cTakePhoto` . **Color**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cTakePhoto` . **Fill**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cTakePhoto` . **FocusedBorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cTakePhoto` . **Height**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48,48)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cTakePhoto` . **OnChange**  _(AddMedia@2.2.1)_
```powerfx
Set(varCNewPhoto,cTakePhoto.Media)
```

### `ScrCameraSearch/cTakePhoto` . **Size**  _(AddMedia@2.2.1)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cTakePhoto` . **Text**  _(AddMedia@2.2.1)_
```powerfx
"Зураг авах"
```

### `ScrCameraSearch/cTakePhoto` . **UseMobileCamera**  _(AddMedia@2.2.1)_
```powerfx
true
```

### `ScrCameraSearch/cTakePhoto` . **Visible**  _(AddMedia@2.2.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cTakePhoto` . **Width**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,174,156)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cTakePhoto` . **X**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cTakePhoto` . **Y**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,625,619)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPickPhoto` . **Align**  _(AddMedia@2.2.1)_
```powerfx
Align.Right
```

### `ScrCameraSearch/cPickPhoto` . **BorderColor**  _(AddMedia@2.2.1)_
```powerfx
RGBA(111,73,224,1)
```

### `ScrCameraSearch/cPickPhoto` . **BorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cPickPhoto` . **ChangePictureText**  _(AddMedia@2.2.1)_
```powerfx
"Галлерей"
```

### `ScrCameraSearch/cPickPhoto` . **Color**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cPickPhoto` . **Fill**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cPickPhoto` . **FocusedBorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cPickPhoto` . **Height**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48,48)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPickPhoto` . **OnChange**  _(AddMedia@2.2.1)_
```powerfx
Set(varCNewPhoto,cPickPhoto.Media)
```

### `ScrCameraSearch/cPickPhoto` . **Size**  _(AddMedia@2.2.1)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cPickPhoto` . **Text**  _(AddMedia@2.2.1)_
```powerfx
"Галлерей"
```

### `ScrCameraSearch/cPickPhoto` . **Visible**  _(AddMedia@2.2.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cPickPhoto` . **Width**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,174,156)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPickPhoto` . **X**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,980,188)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPickPhoto` . **Y**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,625,619)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cSavePhoto` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrCameraSearch/cSavePhoto` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/cSavePhoto` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrCameraSearch/cSavePhoto` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(varCNewPhoto),DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrCameraSearch/cSavePhoto` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrCameraSearch/cSavePhoto` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cSavePhoto` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cSavePhoto` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48,48)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cSavePhoto` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrCameraSearch/cSavePhoto` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#86968F")
```

### `ScrCameraSearch/cSavePhoto` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cSavePhoto` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(varCItem) || IsBlank(varCNewPhoto),Notify("Бараа болон шинэ зураг сонгоно уу.",NotificationType.Warning),
Set(varCImageJSON,JSON(varCNewPhoto,JSONFormat.IncludeBinaryData));
Collect(colCPhotos,{PhotoId:Text(GUID()),OwnerEmail:Lower(User().Email),ItemNo:varCItem,ImageData:Mid(varCImageJSON,2,Len(varCImageJSON)-2),Created:Now()});
IfError(SaveData(colCPhotos,"CameraPhotosV12"),Notify("Зураг зөвхөн санах ойд байна. Төхөөрөмжид хадгалж чадсангүй.",NotificationType.Error);false,Notify("Зураг төхөөрөмжид хадгалагдлаа. Серверт илгээгээгүй.",NotificationType.Success);true);
Set(varCPhoto,varCNewPhoto);Set(varCNewPhoto,Blank()))
```

### `ScrCameraSearch/cSavePhoto` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cSavePhoto` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cSavePhoto` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Width/640))
```

### `ScrCameraSearch/cSavePhoto` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrCameraSearch/cSavePhoto` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrCameraSearch/cSavePhoto` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCameraSearch/cSavePhoto` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5343")
```

### `ScrCameraSearch/cSavePhoto` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cSavePhoto` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зургийг локал хадгалах"
```

### `ScrCameraSearch/cSavePhoto` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cSavePhoto` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,366,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cSavePhoto` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cSavePhoto` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,690,683)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotoNotice` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrCameraSearch/cPhotoNotice` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cPhotoNotice` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrCameraSearch/cPhotoNotice` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrCameraSearch/cPhotoNotice` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrCameraSearch/cPhotoNotice` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrCameraSearch/cPhotoNotice` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCameraSearch/cPhotoNotice` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,26,28)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/cPhotoNotice` . **OnSelect**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varCItem),Notify("Бараа сонгоно уу.",NotificationType.Warning),
!Connection.Connected,Notify("BC-д илгээхэд интернет хэрэгтэй.",NotificationType.Warning),
IsBlank(Coalesce(varCNewPhoto,varCPhoto)),Notify("Зураг сонгоно уу.",NotificationType.Warning),
With({j:JSON(Coalesce(varCNewPhoto,varCPhoto),JSONFormat.IncludeBinaryData)},
With({payload:Mid(j,2,Len(j)-2)},
If(!StartsWith(payload,"data:image"),Notify("Камер эсвэл локал зураг сонгоно уу.",NotificationType.Warning),
IfError('PowerAppV2->Getrecord(V3)'.Run(varCItem,payload),Notify("Зураг илгээх алдаа: " & FirstError.Message,NotificationType.Error);false,Notify("BC зураг илгээх хүсэлт гүйцэтгэлээ.",NotificationType.Success);true)))))
```

### `ScrCameraSearch/cPhotoNotice` . **Size**  _(Label@2.5.1)_
```powerfx
10*(Min(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366),If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790)))
```

### `ScrCameraSearch/cPhotoNotice` . **Text**  _(Label@2.5.1)_
```powerfx
"BC-д зураг илгээх → (энд дарна уу)"
```

### `ScrCameraSearch/cPhotoNotice` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCView="detail")
```

### `ScrCameraSearch/cPhotoNotice` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,366,322)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhotoNotice` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,788,22)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width/1180,App.Width/366))
```

### `ScrCameraSearch/cPhotoNotice` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,750,741)*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Height/820,App.Height/790))
```

### `ScrCameraSearch/pgDenied252` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrCameraSearch/pgDenied252` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrCameraSearch/pgDenied252` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrCameraSearch/pgDenied252` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCameraSearch/pgDenied252` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCameraSearch/pgDenied252` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCameraSearch/pgDenied252` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCameraSearch/pgDenied252` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrCameraSearch/pgDenied252` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrCameraSearch/pgDenied252` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

