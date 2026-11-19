# ScrCombined — Power Fx formulas

### `ScrCombined` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Set(pgFrom,Date(Year(Today()),Month(Today()),1));Set(pgGroup,"Агуулах");Set(pgTable,false);Set(pgDiff,false);Set(pgRank,0);Set(pgLocation,"");Set(pgReportReady,false);Reset(pgSearch);Set(pgReportReady,false);Clear(pgRows);Clear(pgRaw);Clear(pgFullDays);IfError(ForAll(Sequence(DateDiff(pgFrom,Today())+1) As d,With({a:DateAdd(pgFrom,d.Value-1,TimeUnit.Days),b:DateAdd(pgFrom,d.Value,TimeUnit.Days)},If((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*"),With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true),ForAll(Filter(Split(pgAccess.LocationCode,"|"),!IsBlank(Value)) As w,With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b && LocationCode=w.Value),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true)))));If(!IsEmpty(pgFullDays),Notify("Нэг өдөрт 500-аас олон мөр таарсан тул нийлбэрийг харуулсангүй.",NotificationType.Warning),ClearCollect(pgRows,AddColumns(Filter(pgRaw,!StartsWith(Title,"ARCHIVED:") && ((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode)) As a,pgVariance,IfError(Value(a.Variance),Blank()),cost,LookUp(colOfflineItems,number=a.ItemNo,unitCost)));Clear(pgRaw);Set(pgReportReady,true)),Notify(FirstError.Message,NotificationType.Error))
)
```

### `ScrCombined` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrCombined` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrCombined` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrCombined/ScrCombinedRail` . **Width**  _(Label@2.5.1)_
```powerfx
156
```

### `ScrCombined/ScrCombinedRail` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height
```

### `ScrCombined/ScrCombinedRail` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/ScrCombinedRail` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/ScrCombinedRail` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value)
```

### `ScrCombined/ScrCombinedNav0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
140
```

### `ScrCombined/ScrCombinedNav0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCombined/ScrCombinedNav0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/ScrCombinedNav0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/ScrCombinedNav0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/ScrCombinedNav0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нүүр"
```

### `ScrCombined/ScrCombinedNav0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(нүүр,ScreenTransition.None)
```

### `ScrCombined/ScrCombinedNav0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|home|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrCombined/ScrCombinedNav1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
112
```

### `ScrCombined/ScrCombinedNav1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
140
```

### `ScrCombined/ScrCombinedNav1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCombined/ScrCombinedNav1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/ScrCombinedNav1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/ScrCombinedNav1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/ScrCombinedNav1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллого"
```

### `ScrCombined/ScrCombinedNav1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrCountHome,ScreenTransition.None)
```

### `ScrCombined/ScrCombinedNav1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrCombined/ScrCombinedNav2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
160
```

### `ScrCombined/ScrCombinedNav2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
140
```

### `ScrCombined/ScrCombinedNav2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCombined/ScrCombinedNav2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/ScrCombinedNav2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/ScrCombinedNav2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/ScrCombinedNav2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrCombined/ScrCombinedNav2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(Screen1,ScreenTransition.None)
```

### `ScrCombined/ScrCombinedNav2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrCombined/ScrCombinedNav3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
208
```

### `ScrCombined/ScrCombinedNav3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
140
```

### `ScrCombined/ScrCombinedNav3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCombined/ScrCombinedNav3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/ScrCombinedNav3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/ScrCombinedNav3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/ScrCombinedNav3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зарлага"
```

### `ScrCombined/ScrCombinedNav3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrIssueA25Test,ScreenTransition.None)
```

### `ScrCombined/ScrCombinedNav3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title)))
```

### `ScrCombined/ScrCombinedNav4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
256
```

### `ScrCombined/ScrCombinedNav4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
140
```

### `ScrCombined/ScrCombinedNav4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCombined/ScrCombinedNav4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/ScrCombinedNav4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/ScrCombinedNav4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/ScrCombinedNav4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нэгдсэн тайлан"
```

### `ScrCombined/ScrCombinedNav4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrCombined,ScreenTransition.None)
```

### `ScrCombined/ScrCombinedNav4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))))
```

### `ScrCombined/ScrCombinedNav5` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
304
```

