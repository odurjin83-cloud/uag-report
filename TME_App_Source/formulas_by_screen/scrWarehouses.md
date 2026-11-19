# scrWarehouses — Power Fx formulas

### `scrWarehouses` . **Fill**  _(Screen)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),ColorValue("#F2F6F5")
)
```

### `scrWarehouses` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `scrWarehouses` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `scrWarehouses` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Set(varShowWarehouseList,false);Set(varCountMenuV21,false)
)
```

### `scrWarehouses` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `scrWarehouses/countItemCardV21` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#EEECE9"),ColorFade(Self.Fill, -15%)
)
```

### `scrWarehouses/countItemCardV21` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(1)*App.Width/360,0
)
```

### `scrWarehouses/countItemCardV21` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countItemCardV21` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countItemCardV21` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countItemCardV21` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.View)
```

### `scrWarehouses/countItemCardV21` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,Color.White
)
```

### `scrWarehouses/countItemCardV21` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countItemCardV21` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/countItemCardV21` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(202)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,428*App.Height/820,242*App.Height/1136)
)
```

### `scrWarehouses/countItemCardV21` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countItemCardV21` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `scrWarehouses/countItemCardV21` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#338963")
```

### `scrWarehouses/countItemCardV21` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countItemCardV21` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countItemCardV21` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countItemCardV21` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countItemCardV21` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countItemCardV21` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countItemCardV21` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#174B36")
```

### `scrWarehouses/countItemCardV21` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(18)*App.Width/360,18
)
```

### `scrWarehouses/countItemCardV21` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(18)*App.Width/360,18
)
```

### `scrWarehouses/countItemCardV21` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(18)*App.Width/360,18
)
```

### `scrWarehouses/countItemCardV21` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(18)*App.Width/360,18
)
```

### `scrWarehouses/countItemCardV21` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(18)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countItemCardV21` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/countItemCardV21` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(332)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,534*App.Width/1180,600*App.Width/640)
)
```

### `scrWarehouses/countItemCardV21` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/countItemCardV21` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(55)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,178*App.Height/820,244*App.Height/1136)
)
```

### `scrWarehouses/countStockCardV21` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countStockCardV21` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/countStockCardV21` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countStockCardV21` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countStockCardV21` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countStockCardV21` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.View)
```

### `scrWarehouses/countStockCardV21` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),Color.White
)
```

### `scrWarehouses/countStockCardV21` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countStockCardV21` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/countStockCardV21` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(58)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,145*App.Height/820,134*App.Height/1136)
)
```

### `scrWarehouses/countStockCardV21` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countStockCardV21` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `scrWarehouses/countStockCardV21` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#338963")
```

### `scrWarehouses/countStockCardV21` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countStockCardV21` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countStockCardV21` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countStockCardV21` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countStockCardV21` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countStockCardV21` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countStockCardV21` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#174B36")
```

### `scrWarehouses/countStockCardV21` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countStockCardV21` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countStockCardV21` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countStockCardV21` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countStockCardV21` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(18)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countStockCardV21` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/countStockCardV21` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(96)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,270*App.Width/1180,290*App.Width/640)
)
```

### `scrWarehouses/countStockCardV21` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(30)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,590*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/countStockCardV21` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(181)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,178*App.Height/820,502*App.Height/1136)
)
```

### `scrWarehouses/countBinCardV21` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countBinCardV21` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/countBinCardV21` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countBinCardV21` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countBinCardV21` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countBinCardV21` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.View)
```

### `scrWarehouses/countBinCardV21` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),Color.White
)
```

### `scrWarehouses/countBinCardV21` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countBinCardV21` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/countBinCardV21` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(58)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,145*App.Height/820,134*App.Height/1136)
)
```

### `scrWarehouses/countBinCardV21` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countBinCardV21` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `scrWarehouses/countBinCardV21` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#338963")
```

### `scrWarehouses/countBinCardV21` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countBinCardV21` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countBinCardV21` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countBinCardV21` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countBinCardV21` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countBinCardV21` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countBinCardV21` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#174B36")
```

### `scrWarehouses/countBinCardV21` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countBinCardV21` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countBinCardV21` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countBinCardV21` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countBinCardV21` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(18)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countBinCardV21` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/countBinCardV21` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(96)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,276*App.Width/1180,290*App.Width/640)
)
```

### `scrWarehouses/countBinCardV21` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(133)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,880*App.Width/1180,330*App.Width/640)
)
```

### `scrWarehouses/countBinCardV21` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(181)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,178*App.Height/820,502*App.Height/1136)
)
```

### `scrWarehouses/countInputCardV21` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countInputCardV21` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/countInputCardV21` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countInputCardV21` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countInputCardV21` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countInputCardV21` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.View)
```

### `scrWarehouses/countInputCardV21` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#FFF6E6"),Color.White
)
```

### `scrWarehouses/countInputCardV21` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countInputCardV21` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/countInputCardV21` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(58)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,262*App.Height/820,232*App.Height/1136)
)
```

### `scrWarehouses/countInputCardV21` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countInputCardV21` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `scrWarehouses/countInputCardV21` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#338963")
```

### `scrWarehouses/countInputCardV21` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countInputCardV21` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countInputCardV21` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countInputCardV21` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countInputCardV21` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countInputCardV21` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countInputCardV21` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#174B36")
```

### `scrWarehouses/countInputCardV21` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countInputCardV21` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countInputCardV21` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countInputCardV21` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(9)*App.Width/360,18
)
```

### `scrWarehouses/countInputCardV21` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(18)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countInputCardV21` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/countInputCardV21` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(96)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,566*App.Width/1180,600*App.Width/640)
)
```

### `scrWarehouses/countInputCardV21` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(236)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,590*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/countInputCardV21` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(181)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,344*App.Height/820,652*App.Height/1136)
)
```

### `scrWarehouses/Rectangle5` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Rectangle5` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle5` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#DFE8E2")
)
```

### `scrWarehouses/Rectangle5` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle5` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(85)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,1*App.Height/820,1*App.Height/1136)
)
```

### `scrWarehouses/Rectangle5` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(360)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,1132*App.Width/1180,600*App.Width/640)
)
```

### `scrWarehouses/Rectangle5` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(0)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/Rectangle5` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(635)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,78*App.Height/820,76*App.Height/1136)
)
```

### `scrWarehouses/Rectangle5_1` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle5_1` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E2DEDA"),ColorValue("#DFE8E2")
)
```

### `scrWarehouses/Rectangle5_1` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle5_1` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(1)*App.Height/720,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Height / 820, 1 * App.Height / 1136)
)
```

### `scrWarehouses/Rectangle5_1` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!varShowWarehouseList && !varCountMenuV21,false
))
```

### `scrWarehouses/Rectangle5_1` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(360)*App.Width/360,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1132 * App.Width / 1180, 640 * App.Width / 640)
)
```

### `scrWarehouses/Rectangle5_1` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(0)*App.Width/360,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 24 * App.Width / 1180, 0 * App.Width / 640)
)
```

### `scrWarehouses/Rectangle5_1` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(635)*App.Height/720,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 145 * App.Height / 820, 111 * App.Height / 1136)
)
```

### `scrWarehouses/Rectangle5_2` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle5_2` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/Rectangle5_2` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle5_2` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 535 * App.Height / 820, 1 * App.Height / 1136)
```

### `scrWarehouses/Rectangle5_2` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Rectangle5_2` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Width / 1180, 640 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_2` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 598 * App.Width / 1180, 0 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_2` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 166 * App.Height / 820, 510 * App.Height / 1136)
```

### `scrWarehouses/countPhotoOpenV28` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#E2DEDA"),ColorValue("#DDE6DF")
)
```

### `scrWarehouses/countPhotoOpenV28` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(1)*App.Width/360,0
)
```

### `scrWarehouses/countPhotoOpenV28` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#163D35")
)
```

### `scrWarehouses/countPhotoOpenV28` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countPhotoOpenV28` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#687F79")
```

### `scrWarehouses/countPhotoOpenV28` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5ECE7")
```

### `scrWarehouses/countPhotoOpenV28` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountSaving,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/countPhotoOpenV28` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,ColorValue("#E4EEE6")
)
```

### `scrWarehouses/countPhotoOpenV28` . **FocusedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F16535")
```

### `scrWarehouses/countPhotoOpenV28` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/countPhotoOpenV28` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(45)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,54*App.Height/820,56*App.Height/1136)
)
```

### `scrWarehouses/countPhotoOpenV28` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countPhotoOpenV28` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#163D35")
```

### `scrWarehouses/countPhotoOpenV28` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DCECE4")
```

### `scrWarehouses/countPhotoOpenV28` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(varItem.number),Notify("Эхлээд бараагаа сонгоно уу.",NotificationType.Information),Set(varPhotoRequestedV28,varItem.number);Set(varPhotoReturnV28,"count");Navigate(ScrItemPhotos,ScreenTransition.Fade))
```

### `scrWarehouses/countPhotoOpenV28` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countPhotoOpenV28` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countPhotoOpenV28` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#246C57")
```

### `scrWarehouses/countPhotoOpenV28` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(12)*App.Width/360,16
)
```

### `scrWarehouses/countPhotoOpenV28` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(12)*App.Width/360,16
)
```

### `scrWarehouses/countPhotoOpenV28` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(12)*App.Width/360,16
)
```

### `scrWarehouses/countPhotoOpenV28` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(12)*App.Width/360,16
)
```

### `scrWarehouses/countPhotoOpenV28` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(App.Width/360,App.Height/720),20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/countPhotoOpenV28` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"    Зураг","Зураг авах · харах · илгээх   →"
)
```

### `scrWarehouses/countPhotoOpenV28` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList && !varCountMenuV21
))
```

### `scrWarehouses/countPhotoOpenV28` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(158)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,496*App.Width/1180,592*App.Width/640)
)
```

### `scrWarehouses/countPhotoOpenV28` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(16)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,640*App.Width/1180,24*App.Width/640)
)
```

### `scrWarehouses/countPhotoOpenV28` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(497)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,695*App.Height/820,982*App.Height/1136)
)
```

### `scrWarehouses/Rectangle5_3` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle5_3` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/Rectangle5_3` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle5_3` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Height / 820, 1 * App.Height / 1136)
```

### `scrWarehouses/Rectangle5_3` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Rectangle5_3` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 514 * App.Width / 1180, 640 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_3` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 626 * App.Width / 1180, 0 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_3` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 309 * App.Height / 820, 686 * App.Height / 1136)
```

### `scrWarehouses/Rectangle5_4` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Rectangle5_4` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle5_4` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/Rectangle5_4` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle5_4` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Height / 820, 1 * App.Height / 1136)
```

### `scrWarehouses/Rectangle5_4` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1132 * App.Width / 1180, 640 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_4` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 24 * App.Width / 1180, 0 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_4` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 725 * App.Height / 820, 1057 * App.Height / 1136)
```

### `scrWarehouses/btnChangeWarehouse` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Left,Align.Center
)
```

### `scrWarehouses/btnChangeWarehouse` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/btnChangeWarehouse` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),Color.White
)
```

### `scrWarehouses/btnChangeWarehouse` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/btnChangeWarehouse` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/btnChangeWarehouse` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),ColorValue("#246F50")
)
```

### `scrWarehouses/btnChangeWarehouse` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/btnChangeWarehouse` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/btnChangeWarehouse` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(25)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,44*App.Height/820,44*App.Height/1136)
)
```

### `scrWarehouses/btnChangeWarehouse` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/btnChangeWarehouse` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `scrWarehouses/btnChangeWarehouse` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#338963")
```

### `scrWarehouses/btnChangeWarehouse` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varShowWarehouseList,!varShowWarehouseList)
```

### `scrWarehouses/btnChangeWarehouse` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/btnChangeWarehouse` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/btnChangeWarehouse` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#174B36")
```

### `scrWarehouses/btnChangeWarehouse` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(App.Width/360,App.Height/720),16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/btnChangeWarehouse` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(varShowWarehouseList,"Хаах",varLocationCode & "  ⌄"),If(varShowWarehouseList,"Хаах","Байршил солих")
)
```

### `scrWarehouses/btnChangeWarehouse` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (!IsBlank(varItem.number) && CountRows(colCountLocationsV19)>1)
```

### `scrWarehouses/btnChangeWarehouse` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(185)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,200*App.Width/1180,240*App.Width/640)
)
```

### `scrWarehouses/btnChangeWarehouse` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(51)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,330*App.Width/1180,350*App.Width/640)
)
```

### `scrWarehouses/btnChangeWarehouse` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(28)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,520*App.Height/820,418*App.Height/1136)
)
```

### `scrWarehouses/Агуулах` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Агуулах` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Агуулах` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Агуулах` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Агуулах` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Агуулах` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Агуулах` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/Агуулах` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 42 * App.Height / 820, 40 * App.Height / 1136)
```

### `scrWarehouses/Агуулах` . **Size**  _(Label@2.5.1)_
```powerfx
(Switch(
    true,
    Len(Self.Text) > 12, 14,
    Len(Self.Text) > 10, 16,
    Len(Self.Text) > 8, 18,
    18
))*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/Агуулах` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(varLocationCode),
    "Агуулах сонгоно уу",
    varLocationCode & " · " & varLocationName
)
```

### `scrWarehouses/Агуулах` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Агуулах` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 880 * App.Width / 1180, 381 * App.Width / 640)
```

### `scrWarehouses/Агуулах` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 94 * App.Width / 1180, 100 * App.Width / 640)
```

