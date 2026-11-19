# ScrItemPhotos — Power Fx formulas

### `ScrItemPhotos` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F3F6F2")
```

### `ScrItemPhotos` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrItemPhotos` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrItemPhotos` . **OnHidden**  _(Screen)_
```powerfx
Set(varPhotoZoomV28,false);Set(varPhotoConfirmV28,false)
```

### `ScrItemPhotos` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Set(varPhotoSourceV29,"");Set(varPhotoUploadDataV29,Blank());Set(varPhotoBusyV28,false);Set(varPhotoZoomV28,false);Set(varPhotoConfirmV28,false);Set(varPhotoTabV28,"bc");Set(varPhotoMessageV28,"");
Set(varPhotoItemV28,Coalesce(varPhotoRequestedV28,""));Set(varPhotoServerV28,Blank());Set(varPhotoNewV28,Blank());Set(varPhotoNewItemV28,"");
Set(varPhotoRecordV28,LookUp(colOfflineItems,number=varPhotoItemV28));
Reset(photoSearchV28);Reset(photoCameraV28);Reset(photoPickV28);Set(varPhotoSearchV28,IsBlank(varPhotoItemV28));
If(!IsBlank(varPhotoItemV28),Select(photoLoadV28))
)
```

### `ScrItemPhotos` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrItemPhotos/photoLoadV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoLoadV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoLoadV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoLoadV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoLoadV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoLoadV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoLoadV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoLoadV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoLoadV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoLoadV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoLoadV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoLoadV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!varPhotoBusyV28 && !IsBlank(varPhotoItemV28),
Set(varPhotoBusyV28,true);Set(varPhotoServerV28,Blank());Set(varPhotoMessageV28,"");
If(varPhotoNewItemV28<>varPhotoItemV28,Set(varPhotoNewV28,Blank());Reset(photoCameraV28);Reset(photoPickV28));
Set(varPhotoRecordV28,LookUp(colOfflineItems,number=varPhotoItemV28));
ClearCollect(colPhotoLocationsV28,ForAll(GroupBy(Filter(colOfflineStock,itemNo=varPhotoItemV28 && !IsBlank(locationCode)),locationCode,LocationRows) As l,{Code:l.locationCode,Qty:Sum(l.LocationRows,quantity)}));
If(Connection.Connected,
 IfError(Set(varPhotoServerV28,'PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo...'.Run(varPhotoItemV28).picture);true,
 Set(varPhotoMessageV28,"BC зураг татагдсангүй. Дахин шинэчилж болно.");false),
 Set(varPhotoMessageV28,"BC-ийн зураг харах болон солиход интернет хэрэгтэй."));
Set(varPhotoTabV28,If(!IsBlank(varPhotoNewV28),"new","bc"));Set(varPhotoBusyV28,false))
```

### `ScrItemPhotos/photoLoadV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoLoadV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoLoadV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoLoadV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoLoadV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrItemPhotos/photoTitleV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoTitleV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoTitleV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoTitleV28` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrItemPhotos/photoTitleV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoTitleV28` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.055
```

### `ScrItemPhotos/photoTitleV28` . **Size**  _(Label@2.5.1)_
```powerfx
30*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoTitleV28` . **Text**  _(Label@2.5.1)_
```powerfx
"Барааны зураг"
```

### `ScrItemPhotos/photoTitleV28` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.65
```

### `ScrItemPhotos/photoTitleV28` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.15
```

### `ScrItemPhotos/photoTitleV28` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.035
```

### `ScrItemPhotos/photoBackV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoBackV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoBackV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoBackV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoBackV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoBackV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoBackV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,If(varPhotoBusyV28,DisplayMode.Disabled,DisplayMode.Edit))
```

### `ScrItemPhotos/photoBackV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoBackV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoBackV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoBackV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.06
```

### `ScrItemPhotos/photoBackV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoBackV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoBackV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoBackV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoReturnV28="count",Navigate(scrWarehouses,ScreenTransition.Fade),Navigate(ScrCountHome,ScreenTransition.Fade))
```

### `ScrItemPhotos/photoBackV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoBackV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoBackV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoBackV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoBackV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrItemPhotos/photoBackV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.09
```

### `ScrItemPhotos/photoBackV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.04
```

### `ScrItemPhotos/photoBackV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.03
```

### `ScrItemPhotos/photoSubtitleV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoSubtitleV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoSubtitleV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoSubtitleV28` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrItemPhotos/photoSubtitleV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoSubtitleV28` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.035
```

### `ScrItemPhotos/photoSubtitleV28` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoSubtitleV28` . **Text**  _(Label@2.5.1)_
```powerfx
If(Connection.Connected,"ОНЛАЙН · BC барааны зураг","ОФФЛАЙН · Зураг илгээхэд интернет хэрэгтэй")
```

