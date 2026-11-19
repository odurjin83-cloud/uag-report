# ScrPageMenu — Power Fx formulas

### `ScrPageMenu` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())))
```

### `ScrPageMenu` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrPageMenu` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrPageMenu` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrPageMenu/pgMenuTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width-32
```

### `ScrPageMenu/pgMenuTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenuTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenuTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Миний хуудсууд"
```

### `ScrPageMenu/pgMenuTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrPageMenu/pgMenu0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(0,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+0*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нүүр"
```

### `ScrPageMenu/pgMenu0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|home|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(1,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+0*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллого"
```

### `ScrPageMenu/pgMenu1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrCountHome',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(2,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+1*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrPageMenu/pgMenu2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('Screen1',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(3,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+1*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зарлага"
```

### `ScrPageMenu/pgMenu3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))
```

### `ScrPageMenu/pgMenu3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrIssueA25Test',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(4,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+2*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Камер ба барааны зураг"
```

### `ScrPageMenu/pgMenu4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|photo|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrCameraSearch',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu5` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(5,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu5` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+2*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu5` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu5` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu5` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu5` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu5` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu5` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu5` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Dashboard"
```

### `ScrPageMenu/pgMenu5` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu5` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrDashboard',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu6` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(6,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu6` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+3*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu6` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu6` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu6` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu6` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu6` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu6` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu6` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллогын түүх"
```

### `ScrPageMenu/pgMenu6` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|history|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu6` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrHistory',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu7` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(7,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu7` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+3*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu7` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu7` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu7` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu7` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu7` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu7` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu7` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Миний тайлан"
```

### `ScrPageMenu/pgMenu7` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|report|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu7` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrReport1',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu8` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(8,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu8` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+4*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu8` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu8` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu8` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu8` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu8` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu8` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu8` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нэгдсэн тайлан"
```

### `ScrPageMenu/pgMenu8` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu8` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrCombined',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu9` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(9,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu9` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+4*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu9` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu9` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu9` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu9` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu9` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu9` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu9` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараа засах"
```

### `ScrPageMenu/pgMenu9` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|edit|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu9` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('Master Edit',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu10` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(10,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu10` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+5*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu10` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu10` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu10` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu10` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu10` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu10` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu10` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Синк"
```

### `ScrPageMenu/pgMenu10` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|sync|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrPageMenu/pgMenu10` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrSync',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenu11` . **AccessibleLabel**  _(Classic/Button@2.2.0)_
```powerfx
"Админ · Хэрэглэгч ба эрх"
```

### `ScrPageMenu/pgMenu11` . **X**  _(Classic/Button@2.2.0)_
```powerfx
16+Mod(11,2)*(Parent.Width-24)/2
```

### `ScrPageMenu/pgMenu11` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
74+5*Min(56,(Parent.Height-160)/6)
```

### `ScrPageMenu/pgMenu11` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(Parent.Width-40)/2
```

### `ScrPageMenu/pgMenu11` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Min(48,(Parent.Height-165)/6)
```

### `ScrPageMenu/pgMenu11` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenu11` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenu11` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenu11` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenu11` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Админ · Эрх"
```

### `ScrPageMenu/pgMenu11` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title))
```

### `ScrPageMenu/pgMenu11` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('ScrPageAdmin',ScreenTransition.Fade)
```

### `ScrPageMenu/pgMenuBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height-52
```

### `ScrPageMenu/pgMenuBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
112
```

### `ScrPageMenu/pgMenuBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrPageMenu/pgMenuBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrPageMenu/pgMenuBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrPageMenu/pgMenuBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrPageMenu/pgMenuBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Буцах"
```

### `ScrPageMenu/pgMenuBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Back()
```