### `scrWarehouses/Агуулах` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 91 * App.Height / 820, 65 * App.Height / 1136)
```

### `scrWarehouses/phoneCountScannerIcon` . **X**  _(Image@2.2.3)_
```powerfx
(16)*App.Width/360
```

### `scrWarehouses/phoneCountScannerIcon` . **Y**  _(Image@2.2.3)_
```powerfx
(648)*App.Height/720
```

### `scrWarehouses/phoneCountScannerIcon` . **Width**  _(Image@2.2.3)_
```powerfx
(56)*App.Width/360
```

### `scrWarehouses/phoneCountScannerIcon` . **Height**  _(Image@2.2.3)_
```powerfx
(56)*App.Height/720
```

### `scrWarehouses/phoneCountScannerIcon` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `scrWarehouses/phoneCountScannerIcon` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountScannerIcon` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'><rect width='56' height='56' rx='14' fill='#202225'/><g fill='none' stroke='white' stroke-width='1.6' stroke-linecap='round'><path d='M18 23v-3q0-2 2-2h3m10 0h3q2 0 2 2v3m0 10v3q0 2-2 2h-3m-10 0h-3q-2 0-2-2v-3m6-10v10m4-11v12m4-11v10'/></g></svg>")
```

### `scrWarehouses/BarcodeReader3` . **PressedFillColor**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(255, 255, 255, 1)
)
```

### `scrWarehouses/BarcodeReader3` . **HoverFillColor**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(47, 81, 151, 1)
)
```

### `scrWarehouses/BarcodeReader3` . **TextColor**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,RGBA(255, 255, 255, 1)
)
```

### `scrWarehouses/BarcodeReader3` . **BorderThickness**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,(0)*(Min(App.Width/640,App.Height/1136))
)
```

### `scrWarehouses/BarcodeReader3` . **FillColor**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(99, 139, 44, 1)
)
```

### `scrWarehouses/BarcodeReader3` . **Height**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(56)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,54*App.Height/820,60*App.Height/1136)
)
```

### `scrWarehouses/BarcodeReader3` . **OnScan**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Set(phoneCountItem,Blank());Set(phoneCountValue,Blank());Set(phoneCountReason,Blank());Set(phoneReasonItem,Blank());Set(phoneCountNoteOpen,false);Reset(phoneCountNote);Reset(txtCountQty_2));Set(
    varBarcodeText,
    Text(
        First(BarcodeReader3.Barcodes).Value
    )
);

Set(
    varItem,
    LookUp(
        colOfflineItems,
        number = varBarcodeText
    )
);

If(
    IsBlank(varItem),
    Notify(
        "Бараа олдсонгүй",
        NotificationType.Warning
    ),
    Set(
        varJustSelected,
        true
    )
);Set(varNewPicture,Blank());Set(varItemPicture,Blank());Reset(AddMediaButton2_1);Set(varLocationCode,Blank());Set(varLocationName,Blank());Set(varOpeningBalance,Blank());Set(varShowWarehouseList,false);
ClearCollect(colCountLocationsV19,ForAll(GroupBy(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),itemNo=varItem.number && !IsBlank(locationCode)),locationCode,LocationRows) As l,{code:l.locationCode,displayName:Coalesce(LookUp(colPLocationMaster,Code=l.locationCode,Name),l.locationCode),Qty:Sum(l.LocationRows,quantity)}));
If(!IsBlank(varItem.number),If(CountRows(colCountLocationsV19)=1,Set(varLocationCode,First(colCountLocationsV19).code);Set(varLocationName,First(colCountLocationsV19).displayName);Set(varOpeningBalance,First(colCountLocationsV19).Qty),CountRows(colCountLocationsV19)>1,Set(varShowWarehouseList,true),Notify("Энэ барааны агуулахын үлдэгдэл хадгалсан мэдээлэлд алга. Онлайн шинэчлэлт хийсний дараа дахин шалгана уу.",NotificationType.Warning)))
```

### `scrWarehouses/BarcodeReader3` . **Text**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"","▣"
)
```

### `scrWarehouses/BarcodeReader3` . **Visible**  _(BarcodeReader@1.0.25)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/BarcodeReader3` . **Width**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(56)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,70*App.Width/1180,72*App.Width/640)
)
```

### `scrWarehouses/BarcodeReader3` . **X**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(16)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/BarcodeReader3` . **Y**  _(BarcodeReader@1.0.25)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(648)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,104*App.Height/820,164*App.Height/1136)
)
```

### `scrWarehouses/Icon13_1` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon13_1` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon13_1` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon13_1` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon13_1` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon13_1` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,32*App.Height/820,32*App.Height/1136)
```

### `scrWarehouses/Icon13_1` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon13_1` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Save
```

### `scrWarehouses/Icon13_1` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
If(IsBlank(varItem.number),Notify("Эхлээд бараа сонгоно уу.",NotificationType.Warning),
!Connection.Connected,Notify("BC-д зураг илгээхэд интернет хэрэгтэй.",NotificationType.Warning),
IsBlank(varNewPicture),Notify("Эхлээд шинэ зураг авна уу.",NotificationType.Warning),
Set(varUploadPicture,JSON(varNewPicture,JSONFormat.IncludeBinaryData));
Set(varUploadPicture,Mid(varUploadPicture,2,Len(varUploadPicture)-2));
IfError('PowerAppV2->Getrecord(V3)'.Run(varItem.number,varUploadPicture),
Notify("BC зураг илгээх алдаа: " & FirstError.Message,NotificationType.Error);false,
Notify("BC зураг илгээх хүсэлт гүйцэтгэлээ.",NotificationType.Success);true))
```

### `scrWarehouses/Icon13_1` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon13_1` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon13_1` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon13_1` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon13_1` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon13_1` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Icon13_1` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,32*App.Width/1180,32*App.Width/640)
```

### `scrWarehouses/Icon13_1` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,900*App.Width/1180,342*App.Width/640)
```

### `scrWarehouses/Icon13_1` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,708*App.Height/820,994*App.Height/1136)
```

### `scrWarehouses/Image8_1` . **Fill**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#EEECE8"),RGBA(0, 0, 0, 0)
)
```

### `scrWarehouses/Image8_1` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Image8_1` . **BorderThickness**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image8_1` . **FocusedBorderThickness**  _(Image@2.2.3)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image8_1` . **Height**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(66)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,240*App.Height/820,184*App.Height/1136)
)
```

### `scrWarehouses/Image8_1` . **Image**  _(Image@2.2.3)_
```powerfx
If(
    IsBlank(varItem),
    Blank(),
    If(
        !IsBlank(varNewPicture),
        varNewPicture,
        varItemPicture
    )
)
```

### `scrWarehouses/Image8_1` . **OnSelect**  _(Image@2.2.3)_
```powerfx
If(IsBlank(varItem.number),Notify("Эхлээд бараагаа сонгоно уу.",NotificationType.Information),Set(varPhotoRequestedV28,varItem.number);Set(varPhotoReturnV28,"count");Navigate(ScrItemPhotos,ScreenTransition.Fade))
```

### `scrWarehouses/Image8_1` . **PaddingBottom**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Image8_1` . **PaddingLeft**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Image8_1` . **PaddingRight**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Image8_1` . **PaddingTop**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Image8_1` . **RadiusBottomLeft**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image8_1` . **RadiusBottomRight**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image8_1` . **RadiusTopLeft**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image8_1` . **RadiusTopRight**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image8_1` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList && (!IsBlank(varNewPicture) || !IsBlank(varItemPicture))
))
```

### `scrWarehouses/Image8_1` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(65)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,190*App.Width/1180,150*App.Width/640)
)
```

### `scrWarehouses/Image8_1` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(30)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48*App.Width/1180,40*App.Width/640)
)
```

### `scrWarehouses/Image8_1` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(72)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,230*App.Height/820,270*App.Height/1136)
)
```

### `scrWarehouses/AddMediaButton2_1` . **Align**  _(AddMedia@2.2.1)_
```powerfx
Align.Right
```

### `scrWarehouses/AddMediaButton2_1` . **BorderColor**  _(AddMedia@2.2.1)_
```powerfx
RGBA(111,73,224,1)
```

### `scrWarehouses/AddMediaButton2_1` . **BorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/AddMediaButton2_1` . **ChangePictureText**  _(AddMedia@2.2.1)_
```powerfx
"ЗУРАГ АВАХ"
```

### `scrWarehouses/AddMediaButton2_1` . **Color**  _(AddMedia@2.2.1)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/AddMediaButton2_1` . **DisplayMode**  _(AddMedia@2.2.1)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/AddMediaButton2_1` . **Fill**  _(AddMedia@2.2.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/AddMediaButton2_1` . **FocusedBorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/AddMediaButton2_1` . **Height**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,46*App.Height/820,46*App.Height/1136)
```

### `scrWarehouses/AddMediaButton2_1` . **OnChange**  _(AddMedia@2.2.1)_
```powerfx
Set(varNewPicture, AddMediaButton2_1.Media)
```

### `scrWarehouses/AddMediaButton2_1` . **Size**  _(AddMedia@2.2.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/AddMediaButton2_1` . **Text**  _(AddMedia@2.2.1)_
```powerfx
"Зураг авах"
```

### `scrWarehouses/AddMediaButton2_1` . **UseMobileCamera**  _(AddMedia@2.2.1)_
```powerfx
true
```

### `scrWarehouses/AddMediaButton2_1` . **Visible**  _(AddMedia@2.2.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/AddMediaButton2_1` . **Width**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,180*App.Width/1180,180*App.Width/640)
```

### `scrWarehouses/AddMediaButton2_1` . **X**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,654*App.Width/1180,84*App.Width/640)
```

### `scrWarehouses/AddMediaButton2_1` . **Y**  _(AddMedia@2.2.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,700*App.Height/820,986*App.Height/1136)
```

### `scrWarehouses/Label17_1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `scrWarehouses/Label17_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label17_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label17_1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label17_1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label17_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label17_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label17_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/Label17_1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,46*App.Height/820,46*App.Height/1136)
```

### `scrWarehouses/Label17_1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Icon13_1)
```

### `scrWarehouses/Label17_1` . **Size**  _(Label@2.5.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/Label17_1` . **Text**  _(Label@2.5.1)_
```powerfx
"Зураг илгээх"
```

### `scrWarehouses/Label17_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Label17_1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,192*App.Width/1180,214*App.Width/640)
```

### `scrWarehouses/Label17_1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,944*App.Width/1180,386*App.Width/640)
```

### `scrWarehouses/Label17_1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,700*App.Height/820,986*App.Height/1136)
```

### `scrWarehouses/Icon7_2` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon7_2` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon7_2` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon7_2` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon7_2` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon7_2` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,32*App.Height/820,32*App.Height/1136)
```

### `scrWarehouses/Icon7_2` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon7_2` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Camera
```

### `scrWarehouses/Icon7_2` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon7_2` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon7_2` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon7_2` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon7_2` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon7_2` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Icon7_2` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,32*App.Width/1180,32*App.Width/640)
```

### `scrWarehouses/Icon7_2` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610*App.Width/1180,40*App.Width/640)
```

### `scrWarehouses/Icon7_2` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,708*App.Height/820,994*App.Height/1136)
```

### `scrWarehouses/Label8_17` . **AutoHeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,false,false
)
```

### `scrWarehouses/Label8_17` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label8_17` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_17` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label8_17` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label8_17` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_17` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label8_17` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Semibold
)
```

### `scrWarehouses/Label8_17` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(64)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,130*App.Height/820,90*App.Height/1136)
)
```

### `scrWarehouses/Label8_17` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(App.Width/360,App.Height/720),Min(24*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),Self.Width/Max(12,Len(Self.Text))*3)
)
```

### `scrWarehouses/Label8_17` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(varItem),
    "-",
    varItem.displayName
)
```

### `scrWarehouses/Label8_17` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/Label8_17` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(230)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),270,480)*App.Width/1180,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),380,560)*App.Width/640)
)
```

### `scrWarehouses/Label8_17` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(102)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),260,48)*App.Width/1180,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),210,40)*App.Width/640)
)
```

### `scrWarehouses/Label8_17` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(90)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,284*App.Height/820,316*App.Height/1136)
)
```

### `scrWarehouses/Label8_18` . **OnSelect**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Select(txtSearch_4);Reset(txtSearch_4);SetFocus(txtSearch_4),false)
```

### `scrWarehouses/Label8_18` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label8_18` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_18` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#C84B0B"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label8_18` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label8_18` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_18` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label8_18` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Bold
)
```

### `scrWarehouses/Label8_18` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(23)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,44*App.Height/820,42*App.Height/1136)
)
```

### `scrWarehouses/Label8_18` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(App.Width/360,App.Height/720),24*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Label8_18` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(varItem.number,"Бараа сонгоно уу")
```

### `scrWarehouses/Label8_18` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `scrWarehouses/Label8_18` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/Label8_18` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(227)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),270,480)*App.Width/1180,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),380,560)*App.Width/640)
)
```

### `scrWarehouses/Label8_18` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label8_18` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(102)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),260,48)*App.Width/1180,If(!IsBlank(varNewPicture) || !IsBlank(varItemPicture),210,40)*App.Width/640)
)
```

### `scrWarehouses/Label8_18` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(68)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,224*App.Height/820,268*App.Height/1136)
)
```