### `ScrItemPhotos/photoSubtitleV28` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.81
```

### `ScrItemPhotos/photoSubtitleV28` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.15
```

### `ScrItemPhotos/photoSubtitleV28` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.091
```

### `ScrItemPhotos/photoSearchV28` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoSearchV28` . **AccessibleLabel**  _(Classic/TextInput@2.3.2)_
```powerfx
"Зураг харах барааны код эсвэл нэр"
```

### `ScrItemPhotos/photoSearchV28` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoSearchV28` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoSearchV28` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
varPhotoItemV28
```

### `ScrItemPhotos/photoSearchV28` . **DelayOutput**  _(Classic/TextInput@2.3.2)_
```powerfx
true
```

### `ScrItemPhotos/photoSearchV28` . **DisplayMode**  _(Classic/TextInput@2.3.2)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,If(varPhotoBusyV28,DisplayMode.Disabled,DisplayMode.Edit))
```

### `ScrItemPhotos/photoSearchV28` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoSearchV28` . **FocusedBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#237653")
```

### `ScrItemPhotos/photoSearchV28` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoSearchV28` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoSearchV28` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
App.Height*0.06
```

### `ScrItemPhotos/photoSearchV28` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Барааны код эсвэл нэрээр хайх"
```

### `ScrItemPhotos/photoSearchV28` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoSearchV28` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ScrItemPhotos/photoSearchV28` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
Set(varPhotoSearchV28,true)
```

### `ScrItemPhotos/photoSearchV28` . **OnSelect**  _(Classic/TextInput@2.3.2)_
```powerfx
Set(varPhotoSearchV28,true)
```

### `ScrItemPhotos/photoSearchV28` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrItemPhotos/photoSearchV28` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrItemPhotos/photoSearchV28` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrItemPhotos/photoSearchV28` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrItemPhotos/photoSearchV28` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoSearchV28` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
App.Width*0.76
```

### `ScrItemPhotos/photoSearchV28` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
App.Width*0.04
```

### `ScrItemPhotos/photoSearchV28` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
App.Height*0.145
```

### `ScrItemPhotos/photoFindV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoFindV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoFindV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoFindV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoFindV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoFindV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoFindV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrItemPhotos/photoFindV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoFindV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoFindV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoFindV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.06
```

### `ScrItemPhotos/photoFindV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoFindV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoFindV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoFindV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28),If(IsBlank(LookUp(colOfflineItems,number=Trim(photoSearchV28.Text))),Set(varPhotoSearchV28,true),Set(varPhotoItemV28,Trim(photoSearchV28.Text));Set(varPhotoSearchV28,false);Select(photoLoadV28)))
```

### `ScrItemPhotos/photoFindV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoFindV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoFindV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoFindV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoFindV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хайх"
```

### `ScrItemPhotos/photoFindV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.14
```

### `ScrItemPhotos/photoFindV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.82
```

### `ScrItemPhotos/photoFindV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.145
```

### `ScrItemPhotos/photoItemV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoItemV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoItemV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoItemV28` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrItemPhotos/photoItemV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoItemV28` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.055,0.062)*App.Height
```

### `ScrItemPhotos/photoItemV28` . **Size**  _(Label@2.5.1)_
```powerfx
19*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoItemV28` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varPhotoItemV28),"Эхлээд бараагаа сонгоорой",varPhotoItemV28 & " · " & Coalesce(varPhotoRecordV28.displayName,""))
```

### `ScrItemPhotos/photoItemV28` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.92,0.92)*App.Width
```

### `ScrItemPhotos/photoItemV28` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.04,0.04)*App.Width
```

