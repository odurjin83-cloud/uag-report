# ScrPageAdmin — Power Fx formulas

### `ScrPageAdmin` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title)),Set(pgPane,false);Set(pgAdding,false);Set(pgBusy,false);Set(pgSaving,false);Set(pgReadOk,false);Set(pgPage,0);Reset(pgFind);Clear(pgBCMatches);Set(pgDirectoryOk,false);Clear(pgAssigned);Set(pgOffset,0);IfError(ClearCollect(pgAssigned,SortByColumns(Filter(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && (IsBlank(Trim(pgFind.Text)) || StartsWith(UserEmail,Lower(Trim(pgFind.Text))) || StartsWith(Title,Trim(pgFind.Text)))),"UserEmail",SortOrder.Ascending)),Clear(pgAssigned);Notify("Эрхийн жагсаалт уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgDirectoryOk,true);true);Set(pgLocationsOk,false);Clear(pgLocations);IfError(ClearCollect(pgLocations,SortByColumns('locations (v2.0)',"code",SortOrder.Ascending));Set(pgLocationsOk,true),Clear(pgLocations);Notify("BC агуулахын жагсаалт уншсангүй.",NotificationType.Warning))
)
```

### `ScrPageAdmin` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrPageAdmin` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrPageAdmin` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrPageAdmin/ScrPageAdminRail` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,182*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminRail` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height
```

### `ScrPageAdmin/ScrPageAdminRail` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/ScrPageAdminRail` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/ScrPageAdminRail` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width>=First(App.SizeBreakpoints).Value)
```

### `ScrPageAdmin/ScrPageAdminNav0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/ScrPageAdminNav0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,105*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,160*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,40*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/ScrPageAdminNav0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/ScrPageAdminNav0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нүүр"
```

### `ScrPageAdmin/ScrPageAdminNav0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(нүүр,ScreenTransition.None)
```

### `ScrPageAdmin/ScrPageAdminNav0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|home|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrPageAdmin/ScrPageAdminNav1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/ScrPageAdminNav1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,154*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,160*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,40*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/ScrPageAdminNav1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/ScrPageAdminNav1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллого"
```

### `ScrPageAdmin/ScrPageAdminNav1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrCountHome,ScreenTransition.None)
```

### `ScrPageAdmin/ScrPageAdminNav1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrPageAdmin/ScrPageAdminNav2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/ScrPageAdminNav2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,203*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,160*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,40*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/ScrPageAdminNav2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/ScrPageAdminNav2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrPageAdmin/ScrPageAdminNav2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(Screen1,ScreenTransition.None)
```

### `ScrPageAdmin/ScrPageAdminNav2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrPageAdmin/ScrPageAdminNav3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/ScrPageAdminNav3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,252*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,160*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,40*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/ScrPageAdminNav3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/ScrPageAdminNav3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зарлага"
```

### `ScrPageAdmin/ScrPageAdminNav3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrIssueA25Test,ScreenTransition.None)
```

### `ScrPageAdmin/ScrPageAdminNav3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title)))
```

### `ScrPageAdmin/ScrPageAdminNav4` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/ScrPageAdminNav4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,301*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,160*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,40*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/ScrPageAdminNav4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/ScrPageAdminNav4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нэгдсэн тайлан"
```

### `ScrPageAdmin/ScrPageAdminNav4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrCombined,ScreenTransition.None)
```

### `ScrPageAdmin/ScrPageAdminNav4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrPageAdmin/ScrPageAdminNav5` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/ScrPageAdminNav5` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,350*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,160*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,40*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E5")
```

### `ScrPageAdmin/ScrPageAdminNav5` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/ScrPageAdminNav5` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хэрэглэгч ба эрх"
```

### `ScrPageAdmin/ScrPageAdminNav5` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrPageAdmin,ScreenTransition.None)
```

### `ScrPageAdmin/ScrPageAdminNav5` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title)))
```

### `ScrPageAdmin/ScrPageAdminHead` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (true)
```

### `ScrPageAdmin/ScrPageAdminHead` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,207*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminHead` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,8*Parent.Height/700,14*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminHead` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,234*Parent.Width/360,435*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminHead` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,40*Parent.Height/700,42*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminHead` . **Size**  _(Label@2.5.1)_
```powerfx
22*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminHead` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/ScrPageAdminHead` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrPageAdmin/ScrPageAdminHead` . **Text**  _(Label@2.5.1)_
```powerfx
"Хэрэглэгч ба эрх"
```

### `ScrPageAdmin/ScrPageAdminHead` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrPageAdmin/ScrPageAdminBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,281*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Parent.Height/700,0*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,65*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrPageAdmin/ScrPageAdminBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,34*Parent.Height/700,0*Parent.Height/680)
```

### `ScrPageAdmin/ScrPageAdminBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/ScrPageAdminBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/ScrPageAdminBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/ScrPageAdminBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/ScrPageAdminBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/ScrPageAdminBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(pgPane,"Жагсаалт","Буцах")
```

### `ScrPageAdmin/ScrPageAdminBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (App.Width<First(App.SizeBreakpoints).Value)
```

### `ScrPageAdmin/ScrPageAdminBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(pgPane,Set(pgPane,false),Back())
```

### `ScrPageAdmin/pgFind` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane))
```

### `ScrPageAdmin/pgFind` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgFind` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,110*Parent.Height/700,120*Parent.Height/680)
```

### `ScrPageAdmin/pgFind` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,236*Parent.Width/360,294*Parent.Width/1100)
```

### `ScrPageAdmin/pgFind` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,42*Parent.Height/680)
```

### `ScrPageAdmin/pgFind` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgFind` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgFind` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgFind` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
If(pgAdding,"BC ажилтны нэр эсвэл код","Нэвтрэх имэйл эсвэл ажилтны код")
```

### `ScrPageAdmin/pgFind` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
Set(pgPane,false);Set(pgOffset,0);Clear(pgBCMatches);If(!pgAdding,Set(pgDirectoryOk,false);Clear(pgAssigned);Set(pgOffset,0);IfError(ClearCollect(pgAssigned,SortByColumns(Filter(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && (IsBlank(Trim(pgFind.Text)) || StartsWith(UserEmail,Lower(Trim(pgFind.Text))) || StartsWith(Title,Trim(pgFind.Text)))),"UserEmail",SortOrder.Ascending)),Clear(pgAssigned);Notify("Эрхийн жагсаалт уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgDirectoryOk,true);true))
```

### `ScrPageAdmin/pgNew` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane))
```

### `ScrPageAdmin/pgNew` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,258*Parent.Width/360,510*Parent.Width/1100)
```