### `scrWarehouses/Label8_19` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label8_19` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_19` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label8_19` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label8_19` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_19` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label8_19` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `scrWarehouses/Label8_19` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 42 * App.Height / 820, 43 * App.Height / 1136)
```

### `scrWarehouses/Label8_19` . **Size**  _(Label@2.5.1)_
```powerfx
(18)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/Label8_19` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(varItem),
    "-",
    varItem.type
)
```

### `scrWarehouses/Label8_19` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Label8_19` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 288 * App.Width / 1180, 168 * App.Width / 640)
```

### `scrWarehouses/Label8_19` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 275 * App.Width / 1180, 267 * App.Width / 640)
```

### `scrWarehouses/Label8_19` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 267 * App.Height / 820, 269 * App.Height / 1136)
```

### `scrWarehouses/Label8_20` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label8_20` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_20` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label8_20` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label8_20` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_20` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label8_20` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/Label8_20` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(20)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,42*App.Height/820,42*App.Height/1136)
)
```

### `scrWarehouses/Label8_20` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(App.Width/360,App.Height/720),20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Label8_20` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Coalesce(varLocationCode,"Агуулах сонгох") & If(!IsBlank(varItem.number) && !IsBlank(varLocationCode),"  ·  Тавиур " & Label16.Text,""),If(IsBlank(varLocationCode),"Агуулах сонгоно уу",varLocationCode)
)
```

### `scrWarehouses/Label8_20` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!varCountMenuV21 && (IsBlank(varItem.number) || CountRows(colCountLocationsV19)<=1),!varShowWarehouseList
))
```

### `scrWarehouses/Label8_20` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(208)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,270*App.Width/1180,280*App.Width/640)
)
```

### `scrWarehouses/Label8_20` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label8_20` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(52)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48*App.Width/1180,40*App.Width/640)
)
```

### `scrWarehouses/Label8_20` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(29)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,520*App.Height/820,420*App.Height/1136)
)
```

### `scrWarehouses/Label8_21` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label8_21` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_21` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label8_21` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label8_21` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_21` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label8_21` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/Label8_21` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(26)*App.Height/720,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 40 * App.Height / 820, 34 * App.Height / 1136)
)
```

### `scrWarehouses/Label8_21` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(App.Width/360,App.Height/720),(24)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Label8_21` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Coalesce(varItem.unitOfMeasure,"") & "  ·  " & Coalesce(varItem.itemCategory,""),If(IsBlank(varItem),"-",Coalesce(varItem.unitOfMeasure,""))
)
```

### `scrWarehouses/Label8_21` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,false
))
```

### `scrWarehouses/Label8_21` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(229)*App.Width/360,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 58 * App.Width / 1180, 68 * App.Width / 640)
)
```

### `scrWarehouses/Label8_21` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(102)*App.Width/360,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 832 * App.Width / 1180, 188 * App.Width / 640)
)
```

### `scrWarehouses/Label8_21` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(149)*App.Height/720,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 235 * App.Height / 820, 609 * App.Height / 1136)
)
```

### `scrWarehouses/Rectangle9` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle9` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/Rectangle9` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle9` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Height / 820, 266 * App.Height / 1136)
```

### `scrWarehouses/Rectangle9` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Rectangle9` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 550 * App.Width / 1180, 2 * App.Width / 640)
```

### `scrWarehouses/Rectangle9` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 24 * App.Width / 1180, 495 * App.Width / 640)
```

### `scrWarehouses/Rectangle9` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 565 * App.Height / 820, 225 * App.Height / 1136)
```

### `scrWarehouses/Icon17` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon17` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon17` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon17` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon17` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `scrWarehouses/Icon17` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon17` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 48 * App.Height / 820, 64 * App.Height / 1136)
```

### `scrWarehouses/Icon17` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon17` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Waypoint
```

### `scrWarehouses/Icon17` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon17` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Icon17` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 48 * App.Width / 1180, 64 * App.Width / 640)
```

### `scrWarehouses/Icon17` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 35 * App.Width / 1180, 536 * App.Width / 640)
```

### `scrWarehouses/Icon17` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 590 * App.Height / 820, 257 * App.Height / 1136)
```

### `scrWarehouses/Label3_21` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Label3_21` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label3_21` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_21` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#657C73")
)
```

### `scrWarehouses/Label3_21` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(0,0,0,0)
)
```

### `scrWarehouses/Label3_21` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_21` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label3_21` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(21)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,30*App.Height/820,30*App.Height/1136)
)
```

### `scrWarehouses/Label3_21` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/Label3_21` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Min(App.Width/360,App.Height/720),16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Label3_21` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Системд","Агуулахын үлдэгдэл"
)
```

### `scrWarehouses/Label3_21` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(80)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,230*App.Width/1180,250*App.Width/640)
)
```

### `scrWarehouses/Label3_21` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(38)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610*App.Width/1180,40*App.Width/640)
)
```

### `scrWarehouses/Label3_21` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(185)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,194*App.Height/820,518*App.Height/1136)
)
```

### `scrWarehouses/Label8_22` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Label8_22` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label8_22` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_22` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label8_22` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(0,0,0,0)
)
```

### `scrWarehouses/Label8_22` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label8_22` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label8_22` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Bold
)
```

### `scrWarehouses/Label8_22` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(31)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,64*App.Height/820,58*App.Height/1136)
)
```

### `scrWarehouses/Label8_22` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/Label8_22` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(App.Width/360,App.Height/720),Min(32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),Self.Width/Max(8,Len(Self.Text))*1.05)
)
```

### `scrWarehouses/Label8_22` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(IsBlank(varOpeningBalance),"—",Text(varOpeningBalance,"0.###")),If(IsBlank(varItem.number) || IsBlank(varLocationCode),"—",With({q:Sum(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),itemNo=varItem.number && locationCode=varLocationCode),quantity)},Text(q,If(Mod(q,1)=0,"#,##0","#,##0.###")))) & If(IsBlank(varItem.number),""," " & Coalesce(varItem.unitOfMeasure,""))
)
```

### `scrWarehouses/Label8_22` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `scrWarehouses/Label8_22` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(80)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,230*App.Width/1180,250*App.Width/640)
)
```

### `scrWarehouses/Label8_22` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label8_22` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(38)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610*App.Width/1180,40*App.Width/640)
)
```

### `scrWarehouses/Label8_22` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(204)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,240*App.Height/820,558*App.Height/1136)
)
```

### `scrWarehouses/Label3_24` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Label3_24` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label3_24` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_24` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#657C73")
```

### `scrWarehouses/Label3_24` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label3_24` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_24` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label3_24` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,30*App.Height/820,30*App.Height/1136)
```

### `scrWarehouses/Label3_24` . **Size**  _(Label@2.5.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/Label3_24` . **Text**  _(Label@2.5.1)_
```powerfx
"Тавиур"
```

### `scrWarehouses/Label3_24` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,236*App.Width/1180,250*App.Width/640)
```

### `scrWarehouses/Label3_24` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,900*App.Width/1180,350*App.Width/640)
```

### `scrWarehouses/Label3_24` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,194*App.Height/820,518*App.Height/1136)
```

### `scrWarehouses/Label3_22` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Label3_22` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label3_22` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_22` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label3_22` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(0,0,0,0)
)
```

### `scrWarehouses/Label3_22` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_22` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label3_22` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(21)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,30*App.Height/820,30*App.Height/1136)
)
```

### `scrWarehouses/Label3_22` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/Label3_22` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Min(App.Width/360,App.Height/720),16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Label3_22` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Өмнөх","Өмнөх тооллого"
)
```

### `scrWarehouses/Label3_22` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(80)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,210*App.Width/1180,250*App.Width/640)
)
```

### `scrWarehouses/Label3_22` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(141)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610*App.Width/1180,40*App.Width/640)
)
```

### `scrWarehouses/Label3_22` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(185)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,362*App.Height/820,668*App.Height/1136)
)
```

### `scrWarehouses/Label3_23` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Label3_23` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label3_23` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_23` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label3_23` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(0,0,0,0)
)
```

### `scrWarehouses/Label3_23` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label3_23` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label3_23` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Bold
)
```

### `scrWarehouses/Label3_23` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(31)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,62*App.Height/820,56*App.Height/1136)
)
```

### `scrWarehouses/Label3_23` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/Label3_23` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(App.Width/360,App.Height/720),Min(32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),Self.Width/Max(8,Len(Self.Text))*1.1)
)
```

### `scrWarehouses/Label3_23` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varItem) || IsBlank(varLocationCode),"-",
With({_last:First(SortByColumns(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),!Coalesce(Archived,false) && OwnerEmail=varCountOwner && ItemNo=varItem.number && LocationCode=varLocationCode &&
CountDate>=DatePicker3.SelectedDate && CountDate<DateAdd(DatePicker4.SelectedDate,1,TimeUnit.Days)),"CountDate",SortOrder.Descending,"SyncKey",SortOrder.Descending))},
If(IsBlank(_last.SyncKey),"-",Text(_last.CountQty,If(Mod(_last.CountQty,1)=0,"#,##0","#,##0.###")))))
```

### `scrWarehouses/Label3_23` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `scrWarehouses/Label3_23` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(80)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,205*App.Width/1180,230*App.Width/640)
)
```

### `scrWarehouses/Label3_23` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label3_23` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(141)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610*App.Width/1180,40*App.Width/640)
)
```

### `scrWarehouses/Label3_23` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(204)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,404*App.Height/820,708*App.Height/1136)
)
```

### `scrWarehouses/Label10_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Label10_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label10_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label10_1` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#AF500F"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label10_1` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(0,0,0,0)
)
```

### `scrWarehouses/Label10_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label10_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label10_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/Label10_1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(21)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,34*App.Height/820,34*App.Height/1136)
)
```

### `scrWarehouses/Label10_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/Label10_1` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Min(App.Width/360,App.Height/720),(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Label10_1` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Зөрүү","Зөрүү:"
)
```

### `scrWarehouses/Label10_1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(80)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,80*App.Width/1180,80*App.Width/640)
)
```

### `scrWarehouses/Label10_1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(244)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610*App.Width/1180,40*App.Width/640)
)
```

### `scrWarehouses/Label10_1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(185)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,538*App.Height/820,826*App.Height/1136)
)
```

### `scrWarehouses/Label18_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Label18_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label18_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label18_1` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#B8490D"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label18_1` . **Fill**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.Transparent,RGBA(0,0,0,0)
)
```

### `scrWarehouses/Label18_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label18_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label18_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Semibold
)
```

### `scrWarehouses/Label18_1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(31)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,34*App.Height/820,34*App.Height/1136)
)
```

### `scrWarehouses/Label18_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,0
)
```

### `scrWarehouses/Label18_1` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(App.Width/360,App.Height/720),Min(24*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),Self.Width/Max(10,Len(Self.Text))*1.1)
)
```

### `scrWarehouses/Label18_1` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(IsBlank(varOpeningBalance) || !IsNumeric(txtCountQty_2.Text),"—",With({d:Value(txtCountQty_2.Text)-varOpeningBalance},If(d<0,"−",d>0,"+","") & Text(Abs(d),"0.###"))),If(IsBlank(varItem.number) || IsBlank(varLocationCode) || !IsNumeric(txtCountQty_2.Text),"—",With({v:Value(txtCountQty_2.Text)-Sum(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),itemNo=varItem.number && locationCode=varLocationCode),quantity)},If(v=0,"Таарсан",If(v>0,"Илүү ","Дутуу ") & Text(Abs(v),If(Mod(v,1)=0,"#,##0","#,##0.###")) & " " & varItem.unitOfMeasure)))
)
```

### `scrWarehouses/Label18_1` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `scrWarehouses/Label18_1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(80)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,430*App.Width/1180,455*App.Width/640)
)
```

### `scrWarehouses/Label18_1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label18_1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(244)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,700*App.Width/1180,132*App.Width/640)
)
```

### `scrWarehouses/Label18_1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(204)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,538*App.Height/820,826*App.Height/1136)
)
```

### `scrWarehouses/Label16` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Label16` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label16` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label16` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label16` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label16` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label16` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label16` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `scrWarehouses/Label16` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,64*App.Height/820,58*App.Height/1136)
```

### `scrWarehouses/Label16` . **Size**  _(Label@2.5.1)_
```powerfx
Min(28*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),Self.Width/Max(8,Len(Self.Text))*1.05)
```

### `scrWarehouses/Label16` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(varItem) || IsBlank(varLocationCode),
    "-",
    Coalesce(
        LookUp(
            colOfflineBins,
            itemNo = varItem.number &&
            locationCode = varLocationCode,
            binCode
        ),
        "-"
    )
)
```

### `scrWarehouses/Label16` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Self.Text
```

### `scrWarehouses/Label16` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,236*App.Width/1180,250*App.Width/640)
```

### `scrWarehouses/Label16` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label16` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,900*App.Width/1180,350*App.Width/640)
```

### `scrWarehouses/Label16` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,240*App.Height/820,558*App.Height/1136)
```

### `scrWarehouses/txtCountQty_2` . **FontWeight**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Normal
)
```

### `scrWarehouses/txtCountQty_2` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F5F4F1"),RGBA(255, 255, 255, 1)
)
```

### `scrWarehouses/txtCountQty_2` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/txtCountQty_2` . **AccessibleLabel**  _(Classic/TextInput@2.3.2)_
```powerfx
"Одоо тоолсон тоо"
```

### `scrWarehouses/txtCountQty_2` . **Align**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Center,Align.Center
)
```

### `scrWarehouses/txtCountQty_2` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#B9D4C5")
```