### `ScrItemPhotos/photoItemV28` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.215,0.215)*App.Height
```

### `ScrItemPhotos/photoBCTabV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoBCTabV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoBCTabV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoTabV28="bc",Color.White,ColorValue("#163D35"))
```

### `ScrItemPhotos/photoBCTabV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoBCTabV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoBCTabV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoBCTabV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrItemPhotos/photoBCTabV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoTabV28="bc",ColorValue("#246C57"),Color.White)
```

### `ScrItemPhotos/photoBCTabV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoBCTabV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoBCTabV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.055,0.05)*App.Height
```

### `ScrItemPhotos/photoBCTabV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoBCTabV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoBCTabV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoBCTabV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPhotoTabV28,"bc")
```

### `ScrItemPhotos/photoBCTabV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoBCTabV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoBCTabV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoBCTabV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoBCTabV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"BC-д байгаа зураг"
```

### `ScrItemPhotos/photoBCTabV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.25,0.45)*App.Width
```

### `ScrItemPhotos/photoBCTabV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.04,0.04)*App.Width
```

### `ScrItemPhotos/photoBCTabV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.28,0.425)*App.Height
```

### `ScrItemPhotos/photoNewTabV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoNewTabV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoNewTabV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoTabV28="new",Color.White,ColorValue("#163D35"))
```

### `ScrItemPhotos/photoNewTabV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoNewTabV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoNewTabV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoNewTabV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrItemPhotos/photoNewTabV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoTabV28="new",ColorValue("#246C57"),Color.White)
```

### `ScrItemPhotos/photoNewTabV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoNewTabV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoNewTabV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.055,0.05)*App.Height
```

### `ScrItemPhotos/photoNewTabV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoNewTabV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoNewTabV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoNewTabV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPhotoTabV28,"new")
```

### `ScrItemPhotos/photoNewTabV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoNewTabV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoNewTabV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoNewTabV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoNewTabV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Шинэ зураг"
```

### `ScrItemPhotos/photoNewTabV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.25,0.45)*App.Width
```

### `ScrItemPhotos/photoNewTabV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.31,0.51)*App.Width
```

### `ScrItemPhotos/photoNewTabV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.28,0.425)*App.Height
```

### `ScrItemPhotos/photoPreviewV28` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoPreviewV28` . **AccessibleLabel**  _(Image@2.2.3)_
```powerfx
"Зураг · дарж томруулна"
```

### `ScrItemPhotos/photoPreviewV28` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoPreviewV28` . **Fill**  _(Image@2.2.3)_
```powerfx
ColorValue("#E7EDE7")
```

### `ScrItemPhotos/photoPreviewV28` . **Height**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.53,0.22)*App.Height
```

### `ScrItemPhotos/photoPreviewV28` . **Image**  _(Image@2.2.3)_
```powerfx
If(varPhotoTabV28="new",varPhotoNewV28,varPhotoServerV28)
```

### `ScrItemPhotos/photoPreviewV28` . **OnSelect**  _(Image@2.2.3)_
```powerfx
If(!varPhotoBusyV28 && !varPhotoConfirmV28 && !IsBlank(Self.Image),Set(varPhotoZoomV28,true))
```

### `ScrItemPhotos/photoPreviewV28` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.52,0.92)*App.Width
```

### `ScrItemPhotos/photoPreviewV28` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.04,0.04)*App.Width
```

### `ScrItemPhotos/photoPreviewV28` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.35,0.49)*App.Height
```

### `ScrItemPhotos/photoEmptyV28` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrItemPhotos/photoEmptyV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoEmptyV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoEmptyV28` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrItemPhotos/photoEmptyV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoEmptyV28` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.12,0.1)*App.Height
```

### `ScrItemPhotos/photoEmptyV28` . **Size**  _(Label@2.5.1)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoEmptyV28` . **Text**  _(Label@2.5.1)_
```powerfx
If(varPhotoBusyV28,"Зургийг уншиж байна…",IsBlank(varPhotoItemV28),"Бараагаа хайж сонгоно уу",varPhotoTabV28="new","Зураг аваарай эсвэл төхөөрөмжөөсөө сонгоорой","Энэ бараанд BC зураг хараахан алга")
```

### `ScrItemPhotos/photoEmptyV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(photoPreviewV28.Image))
```

### `ScrItemPhotos/photoEmptyV28` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.4,0.76)*App.Width
```

### `ScrItemPhotos/photoEmptyV28` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.1,0.12)*App.Width
```

### `ScrItemPhotos/photoEmptyV28` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.53,0.54)*App.Height
```

### `ScrItemPhotos/photoCameraV28` . **Visible**  _(AddMedia@2.2.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoCameraV28` . **AccessibleLabel**  _(AddMedia@2.2.1)_
```powerfx
"Зураг авах"
```