### `ScrPageAdmin/pgNew` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,110*Parent.Height/700,120*Parent.Height/680)
```

### `ScrPageAdmin/pgNew` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,86*Parent.Width/360,94*Parent.Width/1100)
```

### `ScrPageAdmin/pgNew` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,42*Parent.Height/680)
```

### `ScrPageAdmin/pgNew` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgNew` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgNew` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#C34810")
```

### `ScrPageAdmin/pgNew` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgNew` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgNew` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хайх"
```

### `ScrPageAdmin/pgNew` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Connection.Connected && !pgBusy && (!pgAdding || Len(Trim(pgFind.Text))>=2),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrPageAdmin/pgNew` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(pgAdding,Set(pgBusy,true);Set(pgPane,false);Clear(pgBCMatches);Set(pgOffset,0);IfError(ClearCollect(pgBCMatches,ForAll(Table(ParseJSON(TMEIssueA25Test.Run(JSON({mode:"search",query:Trim(pgFind.Text)})).itemsjson)) As e,{code:Text(e.Value.No),fullName:Text(e.Value.First_Name) & " " & Text(e.Value.Last_Name),org:Text(e.Value.Department_Name),job:Text(e.Value.Position_Name)}));If(IsEmpty(pgBCMatches),Notify("Ажилтан олдсонгүй.",NotificationType.Information)),Notify(FirstError.Message,NotificationType.Error));Set(pgBusy,false),Set(pgDirectoryOk,false);Clear(pgAssigned);Set(pgOffset,0);IfError(ClearCollect(pgAssigned,SortByColumns(Filter(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && (IsBlank(Trim(pgFind.Text)) || StartsWith(UserEmail,Lower(Trim(pgFind.Text))) || StartsWith(Title,Trim(pgFind.Text)))),"UserEmail",SortOrder.Ascending)),Clear(pgAssigned);Notify("Эрхийн жагсаалт уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgDirectoryOk,true);true))
```

### `ScrPageAdmin/pgUser0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DB")
```

### `ScrPageAdmin/pgUser0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Width/360,16*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser0` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgUser0` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(pgBusy || pgSaving,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrPageAdmin/pgUser0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,209*Parent.Height/700,211*Parent.Height/680)
```

### `ScrPageAdmin/pgUser0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Width/360,396*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Parent.Height/700,62*Parent.Height/680)
```

### `ScrPageAdmin/pgUser0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgUser0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgUser0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgUser0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgUser0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgUser0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane) && If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+1)
```

### `ScrPageAdmin/pgUser0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+1,If(pgAdding,With({r:Index(pgBCMatches,Coalesce(pgOffset,0)+1)},r.fullName & Char(10) & r.code & "  ·  " & r.org),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+1)},r.UserEmail & Char(10) & First(Split(r.Title,"|")).Value & "  ·  " & Switch(r.Role.Value,"Admin","Админ","Supervisor","Ахлагч","Auditor","Аудитор","Counter","Нярав","") & If(r.Active,"  ·  Идэвхтэй","  ·  Түр хаасан"))),"")
```

### `ScrPageAdmin/pgUser0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgBusy,true);If(pgAdding,Set(pgPerson,Index(pgBCMatches,Coalesce(pgOffset,0)+1)),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+1)},Set(pgExpectedId,r.ID);Set(pgPerson,{code:First(Split(r.Title,"|")).Value,fullName:r.UserEmail,org:"",job:""}));IfError(With({reply:ParseJSON(TMEIssueA25Test.Run(JSON({mode:"search",query:pgPerson.code})).itemsjson)},With({e:LookUp(Table(reply),Text(Value.No)=pgPerson.code).Value},If(!IsBlank(Text(e.No)),Set(pgPerson,{code:Text(e.No),fullName:Trim(Text(e.First_Name) & " " & Text(e.Last_Name)),org:Text(e.Department_Name),job:Text(e.Position_Name)})))),Notify("BC ажилтны дэлгэрэнгүйг уншсангүй.",NotificationType.Warning)));Set(pgReadOk,false);Set(pgPane,false);Set(pgEdit,Blank());IfError(Refresh(AssetUserAccess),Notify("Эрхийн жагсаалт шинэчилсэнгүй. " & FirstError.Message,NotificationType.Error);false,Set(pgEdit,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && StartsWith(Title,pgPerson.code & "|"))),Notify("Эрхийн бүртгэлийг уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgReadOk,pgAdding || (!IsBlank(pgEdit.ID) && pgEdit.ID=pgExpectedId));If(!pgReadOk,Notify("Бүртгэл өөрчлөгдсөн. Жагсаалтаа шинэчилнэ үү.",NotificationType.Warning));true);If(pgReadOk,ClearCollect(pgRights,Filter(Split(Coalesce(pgEdit.Title,""),"|"),Value in ["home","count","stock","issue","photo","dashboard","history","report","combined","edit","sync","admin"]));Set(pgRole,Coalesce(pgEdit.Role.Value,"Counter"));Set(pgEnabled,Coalesce(pgEdit.Active,true));ClearCollect(pgWh,Filter(Split(Coalesce(pgEdit.LocationCode,""),"|"),!IsBlank(Value) && Value<>"*"));Set(pgAllWh,pgEdit.LocationCode="*");Set(pgShowWh,false);Set(pgPage,0);Set(pgWhPage,0);Reset(pgLogin);Set(pgPane,true));Set(pgBusy,false)
```

### `ScrPageAdmin/pgUser1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DB")
```

### `ScrPageAdmin/pgUser1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Width/360,16*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser1` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgUser1` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(pgBusy || pgSaving,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrPageAdmin/pgUser1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,280*Parent.Height/700,279*Parent.Height/680)
```

### `ScrPageAdmin/pgUser1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Width/360,396*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Parent.Height/700,62*Parent.Height/680)
```

### `ScrPageAdmin/pgUser1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgUser1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgUser1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgUser1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgUser1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgUser1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane) && If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+2)
```

### `ScrPageAdmin/pgUser1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+2,If(pgAdding,With({r:Index(pgBCMatches,Coalesce(pgOffset,0)+2)},r.fullName & Char(10) & r.code & "  ·  " & r.org),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+2)},r.UserEmail & Char(10) & First(Split(r.Title,"|")).Value & "  ·  " & Switch(r.Role.Value,"Admin","Админ","Supervisor","Ахлагч","Auditor","Аудитор","Counter","Нярав","") & If(r.Active,"  ·  Идэвхтэй","  ·  Түр хаасан"))),"")
```

### `ScrPageAdmin/pgUser1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgBusy,true);If(pgAdding,Set(pgPerson,Index(pgBCMatches,Coalesce(pgOffset,0)+2)),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+2)},Set(pgExpectedId,r.ID);Set(pgPerson,{code:First(Split(r.Title,"|")).Value,fullName:r.UserEmail,org:"",job:""}));IfError(With({reply:ParseJSON(TMEIssueA25Test.Run(JSON({mode:"search",query:pgPerson.code})).itemsjson)},With({e:LookUp(Table(reply),Text(Value.No)=pgPerson.code).Value},If(!IsBlank(Text(e.No)),Set(pgPerson,{code:Text(e.No),fullName:Trim(Text(e.First_Name) & " " & Text(e.Last_Name)),org:Text(e.Department_Name),job:Text(e.Position_Name)})))),Notify("BC ажилтны дэлгэрэнгүйг уншсангүй.",NotificationType.Warning)));Set(pgReadOk,false);Set(pgPane,false);Set(pgEdit,Blank());IfError(Refresh(AssetUserAccess),Notify("Эрхийн жагсаалт шинэчилсэнгүй. " & FirstError.Message,NotificationType.Error);false,Set(pgEdit,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && StartsWith(Title,pgPerson.code & "|"))),Notify("Эрхийн бүртгэлийг уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgReadOk,pgAdding || (!IsBlank(pgEdit.ID) && pgEdit.ID=pgExpectedId));If(!pgReadOk,Notify("Бүртгэл өөрчлөгдсөн. Жагсаалтаа шинэчилнэ үү.",NotificationType.Warning));true);If(pgReadOk,ClearCollect(pgRights,Filter(Split(Coalesce(pgEdit.Title,""),"|"),Value in ["home","count","stock","issue","photo","dashboard","history","report","combined","edit","sync","admin"]));Set(pgRole,Coalesce(pgEdit.Role.Value,"Counter"));Set(pgEnabled,Coalesce(pgEdit.Active,true));ClearCollect(pgWh,Filter(Split(Coalesce(pgEdit.LocationCode,""),"|"),!IsBlank(Value) && Value<>"*"));Set(pgAllWh,pgEdit.LocationCode="*");Set(pgShowWh,false);Set(pgPage,0);Set(pgWhPage,0);Reset(pgLogin);Set(pgPane,true));Set(pgBusy,false)
```

### `ScrPageAdmin/pgUser2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DB")
```

### `ScrPageAdmin/pgUser2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Width/360,16*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser2` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgUser2` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(pgBusy || pgSaving,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrPageAdmin/pgUser2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,351*Parent.Height/700,347*Parent.Height/680)
```

### `ScrPageAdmin/pgUser2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Width/360,396*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Parent.Height/700,62*Parent.Height/680)
```

### `ScrPageAdmin/pgUser2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgUser2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgUser2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgUser2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgUser2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgUser2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane) && If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+3)
```

### `ScrPageAdmin/pgUser2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+3,If(pgAdding,With({r:Index(pgBCMatches,Coalesce(pgOffset,0)+3)},r.fullName & Char(10) & r.code & "  ·  " & r.org),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+3)},r.UserEmail & Char(10) & First(Split(r.Title,"|")).Value & "  ·  " & Switch(r.Role.Value,"Admin","Админ","Supervisor","Ахлагч","Auditor","Аудитор","Counter","Нярав","") & If(r.Active,"  ·  Идэвхтэй","  ·  Түр хаасан"))),"")
```

### `ScrPageAdmin/pgUser2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgBusy,true);If(pgAdding,Set(pgPerson,Index(pgBCMatches,Coalesce(pgOffset,0)+3)),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+3)},Set(pgExpectedId,r.ID);Set(pgPerson,{code:First(Split(r.Title,"|")).Value,fullName:r.UserEmail,org:"",job:""}));IfError(With({reply:ParseJSON(TMEIssueA25Test.Run(JSON({mode:"search",query:pgPerson.code})).itemsjson)},With({e:LookUp(Table(reply),Text(Value.No)=pgPerson.code).Value},If(!IsBlank(Text(e.No)),Set(pgPerson,{code:Text(e.No),fullName:Trim(Text(e.First_Name) & " " & Text(e.Last_Name)),org:Text(e.Department_Name),job:Text(e.Position_Name)})))),Notify("BC ажилтны дэлгэрэнгүйг уншсангүй.",NotificationType.Warning)));Set(pgReadOk,false);Set(pgPane,false);Set(pgEdit,Blank());IfError(Refresh(AssetUserAccess),Notify("Эрхийн жагсаалт шинэчилсэнгүй. " & FirstError.Message,NotificationType.Error);false,Set(pgEdit,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && StartsWith(Title,pgPerson.code & "|"))),Notify("Эрхийн бүртгэлийг уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgReadOk,pgAdding || (!IsBlank(pgEdit.ID) && pgEdit.ID=pgExpectedId));If(!pgReadOk,Notify("Бүртгэл өөрчлөгдсөн. Жагсаалтаа шинэчилнэ үү.",NotificationType.Warning));true);If(pgReadOk,ClearCollect(pgRights,Filter(Split(Coalesce(pgEdit.Title,""),"|"),Value in ["home","count","stock","issue","photo","dashboard","history","report","combined","edit","sync","admin"]));Set(pgRole,Coalesce(pgEdit.Role.Value,"Counter"));Set(pgEnabled,Coalesce(pgEdit.Active,true));ClearCollect(pgWh,Filter(Split(Coalesce(pgEdit.LocationCode,""),"|"),!IsBlank(Value) && Value<>"*"));Set(pgAllWh,pgEdit.LocationCode="*");Set(pgShowWh,false);Set(pgPage,0);Set(pgWhPage,0);Reset(pgLogin);Set(pgPane,true));Set(pgBusy,false)
```

### `ScrPageAdmin/pgUser3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DB")
```

### `ScrPageAdmin/pgUser3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Width/360,16*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser3` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgUser3` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(pgBusy || pgSaving,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrPageAdmin/pgUser3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,422*Parent.Height/700,415*Parent.Height/680)
```

### `ScrPageAdmin/pgUser3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Width/360,396*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Parent.Height/700,62*Parent.Height/680)
```

### `ScrPageAdmin/pgUser3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgUser3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgUser3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgUser3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgUser3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgUser3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane) && If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+4)
```

### `ScrPageAdmin/pgUser3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+4,If(pgAdding,With({r:Index(pgBCMatches,Coalesce(pgOffset,0)+4)},r.fullName & Char(10) & r.code & "  ·  " & r.org),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+4)},r.UserEmail & Char(10) & First(Split(r.Title,"|")).Value & "  ·  " & Switch(r.Role.Value,"Admin","Админ","Supervisor","Ахлагч","Auditor","Аудитор","Counter","Нярав","") & If(r.Active,"  ·  Идэвхтэй","  ·  Түр хаасан"))),"")
```

### `ScrPageAdmin/pgUser3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgBusy,true);If(pgAdding,Set(pgPerson,Index(pgBCMatches,Coalesce(pgOffset,0)+4)),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+4)},Set(pgExpectedId,r.ID);Set(pgPerson,{code:First(Split(r.Title,"|")).Value,fullName:r.UserEmail,org:"",job:""}));IfError(With({reply:ParseJSON(TMEIssueA25Test.Run(JSON({mode:"search",query:pgPerson.code})).itemsjson)},With({e:LookUp(Table(reply),Text(Value.No)=pgPerson.code).Value},If(!IsBlank(Text(e.No)),Set(pgPerson,{code:Text(e.No),fullName:Trim(Text(e.First_Name) & " " & Text(e.Last_Name)),org:Text(e.Department_Name),job:Text(e.Position_Name)})))),Notify("BC ажилтны дэлгэрэнгүйг уншсангүй.",NotificationType.Warning)));Set(pgReadOk,false);Set(pgPane,false);Set(pgEdit,Blank());IfError(Refresh(AssetUserAccess),Notify("Эрхийн жагсаалт шинэчилсэнгүй. " & FirstError.Message,NotificationType.Error);false,Set(pgEdit,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && StartsWith(Title,pgPerson.code & "|"))),Notify("Эрхийн бүртгэлийг уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgReadOk,pgAdding || (!IsBlank(pgEdit.ID) && pgEdit.ID=pgExpectedId));If(!pgReadOk,Notify("Бүртгэл өөрчлөгдсөн. Жагсаалтаа шинэчилнэ үү.",NotificationType.Warning));true);If(pgReadOk,ClearCollect(pgRights,Filter(Split(Coalesce(pgEdit.Title,""),"|"),Value in ["home","count","stock","issue","photo","dashboard","history","report","combined","edit","sync","admin"]));Set(pgRole,Coalesce(pgEdit.Role.Value,"Counter"));Set(pgEnabled,Coalesce(pgEdit.Active,true));ClearCollect(pgWh,Filter(Split(Coalesce(pgEdit.LocationCode,""),"|"),!IsBlank(Value) && Value<>"*"));Set(pgAllWh,pgEdit.LocationCode="*");Set(pgShowWh,false);Set(pgPage,0);Set(pgWhPage,0);Reset(pgLogin);Set(pgPane,true));Set(pgBusy,false)
```

### `ScrPageAdmin/pgUser4` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DB")
```

### `ScrPageAdmin/pgUser4` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Width/360,16*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser4` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgUser4` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(pgBusy || pgSaving,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrPageAdmin/pgUser4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,493*Parent.Height/700,483*Parent.Height/680)
```

### `ScrPageAdmin/pgUser4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Width/360,396*Parent.Width/1100)
```

### `ScrPageAdmin/pgUser4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,64*Parent.Height/700,62*Parent.Height/680)
```

### `ScrPageAdmin/pgUser4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgUser4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgUser4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgUser4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgUser4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgUser4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane) && If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+5)
```

### `ScrPageAdmin/pgUser4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>=Coalesce(pgOffset,0)+5,If(pgAdding,With({r:Index(pgBCMatches,Coalesce(pgOffset,0)+5)},r.fullName & Char(10) & r.code & "  ·  " & r.org),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+5)},r.UserEmail & Char(10) & First(Split(r.Title,"|")).Value & "  ·  " & Switch(r.Role.Value,"Admin","Админ","Supervisor","Ахлагч","Auditor","Аудитор","Counter","Нярав","") & If(r.Active,"  ·  Идэвхтэй","  ·  Түр хаасан"))),"")
```

### `ScrPageAdmin/pgUser4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgBusy,true);If(pgAdding,Set(pgPerson,Index(pgBCMatches,Coalesce(pgOffset,0)+5)),With({r:Index(pgAssigned,Coalesce(pgOffset,0)+5)},Set(pgExpectedId,r.ID);Set(pgPerson,{code:First(Split(r.Title,"|")).Value,fullName:r.UserEmail,org:"",job:""}));IfError(With({reply:ParseJSON(TMEIssueA25Test.Run(JSON({mode:"search",query:pgPerson.code})).itemsjson)},With({e:LookUp(Table(reply),Text(Value.No)=pgPerson.code).Value},If(!IsBlank(Text(e.No)),Set(pgPerson,{code:Text(e.No),fullName:Trim(Text(e.First_Name) & " " & Text(e.Last_Name)),org:Text(e.Department_Name),job:Text(e.Position_Name)})))),Notify("BC ажилтны дэлгэрэнгүйг уншсангүй.",NotificationType.Warning)));Set(pgReadOk,false);Set(pgPane,false);Set(pgEdit,Blank());IfError(Refresh(AssetUserAccess),Notify("Эрхийн жагсаалт шинэчилсэнгүй. " & FirstError.Message,NotificationType.Error);false,Set(pgEdit,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && StartsWith(Title,pgPerson.code & "|"))),Notify("Эрхийн бүртгэлийг уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgReadOk,pgAdding || (!IsBlank(pgEdit.ID) && pgEdit.ID=pgExpectedId));If(!pgReadOk,Notify("Бүртгэл өөрчлөгдсөн. Жагсаалтаа шинэчилнэ үү.",NotificationType.Warning));true);If(pgReadOk,ClearCollect(pgRights,Filter(Split(Coalesce(pgEdit.Title,""),"|"),Value in ["home","count","stock","issue","photo","dashboard","history","report","combined","edit","sync","admin"]));Set(pgRole,Coalesce(pgEdit.Role.Value,"Counter"));Set(pgEnabled,Coalesce(pgEdit.Active,true));ClearCollect(pgWh,Filter(Split(Coalesce(pgEdit.LocationCode,""),"|"),!IsBlank(Value) && Value<>"*"));Set(pgAllWh,pgEdit.LocationCode="*");Set(pgShowWh,false);Set(pgPage,0);Set(pgWhPage,0);Reset(pgLogin);Set(pgPane,true));Set(pgBusy,false)
```

### `ScrPageAdmin/pgUsersNext` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgUsersNext` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,578*Parent.Height/700,558*Parent.Height/680)
```

### `ScrPageAdmin/pgUsersNext` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Width/360,396*Parent.Width/1100)
```