### `scrWarehouses/txtCountQty_2` . **BorderStyle**  _(Classic/TextInput@2.3.2)_
```powerfx
BorderStyle.Dotted
```

### `scrWarehouses/txtCountQty_2` . **BorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0,(1)*(Min(App.Width/640,App.Height/1136))
)
```

### `scrWarehouses/txtCountQty_2` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#17382E")
)
```

### `scrWarehouses/txtCountQty_2` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(phoneCountItem=varItem.number,phoneCountValue,Blank()),""
)
```

### `scrWarehouses/txtCountQty_2` . **DisplayMode**  _(Classic/TextInput@2.3.2)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/txtCountQty_2` . **FocusedBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/txtCountQty_2` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/txtCountQty_2` . **Format**  _(Classic/TextInput@2.3.2)_
```powerfx
TextFormat.Number
```

### `scrWarehouses/txtCountQty_2` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(74)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,98*App.Height/820,90*App.Height/1136)
)
```

### `scrWarehouses/txtCountQty_2` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"0"
```

### `scrWarehouses/txtCountQty_2` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/txtCountQty_2` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `scrWarehouses/txtCountQty_2` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/txtCountQty_2` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/txtCountQty_2` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/txtCountQty_2` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/txtCountQty_2` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,40*Min(App.Width/360,App.Height/720),Min(32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),Self.Width/Max(8,Len(Self.Text))*1.1)
)
```

### `scrWarehouses/txtCountQty_2` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(120)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,280*App.Width/1180,260*App.Width/640)
)
```

### `scrWarehouses/txtCountQty_2` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(120)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,850*App.Width/1180,330*App.Width/640)
)
```

### `scrWarehouses/txtCountQty_2` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(296)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,404*App.Height/820,708*App.Height/1136)
)
```

### `scrWarehouses/Button1_2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!varShowWarehouseList && !varCountMenuV21,true
))
```

### `scrWarehouses/Button1_2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/Button1_2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,Color.White
)
```

### `scrWarehouses/Button1_2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/Button1_2` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(IsBlank(varItem.number) || IsBlank(varLocationCode),DisplayMode.Disabled,If(varCountMenuV21,DisplayMode.Disabled,If(varCountSaving || varCountSyncBusy || varHistoryLoading,DisplayMode.Disabled,DisplayMode.Edit))),If(varCountMenuV21,DisplayMode.Disabled,If(varCountSaving || varCountSyncBusy || varHistoryLoading,DisplayMode.Disabled,DisplayMode.Edit))
)
```

### `scrWarehouses/Button1_2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#F15D18"),ColorValue("#246F50")
)
```

### `scrWarehouses/Button1_2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Button1_2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/Button1_2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(56)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,62*App.Height/820,64*App.Height/1136)
)
```

### `scrWarehouses/Button1_2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/Button1_2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/Button1_2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#338963")
```

### `scrWarehouses/Button1_2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(varLocationCode) & "|") in pgAccess.LocationCode),If(Coalesce(varHistoryLoading,false) || Coalesce(varCountSaving,false) || Coalesce(varCountSyncBusy,false),
 Notify("Одоогийн хадгалалт дуусахыг хүлээнэ үү.",NotificationType.Information),
IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),
IsBlank(varItem.number) || IsBlank(varLocationCode) || Trim(txtSearch_4.Text)<>varItem.number,Notify("Бараа болон тухайн агуулахыг сонгоно уу. Хайлтад бичсэн бараагаа баталгаажуулна уу.",NotificationType.Warning),
IsBlank(txtCountQty_2.Text) || !IsNumeric(txtCountQty_2.Text) || IfError(Value(txtCountQty_2.Text)<0,true),Notify("0 буюу түүнээс их тоо оруулна уу.",NotificationType.Warning),
IsEmpty(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),itemNo=varItem.number && locationCode=varLocationCode)),Notify("Энэ барааны агуулахын үлдэгдэл алга байна.",NotificationType.Warning),
Set(varCountSaving,true);Set(varCountSavedV21,false);Set(varCountCloudOnlyV21,false);
If(IsBlank(varCountAttemptKeyV21),Set(varCountAttemptKeyV21,Text(GUID())));Set(varCountAttemptTitleV21,"COUNT:" & varCountAttemptKeyV21);
With({_key:varCountAttemptKeyV21,_opening:Sum(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),itemNo=varItem.number && locationCode=varLocationCode),quantity),_qty:Value(txtCountQty_2.Text)},
 Collect(colOfflineInventory,{SyncKey:_key,CountKeyV27:_key,Title:"COUNT:" & _key,ItemNo:varItem.number,ItemName:varItem.displayName,
 LocationCode:varLocationCode,OpeningBalance:_opening,CountQty:_qty,Variance:_qty-_opening,CountDate:Now(),Counter:User().FullName,
 OwnerEmail:varCountOwner,Revision:1,Archived:false,SharePointID:0,SyncError:"",Reason:If(App.Width<First(App.SizeBreakpoints).Value && phoneReasonItem=varItem.number,Coalesce(phoneCountReason,""),""),Comment:If(App.Width<First(App.SizeBreakpoints).Value,phoneCountNote.Text,""),Resolved:false,Synced:false});
 IfError(If(!varCountDiskSafeV21,Error({Kind:ErrorKind.Validation,Message:"Төхөөрөмжийн эх санг аюулгүй уншаагүй тул дарж бичихгүй."}),
ClearCollect(colCountDiskV21,{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)});
SaveData(colCountDiskV21,varCountCacheKey)),
  Set(varCountCacheReady,false);Set(varCountStorageError,FirstError.Message),
  Set(varCountCacheReady,true);Set(varCountStorageError,"");Set(varCountSavedV21,true));
 If(!varCountSavedV21 && Connection.Connected,
  IfError(With({_existing:Coalesce(LookUp(InventoryCount,CountKeyV27=_key && Counter=varCountOwner),LookUp(InventoryCount,Title=varCountAttemptTitleV21 && Counter=varCountOwner))},
   With({_saved:Patch(InventoryCount,If(IsBlank(_existing.ID),Defaults(InventoryCount),_existing),{
    CountKeyV27:_key,Title:"COUNT:" & _key,ItemNo:varItem.number,ItemName:varItem.displayName,LocationCode:varLocationCode,
    OpeningBalance:_opening,CountQty:_qty,Variance:_qty-_opening,CountDate:LookUp(colOfflineInventory,SyncKey=_key,CountDate),
    Counter:varCountOwner,Reason:If(App.Width<First(App.SizeBreakpoints).Value && phoneReasonItem=varItem.number,Coalesce(phoneCountReason,""),""),Comment:If(App.Width<First(App.SizeBreakpoints).Value,phoneCountNote.Text,""),Resolved:false})},
    If(IsBlank(_saved.ID),Error({Kind:ErrorKind.Validation,Message:"Сервер хадгалалтыг баталгаажуулсангүй."}),
     Patch(colOfflineInventory,LookUp(colOfflineInventory,SyncKey=_key),{SharePointID:_saved.ID,Synced:true});Set(varCountSavedV21,true);Set(varCountCloudOnlyV21,true))));true,
   Set(varCountCloudSaveErrorV21,FirstError.Message);false));
 If(varCountSavedV21,
  Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);Set(varCountLastSavedItemV21,varItem.number);
  Notify(If(varCountCloudOnlyV21,"SharePoint-д хадгаллаа. Төхөөрөмжийн оффлайн хуулбар хадгалагдаагүй.","Төхөөрөмжид хадгаллаа · интернет ормогц автоматаар илгээнэ."),If(varCountCloudOnlyV21,NotificationType.Warning,NotificationType.Success));
  Set(varCountAttemptKeyV21,Blank());Set(varItem,Blank());Set(varOpeningBalance,Blank());Set(varBarcodeText,Blank());
  Set(varItemPicture,Blank());Set(varNewPicture,Blank());Set(varJustSelected,false);Set(varLocationCode,Blank());Set(varLocationName,Blank());Clear(colCountLocationsV19);
  Set(phoneCountItem,Blank());Set(phoneCountValue,Blank());Set(phoneCountReason,Blank());Set(phoneReasonItem,Blank());Set(phoneCountNoteOpen,false);Reset(phoneCountNote);Reset(txtCountQty_2);Reset(txtSearch_4);Reset(AddMediaButton2_1),
  RemoveIf(colOfflineInventory,SyncKey=_key);
  Notify("Хадгалагдсангүй. Оруулсан тоо хэвээр үлдсэн. " & If(Connection.Connected,Coalesce(varCountCloudSaveErrorV21,varCountStorageError),varCountStorageError),NotificationType.Error)));
Set(varCountUploadQueue,Connection.Connected && varCountCacheReady && !IsEmpty(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),OwnerEmail=varCountOwner && !Synced)));Set(varCountSaving,false))
,Notify("Энэ агуулахад тооллого хадгалах эрхгүй.",NotificationType.Error))
```

### `scrWarehouses/Button1_2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Button1_2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Button1_2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Button1_2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Button1_2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/Button1_2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/Button1_2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#174B36")
```

### `scrWarehouses/Button1_2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,12
)
```

### `scrWarehouses/Button1_2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,12
)
```

### `scrWarehouses/Button1_2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,12
)
```

### `scrWarehouses/Button1_2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(14)*App.Width/360,12
)
```

### `scrWarehouses/Button1_2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(App.Width/360,App.Height/720),22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Button1_2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,If(varCountSaving,"Хадгалж байна…","Хадгалаад дараагийнх →"),If(varCountSaving,"Хадгалж байна…","Хадгалах  →")
)
```

### `scrWarehouses/Button1_2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(263)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,566*App.Width/1180,600*App.Width/640)
)
```

### `scrWarehouses/Button1_2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(81)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,590*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/Button1_2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(648)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,626*App.Height/820,904*App.Height/1136)
)
```

### `scrWarehouses/Icon16_4` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Icon16_4` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Тооллогын түүх"
```

### `scrWarehouses/Icon16_4` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon16_4` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_4` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon16_4` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon16_4` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_4` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 34 * App.Height / 820, 37 * App.Height / 1136)
```

### `scrWarehouses/Icon16_4` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon16_4` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.History
```

### `scrWarehouses/Icon16_4` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate('ScrHistory')
```

### `scrWarehouses/Icon16_4` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_4` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_4` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_4` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_4` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon16_4` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 36 * App.Width / 1180, 32 * App.Width / 640)
```

### `scrWarehouses/Icon16_4` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 420 * App.Width / 1180, 211 * App.Width / 640)
```

### `scrWarehouses/Icon16_4` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 742 * App.Height / 820, 1069 * App.Height / 1136)
```

### `scrWarehouses/Icon16_5` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Icon16_5` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Тооллогын тайлан"
```

### `scrWarehouses/Icon16_5` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon16_5` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_5` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon16_5` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon16_5` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_5` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 34 * App.Height / 820, 37 * App.Height / 1136)
```

### `scrWarehouses/Icon16_5` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon16_5` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.TrendingUpwards
```

### `scrWarehouses/Icon16_5` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate(ScrReport1,ScreenTransition.Fade)
```

### `scrWarehouses/Icon16_5` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_5` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_5` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_5` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_5` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon16_5` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 36 * App.Width / 1180, 32 * App.Width / 640)
```

### `scrWarehouses/Icon16_5` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 710 * App.Width / 1180, 375 * App.Width / 640)
```

### `scrWarehouses/Icon16_5` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 742 * App.Height / 820, 1069 * App.Height / 1136)
```

### `scrWarehouses/Icon16_6` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Icon16_6` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Буцах"
```

### `scrWarehouses/Icon16_6` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon16_6` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_6` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon16_6` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon16_6` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_6` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 34 * App.Height / 820, 37 * App.Height / 1136)
```

### `scrWarehouses/Icon16_6` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon16_6` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Settings
```

### `scrWarehouses/Icon16_6` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `scrWarehouses/Icon16_6` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_6` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_6` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_6` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_6` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon16_6` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 36 * App.Width / 1180, 32 * App.Width / 640)
```

### `scrWarehouses/Icon16_6` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1000 * App.Width / 1180, 549 * App.Width / 640)
```

### `scrWarehouses/Icon16_6` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 742 * App.Height / 820, 1069 * App.Height / 1136)
```

### `scrWarehouses/Icon16_7` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Icon16_7` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Буцах"
```

### `scrWarehouses/Icon16_7` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon16_7` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_7` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon16_7` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon16_7` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon16_7` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 34 * App.Height / 820, 37 * App.Height / 1136)
```

### `scrWarehouses/Icon16_7` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon16_7` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Scan
```

### `scrWarehouses/Icon16_7` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `scrWarehouses/Icon16_7` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_7` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_7` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Icon16_7` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Icon16_7` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon16_7` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 36 * App.Width / 1180, 32 * App.Width / 640)
```

### `scrWarehouses/Icon16_7` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 130 * App.Width / 1180, 55 * App.Width / 640)
```

### `scrWarehouses/Icon16_7` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 742 * App.Height / 820, 1069 * App.Height / 1136)
```

### `scrWarehouses/Label19_4` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Label19_4` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `scrWarehouses/Label19_4` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label19_4` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_4` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label19_4` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label19_4` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_4` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label19_4` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 32 * App.Height / 820, 32 * App.Height / 1136)
```

### `scrWarehouses/Label19_4` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Navigate(ScrReport1,ScreenTransition.Fade)
```