### `ScrItemPhotos/photoCameraV28` . **Align**  _(AddMedia@2.2.1)_
```powerfx
Align.Right
```

### `ScrItemPhotos/photoCameraV28` . **BorderColor**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoCameraV28` . **BorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoCameraV28` . **ChangePictureText**  _(AddMedia@2.2.1)_
```powerfx
"Зураг авах"
```

### `ScrItemPhotos/photoCameraV28` . **Color**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoCameraV28` . **DisplayMode**  _(AddMedia@2.2.1)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,If(varPhotoBusyV28 || IsBlank(varPhotoItemV28),DisplayMode.Disabled,DisplayMode.Edit))
```

### `ScrItemPhotos/photoCameraV28` . **Fill**  _(AddMedia@2.2.1)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoCameraV28` . **FocusedBorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoCameraV28` . **Height**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.08,0.06)*App.Height
```

### `ScrItemPhotos/photoCameraV28` . **OnChange**  _(AddMedia@2.2.1)_
```powerfx
If(!IsBlank(photoCameraV28.Media),
Set(varPhotoSourceV29,"camera");Set(varPhotoNewV28,photoCameraV28.Media);
Set(varPhotoNewItemV28,varPhotoItemV28);Set(varPhotoTabV28,"new");
Set(varPhotoMessageV28,"Зураг бэлэн. Preview-гээ шалгаад BC-д зураг илгээх товчийг дарна уу."))
```

### `ScrItemPhotos/photoCameraV28` . **Size**  _(AddMedia@2.2.1)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoCameraV28` . **Text**  _(AddMedia@2.2.1)_
```powerfx
"Зураг авах"
```

### `ScrItemPhotos/photoCameraV28` . **UseMobileCamera**  _(AddMedia@2.2.1)_
```powerfx
true
```

### `ScrItemPhotos/photoCameraV28` . **Width**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.17,0.45)*App.Width
```

### `ScrItemPhotos/photoCameraV28` . **X**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.6,0.04)*App.Width
```

### `ScrItemPhotos/photoCameraV28` . **Y**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.55,0.73)*App.Height
```

### `ScrItemPhotos/photoPickV28` . **Visible**  _(AddMedia@2.2.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoPickV28` . **AccessibleLabel**  _(AddMedia@2.2.1)_
```powerfx
"Файлаас сонгох"
```

### `ScrItemPhotos/photoPickV28` . **Align**  _(AddMedia@2.2.1)_
```powerfx
Align.Right
```

### `ScrItemPhotos/photoPickV28` . **BorderColor**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoPickV28` . **BorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoPickV28` . **ChangePictureText**  _(AddMedia@2.2.1)_
```powerfx
"Файлаас сонгох"
```

### `ScrItemPhotos/photoPickV28` . **Color**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoPickV28` . **DisplayMode**  _(AddMedia@2.2.1)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,If(varPhotoBusyV28 || IsBlank(varPhotoItemV28),DisplayMode.Disabled,DisplayMode.Edit))
```

### `ScrItemPhotos/photoPickV28` . **Fill**  _(AddMedia@2.2.1)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoPickV28` . **FocusedBorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoPickV28` . **Height**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.08,0.06)*App.Height
```

### `ScrItemPhotos/photoPickV28` . **OnChange**  _(AddMedia@2.2.1)_
```powerfx
If(!IsBlank(photoPickV28.Media),
Set(varPhotoSourceV29,"file");Set(varPhotoNewV28,photoPickV28.Media);
Set(varPhotoNewItemV28,varPhotoItemV28);Set(varPhotoTabV28,"new");
Set(varPhotoMessageV28,"Зураг бэлэн. Preview-гээ шалгаад BC-д зураг илгээх товчийг дарна уу."))
```

### `ScrItemPhotos/photoPickV28` . **Size**  _(AddMedia@2.2.1)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoPickV28` . **Text**  _(AddMedia@2.2.1)_
```powerfx
"Файлаас сонгох"
```

### `ScrItemPhotos/photoPickV28` . **Width**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.17,0.45)*App.Width
```

### `ScrItemPhotos/photoPickV28` . **X**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.79,0.51)*App.Width
```