### `ScrPageAdmin/pgUsersNext` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,42*Parent.Height/680)
```

### `ScrPageAdmin/pgUsersNext` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgUsersNext` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgUsersNext` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgUsersNext` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgUsersNext` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgUsersNext` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane) && If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))>5)
```

### `ScrPageAdmin/pgUsersNext` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн хэрэглэгчид  →"
```

### `ScrPageAdmin/pgUsersNext` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgOffset,If(pgOffset+5>=If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned)),0,pgOffset+5))
```

### `ScrPageAdmin/pgEditing` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgEditing` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,57*Parent.Height/700,68*Parent.Height/680)
```

### `ScrPageAdmin/pgEditing` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgEditing` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,56*Parent.Height/700,65*Parent.Height/680)
```

### `ScrPageAdmin/pgEditing` . **Size**  _(Label@2.5.1)_
```powerfx
16*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgEditing` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgEditing` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgEditing` . **Text**  _(Label@2.5.1)_
```powerfx
pgPerson.fullName & "  ·  " & pgPerson.code & Char(10) & Trim(pgPerson.org & "  " & pgPerson.job)
```

### `ScrPageAdmin/pgEditing` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgEditing` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrPageAdmin/pgLogin` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgLogin` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,121*Parent.Height/700,143*Parent.Height/680)
```

### `ScrPageAdmin/pgLogin` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgLogin` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgLogin` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgLogin` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgLogin` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgLogin` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Power Apps-д нэвтрэх имэйл"
```

### `ScrPageAdmin/pgLogin` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
Coalesce(pgEdit.UserEmail,"")
```