### `scrWarehouses/Label19_4` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(14,Self.Width/Max(8,Len(Self.Text))*1.5))
```

### `scrWarehouses/Label19_4` . **Text**  _(Label@2.5.1)_
```powerfx
"Тайлан"
```

### `scrWarehouses/Label19_4` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 146 * App.Width / 1180, 87 * App.Width / 640)
```

### `scrWarehouses/Label19_4` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label19_4` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 655 * App.Width / 1180, 346 * App.Width / 640)
```

### `scrWarehouses/Label19_4` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 778 * App.Height / 820, 1104 * App.Height / 1136)
```

### `scrWarehouses/Label19_5` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Label19_5` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `scrWarehouses/Label19_5` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label19_5` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_5` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label19_5` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label19_5` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_5` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label19_5` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 32 * App.Height / 820, 32 * App.Height / 1136)
```

### `scrWarehouses/Label19_5` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `scrWarehouses/Label19_5` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(14,Self.Width/Max(8,Len(Self.Text))*1.5))
```

### `scrWarehouses/Label19_5` . **Text**  _(Label@2.5.1)_
```powerfx
"Профайл"
```

### `scrWarehouses/Label19_5` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 146 * App.Width / 1180, 97 * App.Width / 640)
```

### `scrWarehouses/Label19_5` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label19_5` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 75 * App.Width / 1180, 24 * App.Width / 640)
```

### `scrWarehouses/Label19_5` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 778 * App.Height / 820, 1104 * App.Height / 1136)
```

### `scrWarehouses/Label19_6` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Label19_6` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `scrWarehouses/Label19_6` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label19_6` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_6` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label19_6` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label19_6` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_6` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label19_6` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 32 * App.Height / 820, 32 * App.Height / 1136)
```

### `scrWarehouses/Label19_6` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Navigate(ScrHistory,ScreenTransition.Fade)
```

### `scrWarehouses/Label19_6` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(14,Self.Width/Max(8,Len(Self.Text))*1.5))
```

### `scrWarehouses/Label19_6` . **Text**  _(Label@2.5.1)_
```powerfx
"Түүх"
```

### `scrWarehouses/Label19_6` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 146 * App.Width / 1180, 77 * App.Width / 640)
```

### `scrWarehouses/Label19_6` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label19_6` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 365 * App.Width / 1180, 187 * App.Width / 640)
```

### `scrWarehouses/Label19_6` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 778 * App.Height / 820, 1104 * App.Height / 1136)
```

### `scrWarehouses/Label19_7` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Label19_7` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `scrWarehouses/Label19_7` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label19_7` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_7` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label19_7` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label19_7` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label19_7` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label19_7` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 32 * App.Height / 820, 38 * App.Height / 1136)
```

### `scrWarehouses/Label19_7` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `scrWarehouses/Label19_7` . **Size**  _(Label@2.5.1)_
```powerfx
Max(10,Min(14,Self.Width/Max(8,Len(Self.Text))*1.5))
```

### `scrWarehouses/Label19_7` . **Text**  _(Label@2.5.1)_
```powerfx
"Тохиргоо"
```

### `scrWarehouses/Label19_7` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 146 * App.Width / 1180, 120 * App.Width / 640)
```

### `scrWarehouses/Label19_7` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/Label19_7` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 945 * App.Width / 1180, 504 * App.Width / 640)
```

### `scrWarehouses/Label19_7` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 778 * App.Height / 820, 1098 * App.Height / 1136)
```

### `scrWarehouses/Rectangle9_2` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle9_2` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/Rectangle9_2` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle9_2` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 80 * App.Height / 820, 102 * App.Height / 1136)
```

### `scrWarehouses/Rectangle9_2` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Rectangle9_2` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Width / 1180, 2 * App.Width / 640)
```

### `scrWarehouses/Rectangle9_2` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 787 * App.Width / 1180, 189 * App.Width / 640)
```

### `scrWarehouses/Rectangle9_2` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 382 * App.Height / 820, 727 * App.Height / 1136)
```

### `scrWarehouses/Image5` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Image5` . **BorderThickness**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image5` . **FocusedBorderThickness**  _(Image@2.2.3)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image5` . **Height**  _(Image@2.2.3)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 40 * App.Height / 820, 39 * App.Height / 1136)
```

### `scrWarehouses/Image5` . **Image**  _(Image@2.2.3)_
```powerfx
'png-transparent-warehouse-building-computer-icons-modern-elements-miscellaneous-angle-logo'
```

### `scrWarehouses/Image5` . **PaddingBottom**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Image5` . **PaddingLeft**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Image5` . **PaddingRight**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/Image5` . **PaddingTop**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/Image5` . **RadiusBottomLeft**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image5` . **RadiusBottomRight**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image5` . **RadiusTopLeft**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image5` . **RadiusTopRight**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Image5` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Image5` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 48 * App.Width / 1180, 55 * App.Width / 640)
```

### `scrWarehouses/Image5` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 30 * App.Width / 1180, 26 * App.Width / 640)
```

### `scrWarehouses/Image5` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 91 * App.Height / 820, 62 * App.Height / 1136)
```

### `scrWarehouses/Rectangle5_5` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle5_5` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/Rectangle5_5` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle5_5` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Height / 820, 1 * App.Height / 1136)
```

### `scrWarehouses/Rectangle5_5` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Rectangle5_5` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 514 * App.Width / 1180, 640 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_5` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 626 * App.Width / 1180, 0 * App.Width / 640)
```

### `scrWarehouses/Rectangle5_5` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 541 * App.Height / 820, 901 * App.Height / 1136)
```

### `scrWarehouses/Rectangle9_3` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Rectangle9_3` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/Rectangle9_3` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Rectangle9_3` . **Height**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 120 * App.Height / 820, 154 * App.Height / 1136)
```

### `scrWarehouses/Rectangle9_3` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,false
))
```

### `scrWarehouses/Rectangle9_3` . **Width**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 1 * App.Width / 1180, 2 * App.Width / 640)
```

### `scrWarehouses/Rectangle9_3` . **X**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 900 * App.Width / 1180, 314 * App.Width / 640)
```

### `scrWarehouses/Rectangle9_3` . **Y**  _(Rectangle@2.3.0)_
```powerfx
If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 172 * App.Height / 820, 523 * App.Height / 1136)
```

### `scrWarehouses/txtSearch_4` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Color.White,RGBA(255, 255, 255, 1)
)
```

### `scrWarehouses/txtSearch_4` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),RGBA(0, 0, 0, 1)
)
```

### `scrWarehouses/txtSearch_4` . **AccessibleLabel**  _(Classic/TextInput@2.3.2)_
```powerfx
"Барааны код эсвэл нэрээр хайх"
```

### `scrWarehouses/txtSearch_4` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#C7DAD0")
```

### `scrWarehouses/txtSearch_4` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
varBarcodeText
```

### `scrWarehouses/txtSearch_4` . **DisplayMode**  _(Classic/TextInput@2.3.2)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/txtSearch_4` . **FocusedBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/txtSearch_4` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/txtSearch_4` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/txtSearch_4` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(52)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,54*App.Height/820,60*App.Height/1136)
)
```

### `scrWarehouses/txtSearch_4` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Барааны код эсвэл нэр хайх","Код эсвэл барааны нэр"
)
```

### `scrWarehouses/txtSearch_4` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/txtSearch_4` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `scrWarehouses/txtSearch_4` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
If(Trim(Self.Text)<>Coalesce(varItem.number,""),Set(varJustSelected,false);Set(varCountAttemptKeyV21,Blank());Reset(txtCountQty_2);Set(varItem,LookUp(colOfflineItems,number=Trim(txtSearch_4.Text)));Set(varBarcodeText,If(IsBlank(varItem),Blank(),varItem.number));Set(varNewPicture,Blank());Set(varItemPicture,Blank());Set(varPictureResponse,Blank());Set(varLocationCode,Blank());Set(varLocationName,Blank());Set(varOpeningBalance,Blank());Set(varShowWarehouseList,false);
ClearCollect(colCountLocationsV19,ForAll(GroupBy(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),itemNo=varItem.number && !IsBlank(locationCode)),locationCode,LocationRows) As l,{code:l.locationCode,displayName:Coalesce(LookUp(colPLocationMaster,Code=l.locationCode,Name),l.locationCode),Qty:Sum(l.LocationRows,quantity)}));
If(!IsBlank(varItem.number),If(CountRows(colCountLocationsV19)=1,Set(varLocationCode,First(colCountLocationsV19).code);Set(varLocationName,First(colCountLocationsV19).displayName);Set(varOpeningBalance,First(colCountLocationsV19).Qty),CountRows(colCountLocationsV19)>1,Set(varShowWarehouseList,true),Notify("Энэ барааны агуулахын үлдэгдэл хадгалсан мэдээлэлд алга. Онлайн шинэчлэлт хийсний дараа дахин шалгана уу.",NotificationType.Warning))))
```

### `scrWarehouses/txtSearch_4` . **OnSelect**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Set(phoneCountItem,Blank());Set(phoneCountValue,Blank());Set(phoneCountReason,Blank());Set(phoneReasonItem,Blank());Set(phoneCountNoteOpen,false);Reset(phoneCountNote);Reset(txtCountQty_2));Set(varItem, Blank());
Set(varOpeningBalance, Blank());
Set(varBarcodeText, Blank());
Set(varJustSelected, false);

Set(varNewPicture, Blank());
Set(varItemPicture, Blank());
Set(varPictureResponse, Blank());Set(varLocationCode,Blank());Set(varShowWarehouseList,false)
```

### `scrWarehouses/txtSearch_4` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/txtSearch_4` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/txtSearch_4` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/txtSearch_4` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/txtSearch_4` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(App.Width/360,App.Height/720),22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/txtSearch_4` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,IsBlank(varItem.number) && !varCountMenuV21 && !varShowWarehouseList,!varShowWarehouseList
))
```

### `scrWarehouses/txtSearch_4` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(328)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,448*App.Width/1180,514*App.Width/640)
)
```

### `scrWarehouses/txtSearch_4` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(16)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,110*App.Width/1180,106*App.Width/640)
)
```

### `scrWarehouses/txtSearch_4` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(85)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,104*App.Height/820,164*App.Height/1136)
)
```

### `scrWarehouses/Label20` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!varCountMenuV21,true
))
```

### `scrWarehouses/Label20` . **Align**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Left,Align.Center
)
```

### `scrWarehouses/Label20` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label20` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label20` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#17382E")
)
```

### `scrWarehouses/Label20` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label20` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label20` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label20` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,FontWeight.Bold,FontWeight.Bold
)
```

### `scrWarehouses/Label20` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(33)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48*App.Height/820,48*App.Height/1136)
)
```

### `scrWarehouses/Label20` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(App.Width/360,App.Height/720),28*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/Label20` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Тооллого","Тооллого"
)
```

### `scrWarehouses/Label20` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(170)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,500*App.Width/1180,340*App.Width/640)
)
```

### `scrWarehouses/Label20` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(52)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,84*App.Width/1180,76*App.Width/640)
)
```

### `scrWarehouses/Label20` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(0)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,16*App.Height/820,12*App.Height/1136)
)
```

### `scrWarehouses/Icon7` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Тооллогын цэс"
```

### `scrWarehouses/Icon7` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon7` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon7` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#202225"),ColorValue("#237653")
)
```

### `scrWarehouses/Icon7` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon7` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon7` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(31)*App.Height/720,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 36 * App.Height / 820, 32 * App.Height / 1136)
)
```

### `scrWarehouses/Icon7` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon7` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronLeft
```

### `scrWarehouses/Icon7` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate(ScrCountHome,ScreenTransition.Fade)
```

### `scrWarehouses/Icon7` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon7` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!varCountMenuV21,false
))
```

### `scrWarehouses/Icon7` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(30)*App.Width/360,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 36 * App.Width / 1180, 46 * App.Width / 640)
)
```

### `scrWarehouses/Icon7` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(13)*App.Width/360,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 76 * App.Width / 1180, 79 * App.Width / 640)
)
```

### `scrWarehouses/Icon7` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(11)*App.Height/720,If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height, 20 * App.Height / 820, 12 * App.Height / 1136)
)
```

### `scrWarehouses/Circle1` . **Visible**  _(Circle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Circle1` . **BorderColor**  _(Circle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Circle1` . **BorderThickness**  _(Circle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Circle1` . **Fill**  _(Circle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `scrWarehouses/Circle1` . **Height**  _(Circle@2.3.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,50*App.Height/820,48*App.Height/1136)
```

### `scrWarehouses/Circle1` . **Width**  _(Circle@2.3.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,50*App.Width/1180,48*App.Width/640)
```

### `scrWarehouses/Circle1` . **X**  _(Circle@2.3.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,1100*App.Width/1180,566*App.Width/640)
```

### `scrWarehouses/Circle1` . **Y**  _(Circle@2.3.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,16*App.Height/820,14*App.Height/1136)
```

### `scrWarehouses/Label21` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Label21` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `scrWarehouses/Label21` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Label21` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label21` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/Label21` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/Label21` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Label21` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/Label21` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/Label21` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,50*App.Height/820,48*App.Height/1136)
```

### `scrWarehouses/Label21` . **Size**  _(Label@2.5.1)_
```powerfx
18*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/Label21` . **Text**  _(Label@2.5.1)_
```powerfx
With(
    {
        parts: Split(Trim(User().FullName), " ")
    },
    Upper(
        Left(First(parts).Value, 1) &
        If(
            CountRows(parts) > 1,
            Left(Last(parts).Value, 1),
            ""
        )
    )
)
```

### `scrWarehouses/Label21` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,50*App.Width/1180,48*App.Width/640)
```

