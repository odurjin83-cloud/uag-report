# IMPORT — Power Fx formulas

### `IMPORT` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `IMPORT` . **Fill**  _(Screen)_
```powerfx
RGBA(255,255,255,1)
```

### `IMPORT` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `IMPORT` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `IMPORT` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `IMPORT/Label6` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `IMPORT/Label6` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `IMPORT/Label6` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `IMPORT/Label6` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `IMPORT/Label6` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `IMPORT/Label6` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `IMPORT/Label6` . **Height**  _(Label@2.5.1)_
```powerfx
(98)*((App.Height/1136))
```

### `IMPORT/Label6` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `IMPORT/Label6` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `IMPORT/Label6` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `IMPORT/Label6` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `IMPORT/Label6` . **Size**  _(Label@2.5.1)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `IMPORT/Label6` . **Text**  _(Label@2.5.1)_
```powerfx
"CONFIGURATION PACKAGE ЗАСАХ МЭДЭЭЛЭЛ"
```

### `IMPORT/Label6` . **Width**  _(Label@2.5.1)_
```powerfx
(560)*((App.Width/640))
```

### `IMPORT/Label6` . **X**  _(Label@2.5.1)_
```powerfx
(39)*((App.Width/640))
```

### `IMPORT/Label6` . **Y**  _(Label@2.5.1)_
```powerfx
(48)*((App.Height/1136))
```

### `IMPORT/Icon9` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `IMPORT/Icon9` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `IMPORT/Icon9` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `IMPORT/Icon9` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `IMPORT/Icon9` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `IMPORT/Icon9` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Height/1136))
```

### `IMPORT/Icon9` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Home
```

### `IMPORT/Icon9` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate('нүүр')
```

### `IMPORT/Icon9` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Width/640))
```

### `IMPORT/Icon9` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(18)*((App.Width/640))
```

### `IMPORT/Icon9` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(1047)*((App.Height/1136))
```

### `IMPORT/pgDenied314` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `IMPORT/pgDenied314` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `IMPORT/pgDenied314` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `IMPORT/pgDenied314` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `IMPORT/pgDenied314` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `IMPORT/pgDenied314` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `IMPORT/pgDenied314` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `IMPORT/pgDenied314` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `IMPORT/pgDenied314` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `IMPORT/pgDenied314` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