### `ScrPageAdmin/pgLogin` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgActive` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Lower(Trim(pgLogin.Text))="od.u@tme.mn" || Lower(Coalesce(pgEdit.UserEmail,""))="od.u@tme.mn",DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrPageAdmin/pgActive` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgActive` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,249*Parent.Height/700,275*Parent.Height/680)
```

### `ScrPageAdmin/pgActive` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,117*Parent.Width/360,150*Parent.Width/1100)
```

### `ScrPageAdmin/pgActive` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/700,38*Parent.Height/680)
```

### `ScrPageAdmin/pgActive` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgActive` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgActive` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgEnabled,ColorValue("#E4F6EB"),ColorValue("#F0EEEB"))
```

### `ScrPageAdmin/pgActive` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgActive` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgActive` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(Lower(Trim(pgLogin.Text))="od.u@tme.mn" || Lower(Coalesce(pgEdit.UserEmail,""))="od.u@tme.mn" || pgEnabled,"● Идэвхтэй","○ Түр хаасан")
```

### `ScrPageAdmin/pgActive` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgActive` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgEnabled,!pgEnabled)
```

### `ScrPageAdmin/pgSection` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,138*Parent.Width/360,793*Parent.Width/1100)
```

### `ScrPageAdmin/pgSection` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,249*Parent.Height/700,275*Parent.Height/680)
```

### `ScrPageAdmin/pgSection` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,207*Parent.Width/360,285*Parent.Width/1100)
```