### `scrWarehouses/Label21` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,1100*App.Width/1180,566*App.Width/640)
```

### `scrWarehouses/Label21` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,16*App.Height/820,14*App.Height/1136)
```

### `scrWarehouses/DatePicker3` . **Visible**  _(Classic/DatePicker@2.6.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/DatePicker3` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#D8E5DE")
```

### `scrWarehouses/DatePicker3` . **BorderStyle**  _(Classic/DatePicker@2.6.0)_
```powerfx
BorderStyle.None
```

### `scrWarehouses/DatePicker3` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/DatePicker3` . **DisplayMode**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/DatePicker3` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/DatePicker3` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/DatePicker3` . **FontWeight**  _(Classic/DatePicker@2.6.0)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/DatePicker3` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48*App.Height/820,48*App.Height/1136)
```

### `scrWarehouses/DatePicker3` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/DatePicker3` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
Color.White
```

### `scrWarehouses/DatePicker3` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/DatePicker3` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/DatePicker3` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/DatePicker3` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,230*App.Width/1180,215*App.Width/640)
```

### `scrWarehouses/DatePicker3` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,590*App.Width/1180,20*App.Width/640)
```

### `scrWarehouses/DatePicker3` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,104*App.Height/820,94*App.Height/1136)
```

### `scrWarehouses/DatePicker4` . **Visible**  _(Classic/DatePicker@2.6.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/DatePicker4` . **BorderColor**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#D8E5DE")
```

### `scrWarehouses/DatePicker4` . **BorderStyle**  _(Classic/DatePicker@2.6.0)_
```powerfx
BorderStyle.None
```

### `scrWarehouses/DatePicker4` . **BorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/DatePicker4` . **DisplayMode**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/DatePicker4` . **FocusedBorderThickness**  _(Classic/DatePicker@2.6.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/DatePicker4` . **Font**  _(Classic/DatePicker@2.6.0)_
```powerfx
Font.'Open Sans'
```

### `scrWarehouses/DatePicker4` . **FontWeight**  _(Classic/DatePicker@2.6.0)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/DatePicker4` . **Height**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,48*App.Height/820,48*App.Height/1136)
```

### `scrWarehouses/DatePicker4` . **IconBackground**  _(Classic/DatePicker@2.6.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/DatePicker4` . **IconFill**  _(Classic/DatePicker@2.6.0)_
```powerfx
Color.White
```

### `scrWarehouses/DatePicker4` . **PaddingLeft**  _(Classic/DatePicker@2.6.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/DatePicker4` . **PaddingRight**  _(Classic/DatePicker@2.6.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/DatePicker4` . **Size**  _(Classic/DatePicker@2.6.0)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/DatePicker4` . **Width**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,230*App.Width/1180,215*App.Width/640)
```

### `scrWarehouses/DatePicker4` . **X**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,836*App.Width/1180,250*App.Width/640)
```

### `scrWarehouses/DatePicker4` . **Y**  _(Classic/DatePicker@2.6.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,104*App.Height/820,94*App.Height/1136)
```

### `scrWarehouses/countNewLabelV21` . **Align**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Align.Center,Align.Left
)
```

### `scrWarehouses/countNewLabelV21` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/countNewLabelV21` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countNewLabelV21` . **Color**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,ColorValue("#635C54"),ColorValue("#17382E")
)
```

### `scrWarehouses/countNewLabelV21` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/countNewLabelV21` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countNewLabelV21` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/countNewLabelV21` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(29)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,30*App.Height/820,30*App.Height/1136)
)
```

### `scrWarehouses/countNewLabelV21` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(App.Width/360,App.Height/720),16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
)
```

### `scrWarehouses/countNewLabelV21` . **Text**  _(Label@2.5.1)_
```powerfx
"Одоо тоолсон тоо"
```

### `scrWarehouses/countNewLabelV21` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21,!varShowWarehouseList
))
```

### `scrWarehouses/countNewLabelV21` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(324)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,280*App.Width/1180,260*App.Width/640)
)
```

### `scrWarehouses/countNewLabelV21` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(18)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,850*App.Width/1180,330*App.Width/640)
)
```

### `scrWarehouses/countNewLabelV21` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(270)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,362*App.Height/820,668*App.Height/1136)
)
```

### `scrWarehouses/countPreviousDateV21` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/countPreviousDateV21` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countPreviousDateV21` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#657C73")
```

### `scrWarehouses/countPreviousDateV21` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/countPreviousDateV21` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countPreviousDateV21` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/countPreviousDateV21` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,28*App.Height/820,28*App.Height/1136)
```

### `scrWarehouses/countPreviousDateV21` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countPreviousDateV21` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:First(SortByColumns(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),!Coalesce(Archived,false) && OwnerEmail=varCountOwner && ItemNo=varItem.number && LocationCode=varLocationCode && CountDate>=DatePicker3.SelectedDate && CountDate<DateAdd(DatePicker4.SelectedDate,1,TimeUnit.Days)),"CountDate",SortOrder.Descending,"SyncKey",SortOrder.Descending))},If(IsBlank(r.SyncKey),"Сонгосон хугацаанд тоолоогүй",Text(r.CountDate,"mm/dd hh:mm") & " · таны тооллого"))
```

### `scrWarehouses/countPreviousDateV21` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,!varShowWarehouseList
))
```

### `scrWarehouses/countPreviousDateV21` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,220*App.Width/1180,250*App.Width/640)
```

### `scrWarehouses/countPreviousDateV21` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/countPreviousDateV21` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,610*App.Width/1180,40*App.Width/640)
```

### `scrWarehouses/countPreviousDateV21` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,474*App.Height/820,770*App.Height/1136)
```

### `scrWarehouses/countStorageStatusV21` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/countStorageStatusV21` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/countStorageStatusV21` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countStorageStatusV21` . **Color**  _(Label@2.5.1)_
```powerfx
If(varCountCacheReady,ColorValue("#237653"),ColorValue("#A05A18"))
```

### `scrWarehouses/countStorageStatusV21` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/countStorageStatusV21` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countStorageStatusV21` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/countStorageStatusV21` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,32*App.Height/820,22*App.Height/1136)
```

### `scrWarehouses/countStorageStatusV21` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countStorageStatusV21` . **Text**  _(Label@2.5.1)_
```powerfx
If(varCountSaving,"Хадгалж байна…",varCountCacheReady,"● Оффлайн хадгалалт бэлэн",Connection.Connected,"● Онлайн хадгалалт · оффлайн санг шалгах","● Оффлайн хадгалалт бэлэн биш")
```

### `scrWarehouses/countStorageStatusV21` . **Tooltip**  _(Label@2.5.1)_
```powerfx
varCountStorageError
```

### `scrWarehouses/countStorageStatusV21` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,534*App.Width/1180,600*App.Width/640)
```

### `scrWarehouses/countStorageStatusV21` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `scrWarehouses/countStorageStatusV21` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24*App.Width/1180,20*App.Width/640)
```

### `scrWarehouses/countStorageStatusV21` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,624*App.Height/820,970*App.Height/1136)
```

### `scrWarehouses/galSuggestions_3` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galSuggestions_3` . **BorderThickness**  _(Gallery@2.15.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3` . **Fill**  _(Gallery@2.15.0)_
```powerfx
Color.White
```

### `scrWarehouses/galSuggestions_3` . **FocusedBorderThickness**  _(Gallery@2.15.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3` . **Height**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(407)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,340*App.Height/820,260*App.Height/1136)
)
```

### `scrWarehouses/galSuggestions_3` . **Items**  _(Gallery@2.15.0)_
```powerfx
With(
    {
        _searchText: Trim(txtSearch_4.Text),
        _barcodeText: Coalesce(
            Text(varBarcodeText),
            ""
        )
    },

    If(
        varJustSelected &&
        _searchText = _barcodeText,

        FirstN(
            Filter(
                colOfflineItems,
                number = _barcodeText
            ),
            1
        ),

        FirstN(
            Filter(
                colOfflineItems,
                !IsBlank(_searchText) &&
                (
                    _searchText in number ||
                    _searchText in displayName
                )
            ),
            30
        )
    )
)
```

### `scrWarehouses/galSuggestions_3` . **OnSelect**  _(Gallery@2.15.0)_
```powerfx
Set(varItem, ThisItem);
Set(varBarcodeText, ThisItem.number);
Set(varJustSelected, true);Set(varNewPicture,Blank());Set(varItemPicture,Blank());Reset(AddMediaButton2_1);Set(varLocationCode,Blank());Set(varLocationName,Blank());Set(varOpeningBalance,Blank());Set(varShowWarehouseList,false);
ClearCollect(colCountLocationsV19,ForAll(GroupBy(Filter(colOfflineStock,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode),itemNo=varItem.number && !IsBlank(locationCode)),locationCode,LocationRows) As l,{code:l.locationCode,displayName:Coalesce(LookUp(colPLocationMaster,Code=l.locationCode,Name),l.locationCode),Qty:Sum(l.LocationRows,quantity)}));
If(!IsBlank(varItem.number),If(CountRows(colCountLocationsV19)=1,Set(varLocationCode,First(colCountLocationsV19).code);Set(varLocationName,First(colCountLocationsV19).displayName);Set(varOpeningBalance,First(colCountLocationsV19).Qty),CountRows(colCountLocationsV19)>1,Set(varShowWarehouseList,true),Notify("Энэ барааны агуулахын үлдэгдэл хадгалсан мэдээлэлд алга. Онлайн шинэчлэлт хийсний дараа дахин шалгана уу.",NotificationType.Warning)))
```

### `scrWarehouses/galSuggestions_3` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(0)*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(42)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/galSuggestions_3` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,(IsBlank(varItem.number) && !varCountMenuV21 && !varShowWarehouseList) && !IsBlank(Trim(txtSearch_4.Text)),!varShowWarehouseList && !IsBlank(Trim(txtSearch_4.Text)) && (IsBlank(varItem.number) || Trim(txtSearch_4.Text)<>varItem.number)
))
```

### `scrWarehouses/galSuggestions_3` . **Width**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(328)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,534*App.Width/1180,600*App.Width/640)
)
```

### `scrWarehouses/galSuggestions_3` . **X**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(16)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/galSuggestions_3` . **Y**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(144)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,170*App.Height/820,234*App.Height/1136)
)
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.number & " - " & Left(ThisItem.displayName, 30)
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Width**  _(Label@2.5.1)_
```powerfx
(416)*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **X**  _(Label@2.5.1)_
```powerfx
(16)*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/Title1_3` . **Y**  _(Label@2.5.1)_
```powerfx
(8)*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **Height**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Separator1_3.Height/((App.Height/1136))))*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
ThisItem.IsSelected
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(4)*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/Rectangle1_3` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
ThisItem.number & " " & ThisItem.displayName
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(42)*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronRight
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Select(Parent)
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **Tooltip**  _(Classic/Icon@2.5.0)_
```powerfx
"View item details"
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(50)*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - (Self.Width/((App.Width/640))) - 12)*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/NextArrow1_3` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(8)*((App.Height/1136))
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **Width**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))))*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `scrWarehouses/galSuggestions_3/Separator1_3` . **Y**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Self.Height/((App.Height/1136))))*((App.Height/1136))
```

### `scrWarehouses/galWarehousePicker` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galWarehousePicker` . **Fill**  _(Gallery@2.15.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `scrWarehouses/galWarehousePicker` . **Height**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(451)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,430*App.Height/820,430*App.Height/1136)
)
```

### `scrWarehouses/galWarehousePicker` . **Items**  _(Gallery@2.15.0)_
```powerfx
SortByColumns(Filter(colCountLocationsV19,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(code) & "|") in pgAccess.LocationCode)),"code",SortOrder.Ascending)
```

### `scrWarehouses/galWarehousePicker` . **OnSelect**  _(Gallery@2.15.0)_
```powerfx
Set(varLocationCode,ThisItem.code);Set(varLocationName,ThisItem.displayName);Set(varOpeningBalance,ThisItem.Qty);Set(varShowWarehouseList,false)
```

### `scrWarehouses/galWarehousePicker` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
128*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))   
```

### `scrWarehouses/galWarehousePicker` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,varShowWarehouseList && !varCountMenuV21,varShowWarehouseList
))
```

### `scrWarehouses/galWarehousePicker` . **Width**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(328)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,534*App.Width/1180,600*App.Width/640)
)
```

### `scrWarehouses/galWarehousePicker` . **X**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(16)*App.Width/360,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24*App.Width/1180,20*App.Width/640)
)
```

### `scrWarehouses/galWarehousePicker` . **Y**  _(Gallery@2.15.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,(85)*App.Height/720,If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,178*App.Height/820,242*App.Height/1136)
)
```

### `scrWarehouses/galWarehousePicker/Image7` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galWarehousePicker/Image7` . **BorderThickness**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Image7` . **FocusedBorderThickness**  _(Image@2.2.3)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Image7` . **Height**  _(Image@2.2.3)_
```powerfx
(72)*((App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Image7` . **Image**  _(Image@2.2.3)_
```powerfx
inventory02new
```

### `scrWarehouses/galWarehousePicker/Image7` . **OnSelect**  _(Image@2.2.3)_
```powerfx
Select(Parent)
```