### `ScrItemPhotos/photoPickV28` . **Y**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.55,0.73)*App.Height
```

### `ScrItemPhotos/photoStatusV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoStatusV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoStatusV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoStatusV28` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrItemPhotos/photoStatusV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoStatusV28` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.11,0.075)*App.Height
```

### `ScrItemPhotos/photoStatusV28` . **Size**  _(Label@2.5.1)_
```powerfx
15*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoStatusV28` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(varPhotoMessageV28,If(varPhotoBusyV28,"Зургийг уншиж байна…",IsBlank(varPhotoItemV28),"Бараагаа сонгоно уу.",IsBlank(varPhotoServerV28) && IsBlank(varPhotoNewV28),"BC зураг алга. Зураг авах эсвэл файлаас сонгоно уу.","Зураг дээр дарж томруулж үзнэ. Upload нь BC барааны үндсэн зургийг шинэчилнэ."))
```

### `ScrItemPhotos/photoStatusV28` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.36,0.92)*App.Width
```

### `ScrItemPhotos/photoStatusV28` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.6,0.04)*App.Width
```

### `ScrItemPhotos/photoStatusV28` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.65,0.8)*App.Height
```

### `ScrItemPhotos/photoUploadV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoUploadV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoUploadV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoUploadV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoUploadV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoUploadV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoUploadV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,If(varPhotoBusyV28 || !Connection.Connected || IsBlank(varPhotoItemV28) || IsBlank(varPhotoNewV28),DisplayMode.Disabled,DisplayMode.Edit))
```

### `ScrItemPhotos/photoUploadV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoUploadV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoUploadV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoUploadV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.09,0.065)*App.Height
```

### `ScrItemPhotos/photoUploadV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoUploadV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoUploadV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoUploadV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!varPhotoBusyV28 && !IsBlank(varPhotoNewV28) && varPhotoNewItemV28=varPhotoItemV28,
Set(varPhotoTabV28,"new");Set(varPhotoConfirmV28,true))
```

### `ScrItemPhotos/photoUploadV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoUploadV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoUploadV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoUploadV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoUploadV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28,"Түр хүлээнэ үү…","BC-д зураг илгээх  ↑")
```

### `ScrItemPhotos/photoUploadV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.36,0.67)*App.Width
```

### `ScrItemPhotos/photoUploadV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.6,0.04)*App.Width
```

### `ScrItemPhotos/photoUploadV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.79,0.89)*App.Height
```

### `ScrItemPhotos/photoRefreshV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoRefreshV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoRefreshV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoRefreshV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoRefreshV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoRefreshV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoRefreshV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,If(varPhotoBusyV28 || !Connection.Connected || IsBlank(varPhotoItemV28),DisplayMode.Disabled,DisplayMode.Edit))
```

### `ScrItemPhotos/photoRefreshV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoRefreshV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoRefreshV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoRefreshV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.06,0.065)*App.Height
```

### `ScrItemPhotos/photoRefreshV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoRefreshV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoRefreshV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoRefreshV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(photoLoadV28)
```

### `ScrItemPhotos/photoRefreshV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoRefreshV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoRefreshV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoRefreshV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoRefreshV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Шинэчлэх"
```

### `ScrItemPhotos/photoRefreshV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.2,0.23)*App.Width
```

### `ScrItemPhotos/photoRefreshV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.36,0.73)*App.Width
```

### `ScrItemPhotos/photoRefreshV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.9,0.89)*App.Height
```

### `ScrItemPhotos/photoInfoV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoInfoV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoInfoV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoInfoV28` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#E4EEE6")
```

### `ScrItemPhotos/photoInfoV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoInfoV28` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.23,0.125)*App.Height
```

### `ScrItemPhotos/photoInfoV28` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
Self.Width*0.035
```

### `ScrItemPhotos/photoInfoV28` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
Self.Width*0.035
```

### `ScrItemPhotos/photoInfoV28` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
Self.Height*0.06
```

### `ScrItemPhotos/photoInfoV28` . **Size**  _(Label@2.5.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoInfoV28` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varPhotoItemV28),"Бараа сонгоход үзүүлэлтүүд энд харагдана", "Нэгж: " & Coalesce(varPhotoRecordV28.unitOfMeasure,"—") & "  ·  Ангилал: " & Coalesce(varPhotoRecordV28.itemCategory,"—") & Char(10) & "Үлдэгдэл: " & Text(Sum(colPhotoLocationsV28,Qty),If(Mod(Sum(colPhotoLocationsV28,Qty),1)=0,"#,##0","#,##0.###")) & "  ·  Нэгж өртөг: " & Text(varPhotoRecordV28.unitCost,"#,##0.##") & " ₮" & Char(10) & "Агуулах: " & Coalesce(Concat(FirstN(colPhotoLocationsV28,3),Code & " (" & Text(Qty,If(Mod(Qty,1)=0,"#,##0","#,##0.###")) & ")",", "),"—") & If(CountRows(colPhotoLocationsV28)>3," +" & Text(CountRows(colPhotoLocationsV28)-3),""))
```

### `ScrItemPhotos/photoInfoV28` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.36,0.92)*App.Width
```