### `ScrPageAdmin/pgSection` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/700,38*Parent.Height/680)
```

### `ScrPageAdmin/pgSection` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgSection` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgSection` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgSection` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgSection` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgSection` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(pgShowWh,"Агуулах   ›   Хуудасны эрх","Хуудасны эрх   ›   Агуулах")
```

### `ScrPageAdmin/pgSection` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgSection` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgShowWh,!pgShowWh)
```

### `ScrPageAdmin/pgGrant0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant0` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgGrant0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,299*Parent.Height/700,325*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgGrant0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgGrant0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgGrant0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgGrant0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgGrant0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && !pgShowWh)
```

### `ScrPageAdmin/pgGrant0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+1)},If(r.key in pgRights.Value,"☑  ","☐  ") & r.caption)
```

### `ScrPageAdmin/pgGrant0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+1)},If(r.key in pgRights.Value,RemoveIf(pgRights,Value=r.key),Collect(pgRights,{Value:r.key})))
```

### `ScrPageAdmin/pgGrant1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant1` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgGrant1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,345*Parent.Height/700,371*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgGrant1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgGrant1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgGrant1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgGrant1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgGrant1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && !pgShowWh)
```

### `ScrPageAdmin/pgGrant1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+2)},If(r.key in pgRights.Value,"☑  ","☐  ") & r.caption)
```

### `ScrPageAdmin/pgGrant1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+2)},If(r.key in pgRights.Value,RemoveIf(pgRights,Value=r.key),Collect(pgRights,{Value:r.key})))
```

### `ScrPageAdmin/pgGrant2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant2` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgGrant2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,391*Parent.Height/700,417*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgGrant2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgGrant2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgGrant2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgGrant2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgGrant2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && !pgShowWh)
```

### `ScrPageAdmin/pgGrant2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+3)},If(r.key in pgRights.Value,"☑  ","☐  ") & r.caption)
```

### `ScrPageAdmin/pgGrant2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+3)},If(r.key in pgRights.Value,RemoveIf(pgRights,Value=r.key),Collect(pgRights,{Value:r.key})))
```

### `ScrPageAdmin/pgGrant3` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant3` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgGrant3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,437*Parent.Height/700,463*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrant3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgGrant3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgGrant3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgGrant3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgGrant3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgGrant3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgGrant3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && !pgShowWh)
```

### `ScrPageAdmin/pgGrant3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+4)},If(r.key in pgRights.Value,"☑  ","☐  ") & r.caption)
```

### `ScrPageAdmin/pgGrant3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({r:Index(Table({key:"home",caption:"Нүүр"},{key:"count",caption:"Тооллого"},{key:"stock",caption:"Агуулах"},{key:"issue",caption:"Зарлага"},{key:"photo",caption:"Камер ба барааны зураг"},{key:"dashboard",caption:"Dashboard"},{key:"history",caption:"Тооллогын түүх"},{key:"report",caption:"Миний тайлан"},{key:"combined",caption:"Нэгдсэн тайлан"},{key:"edit",caption:"Бараа засах"},{key:"sync",caption:"Синк"},{key:"admin",caption:"Хэрэглэгч ба эрх"}),Coalesce(pgPage,0)*4+4)},If(r.key in pgRights.Value,RemoveIf(pgRights,Value=r.key),Collect(pgRights,{Value:r.key})))
```

### `ScrPageAdmin/pgGrantNext` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrantNext` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,491*Parent.Height/700,516*Parent.Height/680)
```

### `ScrPageAdmin/pgGrantNext` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgGrantNext` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/700,36*Parent.Height/680)
```

### `ScrPageAdmin/pgGrantNext` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgGrantNext` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgGrantNext` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgGrantNext` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgGrantNext` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgGrantNext` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && !pgShowWh)
```

### `ScrPageAdmin/pgGrantNext` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хуудасны эрх · " & (pgPage+1) & "/3   ›"
```