### `scrWarehouses/galWarehousePicker/Image7` . **PaddingBottom**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/galWarehousePicker/Image7` . **PaddingLeft**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/galWarehousePicker/Image7` . **PaddingRight**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/galWarehousePicker/Image7` . **PaddingTop**  _(Image@2.2.3)_
```powerfx
(0)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/galWarehousePicker/Image7` . **RadiusBottomLeft**  _(Image@2.2.3)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Image7` . **RadiusBottomRight**  _(Image@2.2.3)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Image7` . **RadiusTopLeft**  _(Image@2.2.3)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Image7` . **RadiusTopRight**  _(Image@2.2.3)_
```powerfx
(8)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Image7` . **Visible**  _(Image@2.2.3)_
```powerfx
false
```

### `scrWarehouses/galWarehousePicker/Image7` . **Width**  _(Image@2.2.3)_
```powerfx
(72)*((App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Image7` . **X**  _(Image@2.2.3)_
```powerfx
(16)*((App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Image7` . **Y**  _(Image@2.2.3)_
```powerfx
(((Parent.TemplateHeight/((App.Height/1136))) / 2) - ((Self.Height/((App.Height/1136))) / 2))*((App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Title7` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `scrWarehouses/galWarehousePicker/Title7` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/galWarehousePicker/Title7` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/galWarehousePicker/Title7` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/galWarehousePicker/Title7` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `scrWarehouses/galWarehousePicker/Title7` . **Height**  _(Label@2.5.1)_
```powerfx
32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Title7` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `scrWarehouses/galWarehousePicker/Title7` . **Size**  _(Label@2.5.1)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Title7` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.code
```

### `scrWarehouses/galWarehousePicker/Title7` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-80
```

### `scrWarehouses/galWarehousePicker/Title7` . **X**  _(Label@2.5.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Title7` . **Y**  _(Label@2.5.1)_
```powerfx
8*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#17382E")
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Height**  _(Label@2.5.1)_
```powerfx
64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Size**  _(Label@2.5.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.displayName & " · үлдэгдэл " & Text(ThisItem.Qty,If(Mod(ThisItem.Qty,1)=0,"#,##0","#,##0.###"))
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.TemplateWidth-80
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **X**  _(Label@2.5.1)_
```powerfx
16*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Subtitle4` . **Y**  _(Label@2.5.1)_
```powerfx
42*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
ThisItem.code & " агуулах сонгох"
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(0, 0, 0, 1)
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **DisabledBorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(56, 56, 56, 1)
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **DisabledColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(119, 119, 119, 1)
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
44*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronRight
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(varLocationCode,ThisItem.code);Set(varLocationName,ThisItem.displayName);Set(varOpeningBalance,ThisItem.Qty);Set(varShowWarehouseList,false)
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(16)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **Tooltip**  _(Classic/Icon@2.5.0)_
```powerfx
"View item details"
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
44*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
Parent.TemplateWidth-56*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/NextArrow5` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Separator5` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galWarehousePicker/Separator5` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/galWarehousePicker/Separator5` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(8)*((App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Separator5` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Set(varLocationCode,ThisItem.code);Set(varLocationName,ThisItem.displayName);Set(varOpeningBalance,ThisItem.Qty);Set(varShowWarehouseList,false)
```

### `scrWarehouses/galWarehousePicker/Separator5` . **Width**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))))*((App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Separator5` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Separator5` . **Y**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Self.Height/((App.Height/1136))))*((App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
ColorValue("#DFE8E2")
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **Height**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Separator5.Height/((App.Height/1136))))*((App.Height/1136))
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Set(varLocationCode,ThisItem.code);Set(varLocationName,ThisItem.displayName);Set(varOpeningBalance,ThisItem.Qty);Set(varShowWarehouseList,false)
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
ThisItem.IsSelected
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(4)*((App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `scrWarehouses/galWarehousePicker/Rectangle8` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Height/1136))
```

### `scrWarehouses/Icon4` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (If(App.Width<First(App.SizeBreakpoints).Value,false,true
))
```

### `scrWarehouses/Icon4` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Цэс нээх"
```

### `scrWarehouses/Icon4` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/Icon4` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon4` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#237653")
```

### `scrWarehouses/Icon4` . **DisplayMode**  _(Classic/Icon@2.5.0)_
```powerfx
If(varCountMenuV21,DisplayMode.Disabled,DisplayMode.Edit)
```

### `scrWarehouses/Icon4` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/Icon4` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,40*App.Height/820,36*App.Height/1136)
```

### `scrWarehouses/Icon4` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/Icon4` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.DetailList
```

### `scrWarehouses/Icon4` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(varCountMenuV21,true);SetFocus(countMenuItemV21_0)
```

### `scrWarehouses/Icon4` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/Icon4` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,40*App.Width/1180,36*App.Width/640)
```

### `scrWarehouses/Icon4` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,24*App.Width/1180,20*App.Width/640)
```

### `scrWarehouses/Icon4` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,20*App.Height/820,18*App.Height/1136)
```

### `scrWarehouses/countMenuShadeV21` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `scrWarehouses/countMenuShadeV21` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuShadeV21` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
RGBA(8,24,17,0.48)
```

### `scrWarehouses/countMenuShadeV21` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
App.Height
```

### `scrWarehouses/countMenuShadeV21` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuShadeV21` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuShadeV21` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuShadeV21` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuShadeV21` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuShadeV21` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
App.Width
```

### `scrWarehouses/countMenuPanelV21` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuPanelV21` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuPanelV21` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuPanelV21` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#122C24")
```

### `scrWarehouses/countMenuPanelV21` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
DisplayMode.View
```

### `scrWarehouses/countMenuPanelV21` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#122C24")
```

### `scrWarehouses/countMenuPanelV21` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuPanelV21` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuPanelV21` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
App.Height
```

### `scrWarehouses/countMenuPanelV21` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuPanelV21` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuPanelV21` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#338963")
```

### `scrWarehouses/countMenuPanelV21` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuPanelV21` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuPanelV21` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuPanelV21` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuPanelV21` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuPanelV21` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuPanelV21` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#174B36")
```

### `scrWarehouses/countMenuPanelV21` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuPanelV21` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuPanelV21` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,App.Width*0.34,App.Width*0.86)
```

### `scrWarehouses/countMenuTitleV21` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `scrWarehouses/countMenuTitleV21` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/countMenuTitleV21` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuTitleV21` . **Color**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuTitleV21` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `scrWarehouses/countMenuTitleV21` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuTitleV21` . **Font**  _(Label@2.5.1)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuTitleV21` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `scrWarehouses/countMenuTitleV21` . **Height**  _(Label@2.5.1)_
```powerfx
54*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuTitleV21` . **Size**  _(Label@2.5.1)_
```powerfx
24*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuTitleV21` . **Text**  _(Label@2.5.1)_
```powerfx
"Тооллогын цэс"
```

### `scrWarehouses/countMenuTitleV21` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuTitleV21` . **Width**  _(Label@2.5.1)_
```powerfx
countMenuPanelV21.Width-100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuTitleV21` . **X**  _(Label@2.5.1)_
```powerfx
24*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuTitleV21` . **Y**  _(Label@2.5.1)_
```powerfx
24*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuCloseV21` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
"Цэс хаах"
```

### `scrWarehouses/countMenuCloseV21` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `scrWarehouses/countMenuCloseV21` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuCloseV21` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuCloseV21` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuCloseV21` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuCloseV21` . **HoverColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#134C36")
```

### `scrWarehouses/countMenuCloseV21` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Cancel
```

### `scrWarehouses/countMenuCloseV21` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(varCountMenuV21,false)
```

### `scrWarehouses/countMenuCloseV21` . **PressedColor**  _(Classic/Icon@2.5.0)_
```powerfx
ColorValue("#EF601B")
```

### `scrWarehouses/countMenuCloseV21` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuCloseV21` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuCloseV21` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
countMenuPanelV21.Width-60*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuCloseV21` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
32*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_0` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `scrWarehouses/countMenuItemV21_0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuItemV21_0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuItemV21_0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1D4033")
```

### `scrWarehouses/countMenuItemV21_0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuItemV21_0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuItemV21_0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-170*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuItemV21_0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5746")
```

### `scrWarehouses/countMenuItemV21_0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,false);SetFocus(txtCountQty_2)
```

### `scrWarehouses/countMenuItemV21_0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_0` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuItemV21_0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuItemV21_0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#367259")
```

### `scrWarehouses/countMenuItemV21_0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллого үргэлжлүүлэх"
```

### `scrWarehouses/countMenuItemV21_0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuItemV21_0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
countMenuPanelV21.Width-40*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))+0*Min(78*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-150*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_1` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `scrWarehouses/countMenuItemV21_1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuItemV21_1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuItemV21_1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1D4033")
```

### `scrWarehouses/countMenuItemV21_1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuItemV21_1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuItemV21_1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-170*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuItemV21_1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5746")
```

### `scrWarehouses/countMenuItemV21_1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,false);Navigate(ScrHistory,ScreenTransition.Fade)
```

### `scrWarehouses/countMenuItemV21_1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuItemV21_1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuItemV21_1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#367259")
```

### `scrWarehouses/countMenuItemV21_1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллогын түүх"
```

### `scrWarehouses/countMenuItemV21_1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuItemV21_1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
countMenuPanelV21.Width-40*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))+1*Min(78*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-150*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_2` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `scrWarehouses/countMenuItemV21_2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuItemV21_2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuItemV21_2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1D4033")
```

### `scrWarehouses/countMenuItemV21_2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuItemV21_2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuItemV21_2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-170*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuItemV21_2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5746")
```

### `scrWarehouses/countMenuItemV21_2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,false);Navigate(ScrReport1,ScreenTransition.Fade)
```

### `scrWarehouses/countMenuItemV21_2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuItemV21_2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuItemV21_2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#367259")
```

### `scrWarehouses/countMenuItemV21_2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллогын тайлан"
```

### `scrWarehouses/countMenuItemV21_2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuItemV21_2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
countMenuPanelV21.Width-40*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))+2*Min(78*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-150*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_3` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `scrWarehouses/countMenuItemV21_3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuItemV21_3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuItemV21_3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1D4033")
```

### `scrWarehouses/countMenuItemV21_3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuItemV21_3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuItemV21_3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-170*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuItemV21_3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5746")
```

### `scrWarehouses/countMenuItemV21_3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,false);Navigate('Бараа засвар хийх',ScreenTransition.Fade)
```

### `scrWarehouses/countMenuItemV21_3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_3` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuItemV21_3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuItemV21_3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#367259")
```

### `scrWarehouses/countMenuItemV21_3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараа засварлах"
```

### `scrWarehouses/countMenuItemV21_3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuItemV21_3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
countMenuPanelV21.Width-40*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))+3*Min(78*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-150*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_4` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `scrWarehouses/countMenuItemV21_4` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuItemV21_4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_4` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuItemV21_4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1D4033")
```

### `scrWarehouses/countMenuItemV21_4` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuItemV21_4` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuItemV21_4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-170*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_4` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuItemV21_4` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5746")
```

### `scrWarehouses/countMenuItemV21_4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,false);Navigate(Screen1,ScreenTransition.Fade)
```

### `scrWarehouses/countMenuItemV21_4` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_4` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_4` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuItemV21_4` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_4` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuItemV21_4` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#367259")
```

### `scrWarehouses/countMenuItemV21_4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `scrWarehouses/countMenuItemV21_4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuItemV21_4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
countMenuPanelV21.Width-40*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))+4*Min(78*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-150*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_5` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `scrWarehouses/countMenuItemV21_5` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuItemV21_5` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_5` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuItemV21_5` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1D4033")
```

### `scrWarehouses/countMenuItemV21_5` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuItemV21_5` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuItemV21_5` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-170*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_5` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuItemV21_5` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_5` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5746")
```

### `scrWarehouses/countMenuItemV21_5` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,false);Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `scrWarehouses/countMenuItemV21_5` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_5` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_5` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuItemV21_5` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_5` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuItemV21_5` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_5` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#367259")
```

### `scrWarehouses/countMenuItemV21_5` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_5` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Профайл · тохиргоо"
```

### `scrWarehouses/countMenuItemV21_5` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuItemV21_5` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
countMenuPanelV21.Width-40*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_5` . **X**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_5` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))+5*Min(78*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-150*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_6` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `scrWarehouses/countMenuItemV21_6` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `scrWarehouses/countMenuItemV21_6` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_6` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `scrWarehouses/countMenuItemV21_6` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1D4033")
```

### `scrWarehouses/countMenuItemV21_6` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `scrWarehouses/countMenuItemV21_6` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.Lato
```

### `scrWarehouses/countMenuItemV21_6` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(64*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-170*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/countMenuItemV21_6` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `scrWarehouses/countMenuItemV21_6` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_6` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#2B5746")
```

### `scrWarehouses/countMenuItemV21_6` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,false);Navigate(нүүр,ScreenTransition.Fade)
```

### `scrWarehouses/countMenuItemV21_6` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_6` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_6` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Width/1180),(App.Width/640)))
```

### `scrWarehouses/countMenuItemV21_6` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*(If(App.Width >= First(App.SizeBreakpoints).Value && App.Width > App.Height,(App.Height/820),(App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_6` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `scrWarehouses/countMenuItemV21_6` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/countMenuItemV21_6` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#367259")
```

### `scrWarehouses/countMenuItemV21_6` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_6` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Үндсэн нүүр"
```

### `scrWarehouses/countMenuItemV21_6` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varCountMenuV21)
```

### `scrWarehouses/countMenuItemV21_6` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
countMenuPanelV21.Width-40*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_6` . **X**  _(Classic/Button@2.2.0)_
```powerfx
20*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))
```

### `scrWarehouses/countMenuItemV21_6` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
100*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136)))+6*Min(78*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))),(App.Height-150*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))/7)
```