### `ScrItemPhotos/photoInfoV28` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.6,0.04)*App.Width
```

### `ScrItemPhotos/photoInfoV28` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,0.29,0.28)*App.Height
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrItemPhotos/photoInfoAsOfV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.025
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Text**  _(Label@2.5.1)_
```powerfx
"Үлдэгдэл шинэчилсэн: " & If(IsBlank(varAutoStockUpdated),"—",Text(varAutoStockUpdated,"mm.dd hh:mm"))
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.92
```

### `ScrItemPhotos/photoInfoAsOfV28` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.04
```

### `ScrItemPhotos/photoInfoAsOfV28` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.965
```

### `ScrItemPhotos/photoUploadSourceV29` . **AccessibleLabel**  _(Image@2.2.3)_
```powerfx
"Зураг · дарж томруулна"
```

### `ScrItemPhotos/photoUploadSourceV29` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoUploadSourceV29` . **Fill**  _(Image@2.2.3)_
```powerfx
ColorValue("#E7EDE7")
```

### `ScrItemPhotos/photoUploadSourceV29` . **Image**  _(Image@2.2.3)_
```powerfx
varPhotoNewV28
```

### `ScrItemPhotos/photoUploadSourceV29` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrItemPhotos/photoResultsV28` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoResultsV28` . **DisplayMode**  _(Gallery@2.15.0)_
```powerfx
If(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrItemPhotos/photoResultsV28` . **Fill**  _(Gallery@2.15.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoResultsV28` . **FocusedBorderThickness**  _(Gallery@2.15.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28` . **Height**  _(Gallery@2.15.0)_
```powerfx
App.Height*0.44
```

### `ScrItemPhotos/photoResultsV28` . **Items**  _(Gallery@2.15.0)_
```powerfx
FirstN(Filter(colOfflineItems,Trim(photoSearchV28.Text) in number || Trim(photoSearchV28.Text) in displayName),6)
```

### `ScrItemPhotos/photoResultsV28` . **OnSelect**  _(Gallery@2.15.0)_
```powerfx
If(!(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28),Set(varPhotoItemV28,ThisItem.number);Set(varPhotoSearchV28,false);Reset(photoSearchV28);Select(photoLoadV28))
```

### `ScrItemPhotos/photoResultsV28` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
App.Height*0.065
```

### `ScrItemPhotos/photoResultsV28` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varPhotoSearchV28 && !IsBlank(Trim(photoSearchV28.Text)))
```

### `ScrItemPhotos/photoResultsV28` . **Width**  _(Gallery@2.15.0)_
```powerfx
App.Width*0.92
```

### `ScrItemPhotos/photoResultsV28` . **X**  _(Gallery@2.15.0)_
```powerfx
App.Width*0.04
```

### `ScrItemPhotos/photoResultsV28` . **Y**  _(Gallery@2.15.0)_
```powerfx
App.Height*0.21
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.TemplateHeight
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **OnSelect**  _(Label@2.5.1)_
```powerfx
If(!(varPhotoBusyV28 || varPhotoConfirmV28 || varPhotoZoomV28),Set(varPhotoItemV28,ThisItem.number);Set(varPhotoSearchV28,false);Reset(photoSearchV28);Select(photoLoadV28))
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **Size**  _(Label@2.5.1)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.number & " · " & ThisItem.displayName
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth*0.87
```

### `ScrItemPhotos/photoResultsV28/photoResultlabel1V28` . **X**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth*0.03
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **Height**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Separator1_3.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
false
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(4)*((App.Width/640))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle2V28` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
ThisItem.number & " " & ThisItem.displayName
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(42)*((App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronRight
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Select(Parent)
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **Tooltip**  _(Classic/Icon@2.5.0)_
```powerfx
"View item details"
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
false
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(50)*((App.Width/640))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - (Self.Width/((App.Width/640))) - 12)*((App.Width/640))
```

### `ScrItemPhotos/photoResultsV28/photoResulticon3V28` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(8)*((App.Height/1136))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
false
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **Width**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))))*((App.Width/640))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `ScrItemPhotos/photoResultsV28/photoResultrectangle4V28` . **Y**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Self.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ScrItemPhotos/photoZoomV28` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoZoomV28` . **Fill**  _(Image@2.2.3)_
```powerfx
ColorValue("#F3F6F2")
```