### `ScrCombined/ScrCombinedNav5` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
140
```

### `ScrCombined/ScrCombinedNav5` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCombined/ScrCombinedNav5` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/ScrCombinedNav5` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/ScrCombinedNav5` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/ScrCombinedNav5` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хэрэглэгч ба эрх"
```

### `ScrCombined/ScrCombinedNav5` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrPageAdmin,ScreenTransition.None)
```

### `ScrCombined/ScrCombinedNav5` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && (Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|admin|" in pgAccess.Title)))
```

### `ScrCombined/ScrCombinedHead` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/ScrCombinedHead` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)
```

### `ScrCombined/ScrCombinedHead` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28)
```

### `ScrCombined/ScrCombinedHead` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/ScrCombinedHead` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrCombined/ScrCombinedHead` . **Text**  _(Label@2.5.1)_
```powerfx
"Нэгдсэн тайлан · бүртгэсэн өдрөөр"
```

### `ScrCombined/ScrCombinedHead` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrCombined/ScrCombinedBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width-78
```

### `ScrCombined/ScrCombinedBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/ScrCombinedBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/ScrCombinedBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/ScrCombinedBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/ScrCombinedBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Буцах"
```

### `ScrCombined/ScrCombinedBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value)
```

### `ScrCombined/ScrCombinedBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Back()
```

### `ScrCombined/pgPeriod0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgPeriod0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0/3
```

### `ScrCombined/pgPeriod0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/3-4
```

### `ScrCombined/pgPeriod0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgPeriod0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgFrom=Today(),ColorValue("#FFE3D2"),Color.White)
```

### `ScrCombined/pgPeriod0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgPeriod0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgPeriod0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Өнөөдөр"
```

### `ScrCombined/pgPeriod0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgFrom,Today());Set(pgRank,0);Set(pgReportReady,false);Clear(pgRows);Clear(pgRaw);Clear(pgFullDays);IfError(ForAll(Sequence(DateDiff(pgFrom,Today())+1) As d,With({a:DateAdd(pgFrom,d.Value-1,TimeUnit.Days),b:DateAdd(pgFrom,d.Value,TimeUnit.Days)},If((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*"),With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true),ForAll(Filter(Split(pgAccess.LocationCode,"|"),!IsBlank(Value)) As w,With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b && LocationCode=w.Value),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true)))));If(!IsEmpty(pgFullDays),Notify("Нэг өдөрт 500-аас олон мөр таарсан тул нийлбэрийг харуулсангүй.",NotificationType.Warning),ClearCollect(pgRows,AddColumns(Filter(pgRaw,!StartsWith(Title,"ARCHIVED:") && ((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode)) As a,pgVariance,IfError(Value(a.Variance),Blank()),cost,LookUp(colOfflineItems,number=a.ItemNo,unitCost)));Clear(pgRaw);Set(pgReportReady,true)),Notify(FirstError.Message,NotificationType.Error))
```

### `ScrCombined/pgPeriod1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgPeriod1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*1/3
```

### `ScrCombined/pgPeriod1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/3-4
```

### `ScrCombined/pgPeriod1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgPeriod1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgFrom=DateAdd(Today(),-6,TimeUnit.Days),ColorValue("#FFE3D2"),Color.White)
```

### `ScrCombined/pgPeriod1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgPeriod1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgPeriod1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"7 хоног"
```

### `ScrCombined/pgPeriod1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgFrom,DateAdd(Today(),-6,TimeUnit.Days));Set(pgRank,0);Set(pgReportReady,false);Clear(pgRows);Clear(pgRaw);Clear(pgFullDays);IfError(ForAll(Sequence(DateDiff(pgFrom,Today())+1) As d,With({a:DateAdd(pgFrom,d.Value-1,TimeUnit.Days),b:DateAdd(pgFrom,d.Value,TimeUnit.Days)},If((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*"),With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true),ForAll(Filter(Split(pgAccess.LocationCode,"|"),!IsBlank(Value)) As w,With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b && LocationCode=w.Value),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true)))));If(!IsEmpty(pgFullDays),Notify("Нэг өдөрт 500-аас олон мөр таарсан тул нийлбэрийг харуулсангүй.",NotificationType.Warning),ClearCollect(pgRows,AddColumns(Filter(pgRaw,!StartsWith(Title,"ARCHIVED:") && ((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode)) As a,pgVariance,IfError(Value(a.Variance),Blank()),cost,LookUp(colOfflineItems,number=a.ItemNo,unitCost)));Clear(pgRaw);Set(pgReportReady,true)),Notify(FirstError.Message,NotificationType.Error))
```

### `ScrCombined/pgPeriod2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgPeriod2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*2/3
```

### `ScrCombined/pgPeriod2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/3-4
```

### `ScrCombined/pgPeriod2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgPeriod2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgFrom=Date(Year(Today()),Month(Today()),1),ColorValue("#FFE3D2"),Color.White)
```

### `ScrCombined/pgPeriod2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgPeriod2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgPeriod2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ сар"
```

### `ScrCombined/pgPeriod2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgFrom,Date(Year(Today()),Month(Today()),1));Set(pgRank,0);Set(pgReportReady,false);Clear(pgRows);Clear(pgRaw);Clear(pgFullDays);IfError(ForAll(Sequence(DateDiff(pgFrom,Today())+1) As d,With({a:DateAdd(pgFrom,d.Value-1,TimeUnit.Days),b:DateAdd(pgFrom,d.Value,TimeUnit.Days)},If((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*"),With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true),ForAll(Filter(Split(pgAccess.LocationCode,"|"),!IsBlank(Value)) As w,With({part:FirstN(Filter(InventoryCount,Created>=a && Created<b && LocationCode=w.Value),500)},If(CountRows(part)>=500,Collect(pgFullDays,{day:a}));Collect(pgRaw,part);true)))));If(!IsEmpty(pgFullDays),Notify("Нэг өдөрт 500-аас олон мөр таарсан тул нийлбэрийг харуулсангүй.",NotificationType.Warning),ClearCollect(pgRows,AddColumns(Filter(pgRaw,!StartsWith(Title,"ARCHIVED:") && ((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode)) As a,pgVariance,IfError(Value(a.Variance),Blank()),cost,LookUp(colOfflineItems,number=a.ItemNo,unitCost)));Clear(pgRaw);Set(pgReportReady,true)),Notify(FirstError.Message,NotificationType.Error))
```

### `ScrCombined/pgSearch` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgSearch` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)
```

### `ScrCombined/pgSearch` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.62
```

### `ScrCombined/pgSearch` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgSearch` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgSearch` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Бараа, код, агуулах, ажилтан хайх"
```

### `ScrCombined/pgSearch` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
Set(pgRank,0)
```

### `ScrCombined/pgDiffOnly` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgDiffOnly` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.63
```

### `ScrCombined/pgDiffOnly` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.37
```

### `ScrCombined/pgDiffOnly` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgDiffOnly` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgDiffOnly` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgDiffOnly` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgDiffOnly` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(pgDiff,"✓ Зөрүүтэй","Зөвхөн зөрүүтэй")
```

### `ScrCombined/pgDiffOnly` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgDiff,!pgDiff);Set(pgRank,0)
```

### `ScrCombined/pgKpi0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgKpi0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*If(App.Width>=First(App.SizeBreakpoints).Value,0,0)/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)
```

### `ScrCombined/pgKpi0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,148,148)
```

### `ScrCombined/pgKpi0` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)-5
```

### `ScrCombined/pgKpi0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgKpi0` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgKpi0` . **Text**  _(Label@2.5.1)_
```powerfx
"Тоолсон мөр" & Char(10) & If(pgReportReady,With({t:Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode))},Text(CountRows(t))),"—")
```

### `ScrCombined/pgKpi0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCombined/pgKpi1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgKpi1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*If(App.Width>=First(App.SizeBreakpoints).Value,1,1)/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)
```

### `ScrCombined/pgKpi1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,148,148)
```

### `ScrCombined/pgKpi1` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)-5
```

### `ScrCombined/pgKpi1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgKpi1` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgKpi1` . **Text**  _(Label@2.5.1)_
```powerfx
"Тоо таарсан мөрийн хувь" & Char(10) & If(pgReportReady,With({t:Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode))},If(IsEmpty(t),"—",Text(CountIf(t,pgVariance=0)/CountRows(t),"0.0%"))),"—")
```

### `ScrCombined/pgKpi1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCombined/pgKpi2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgKpi2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*If(App.Width>=First(App.SizeBreakpoints).Value,2,0)/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)
```

### `ScrCombined/pgKpi2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,148,210)
```

### `ScrCombined/pgKpi2` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)-5
```

### `ScrCombined/pgKpi2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgKpi2` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgKpi2` . **Text**  _(Label@2.5.1)_
```powerfx
"Дутсан барааны дүн" & Char(10) & If(pgReportReady,With({t:Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode))},If(CountIf(t,pgVariance<0 && IsBlank(cost))>0,"Өртөг дутуу",Text(-Sum(Filter(t,pgVariance<0),pgVariance*cost),"#,##0") & " ₮")),"—")
```

### `ScrCombined/pgKpi2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCombined/pgKpi3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgKpi3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*If(App.Width>=First(App.SizeBreakpoints).Value,0,1)/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)
```

### `ScrCombined/pgKpi3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,210,210)
```

### `ScrCombined/pgKpi3` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)-5
```

### `ScrCombined/pgKpi3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgKpi3` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgKpi3` . **Text**  _(Label@2.5.1)_
```powerfx
"Илүү гарсан барааны дүн" & Char(10) & If(pgReportReady,With({t:Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode))},If(CountIf(t,pgVariance>0 && IsBlank(cost))>0,"Өртөг дутуу",Text(Sum(Filter(t,pgVariance>0),pgVariance*cost),"#,##0") & " ₮")),"—")
```

### `ScrCombined/pgKpi3` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCombined/pgKpi4` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgKpi4` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*If(App.Width>=First(App.SizeBreakpoints).Value,1,0)/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)
```

### `ScrCombined/pgKpi4` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,210,272)
```

### `ScrCombined/pgKpi4` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)-5
```

### `ScrCombined/pgKpi4` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgKpi4` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgKpi4` . **Text**  _(Label@2.5.1)_
```powerfx
"Үлдэгдлийн дүнд тоолсон барааны эзлэх хувь" & Char(10) & If(pgReportReady,With({t:Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode))},With({stock:Filter(colDStockBaseV17,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode) && Qty>0)},If(IsEmpty(stock) || Sum(stock,Qty*Cost)<=0,"—",Text(Sum(Filter(stock As st,!IsBlank(LookUp(t,ItemNo=st.itemNo && LocationCode=st.locationCode,ID))),Qty*Cost)/Sum(stock,Qty*Cost),"0.0%")))),"—")
```

### `ScrCombined/pgKpi4` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCombined/pgKpi5` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgKpi5` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*If(App.Width>=First(App.SizeBreakpoints).Value,2,1)/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)
```

### `ScrCombined/pgKpi5` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,210,272)
```

### `ScrCombined/pgKpi5` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/If(App.Width>=First(App.SizeBreakpoints).Value,3,2)-5
```

### `ScrCombined/pgKpi5` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgKpi5` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgKpi5` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүний нийт дүн" & Char(10) & If(pgReportReady,With({t:Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode))},If(CountIf(t,pgVariance<>0 && IsBlank(cost))>0,"Өртөг дутуу",Text(Sum(t,pgVariance*cost),"#,##0") & " ₮")),"—")
```

### `ScrCombined/pgKpi5` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCombined/pgGrouping0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgGrouping0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0/4
```

### `ScrCombined/pgGrouping0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)
```

### `ScrCombined/pgGrouping0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/4-4
```

### `ScrCombined/pgGrouping0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgGrouping0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgGroup="Агуулах",ColorValue("#FFE3D2"),Color.White)
```

### `ScrCombined/pgGrouping0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgGrouping0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgGrouping0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrCombined/pgGrouping0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgGroup,"Агуулах");Set(pgRank,0)
```

### `ScrCombined/pgGrouping1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgGrouping1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*1/4
```

### `ScrCombined/pgGrouping1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)
```

### `ScrCombined/pgGrouping1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/4-4
```

### `ScrCombined/pgGrouping1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgGrouping1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgGroup="Ажилтан",ColorValue("#FFE3D2"),Color.White)
```

### `ScrCombined/pgGrouping1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgGrouping1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgGrouping1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Ажилтан"
```

### `ScrCombined/pgGrouping1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgGroup,"Ажилтан");Set(pgRank,0)
```

### `ScrCombined/pgGrouping2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgGrouping2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*2/4
```

### `ScrCombined/pgGrouping2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)
```

### `ScrCombined/pgGrouping2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/4-4
```

### `ScrCombined/pgGrouping2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgGrouping2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgGroup="Бараа",ColorValue("#FFE3D2"),Color.White)
```

### `ScrCombined/pgGrouping2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgGrouping2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgGrouping2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бараа"
```

### `ScrCombined/pgGrouping2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgGroup,"Бараа");Set(pgRank,0)
```

### `ScrCombined/pgGrouping3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgGrouping3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*3/4
```

### `ScrCombined/pgGrouping3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)
```

### `ScrCombined/pgGrouping3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))/4-4
```

### `ScrCombined/pgGrouping3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgGrouping3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(pgGroup="Өдөр",ColorValue("#FFE3D2"),Color.White)
```

### `ScrCombined/pgGrouping3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgGrouping3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgGrouping3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Өдөр"
```

### `ScrCombined/pgGrouping3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgGroup,"Өдөр");Set(pgRank,0)
```

### `ScrCombined/pgViewMode` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ScrCombined/pgViewMode` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)
```

### `ScrCombined/pgViewMode` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+44
```