### `scrWarehouses/phoneCountLocal` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(267)*App.Width/360
```

### `scrWarehouses/phoneCountLocal` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(7)*App.Height/720
```

### `scrWarehouses/phoneCountLocal` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(78)*App.Width/360
```

### `scrWarehouses/phoneCountLocal` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*App.Height/720
```

### `scrWarehouses/phoneCountLocal` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountLocal` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A94E10")
```

### `scrWarehouses/phoneCountLocal` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF7E8")
```

### `scrWarehouses/phoneCountLocal` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountLocal` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountLocal` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountLocal` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountLocal` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountLocal` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountLocal` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountLocal` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varCountMenuV21,true);SetFocus(countMenuItemV21_0)
```

### `scrWarehouses/phoneCountLocal` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Локал · " & CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced && ((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode)))
```

### `scrWarehouses/phoneCountPhotoEmpty` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(30)*App.Width/360
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(72)*App.Height/720
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(65)*App.Width/360
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(66)*App.Height/720
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#635C54")
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EEECE8")
```

### `scrWarehouses/phoneCountPhotoEmpty` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountPhotoEmpty` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountPhotoEmpty` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountPhotoEmpty` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountPhotoEmpty` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountPhotoEmpty` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21 && IsBlank(varNewPicture) && IsBlank(varItemPicture)))
```

### `scrWarehouses/phoneCountPhotoEmpty` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(countPhotoOpenV28)
```

### `scrWarehouses/phoneCountPhotoEmpty` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Барааны" & Char(10) & "зураг"
```

### `scrWarehouses/phoneCountPhotoEmpty` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Normal
```

### `scrWarehouses/phoneCountMinus` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(60)*App.Width/360
```

### `scrWarehouses/phoneCountMinus` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(305)*App.Height/720
```

### `scrWarehouses/phoneCountMinus` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(56)*App.Width/360
```

### `scrWarehouses/phoneCountMinus` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*App.Height/720
```

### `scrWarehouses/phoneCountMinus` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
21*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountMinus` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `scrWarehouses/phoneCountMinus` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/phoneCountMinus` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*App.Width/360
```

### `scrWarehouses/phoneCountMinus` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountMinus` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountMinus` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountMinus` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountMinus` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountMinus` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountMinus` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountMinus` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({q:IfError(Value(txtCountQty_2.Text),0)},Set(phoneCountItem,varItem.number);Set(phoneCountValue,Text(Max(0,Coalesce(q,0)-1))));Reset(txtCountQty_2)
```

### `scrWarehouses/phoneCountMinus` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"−"
```

### `scrWarehouses/phoneCountMinus` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2DEDA")
```

### `scrWarehouses/phoneCountPlus` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(241)*App.Width/360
```

### `scrWarehouses/phoneCountPlus` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(305)*App.Height/720
```

### `scrWarehouses/phoneCountPlus` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(56)*App.Width/360
```

### `scrWarehouses/phoneCountPlus` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*App.Height/720
```

### `scrWarehouses/phoneCountPlus` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
21*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountPlus` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `scrWarehouses/phoneCountPlus` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/phoneCountPlus` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*App.Width/360
```

### `scrWarehouses/phoneCountPlus` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountPlus` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountPlus` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountPlus` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(15)*App.Width/360
```

### `scrWarehouses/phoneCountPlus` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountPlus` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountPlus` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountPlus` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({q:IfError(Value(txtCountQty_2.Text),0)},Set(phoneCountItem,varItem.number);Set(phoneCountValue,Text(Max(0,Coalesce(q,0)+1))));Reset(txtCountQty_2)
```

### `scrWarehouses/phoneCountPlus` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"+"
```

### `scrWarehouses/phoneCountPlus` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2DEDA")
```

### `scrWarehouses/phoneCountReasonHead` . **X**  _(Label@2.5.1)_
```powerfx
(16)*App.Width/360
```

### `scrWarehouses/phoneCountReasonHead` . **Y**  _(Label@2.5.1)_
```powerfx
(381)*App.Height/720
```

### `scrWarehouses/phoneCountReasonHead` . **Width**  _(Label@2.5.1)_
```powerfx
(326)*App.Width/360
```

### `scrWarehouses/phoneCountReasonHead` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*App.Height/720
```

### `scrWarehouses/phoneCountReasonHead` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountReasonHead` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `scrWarehouses/phoneCountReasonHead` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `scrWarehouses/phoneCountReasonHead` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountReasonHead` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүний шалтгаан"
```

### `scrWarehouses/phoneCountReasonHead` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `scrWarehouses/phoneCountReason0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(16)*App.Width/360
```

### `scrWarehouses/phoneCountReason0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(411)*App.Height/720
```

### `scrWarehouses/phoneCountReason0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(139)*App.Width/360
```

### `scrWarehouses/phoneCountReason0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(34)*App.Height/720
```

### `scrWarehouses/phoneCountReason0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountReason0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Хэмжилтийн зөрүү" && phoneReasonItem=varItem.number,Color.White,ColorValue("#202225"))
```

### `scrWarehouses/phoneCountReason0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Хэмжилтийн зөрүү" && phoneReasonItem=varItem.number,ColorValue("#F15D18"),Color.White)
```

### `scrWarehouses/phoneCountReason0` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*App.Width/360
```

### `scrWarehouses/phoneCountReason0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountReason0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountReason0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountReason0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(phoneCountReason,If(phoneCountReason="Хэмжилтийн зөрүү" && phoneReasonItem=varItem.number,Blank(),"Хэмжилтийн зөрүү"));Set(phoneReasonItem,varItem.number)
```

### `scrWarehouses/phoneCountReason0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хэмжилтийн зөрүү"
```

### `scrWarehouses/phoneCountReason0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2DEDA")
```

### `scrWarehouses/phoneCountReason1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(162)*App.Width/360
```

### `scrWarehouses/phoneCountReason1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(411)*App.Height/720
```

### `scrWarehouses/phoneCountReason1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(86)*App.Width/360
```

### `scrWarehouses/phoneCountReason1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(34)*App.Height/720
```

### `scrWarehouses/phoneCountReason1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountReason1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Гэмтэлтэй" && phoneReasonItem=varItem.number,Color.White,ColorValue("#202225"))
```

### `scrWarehouses/phoneCountReason1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Гэмтэлтэй" && phoneReasonItem=varItem.number,ColorValue("#F15D18"),Color.White)
```

### `scrWarehouses/phoneCountReason1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*App.Width/360
```

### `scrWarehouses/phoneCountReason1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountReason1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountReason1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountReason1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(phoneCountReason,If(phoneCountReason="Гэмтэлтэй" && phoneReasonItem=varItem.number,Blank(),"Гэмтэлтэй"));Set(phoneReasonItem,varItem.number)
```

### `scrWarehouses/phoneCountReason1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гэмтэлтэй"
```

### `scrWarehouses/phoneCountReason1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2DEDA")
```

### `scrWarehouses/phoneCountReason2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(16)*App.Width/360
```

### `scrWarehouses/phoneCountReason2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(450)*App.Height/720
```

### `scrWarehouses/phoneCountReason2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(127)*App.Width/360
```

### `scrWarehouses/phoneCountReason2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(34)*App.Height/720
```

### `scrWarehouses/phoneCountReason2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountReason2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Бичиг баримтгүй" && phoneReasonItem=varItem.number,Color.White,ColorValue("#202225"))
```

### `scrWarehouses/phoneCountReason2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Бичиг баримтгүй" && phoneReasonItem=varItem.number,ColorValue("#F15D18"),Color.White)
```

### `scrWarehouses/phoneCountReason2` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*App.Width/360
```

### `scrWarehouses/phoneCountReason2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountReason2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountReason2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountReason2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(phoneCountReason,If(phoneCountReason="Бичиг баримтгүй" && phoneReasonItem=varItem.number,Blank(),"Бичиг баримтгүй"));Set(phoneReasonItem,varItem.number)
```

### `scrWarehouses/phoneCountReason2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бичиг баримтгүй"
```

### `scrWarehouses/phoneCountReason2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2DEDA")
```

### `scrWarehouses/phoneCountReason3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(150)*App.Width/360
```

### `scrWarehouses/phoneCountReason3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(450)*App.Height/720
```

### `scrWarehouses/phoneCountReason3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(106)*App.Width/360
```

### `scrWarehouses/phoneCountReason3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(34)*App.Height/720
```

### `scrWarehouses/phoneCountReason3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountReason3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Байршил өөр" && phoneReasonItem=varItem.number,Color.White,ColorValue("#202225"))
```

### `scrWarehouses/phoneCountReason3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(phoneCountReason="Байршил өөр" && phoneReasonItem=varItem.number,ColorValue("#F15D18"),Color.White)
```

### `scrWarehouses/phoneCountReason3` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*App.Width/360
```

### `scrWarehouses/phoneCountReason3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(17)*App.Width/360
```

### `scrWarehouses/phoneCountReason3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountReason3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountReason3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountReason3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(phoneCountReason,If(phoneCountReason="Байршил өөр" && phoneReasonItem=varItem.number,Blank(),"Байршил өөр"));Set(phoneReasonItem,varItem.number)
```

### `scrWarehouses/phoneCountReason3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Байршил өөр"
```

### `scrWarehouses/phoneCountReason3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2DEDA")
```

### `scrWarehouses/phoneCountCameraIcon` . **X**  _(Image@2.2.3)_
```powerfx
(61)*App.Width/360
```

### `scrWarehouses/phoneCountCameraIcon` . **Y**  _(Image@2.2.3)_
```powerfx
(510)*App.Height/720
```

### `scrWarehouses/phoneCountCameraIcon` . **Width**  _(Image@2.2.3)_
```powerfx
(18)*App.Width/360
```

### `scrWarehouses/phoneCountCameraIcon` . **Height**  _(Image@2.2.3)_
```powerfx
(18)*App.Height/720
```

### `scrWarehouses/phoneCountCameraIcon` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `scrWarehouses/phoneCountCameraIcon` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountCameraIcon` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='#202225' stroke-width='1.7' stroke-linejoin='round'><path d='M3 7h4l2-3h6l2 3h4v13H3z'/><circle cx='12' cy='13' r='3.5'/></svg>")
```

### `scrWarehouses/phoneCountCameraIcon` . **OnSelect**  _(Image@2.2.3)_
```powerfx
Select(countPhotoOpenV28)
```

### `scrWarehouses/phoneCountCommentButton` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(183)*App.Width/360
```

### `scrWarehouses/phoneCountCommentButton` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(497)*App.Height/720
```

### `scrWarehouses/phoneCountCommentButton` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(161)*App.Width/360
```

### `scrWarehouses/phoneCountCommentButton` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(45)*App.Height/720
```

### `scrWarehouses/phoneCountCommentButton` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountCommentButton` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `scrWarehouses/phoneCountCommentButton` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/phoneCountCommentButton` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(1)*App.Width/360
```

### `scrWarehouses/phoneCountCommentButton` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountCommentButton` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountCommentButton` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountCommentButton` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(12)*App.Width/360
```

### `scrWarehouses/phoneCountCommentButton` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/phoneCountCommentButton` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/phoneCountCommentButton` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21))
```

### `scrWarehouses/phoneCountCommentButton` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(phoneCountNoteOpen,!Coalesce(phoneCountNoteOpen,false))
```

### `scrWarehouses/phoneCountCommentButton` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"+ Тайлбар"
```

### `scrWarehouses/phoneCountCommentButton` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E2DEDA")
```

### `scrWarehouses/phoneCountNote` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(16)*App.Width/360
```

### `scrWarehouses/phoneCountNote` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(551)*App.Height/720
```

### `scrWarehouses/phoneCountNote` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(328)*App.Width/360
```

### `scrWarehouses/phoneCountNote` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(74)*App.Height/720
```

### `scrWarehouses/phoneCountNote` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
13*Min(App.Width/360,App.Height/720)
```

### `scrWarehouses/phoneCountNote` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#242528")
```

### `scrWarehouses/phoneCountNote` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `scrWarehouses/phoneCountNote` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && (!IsBlank(varItem.number) && !varShowWarehouseList && !varCountMenuV21 && Coalesce(phoneCountNoteOpen,false)))
```

### `scrWarehouses/phoneCountNote` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Тооллогын тайлбар"
```

### `scrWarehouses/phoneCountNote` . **Mode**  _(Classic/TextInput@2.3.2)_
```powerfx
TextMode.MultiLine
```

### `scrWarehouses/pgDenied458` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `scrWarehouses/pgDenied458` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `scrWarehouses/pgDenied458` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `scrWarehouses/pgDenied458` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `scrWarehouses/pgDenied458` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `scrWarehouses/pgDenied458` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `scrWarehouses/pgDenied458` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `scrWarehouses/pgDenied458` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `scrWarehouses/pgDenied458` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `scrWarehouses/pgDenied458` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