### `ScrItemPhotos/photoZoomV28` . **Height**  _(Image@2.2.3)_
```powerfx
App.Height*0.88
```

### `ScrItemPhotos/photoZoomV28` . **Image**  _(Image@2.2.3)_
```powerfx
photoPreviewV28.Image
```

### `ScrItemPhotos/photoZoomV28` . **OnSelect**  _(Image@2.2.3)_
```powerfx
Set(varPhotoZoomV28,false)
```

### `ScrItemPhotos/photoZoomV28` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varPhotoZoomV28)
```

### `ScrItemPhotos/photoZoomV28` . **Width**  _(Image@2.2.3)_
```powerfx
App.Width
```

### `ScrItemPhotos/photoZoomV28` . **Y**  _(Image@2.2.3)_
```powerfx
App.Height*0.12
```

### `ScrItemPhotos/photoZoomBackV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoZoomBackV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoZoomBackV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoZoomBackV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoZoomBackV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoZoomBackV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoZoomBackV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoZoomBackV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoZoomBackV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.07
```

### `ScrItemPhotos/photoZoomBackV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoZoomBackV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoZoomBackV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoZoomBackV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPhotoZoomV28,false)
```

### `ScrItemPhotos/photoZoomBackV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoZoomBackV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoZoomBackV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoZoomBackV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoZoomBackV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зураг хаах  ×"
```

### `ScrItemPhotos/photoZoomBackV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varPhotoZoomV28)
```

### `ScrItemPhotos/photoZoomBackV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.28
```

### `ScrItemPhotos/photoZoomBackV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.68
```

### `ScrItemPhotos/photoZoomBackV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.03
```

### `ScrItemPhotos/photoConfirmCardV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoConfirmCardV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoConfirmCardV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoConfirmCardV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoConfirmCardV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoConfirmCardV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
DisplayMode.View
```

### `ScrItemPhotos/photoConfirmCardV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E0EDE5")
```

### `ScrItemPhotos/photoConfirmCardV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoConfirmCardV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoConfirmCardV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.42
```

### `ScrItemPhotos/photoConfirmCardV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoConfirmCardV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoConfirmCardV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoConfirmCardV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoConfirmCardV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoConfirmCardV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoConfirmCardV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoConfirmCardV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varPhotoConfirmV28)
```

### `ScrItemPhotos/photoConfirmCardV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.88
```

### `ScrItemPhotos/photoConfirmCardV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.06
```

### `ScrItemPhotos/photoConfirmCardV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.30
```

### `ScrItemPhotos/photoConfirmTextV28` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrItemPhotos/photoConfirmTextV28` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoConfirmTextV28` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrItemPhotos/photoConfirmTextV28` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoConfirmTextV28` . **Height**  _(Label@2.5.1)_
```powerfx
App.Height*0.19
```

### `ScrItemPhotos/photoConfirmTextV28` . **Size**  _(Label@2.5.1)_
```powerfx
25*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoConfirmTextV28` . **Text**  _(Label@2.5.1)_
```powerfx
varPhotoItemV28 & " барааны BC үндсэн зургийг шинэ зургаар солих уу?"
```

### `ScrItemPhotos/photoConfirmTextV28` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varPhotoConfirmV28)
```

### `ScrItemPhotos/photoConfirmTextV28` . **Width**  _(Label@2.5.1)_
```powerfx
App.Width*0.78
```

### `ScrItemPhotos/photoConfirmTextV28` . **X**  _(Label@2.5.1)_
```powerfx
App.Width*0.11
```

### `ScrItemPhotos/photoConfirmTextV28` . **Y**  _(Label@2.5.1)_
```powerfx
App.Height*0.34
```