### `ScrCombined/pgViewMode` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28)
```

### `ScrCombined/pgViewMode` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgViewMode` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgViewMode` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgViewMode` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgViewMode` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(pgTable,"Хүснэгт  ·  График харах","График  ·  Хүснэгт харах")
```

### `ScrCombined/pgViewMode` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgTable,!pgTable)
```

### `ScrCombined/pgChartTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)
```

### `ScrCombined/pgChartTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+85
```

### `ScrCombined/pgChartTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0)
```

### `ScrCombined/pgChartTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgChartTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgChartTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Өдөр бүр тоолсон мөрийн тоо"
```

### `ScrCombined/pgChartTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrCombined/pgChartTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && !pgTable && pgReportReady)
```

### `ScrCombined/pgChart` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)
```

### `ScrCombined/pgChart` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+119
```

### `ScrCombined/pgChart` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0)
```

### `ScrCombined/pgChart` . **Height**  _(Image@2.2.3)_
```powerfx
142
```

### `ScrCombined/pgChart` . **Fill**  _(Image@2.2.3)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgChart` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl(With({t:Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),n:DateDiff(pgFrom,Today())+1},With({days:AddColumns(Sequence(n) As d,total,CountIf(t,DateValue(Text(Created))=DateAdd(pgFrom,d.Value-1,TimeUnit.Days)))},"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 520 190'><path d='M12 160H510' stroke='#ddd'/>" & Concat(days As d,"<rect x='" & Text(12+(d.Value-1)*496/n,"0.0","en-US") & "' y='" & Text(160-145*d.total/Max(1,Max(days,total)),"0.0","en-US") & "' width='" & Text(Max(2,470/n),"0.0","en-US") & "' height='" & Text(145*d.total/Max(1,Max(days,total)),"0.0","en-US") & "' fill='#ed601f' rx='2'/>") & "</svg>")))
```

### `ScrCombined/pgChart` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width>=First(App.SizeBreakpoints).Value && !pgTable && pgReportReady)
```