### `ScrPageAdmin/pgGrantNext` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgPage,Mod(pgPage+1,3))
```

### `ScrPageAdmin/pgAllWarehouses` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgAllWarehouses` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgAllWarehouses` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgAllWarehouses` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,299*Parent.Height/700,325*Parent.Height/680)
```

### `ScrPageAdmin/pgAllWarehouses` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgAllWarehouses` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgAllWarehouses` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgAllWarehouses` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgAllWarehouses` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgAllWarehouses` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgAllWarehouses` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgAllWarehouses` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && pgShowWh)
```

### `ScrPageAdmin/pgAllWarehouses` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(pgAllWh,"☑  Бүх агуулах","☐  Бүх агуулах")
```

### `ScrPageAdmin/pgAllWarehouses` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgAllWh,!pgAllWh)
```

### `ScrPageAdmin/pgWarehouse0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse0` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgWarehouse0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,345*Parent.Height/700,371*Parent.Height/680)
```

### `ScrPageAdmin/pgWarehouse0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgWarehouse0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgWarehouse0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgWarehouse0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgWarehouse0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgWarehouse0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgWarehouse0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && pgShowWh && CountRows(pgLocations)>=pgWhPage*3+1)
```

### `ScrPageAdmin/pgWarehouse0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(pgLocations)>=pgWhPage*3+1,With({w:Upper(Index(pgLocations,pgWhPage*3+1).Code)},If(pgAllWh || w in pgWh.Value,"☑  ","☐  ") & w),"")
```

### `ScrPageAdmin/pgWarehouse0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({w:Upper(Index(pgLocations,pgWhPage*3+1).Code)},Set(pgAllWh,false);If(w in pgWh.Value,RemoveIf(pgWh,Value=w),Collect(pgWh,{Value:w})))
```

### `ScrPageAdmin/pgWarehouse1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse1` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgWarehouse1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,391*Parent.Height/700,417*Parent.Height/680)
```

### `ScrPageAdmin/pgWarehouse1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgWarehouse1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgWarehouse1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgWarehouse1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgWarehouse1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgWarehouse1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgWarehouse1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && pgShowWh && CountRows(pgLocations)>=pgWhPage*3+2)
```

### `ScrPageAdmin/pgWarehouse1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(pgLocations)>=pgWhPage*3+2,With({w:Upper(Index(pgLocations,pgWhPage*3+2).Code)},If(pgAllWh || w in pgWh.Value,"☑  ","☐  ") & w),"")
```

### `ScrPageAdmin/pgWarehouse1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({w:Upper(Index(pgLocations,pgWhPage*3+2).Code)},Set(pgAllWh,false);If(w in pgWh.Value,RemoveIf(pgWh,Value=w),Collect(pgWh,{Value:w})))
```

### `ScrPageAdmin/pgWarehouse2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse2` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrPageAdmin/pgWarehouse2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,437*Parent.Height/700,463*Parent.Height/680)
```

### `ScrPageAdmin/pgWarehouse2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgWarehouse2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,41*Parent.Height/680)
```

### `ScrPageAdmin/pgWarehouse2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgWarehouse2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgWarehouse2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgWarehouse2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgWarehouse2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgWarehouse2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && pgShowWh && CountRows(pgLocations)>=pgWhPage*3+3)
```

### `ScrPageAdmin/pgWarehouse2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(pgLocations)>=pgWhPage*3+3,With({w:Upper(Index(pgLocations,pgWhPage*3+3).Code)},If(pgAllWh || w in pgWh.Value,"☑  ","☐  ") & w),"")
```

### `ScrPageAdmin/pgWarehouse2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({w:Upper(Index(pgLocations,pgWhPage*3+3).Code)},Set(pgAllWh,false);If(w in pgWh.Value,RemoveIf(pgWh,Value=w),Collect(pgWh,{Value:w})))
```

### `ScrPageAdmin/pgWhNext` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgWhNext` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,491*Parent.Height/700,516*Parent.Height/680)
```

### `ScrPageAdmin/pgWhNext` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,445*Parent.Width/1100)
```

### `ScrPageAdmin/pgWhNext` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/700,36*Parent.Height/680)
```

### `ScrPageAdmin/pgWhNext` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgWhNext` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgWhNext` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgWhNext` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgWhNext` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgWhNext` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane && pgShowWh && CountRows(pgLocations)>3)
```

### `ScrPageAdmin/pgWhNext` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн агуулах   ›"
```

### `ScrPageAdmin/pgWhNext` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgWhPage,If((pgWhPage+1)*3>=CountRows(pgLocations),0,pgWhPage+1))
```

### `ScrPageAdmin/pgSave` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,128*Parent.Width/360,775*Parent.Width/1100)
```

### `ScrPageAdmin/pgSave` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,632*Parent.Height/700,605*Parent.Height/680)
```

### `ScrPageAdmin/pgSave` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,217*Parent.Width/360,303*Parent.Width/1100)
```

### `ScrPageAdmin/pgSave` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,44*Parent.Height/700,44*Parent.Height/680)
```

### `ScrPageAdmin/pgSave` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgSave` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgSave` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#C34810")
```