### `ScrItemPhotos/photoConfirmYesV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoConfirmYesV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoConfirmYesV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoConfirmYesV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoConfirmYesV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoConfirmYesV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varPhotoBusyV28,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrItemPhotos/photoConfirmYesV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoConfirmYesV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoConfirmYesV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoConfirmYesV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.08
```

### `ScrItemPhotos/photoConfirmYesV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoConfirmYesV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoConfirmYesV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoConfirmYesV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!varPhotoBusyV28,
If(!Connection.Connected,
Set(varPhotoConfirmV28,false);Notify("BC-д зураг илгээхийн тулд интернетэд холбогдоно уу.",NotificationType.Warning),
If(IsBlank(varPhotoItemV28) || IsBlank(varPhotoNewV28) || varPhotoNewItemV28<>varPhotoItemV28,
Set(varPhotoConfirmV28,false);Notify("Сонгосон барааны зураг бэлэн биш байна. Зургаа дахин сонгоно уу.",NotificationType.Warning),
Set(varPhotoMessageV28,"Зургийг илгээхэд бэлдэж байна…");
IfError(
Set(varPhotoUploadDataV29,Substitute(JSON(photoPreviewV28.Image,JSONFormat.IncludeBinaryData),Char(34),""));
If(StartsWith(varPhotoUploadDataV29,"data:image") && ";base64," in Left(varPhotoUploadDataV29,100),
Set(varPhotoBusyV28,true);Set(varPhotoConfirmV28,false);
Set(varPhotoMessageV28,"BC-д зураг илгээж байна…");
IfError('PowerAppV2->Getrecord(V3)'.Run(varPhotoItemV28,varPhotoUploadDataV29);true,
Set(varPhotoMessageV28,"BC зураг илгээх алдаа: " & FirstError.Message);
Notify(varPhotoMessageV28,NotificationType.Error);false,
Set(varPhotoMessageV28,"Зураг илгээх хүсэлт амжилттай дууслаа. BC-ийн зургийг Шинэчлэх товчоор шалгаж болно.");
Notify("Зураг илгээлээ.",NotificationType.Success);true),
Set(varPhotoMessageV28,"Зургийг хөрвүүлж чадсангүй. JPG эсвэл PNG зураг дахин сонгоно уу.");
Notify(varPhotoMessageV28,NotificationType.Error);false),
Set(varPhotoMessageV28,"Зураг илгээх алдаа: " & FirstError.Message);
Notify(varPhotoMessageV28,NotificationType.Error);false);
Set(varPhotoConfirmV28,false);Set(varPhotoBusyV28,false);Set(varPhotoUploadDataV29,Blank())
)))
```

### `ScrItemPhotos/photoConfirmYesV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoConfirmYesV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoConfirmYesV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoConfirmYesV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoConfirmYesV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тийм, илгээх"
```

### `ScrItemPhotos/photoConfirmYesV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varPhotoConfirmV28)
```

### `ScrItemPhotos/photoConfirmYesV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.40
```

### `ScrItemPhotos/photoConfirmYesV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.49
```

### `ScrItemPhotos/photoConfirmYesV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.59
```

### `ScrItemPhotos/photoConfirmNoV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DDE6DF")
```

### `ScrItemPhotos/photoConfirmNoV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoConfirmNoV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrItemPhotos/photoConfirmNoV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `ScrItemPhotos/photoConfirmNoV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `ScrItemPhotos/photoConfirmNoV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoConfirmNoV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `ScrItemPhotos/photoConfirmNoV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrItemPhotos/photoConfirmNoV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.08
```

### `ScrItemPhotos/photoConfirmNoV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrItemPhotos/photoConfirmNoV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `ScrItemPhotos/photoConfirmNoV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `ScrItemPhotos/photoConfirmNoV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPhotoConfirmV28,false)
```

### `ScrItemPhotos/photoConfirmNoV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrItemPhotos/photoConfirmNoV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/photoConfirmNoV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `ScrItemPhotos/photoConfirmNoV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `ScrItemPhotos/photoConfirmNoV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Буцах"
```

### `ScrItemPhotos/photoConfirmNoV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varPhotoConfirmV28)
```

### `ScrItemPhotos/photoConfirmNoV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.34
```

### `ScrItemPhotos/photoConfirmNoV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
App.Width*0.11
```

### `ScrItemPhotos/photoConfirmNoV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
App.Height*0.59
```

### `ScrItemPhotos/pgDenied220` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrItemPhotos/pgDenied220` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrItemPhotos/pgDenied220` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrItemPhotos/pgDenied220` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrItemPhotos/pgDenied220` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrItemPhotos/pgDenied220` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrItemPhotos/pgDenied220` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrItemPhotos/pgDenied220` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrItemPhotos/pgDenied220` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrItemPhotos/pgDenied220` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