### `ScrCombined/pgReportRow0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+86
```

### `ScrCombined/pgReportRow0` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))-If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgReportRow0` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgReportRow0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (pgReportReady && CountRows(SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending))>=pgRank+1)
```

### `ScrCombined/pgReportRow0` . **Text**  _(Label@2.5.1)_
```powerfx
With({t:SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending)},With({r:Index(t,pgRank+1)},r.pgKey & "   ·   " & r.pgTotal & " мөр   " & If(pgTable,"Тоо таарсан " & CountIf(r.pgMembers,pgVariance=0) & "   ·   Зөрүүтэй " & CountIf(r.pgMembers,pgVariance<>0),Concat(Sequence(RoundUp(12*r.pgTotal/First(t).pgTotal,0)),"━"))))
```

### `ScrCombined/pgReportRow1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+131
```

### `ScrCombined/pgReportRow1` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))-If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgReportRow1` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgReportRow1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (pgReportReady && CountRows(SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending))>=pgRank+2)
```

### `ScrCombined/pgReportRow1` . **Text**  _(Label@2.5.1)_
```powerfx
With({t:SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending)},With({r:Index(t,pgRank+2)},r.pgKey & "   ·   " & r.pgTotal & " мөр   " & If(pgTable,"Тоо таарсан " & CountIf(r.pgMembers,pgVariance=0) & "   ·   Зөрүүтэй " & CountIf(r.pgMembers,pgVariance<>0),Concat(Sequence(RoundUp(12*r.pgTotal/First(t).pgTotal,0)),"━"))))
```

### `ScrCombined/pgReportRow2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+176
```

### `ScrCombined/pgReportRow2` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))-If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgReportRow2` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgReportRow2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (pgReportReady && CountRows(SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending))>=pgRank+3)
```

### `ScrCombined/pgReportRow2` . **Text**  _(Label@2.5.1)_
```powerfx
With({t:SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending)},With({r:Index(t,pgRank+3)},r.pgKey & "   ·   " & r.pgTotal & " мөр   " & If(pgTable,"Тоо таарсан " & CountIf(r.pgMembers,pgVariance=0) & "   ·   Зөрүүтэй " & CountIf(r.pgMembers,pgVariance<>0),Concat(Sequence(RoundUp(12*r.pgTotal/First(t).pgTotal,0)),"━"))))
```

### `ScrCombined/pgReportRow3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)+If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+221
```

### `ScrCombined/pgReportRow3` . **Width**  _(Label@2.5.1)_
```powerfx
(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))-If(pgTable,0,If(App.Width>=First(App.SizeBreakpoints).Value,(If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28))*0.52,0))
```

### `ScrCombined/pgReportRow3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgReportRow3` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgReportRow3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (pgReportReady && CountRows(SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending))>=pgRank+4)
```