### `ScrPageAdmin/pgSave` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgSave` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgSave` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgSave` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Эрх хадгалах"
```

### `ScrPageAdmin/pgSave` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(pgReadOk && !(Lower(Trim(pgLogin.Text))="od.u@tme.mn" || Lower(Coalesce(pgEdit.UserEmail,""))="od.u@tme.mn") && !pgBusy && !pgSaving && Connection.Connected && IsMatch(Trim(pgLogin.Text),Match.Email) && !IsBlank(pgPerson.code),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrPageAdmin/pgSave` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!pgSaving && pgReadOk,Set(pgSaving,true);IfError(Refresh(AssetUserAccess),Notify("Эрхийн жагсаалт шинэчилсэнгүй. " & FirstError.Message,NotificationType.Error);false,With({mail:Lower(Trim(pgLogin.Text)),rightsText:pgPerson.code & "|" & Concat(pgRights,Value & "|"),warehouses:If(pgAllWh,"*",If(IsEmpty(pgWh),"","|" & Concat(pgWh,Value & "|")))},With({byMail:LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=mail),byPerson:LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && StartsWith(Title,pgPerson.code & "|"))},If(!(Lower(User().Email)="od.u@tme.mn" || With({a:LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))},a.Active && (IsBlank(a.ExpiresAt) || a.ExpiresAt>Now()) && "|admin|" in a.Title)) || Lower(Trim(pgLogin.Text))="od.u@tme.mn" || Lower(Coalesce(pgEdit.UserEmail,""))="od.u@tme.mn",Notify("Энэ эрхийг өөрчлөх боломжгүй.",NotificationType.Error),Len(rightsText)>255 || Len(warehouses)>255,Notify("Сонголтын урт 255 тэмдэгтээс хэтэрлээ.",NotificationType.Warning),!IsBlank(byMail.ID) && byMail.ID<>pgEdit.ID,Notify("Энэ имэйл өөр ажилтанд бүртгэгдсэн.",NotificationType.Error),Coalesce(byPerson.ID,0)<>Coalesce(pgEdit.ID,0) || (!IsBlank(pgEdit.ID) && byPerson.Modified<>pgEdit.Modified),Notify("Бүртгэл өөрчлөгдсөн. Ажилтнаа дахин сонгоно уу.",NotificationType.Warning),IfError(Set(pgWritten,Patch(AssetUserAccess,If(IsBlank(pgEdit.ID),Defaults(AssetUserAccess),pgEdit),{CompanyCode:"TME-Inventory-Pages",Title:rightsText,UserEmail:mail,LocationCode:warehouses,Role:{Value:pgRole},Active:pgEnabled})),Notify("Хадгалж чадсангүй. " & FirstError.Message,NotificationType.Error),If(IsBlank(pgWritten.ID),Notify("Хадгалсан бүртгэлийн дугаар ирсэнгүй.",NotificationType.Error),Set(pgPane,false);Set(pgAdding,false);Reset(pgFind);Set(pgDirectoryOk,false);Clear(pgAssigned);Set(pgOffset,0);IfError(ClearCollect(pgAssigned,SortByColumns(Filter(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && (IsBlank(Trim(pgFind.Text)) || StartsWith(UserEmail,Lower(Trim(pgFind.Text))) || StartsWith(Title,Trim(pgFind.Text)))),"UserEmail",SortOrder.Ascending)),Clear(pgAssigned);Notify("Эрхийн жагсаалт уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgDirectoryOk,true);true);Notify("Хуудас, агуулахын эрх хадгалагдлаа.",NotificationType.Success)))))),Notify("Хадгалж чадсангүй. " & FirstError.Message,NotificationType.Error));Set(pgSaving,false))
```

### `ScrPageAdmin/pgCancel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgCancel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,632*Parent.Height/700,605*Parent.Height/680)
```

### `ScrPageAdmin/pgCancel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,105*Parent.Width/360,130*Parent.Width/1100)
```

### `ScrPageAdmin/pgCancel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,44*Parent.Height/700,44*Parent.Height/680)
```

### `ScrPageAdmin/pgCancel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgCancel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageAdmin/pgCancel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageAdmin/pgCancel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgCancel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgCancel` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgCancel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Болих"
```

### `ScrPageAdmin/pgCancel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgPane,false)
```

### `ScrPageAdmin/pgAdminBrand` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,23*Parent.Width/1100)
```

### `ScrPageAdmin/pgAdminBrand` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,31*Parent.Height/680)
```

### `ScrPageAdmin/pgAdminBrand` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,148*Parent.Width/1100)
```

### `ScrPageAdmin/pgAdminBrand` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/700,42*Parent.Height/680)
```

### `ScrPageAdmin/pgAdminBrand` . **Size**  _(Label@2.5.1)_
```powerfx
20*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgAdminBrand` . **Color**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgAdminBrand` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgAdminBrand` . **Text**  _(Label@2.5.1)_
```powerfx
"TME"
```

### `ScrPageAdmin/pgAdminBrand` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrPageAdmin/pgAdminBrand` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (!(App.Width<First(App.SizeBreakpoints).Value))
```

### `ScrPageAdmin/pgDirMode` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,208*Parent.Width/1100)
```

### `ScrPageAdmin/pgDirMode` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,60*Parent.Height/700,67*Parent.Height/680)
```

### `ScrPageAdmin/pgDirMode` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,155*Parent.Width/360,188*Parent.Width/1100)
```

### `ScrPageAdmin/pgDirMode` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/700,38*Parent.Height/680)
```

### `ScrPageAdmin/pgDirMode` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgDirMode` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(pgAdding,ColorValue("#1F2225"),Color.White)
```

### `ScrPageAdmin/pgDirMode` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgAdding,Color.White,ColorValue("#1F2225"))
```

### `ScrPageAdmin/pgDirMode` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgDirMode` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgDirMode` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Эрхтэй хэрэглэгчид"
```

### `ScrPageAdmin/pgDirMode` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane))
```

### `ScrPageAdmin/pgDirMode` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgPane,false);Set(pgAdding,false);Reset(pgFind);Set(pgDirectoryOk,false);Clear(pgAssigned);Set(pgOffset,0);IfError(ClearCollect(pgAssigned,SortByColumns(Filter(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && (IsBlank(Trim(pgFind.Text)) || StartsWith(UserEmail,Lower(Trim(pgFind.Text))) || StartsWith(Title,Trim(pgFind.Text)))),"UserEmail",SortOrder.Ascending)),Clear(pgAssigned);Notify("Эрхийн жагсаалт уншсангүй. " & FirstError.Message,NotificationType.Error);false,Set(pgDirectoryOk,true);true)
```

### `ScrPageAdmin/pgAddMode` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,177*Parent.Width/360,404*Parent.Width/1100)
```

### `ScrPageAdmin/pgAddMode` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,60*Parent.Height/700,67*Parent.Height/680)
```

### `ScrPageAdmin/pgAddMode` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,167*Parent.Width/360,200*Parent.Width/1100)
```

### `ScrPageAdmin/pgAddMode` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/700,38*Parent.Height/680)
```

### `ScrPageAdmin/pgAddMode` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgAddMode` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgAddMode` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#CD4B10")
```

### `ScrPageAdmin/pgAddMode` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgAddMode` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgAddMode` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"+ Хэрэглэгч нэмэх"
```

### `ScrPageAdmin/pgAddMode` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane))
```

### `ScrPageAdmin/pgAddMode` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgPane,false);Set(pgAdding,true);Set(pgOffset,0);Clear(pgBCMatches);Reset(pgFind)
```

### `ScrPageAdmin/pgDirCaption` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,209*Parent.Width/1100)
```

### `ScrPageAdmin/pgDirCaption` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,160*Parent.Height/700,171*Parent.Height/680)
```

### `ScrPageAdmin/pgDirCaption` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,326*Parent.Width/360,390*Parent.Width/1100)
```

### `ScrPageAdmin/pgDirCaption` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/700,37*Parent.Height/680)
```

### `ScrPageAdmin/pgDirCaption` . **Size**  _(Label@2.5.1)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgDirCaption` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#605D57")
```

### `ScrPageAdmin/pgDirCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrPageAdmin/pgDirCaption` . **Text**  _(Label@2.5.1)_
```powerfx
If(pgAdding,"BC ажилтнууд",If(pgDirectoryOk,"Бүртгэлтэй хэрэглэгчид","Жагсаалтыг дахин уншуулна уу"))
```

### `ScrPageAdmin/pgDirCaption` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane))
```

### `ScrPageAdmin/pgNoAgents` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Parent.Width/360,209*Parent.Width/1100)
```

### `ScrPageAdmin/pgNoAgents` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,217*Parent.Height/700,222*Parent.Height/680)
```

### `ScrPageAdmin/pgNoAgents` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,325*Parent.Width/360,390*Parent.Width/1100)
```

### `ScrPageAdmin/pgNoAgents` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,83*Parent.Height/700,72*Parent.Height/680)
```

### `ScrPageAdmin/pgNoAgents` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgNoAgents` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#605D57")
```

### `ScrPageAdmin/pgNoAgents` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrPageAdmin/pgNoAgents` . **Text**  _(Label@2.5.1)_
```powerfx
If(pgAdding,"Нэр эсвэл кодын эхний 2 тэмдэгтийг оруулаад Хайх дарна уу.","Энэ хайлтад тохирох хэрэглэгч алга.")
```

### `ScrPageAdmin/pgNoAgents` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && ((!(App.Width<First(App.SizeBreakpoints).Value) || !pgPane) && !pgBusy && If(pgAdding,CountRows(pgBCMatches),CountRows(pgAssigned))=0)
```

### `ScrPageAdmin/pgOwnerNote` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,634*Parent.Width/1100)
```

### `ScrPageAdmin/pgOwnerNote` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,166*Parent.Height/700,188*Parent.Height/680)
```

### `ScrPageAdmin/pgOwnerNote` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,444*Parent.Width/1100)
```

### `ScrPageAdmin/pgOwnerNote` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,36*Parent.Height/700,36*Parent.Height/680)
```

### `ScrPageAdmin/pgOwnerNote` . **Size**  _(Label@2.5.1)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgOwnerNote` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#605D57")
```

### `ScrPageAdmin/pgOwnerNote` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrPageAdmin/pgOwnerNote` . **Text**  _(Label@2.5.1)_
```powerfx
If(Lower(Trim(pgLogin.Text))="od.u@tme.mn" || Lower(Coalesce(pgEdit.UserEmail,""))="od.u@tme.mn","Эзэмшигч админы эрх байнга идэвхтэй.",!IsBlank(pgEdit.ExpiresAt) && pgEdit.ExpiresAt<=Now(),"Энэ бүртгэлийн эрхийн хугацаа дууссан.","Үүрэг")
```

### `ScrPageAdmin/pgOwnerNote` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgRole0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,633*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,203*Parent.Height/700,226*Parent.Height/680)
```

### `ScrPageAdmin/pgRole0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,78*Parent.Width/360,105*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,36*Parent.Height/700,35*Parent.Height/680)
```

### `ScrPageAdmin/pgRole0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgRole0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgRole0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgRole="Counter",ColorValue("#FFF0E5"),Color.White)
```

### `ScrPageAdmin/pgRole0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgRole0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgRole0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нярав"
```

### `ScrPageAdmin/pgRole0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgRole0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgRole,"Counter")
```

### `ScrPageAdmin/pgRole1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,98*Parent.Width/360,745*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,203*Parent.Height/700,226*Parent.Height/680)
```

### `ScrPageAdmin/pgRole1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,78*Parent.Width/360,105*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,36*Parent.Height/700,35*Parent.Height/680)
```

### `ScrPageAdmin/pgRole1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgRole1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgRole1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgRole="Supervisor",ColorValue("#FFF0E5"),Color.White)
```

### `ScrPageAdmin/pgRole1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgRole1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgRole1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Ахлагч"
```

### `ScrPageAdmin/pgRole1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgRole1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgRole,"Supervisor")
```

### `ScrPageAdmin/pgRole2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,181*Parent.Width/360,857*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,203*Parent.Height/700,226*Parent.Height/680)
```

### `ScrPageAdmin/pgRole2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,78*Parent.Width/360,105*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,36*Parent.Height/700,35*Parent.Height/680)
```

### `ScrPageAdmin/pgRole2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgRole2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgRole2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgRole="Auditor",ColorValue("#FFF0E5"),Color.White)
```

### `ScrPageAdmin/pgRole2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgRole2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgRole2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Аудитор"
```

### `ScrPageAdmin/pgRole2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgRole2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgRole,"Auditor")
```

### `ScrPageAdmin/pgRole3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,264*Parent.Width/360,969*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,203*Parent.Height/700,226*Parent.Height/680)
```

### `ScrPageAdmin/pgRole3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,78*Parent.Width/360,105*Parent.Width/1100)
```

### `ScrPageAdmin/pgRole3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,36*Parent.Height/700,35*Parent.Height/680)
```

### `ScrPageAdmin/pgRole3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(Parent.Width/360,Parent.Height/700),Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrPageAdmin/pgRole3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2225")
```

### `ScrPageAdmin/pgRole3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgRole="Admin",ColorValue("#FFF0E5"),Color.White)
```

### `ScrPageAdmin/pgRole3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgRole3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgRole3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Админ"
```

### `ScrPageAdmin/pgRole3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))) && (pgPane)
```

### `ScrPageAdmin/pgRole3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgRole,"Admin")
```

### `ScrPageAdmin/pgDenied1392` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrPageAdmin/pgDenied1392` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrPageAdmin/pgDenied1392` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrPageAdmin/pgDenied1392` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrPageAdmin/pgDenied1392` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrPageAdmin/pgDenied1392` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageAdmin/pgDenied1392` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageAdmin/pgDenied1392` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrPageAdmin/pgDenied1392` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))
```

### `ScrPageAdmin/pgDenied1392` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

