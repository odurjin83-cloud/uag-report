# Master Edit — Power Fx formulas

### `Master Edit` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `Master Edit` . **Fill**  _(Screen)_
```powerfx
RGBA(255,255,255,1)
```

### `Master Edit` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `Master Edit` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `Master Edit` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `Master Edit/Icon11` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `Master Edit/Icon11` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Master Edit/Icon11` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Master Edit/Icon11` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Master Edit/Icon11` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `Master Edit/Icon11` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Height/1136))
```

### `Master Edit/Icon11` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Home
```

### `Master Edit/Icon11` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate('нүүр')
```

### `Master Edit/Icon11` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(64)*((App.Width/640))
```

### `Master Edit/Icon11` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(21)*((App.Width/640))
```

### `Master Edit/Icon11` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(1053)*((App.Height/1136))
```

### `Master Edit/Arrow7` . **Visible**  _(Arrow@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `Master Edit/Arrow7` . **BorderColor**  _(Arrow@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Master Edit/Arrow7` . **Fill**  _(Arrow@2.3.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `Master Edit/Arrow7` . **Height**  _(Arrow@2.3.0)_
```powerfx
(100)*((App.Height/1136))
```

### `Master Edit/Arrow7` . **OnSelect**  _(Arrow@2.3.0)_
```powerfx
Navigate('Бараа засвар хийх')
```

### `Master Edit/Arrow7` . **Width**  _(Arrow@2.3.0)_
```powerfx
(100)*((App.Width/640))
```

### `Master Edit/Arrow7` . **X**  _(Arrow@2.3.0)_
```powerfx
(21)*((App.Width/640))
```

### `Master Edit/Arrow7` . **Y**  _(Arrow@2.3.0)_
```powerfx
(24)*((App.Height/1136))
```

### `Master Edit/Label33` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `Master Edit/Label33` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `Master Edit/Label33` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Master Edit/Label33` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `Master Edit/Label33` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `Master Edit/Label33` . **Height**  _(Label@2.5.1)_
```powerfx
(84)*((App.Height/1136))
```

### `Master Edit/Label33` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `Master Edit/Label33` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `Master Edit/Label33` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `Master Edit/Label33` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `Master Edit/Label33` . **Size**  _(Label@2.5.1)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `Master Edit/Label33` . **Text**  _(Label@2.5.1)_
```powerfx
"Бараан"
```

### `Master Edit/Label33` . **Width**  _(Label@2.5.1)_
```powerfx
(196)*((App.Width/640))
```

### `Master Edit/Label33` . **X**  _(Label@2.5.1)_
```powerfx
(21)*((App.Width/640))
```

### `Master Edit/Label33` . **Y**  _(Label@2.5.1)_
```powerfx
(151)*((App.Height/1136))
```

### `Master Edit/pgDenied454` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `Master Edit/pgDenied454` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `Master Edit/pgDenied454` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `Master Edit/pgDenied454` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `Master Edit/pgDenied454` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `Master Edit/pgDenied454` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `Master Edit/pgDenied454` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `Master Edit/pgDenied454` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `Master Edit/pgDenied454` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `Master Edit/pgDenied454` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