### `ScrCombined/pgReportRow3` . **Text**  _(Label@2.5.1)_
```powerfx
With({t:SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending)},With({r:Index(t,pgRank+4)},r.pgKey & "   ·   " & r.pgTotal & " мөр   " & If(pgTable,"Тоо таарсан " & CountIf(r.pgMembers,pgVariance=0) & "   ·   Зөрүүтэй " & CountIf(r.pgMembers,pgVariance<>0),Concat(Sequence(RoundUp(12*r.pgTotal/First(t).pgTotal,0)),"━"))))
```

### `ScrCombined/pgMoreRows` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)
```

### `ScrCombined/pgMoreRows` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+270
```

### `ScrCombined/pgMoreRows` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28)
```

### `ScrCombined/pgMoreRows` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgMoreRows` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgMoreRows` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgMoreRows` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgMoreRows` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн мөрүүд"
```

### `ScrCombined/pgMoreRows` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (pgReportReady && CountRows(SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending))>4)
```

### `ScrCombined/pgMoreRows` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(pgRank,If(pgRank+4>=CountRows(SortByColumns(AddColumns(GroupBy(AddColumns(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode)),pgKey,Switch(pgGroup,"Агуулах",LocationCode,"Ажилтан",Counter,"Бараа",ItemNo,Text(Created,"yyyy-mm-dd"))),pgKey,pgMembers),pgTotal,CountRows(pgMembers)),"pgTotal",SortOrder.Descending)),0,pgRank+4))
```

### `ScrCombined/pgEmpty` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,176,14)
```

### `ScrCombined/pgEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,274,336)+90
```

### `ScrCombined/pgEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width>=First(App.SizeBreakpoints).Value,Parent.Width-192,Parent.Width-28)
```

### `ScrCombined/pgEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrCombined/pgEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrCombined/pgEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
If(pgReportReady,"Сонгосон нөхцөлд мөр олдсонгүй.","Тайлан бүрэн ачаалагдаагүй.")
```

### `ScrCombined/pgEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (!pgReportReady || IsEmpty(Filter(pgRows,(!pgDiff || pgVariance<>0) && (IsBlank(pgSearch.Text) || pgSearch.Text in ItemName || StartsWith(ItemNo,pgSearch.Text) || pgSearch.Text in Counter || pgSearch.Text in LocationCode))))
```

### `ScrCombined/pgDenied1393` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrCombined/pgDenied1393` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrCombined/pgDenied1393` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrCombined/pgDenied1393` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrCombined/pgDenied1393` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrCombined/pgDenied1393` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrCombined/pgDenied1393` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrCombined/pgDenied1393` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrCombined/pgDenied1393` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|combined|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrCombined/pgDenied1393` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

