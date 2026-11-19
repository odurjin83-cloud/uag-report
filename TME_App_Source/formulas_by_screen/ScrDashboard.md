# ScrDashboard — Power Fx formulas

### `ScrDashboard` . **Fill**  _(Screen)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrDashboard` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrDashboard` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),Clear(colDLatest);Clear(colDVariance);Clear(colDStock);Clear(colDMonths);Clear(colDTop);Clear(colDTrend);Set(varDAccuracy,Blank());Set(varDPdfPendingV23,false);Set(varDView,"overview");Set(varDExport,false);Set(varDBusy,false);If(IsBlank(varDPeriod),Set(varDPeriod,"Сар"));If(IsBlank(varDIncomplete),Set(varDIncomplete,false));
If(Coalesce(varWInitialized,false),ClearCollect(colDMinimums,colWMinimums),ClearCollect(colDMinimums,{OwnerEmail:"",ItemNo:"",LocationCode:"",Minimum:0});Clear(colDMinimums);If(!IsBlank(Host.Version),IfError(LoadData(colDMinimums,"WarehouseMinimumsV6",true),Clear(colDMinimums); false, true)));
If(!Coalesce(varDInitialized,false),ClearCollect(colDValueHistory,{OwnerEmail:"",Day:Today(),Amount:0,LocationScope:"*"});Clear(colDValueHistory);IfError(LoadData(colDValueHistory,"DashboardValueHistoryV7",true),Clear(colDValueHistory); false, true);Set(varDInitialized,true));
Select(dCalculate);Set(mobDashboardMenu,false)
)
```

### `ScrDashboard` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrDashboard/dCalculate` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dCalculate` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dCalculate` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dCalculate` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dCalculate` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dCalculate` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dCalculate` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dCalculate` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dCalculate` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dCalculate` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dCalculate` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDFrom,Switch(varDPeriod,"Live",Today(),"7 хоног",DateAdd(Today(),-6,TimeUnit.Days),Date(Year(Today()),Month(Today()),1)));
ClearCollect(colDLatest,ForAll(GroupBy(Filter(colOfflineInventory,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),!Coalesce(Archived,false) && OwnerEmail=varCountOwner && !IsBlank(ItemNo) && CountDate>=varDFrom && CountDate<DateAdd(Today(),1,TimeUnit.Days)),ItemNo,LocationCode,DRows) As g,Patch(First(SortByColumns(g.DRows,"CountDate",SortOrder.Descending,"SyncKey",SortOrder.Descending)),{ItemNo:g.ItemNo,LocationCode:g.LocationCode})));
ClearCollect(colDValid,Filter(colDLatest,!IsBlank(CountQty) && !IsBlank(OpeningBalance)));
ClearCollect(colDVariance,SortByColumns(AddColumns(AddColumns(Filter(colDValid,CountQty<>OpeningBalance),DVariance,CountQty-OpeningBalance) As r,DAbsAmount,Abs(r.DVariance),DReason,Coalesce(r.Reason,"Тайлбаргүй")),"DAbsAmount",SortOrder.Descending));
Set(varDAccuracy,If(IsEmpty(colDValid),Blank(),CountRows(Filter(colDValid,CountQty=OpeningBalance))/CountRows(colDValid)*100));
ClearCollect(colDReasons,SortByColumns(AddColumns(GroupBy(colDVariance,DReason,DReasonRows),Total,CountRows(DReasonRows)),"Total",SortOrder.Descending));
ClearCollect(colDStock,AddColumns(Filter(colDStockBaseV17,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode)) As r,Minimum,If(IsEmpty(colDMinimums),Blank(),LookUp(colDMinimums,OwnerEmail=User().Email && ItemNo=r.itemNo && LocationCode=r.locationCode,Minimum))));
ClearCollect(colDWarehouses,AddColumns(GroupBy(colDStock,locationCode,DLocationRows),SKU,CountRows(DLocationRows),Shortage,CountRows(Filter(DLocationRows,!IsBlank(Minimum) && Qty<Minimum)),Configured,CountRows(Filter(DLocationRows,!IsBlank(Minimum)))));
ClearCollect(colDUsage,SortByColumns(AddColumns(GroupBy(Filter(colDLedger,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),!varDIncomplete && DDate>=varDFrom && DDate<DateAdd(Today(),1,TimeUnit.Days) && Quantity<0),ItemNo,LocationCode,Uom,DUsageRows),Qty,-Sum(DUsageRows,Quantity),Amount,Sum(DUsageRows,Abs(Cost))),"Amount",SortOrder.Descending));
ClearCollect(colDTop,FirstN(colDUsage,5));
ClearCollect(colDMonths,ForAll(Sequence(8) As m,With({d:DateAdd(Date(Year(Today()),Month(Today()),1),m.Value-8,TimeUnit.Months)},{Index:m.Value,MonthDate:d,Income:Sum(Filter(colDLedger,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),!varDIncomplete && DDate>=d && DDate<DateAdd(d,1,TimeUnit.Months) && Quantity>0),Abs(Cost)),Expense:Sum(Filter(colDLedger,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper(LocationCode) & "|") in pgAccess.LocationCode),!varDIncomplete && DDate>=d && DDate<DateAdd(d,1,TimeUnit.Months) && Quantity<0),Abs(Cost))})));
Set(varDMaxMonth,Max(1,Max(colDMonths,Max(Income,Expense))));
Set(varDDonut,"<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><circle cx='80' cy='80' r='62' fill='none' stroke='#EAE7E3' stroke-width='12'/><circle cx='80' cy='80' r='62' pathLength='100' fill='none' stroke='#85DFAC' stroke-width='12' stroke-dasharray='" & Text(Coalesce(varDAccuracy,0),"0.00","en-US") & " 100' transform='rotate(-90 80 80)'/></svg>");
ClearCollect(colDTrend,LastN(SortByColumns(Filter(colDValueHistory,OwnerEmail=User().Email && Coalesce(LocationScope,"*")=If((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*"),"*",pgAccess.LocationCode)),"Day",SortOrder.Ascending),12));
Set(varDTrendSvg,"<svg xmlns='http://www.w3.org/2000/svg' width='500' height='140'><polyline fill='none' stroke='#ED5F1C' stroke-width='3' points='" & Concat(Sequence(CountRows(colDTrend)) As s,Text((s.Value-1)*500/Max(1,CountRows(colDTrend)-1),"0.00","en-US") & "," & Text(130-(Last(FirstN(colDTrend,s.Value)).Amount-Min(colDTrend,Amount))*120/Max(1,Max(colDTrend,Amount)-Min(colDTrend,Amount)),"0.00","en-US")," ") & "'/></svg>")
```

### `ScrDashboard/dCalculate` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dCalculate` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dCalculate` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dCalculate` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dCalculate` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dCalculate` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCalculate` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCalculate` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCalculate` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCalculate` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCalculate` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrDashboard/dCalculate` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dCalculate` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dCalculate` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dReadBC` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dReadBC` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dReadBC` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dReadBC` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dReadBC` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dReadBC` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dReadBC` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dReadBC` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dReadBC` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dReadBC` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dReadBC` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!Connection.Connected,Notify("Интернет холболт алга. Тооллого болон локал үнэлгээ харагдана.",NotificationType.Warning),
Set(varDBusy,true);Set(varDLoaded,false);Set(varDIncomplete,false);Clear(colDLedger);
IfError(ClearCollect(colDLedgerRaw,Sort('itemLedgerEntries (microsoft/analytics/v1.0)','Entry No.',SortOrder.Descending));
Set(varDIncomplete,CountRows(colDLedgerRaw)>=2000);
If(varDIncomplete,Notify("BC хөдөлгөөн 2000 мөрийн хязгаарт хүрлээ. Дутуу дүн харуулахгүйн тулд зарцуулалтын график түр хаалттай.",NotificationType.Warning),
ClearCollect(colDLedger,ForAll(Filter(colDLedgerRaw,((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*") || ("|" & Upper('Location Code') & "|") in pgAccess.LocationCode)) As r,{ItemNo:r.'Item No.',LocationCode:r.'Location Code',DDate:IfError(DateValue(Text(r.'Posting Date')),Blank()),Quantity:r.Quantity,Uom:r.'Unit of Measure Code',Cost:r.'Cost Amount (Actual)'}));Set(varDLoaded,true);Set(varDChecked,Now())),
Notify("BC хөдөлгөөн уншиж чадсангүй: " & FirstError.Message,NotificationType.Error));
Clear(colDLedgerRaw);Set(varDBusy,false));Select(dCalculate)
```

### `ScrDashboard/dReadBC` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dReadBC` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dReadBC` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dReadBC` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dReadBC` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dReadBC` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dReadBC` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dReadBC` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dReadBC` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dReadBC` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dReadBC` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrDashboard/dReadBC` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dReadBC` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dReadBC` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dCapture` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dCapture` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dCapture` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dCapture` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dCapture` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dCapture` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dCapture` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dCapture` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dCapture` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dCapture` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dCapture` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!IsBlank(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())),RemoveIf(colDValueHistory,OwnerEmail=User().Email && Coalesce(LocationScope,"*")=If((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*"),"*",pgAccess.LocationCode) && Day=Today());Collect(colDValueHistory,{OwnerEmail:User().Email,Day:Today(),LocationScope:If((Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*"),"*",pgAccess.LocationCode),Amount:If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())});IfError(SaveData(colDValueHistory,"DashboardValueHistoryV7"),Notify("Үнэлгээний snapshot зөвхөн санах ойд хадгалагдлаа.",NotificationType.Warning); false, true);Select(dCalculate))
```

### `ScrDashboard/dCapture` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dCapture` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dCapture` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dCapture` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dCapture` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dCapture` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCapture` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCapture` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCapture` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCapture` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dCapture` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrDashboard/dCapture` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(1)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dCapture` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dCapture` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPhoneOverview` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((!(ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height) && varDView="overview") && !(App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23))
```

### `ScrDashboard/dPhoneOverview` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366))))/2
```

### `ScrDashboard/dPhoneOverview` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790))))/2
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Visible**  _(Label@2.5.1)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#168A70"),ColorValue("#85DFAC"))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Visible**  _(Label@2.5.1)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр',ScreenTransition.Fade)
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Dashboard"
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/doverviewTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Live",ColorValue("#16324F"),ColorValue("#526777")),If(varDPeriod="Live",ColorValue("#F5F4F1"),ColorValue("#66615B")))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Live",ColorValue("#DFEBF9"),ColorValue("#FFFFFF")),If(varDPeriod="Live",ColorValue("#202225"),ColorValue("#FFFFFF")))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"Live");Select(dCalculate)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Live"
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(46)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(203)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(98)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="7 хоног",ColorValue("#16324F"),ColorValue("#526777")),If(varDPeriod="7 хоног",ColorValue("#F5F4F1"),ColorValue("#66615B")))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="7 хоног",ColorValue("#DFEBF9"),ColorValue("#FFFFFF")),If(varDPeriod="7 хоног",ColorValue("#202225"),ColorValue("#FFFFFF")))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"7 хоног");Select(dCalculate)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"7 хоног"
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(46)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(250)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(98)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Сар",ColorValue("#16324F"),ColorValue("#526777")),If(varDPeriod="Сар",ColorValue("#F5F4F1"),ColorValue("#66615B")))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Сар",ColorValue("#DFEBF9"),ColorValue("#FFFFFF")),If(varDPeriod="Сар",ColorValue("#202225"),ColorValue("#FFFFFF")))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"Сар");Select(dCalculate)
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Сар"
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(46)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(297)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhonePeriod2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(98)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varDBusy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(dReadBC)
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"BC шинэчлэх"
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(106)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneRead` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(98)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(213)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(143)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Text**  _(Label@2.5.1)_
```powerfx
"Нийт үлдэгдэл · локал үнэлгээ"
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Width**  _(Label@2.5.1)_
```powerfx
(298)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **X**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroCaption` . **Y**  _(Label@2.5.1)_
```powerfx
(156)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Height**  _(Label@2.5.1)_
```powerfx
(59)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,Min(Self.Height*0.48,Self.Width/Max(10,Len(Self.Text))*1.15))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())),"—",Text(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank()),"#,##0") & " ₮")
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Tooltip**  _(Label@2.5.1)_
```powerfx
If(IsBlank(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())),"Үнэлгээ хараахан бэлэн болоогүй",Text(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank()),"#,##0.##") & " ₮")
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Width**  _(Label@2.5.1)_
```powerfx
(298)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **X**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroValue` . **Y**  _(Label@2.5.1)_
```powerfx
(187)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Height**  _(Label@2.5.1)_
```powerfx
(19)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Text**  _(Label@2.5.1)_
```powerfx
If(varDStockBuildingV17,"Үнэлгээг шинэчилж байна…",!varDStockReadyV17,"Үнэлгээ хараахан бэлэн болоогүй",CountIf(colDStock,IsBlank(Cost))>0,"Өртөггүй мөр: " & CountIf(colDStock,IsBlank(Cost)),"Хадгалсан snapshot · ₮")
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Width**  _(Label@2.5.1)_
```powerfx
(298)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **X**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroScope` . **Y**  _(Label@2.5.1)_
```powerfx
(250)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrend` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrend` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrend` . **Height**  _(Image@2.2.3)_
```powerfx
(75)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrend` . **Image**  _(Image@2.2.3)_
```powerfx
If(varDPdfPendingV23,Substitute(Substitute(Substitute(Substitute(Substitute("data:image/svg+xml;utf8," & EncodeUrl(varDTrendSvg),"%23F5F4F2","%2316324F"),"%23858B94","%23526777"),"%23363A40","%23DFE8F0"),"%23FA7020","%23FFE1CD"),"%23ED242B","%23FFD1BF"),"data:image/svg+xml;utf8," & EncodeUrl(varDTrendSvg))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrend` . **Width**  _(Image@2.2.3)_
```powerfx
(322)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrend` . **X**  _(Image@2.2.3)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrend` . **Y**  _(Image@2.2.3)_
```powerfx
(276)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Түүх үүсэхэд график харагдана"
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
CountRows(colDTrend)<2
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(298)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneHeroTrendEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(308)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(83)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(161)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(368)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneDonut` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneDonut` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneDonut` . **Height**  _(Image@2.2.3)_
```powerfx
(55)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneDonut` . **Image**  _(Image@2.2.3)_
```powerfx
If(varDPdfPendingV23,Substitute(Substitute(Substitute(Substitute(Substitute("data:image/svg+xml;utf8," & EncodeUrl(varDDonut),"%23F5F4F2","%2316324F"),"%23858B94","%23526777"),"%23363A40","%23DFE8F0"),"%23FA7020","%23FFE1CD"),"%23ED242B","%23FFD1BF"),"data:image/svg+xml;utf8," & EncodeUrl(varDDonut))
```

### `ScrDashboard/dPhoneOverview/dPhoneDonut` . **Width**  _(Image@2.2.3)_
```powerfx
(55)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneDonut` . **X**  _(Image@2.2.3)_
```powerfx
(28)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneDonut` . **Y**  _(Image@2.2.3)_
```powerfx
(382)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Height**  _(Label@2.5.1)_
```powerfx
(29)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Size**  _(Label@2.5.1)_
```powerfx
17*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varDAccuracy),"—",Text(varDAccuracy,"0.0") & "%")
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Width**  _(Label@2.5.1)_
```powerfx
(78)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **X**  _(Label@2.5.1)_
```powerfx
(92)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracy` . **Y**  _(Label@2.5.1)_
```powerfx
(383)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#E7EEF6"),ColorValue("#24282D"))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
28*(Parent.Height/790)
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,true);Set(varDExportKind,If(varDView="variance","CSV","PDF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*(Parent.Width/366)
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"PDF · мэйл"
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (!varDPdfPendingV23)
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
110*(Parent.Width/366)
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **X**  _(Classic/Button@2.2.0)_
```powerfx
126*(Parent.Width/366)
```

### `ScrDashboard/dPhoneOverview/dPhoneExportV24Overview` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
18*(Parent.Height/790)
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Height**  _(Label@2.5.1)_
```powerfx
(19)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Text**  _(Label@2.5.1)_
```powerfx
"Нарийвчлал"
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Width**  _(Label@2.5.1)_
```powerfx
(78)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **X**  _(Label@2.5.1)_
```powerfx
(92)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneAccuracyCaption` . **Y**  _(Label@2.5.1)_
```powerfx
(415)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(83)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDView,"variance")
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
16*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Зөрүүтэй " & CountRows(colDVariance) & " ↗"
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(161)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(188)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneVariance` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(368)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(196)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(463)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"TOP 5 зарлага · өртгийн дүнгээр"
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(302)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(475)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(142)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDTop
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
21.0*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(314)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(510)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Height**  _(Label@2.5.1)_
```powerfx
21*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(LookUp(colOfflineItems,number=ThisItem.ItemNo,displayName),ThisItem.ItemNo)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Width**  _(Label@2.5.1)_
```powerfx
(200)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopItem` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Height**  _(Label@2.5.1)_
```powerfx
21*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Qty,"#,##0.###") & " " & ThisItem.Uom
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Width**  _(Label@2.5.1)_
```powerfx
(86)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **X**  _(Label@2.5.1)_
```powerfx
(210)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopQty` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Height**  _(Label@2.5.1)_
```powerfx
(19)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Visible**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Width**  _(Label@2.5.1)_
```powerfx
(290)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopGallery/dPhoneTopLocation` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(37)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Зарлагын өгөгдөл алга"
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(colDTop)
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(296)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(35)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneTopEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(561.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDView,"warehouse")
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах ба зарцуулалт →"
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneWarehouse` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(670)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(58)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneNav` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(718)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр')
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нүүр"
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(52)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavHome` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(727)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(Screen1)
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(66)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(82)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavWarehouse` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(727)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(scrWarehouses)
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
20*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"▢"
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(153)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavScan` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(727)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Dashboard"
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(88)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(211)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavDashboard` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(727)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(39)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Би"
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(307)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dNavMe` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(727)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(23)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(dCapture)
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Snapshot +"
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(96)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(234)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneOverview/dPhoneSnapshot` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(163)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneVarianceRoot` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPhoneVarianceRoot` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (!(ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height) && varDView="variance")
```

### `ScrDashboard/dPhoneVarianceRoot` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366))))/2
```

### `ScrDashboard/dPhoneVarianceRoot` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790))))/2
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#168A70"),ColorValue("#85DFAC"))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDView,"overview")
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүний шинжилгээ"
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dvarianceTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(146)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(112)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroArt` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroArt` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroArt` . **Height**  _(Image@2.2.3)_
```powerfx
(146)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroArt` . **Image**  _(Image@2.2.3)_
```powerfx
If(varDPdfPendingV23,Substitute(Substitute(Substitute(Substitute(Substitute("data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' width='332' height='146'><defs><linearGradient id='g' x2='1' y2='1'><stop stop-color='#FA7020'/><stop offset='1' stop-color='#ED242B'/></linearGradient></defs><rect width='332' height='146' rx='25' fill='url(#g)'/><circle cx='292.16' cy='80.30000000000001' r='68.61999999999999' fill='none' stroke='#FFFFFF' stroke-opacity='.12' stroke-width='17'/></svg>"),"%23F5F4F2","%2316324F"),"%23858B94","%23526777"),"%23363A40","%23DFE8F0"),"%23FA7020","%23FFE1CD"),"%23ED242B","%23FFD1BF"),"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' width='332' height='146'><defs><linearGradient id='g' x2='1' y2='1'><stop stop-color='#FA7020'/><stop offset='1' stop-color='#ED242B'/></linearGradient></defs><rect width='332' height='146' rx='25' fill='url(#g)'/><circle cx='292.16' cy='80.30000000000001' r='68.61999999999999' fill='none' stroke='#FFFFFF' stroke-opacity='.12' stroke-width='17'/></svg>"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroArt` . **Width**  _(Image@2.2.3)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroArt` . **X**  _(Image@2.2.3)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroArt` . **Y**  _(Image@2.2.3)_
```powerfx
(112)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүтэй бараа"
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(296)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **X**  _(Label@2.5.1)_
```powerfx
(35)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(127)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Height**  _(Label@2.5.1)_
```powerfx
(58)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Size**  _(Label@2.5.1)_
```powerfx
35*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colDVariance)) & " / " & CountRows(colDValid)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Width**  _(Label@2.5.1)_
```powerfx
(296)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **X**  _(Label@2.5.1)_
```powerfx
(35)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroTotal` . **Y**  _(Label@2.5.1)_
```powerfx
(161)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Height**  _(Label@2.5.1)_
```powerfx
(29)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Text**  _(Label@2.5.1)_
```powerfx
"дутуу " & CountRows(Filter(colDVariance,DVariance<0)) & "   илүү " & CountRows(Filter(colDVariance,DVariance>0)) & "   тайлбаргүй " & CountRows(Filter(colDVariance,DReason="Тайлбаргүй"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Width**  _(Label@2.5.1)_
```powerfx
(296)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **X**  _(Label@2.5.1)_
```powerfx
(35)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceHeroStats` . **Y**  _(Label@2.5.1)_
```powerfx
(216)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(129)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(270)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүний шалтгаан"
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(302)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(282)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(80)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDReasons
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
31*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(314)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(315)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.DReason
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Width**  _(Label@2.5.1)_
```powerfx
(100.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsReason` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Total/Max(1,CountRows(colDVariance))*100,"0") & "%"
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Width**  _(Label@2.5.1)_
```powerfx
(39)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **X**  _(Label@2.5.1)_
```powerfx
(108.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dReasonsGallery/dReasonsShare` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хамгийн их зөрүү · өртгөөр"
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(324)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **X**  _(Label@2.5.1)_
```powerfx
(21)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceListTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(413)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(237)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDVariance
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
70*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(344)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(11)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(451)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(64)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceRow` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(ThisItem.ItemName,ThisItem.ItemNo)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Width**  _(Label@2.5.1)_
```powerfx
(218)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceName` . **Y**  _(Label@2.5.1)_
```powerfx
(7)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode & " · " & ThisItem.DReason
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Width**  _(Label@2.5.1)_
```powerfx
(218)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceReason` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Height**  _(Label@2.5.1)_
```powerfx
(31)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Text**  _(Label@2.5.1)_
```powerfx
If(ThisItem.DVariance>0,"+","") & Text(ThisItem.DVariance,"#,##0.###")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Width**  _(Label@2.5.1)_
```powerfx
(78)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **X**  _(Label@2.5.1)_
```powerfx
(239)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceGallery/dVarianceQty` . **Y**  _(Label@2.5.1)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,true);Set(varDExportKind,"CSV")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Excel"
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(108)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceExcel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(720)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#DFEBF9"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,true);Set(varDExportKind,If(varDView="variance","CSV","PDF"))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэйл + хавсралт"
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(216)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(133)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneVarianceRoot/dVarianceMail` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(720)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneWarehouseRoot` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPhoneWarehouseRoot` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
790*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (!(ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height) && varDView="warehouse")
```

### `ScrDashboard/dPhoneWarehouseRoot` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
366*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-366*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366))))/2
```

### `ScrDashboard/dPhoneWarehouseRoot` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-790*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790))))/2
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Now(),"hh:mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Visible**  _(Label@2.5.1)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **X**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseClock` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#168A70"),ColorValue("#85DFAC"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Text**  _(Label@2.5.1)_
```powerfx
"ЛОКАЛ"
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Visible**  _(Label@2.5.1)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Width**  _(Label@2.5.1)_
```powerfx
(114)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **X**  _(Label@2.5.1)_
```powerfx
(230)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseStatus` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(38)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDView,"overview")
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
22*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹"
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(36)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(51)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Агуулах ба зарцуулалт"
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(275)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **X**  _(Label@2.5.1)_
```powerfx
(66)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dwarehouseTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(51)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(232)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(112)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Агуулахын төлөв · минимум"
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(302)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(124)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(177)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDWarehouses
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
78*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(316)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(159)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFF1E8"),ColorValue("#23191A"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(77)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(97.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesTile` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.locationCode
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Width**  _(Label@2.5.1)_
```powerfx
(81.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **X**  _(Label@2.5.1)_
```powerfx
(8)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesCode` . **Y**  _(Label@2.5.1)_
```powerfx
(7)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Shortage & " дутуу"
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Width**  _(Label@2.5.1)_
```powerfx
(81.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **X**  _(Label@2.5.1)_
```powerfx
(8)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesShort` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Configured & "/" & ThisItem.SKU & " мин"
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Width**  _(Label@2.5.1)_
```powerfx
(81.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **X**  _(Label@2.5.1)_
```powerfx
(8)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesScope` . **Y**  _(Label@2.5.1)_
```powerfx
(58)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(77)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,89,38,0.1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWLocation,ThisItem.locationCode);Navigate(Screen1,ScreenTransition.Fade)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(97.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneWarehousesGallery/dPhoneWarehousesHit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(159)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(356)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хөдөлгөөн — сараар · ₮"
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(302)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(368)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Text**  _(Label@2.5.1)_
```powerfx
"● орлого   ● зарлага"
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Width**  _(Label@2.5.1)_
```powerfx
(302)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyLegend` . **Y**  _(Label@2.5.1)_
```powerfx
(398)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,1)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(35.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome0` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,1)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,1)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(50.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense0` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,1)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,1)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **X**  _(Label@2.5.1)_
```powerfx
(35.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth0` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,2)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(72.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome1` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,2)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,2)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(87.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense1` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,2)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,2)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **X**  _(Label@2.5.1)_
```powerfx
(72.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth1` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,3)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(109.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,3)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#E7EEF6"),ColorValue("#24282D"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
28*(Parent.Height/790)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,true);Set(varDExportKind,If(varDView="variance","CSV","PDF"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*(Parent.Width/366)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"PDF · мэйл"
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (!varDPdfPendingV23)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
110*(Parent.Width/366)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **X**  _(Classic/Button@2.2.0)_
```powerfx
126*(Parent.Width/366)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneExportV24Warehouse` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
18*(Parent.Height/790)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,3)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(124.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,3)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,3)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **X**  _(Label@2.5.1)_
```powerfx
(109.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth2` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,4)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(146.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome3` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,4)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,4)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(161.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense3` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,4)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,4)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **X**  _(Label@2.5.1)_
```powerfx
(146.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth3` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,5)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(183.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome4` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,5)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,5)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(198.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense4` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,5)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,5)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **X**  _(Label@2.5.1)_
```powerfx
(183.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth4` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,6)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(220.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome5` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,6)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,6)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(235.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense5` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,6)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,6)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **X**  _(Label@2.5.1)_
```powerfx
(220.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth5` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,7)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(257.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome6` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,7)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,7)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(272.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense6` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,7)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,7)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **X**  _(Label@2.5.1)_
```powerfx
(257.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth6` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,8)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(294.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyIncome7` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,8)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(54)*Last(FirstN(colDMonths,8)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(13.69)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(309.91)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyExpense7` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(484-(54)*Last(FirstN(colDMonths,8)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,8)).MonthDate,"mm")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Width**  _(Label@2.5.1)_
```powerfx
(37.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **X**  _(Label@2.5.1)_
```powerfx
(294.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyMonth7` . **Y**  _(Label@2.5.1)_
```powerfx
(490)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(53)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
If(varDIncomplete,"BC мөрийн хязгаарт хүрсэн",!varDLoaded,"BC шинэчлэх товчийг дарна уу.","Хөдөлгөөн алга")
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
!varDLoaded || varDIncomplete || Sum(colDMonths,Income+Expense)=0
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(296)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(35)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dPhoneMonthlyEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(435.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(247)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(332)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(527)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"TOP 5 зарлага · өртгийн дүнгээр"
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(302)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **X**  _(Label@2.5.1)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(539)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(193)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDTop
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
31.200000000000003*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(314)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(574)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Height**  _(Label@2.5.1)_
```powerfx
21*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(LookUp(colOfflineItems,number=ThisItem.ItemNo,displayName),ThisItem.ItemNo)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Width**  _(Label@2.5.1)_
```powerfx
(200)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopItem` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Height**  _(Label@2.5.1)_
```powerfx
21*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Qty,"#,##0.###") & " " & ThisItem.Uom
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Width**  _(Label@2.5.1)_
```powerfx
(86)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **X**  _(Label@2.5.1)_
```powerfx
(210)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopQty` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Height**  _(Label@2.5.1)_
```powerfx
(19)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Visible**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Width**  _(Label@2.5.1)_
```powerfx
(290)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopGallery/dWarehouseTopLocation` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(37)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Зарлагын өгөгдөл алга"
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(colDTop)
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(296)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(35)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPhoneWarehouseRoot/dWarehouseTopEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(650.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPadRoot` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
820*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height))
```

### `ScrDashboard/dPadRoot` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
1180*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-1180*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366))))/2
```

### `ScrDashboard/dPadRoot` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-820*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790))))/2
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(820)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
0*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(94)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadSidebar` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadLogo` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadLogo` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadLogo` . **Height**  _(Image@2.2.3)_
```powerfx
(48)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadLogo` . **Image**  _(Image@2.2.3)_
```powerfx
'Buuruljuut logo 3-6-03 2'
```

### `ScrDashboard/dPadRoot/dPadLogo` . **Width**  _(Image@2.2.3)_
```powerfx
(60)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadLogo` . **X**  _(Image@2.2.3)_
```powerfx
(17)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadLogo` . **Y**  _(Image@2.2.3)_
```powerfx
(24)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadNav0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadNav0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр')
```

### `ScrDashboard/dPadRoot/dPadNav0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadNav0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadNav0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нүүр"
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(68)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(116)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadNav1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadNav1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrCountHome,ScreenTransition.Fade)
```

### `ScrDashboard/dPadRoot/dPadNav1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadNav1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadNav1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Тооллого"
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(68)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(185)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadNav2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadNav2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(Screen1)
```

### `ScrDashboard/dPadRoot/dPadNav2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadNav2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadNav2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(68)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(254)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#F4F7FB"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadNav3` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadNav3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(ScrCameraSearch,ScreenTransition.Fade)
```

### `ScrDashboard/dPadRoot/dPadNav3` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadNav3` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadNav3` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Камер"
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(68)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(323)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(56)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadNav4` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadNav4` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadNav4` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadNav4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadNav4` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Dashboard"
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(68)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadNav4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(392)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadUser` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadUser` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadUser` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadUser` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadUser` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadUser` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(43)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadUser` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadUser` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadUser` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `ScrDashboard/dPadRoot/dPadUser` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadUser` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadUser` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadUser` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadUser` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadUser` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Upper(Left(User().FullName,2))
```

### `ScrDashboard/dPadRoot/dPadUser` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(43)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadUser` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(755)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadOverline` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadOverline` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadOverline` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Text**  _(Label@2.5.1)_
```powerfx
If(varDLoaded && !varDIncomplete,"BC " & Text(varDChecked,"hh:mm"),"DASHBOARD · ЛОКАЛ")
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Width**  _(Label@2.5.1)_
```powerfx
(475)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **X**  _(Label@2.5.1)_
```powerfx
(122)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadOverline` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadHeading` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadHeading` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadHeading` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Height**  _(Label@2.5.1)_
```powerfx
(29)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Size**  _(Label@2.5.1)_
```powerfx
24*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"Dashboard"
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Width**  _(Label@2.5.1)_
```powerfx
(405)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **X**  _(Label@2.5.1)_
```powerfx
(122)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeading` . **Y**  _(Label@2.5.1)_
```powerfx
(43)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#F5F4F1"))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#DFEBF9"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Бүгд"
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(62)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(645)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadBusiness0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Notify("Power/Mining ангиллын өгөгдөл холбогдоогүй байна.",NotificationType.Information)
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Power"
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(62)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(711)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadBusiness1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Notify("Power/Mining ангиллын өгөгдөл холбогдоогүй байна.",NotificationType.Information)
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Mining"
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(62)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(777)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadBusiness2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(32)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Live",ColorValue("#16324F"),ColorValue("#526777")),If(varDPeriod="Live",ColorValue("#F5F4F1"),ColorValue("#66615B")))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Live",ColorValue("#DFEBF9"),ColorValue("#FFFFFF")),If(varDPeriod="Live",ColorValue("#202225"),ColorValue("#FFFFFF")))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"Live");Select(dCalculate)
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Live"
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(46)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(852)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadPeriod0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="7 хоног",ColorValue("#16324F"),ColorValue("#526777")),If(varDPeriod="7 хоног",ColorValue("#F5F4F1"),ColorValue("#66615B")))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="7 хоног",ColorValue("#DFEBF9"),ColorValue("#FFFFFF")),If(varDPeriod="7 хоног",ColorValue("#202225"),ColorValue("#FFFFFF")))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"7 хоног");Select(dCalculate)
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"7 хоног"
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(46)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(899)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadPeriod1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Сар",ColorValue("#16324F"),ColorValue("#526777")),If(varDPeriod="Сар",ColorValue("#F5F4F1"),ColorValue("#66615B")))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,If(varDPeriod="Сар",ColorValue("#DFEBF9"),ColorValue("#FFFFFF")),If(varDPeriod="Сар",ColorValue("#202225"),ColorValue("#FFFFFF")))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"Сар");Select(dCalculate)
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Сар"
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(46)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(946)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadPeriod2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadExport` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadExport` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadExport` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadExport` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadExport` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadExport` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadExport` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadExport` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadExport` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,true);Set(varDExportKind,If(varDView="variance","CSV","PDF"))
```

### `ScrDashboard/dPadRoot/dPadExport` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadExport` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadExport` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadExport` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadExport` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadExport` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"PDF · мэйл"
```

### `ScrDashboard/dPadRoot/dPadExport` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPadRoot/dPadExport` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(142)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(1009)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadExport` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(33)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(221)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(440)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(122)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(105)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Text**  _(Label@2.5.1)_
```powerfx
"Нийт үлдэгдэл · локал үнэлгээ"
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Width**  _(Label@2.5.1)_
```powerfx
(406)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **X**  _(Label@2.5.1)_
```powerfx
(139)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroCaption` . **Y**  _(Label@2.5.1)_
```powerfx
(118)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Height**  _(Label@2.5.1)_
```powerfx
(59)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Size**  _(Label@2.5.1)_
```powerfx
Max(12,Min(Self.Height*0.48,Self.Width/Max(10,Len(Self.Text))*1.15))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())),"—",Text(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank()),"#,##0") & " ₮")
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Tooltip**  _(Label@2.5.1)_
```powerfx
If(IsBlank(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())),"Үнэлгээ хараахан бэлэн болоогүй",Text(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank()),"#,##0.##") & " ₮")
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Width**  _(Label@2.5.1)_
```powerfx
(406)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **X**  _(Label@2.5.1)_
```powerfx
(139)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroValue` . **Y**  _(Label@2.5.1)_
```powerfx
(149)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Height**  _(Label@2.5.1)_
```powerfx
(19)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Text**  _(Label@2.5.1)_
```powerfx
"Snapshot түүх · энэ төхөөрөмж"
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Width**  _(Label@2.5.1)_
```powerfx
(406)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **X**  _(Label@2.5.1)_
```powerfx
(139)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroScope` . **Y**  _(Label@2.5.1)_
```powerfx
(212)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrend` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadHeroTrend` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadHeroTrend` . **Height**  _(Image@2.2.3)_
```powerfx
(83)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrend` . **Image**  _(Image@2.2.3)_
```powerfx
If(varDPdfPendingV23,Substitute(Substitute(Substitute(Substitute(Substitute("data:image/svg+xml;utf8," & EncodeUrl(varDTrendSvg),"%23F5F4F2","%2316324F"),"%23858B94","%23526777"),"%23363A40","%23DFE8F0"),"%23FA7020","%23FFE1CD"),"%23ED242B","%23FFD1BF"),"data:image/svg+xml;utf8," & EncodeUrl(varDTrendSvg))
```

### `ScrDashboard/dPadRoot/dPadHeroTrend` . **Width**  _(Image@2.2.3)_
```powerfx
(430)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrend` . **X**  _(Image@2.2.3)_
```powerfx
(127)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrend` . **Y**  _(Image@2.2.3)_
```powerfx
(238)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Түүх үүсэхэд график харагдана"
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
CountRows(colDTrend)<2
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(406)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(139)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadHeroTrendEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(278)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(221)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(279)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(576)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(105)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Тооллогын нарийвчлал"
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(243)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **X**  _(Label@2.5.1)_
```powerfx
(594)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadAccuracyTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(122)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadDonut` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadDonut` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadDonut` . **Height**  _(Image@2.2.3)_
```powerfx
(128)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadDonut` . **Image**  _(Image@2.2.3)_
```powerfx
If(varDPdfPendingV23,Substitute(Substitute(Substitute(Substitute(Substitute("data:image/svg+xml;utf8," & EncodeUrl(varDDonut),"%23F5F4F2","%2316324F"),"%23858B94","%23526777"),"%23363A40","%23DFE8F0"),"%23FA7020","%23FFE1CD"),"%23ED242B","%23FFD1BF"),"data:image/svg+xml;utf8," & EncodeUrl(varDDonut))
```

### `ScrDashboard/dPadRoot/dPadDonut` . **Width**  _(Image@2.2.3)_
```powerfx
(128)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadDonut` . **X**  _(Image@2.2.3)_
```powerfx
(594)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadDonut` . **Y**  _(Image@2.2.3)_
```powerfx
(170)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Height**  _(Label@2.5.1)_
```powerfx
(31)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Size**  _(Label@2.5.1)_
```powerfx
19*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varDAccuracy),"—",Text(varDAccuracy,"0.0") & "%")
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Width**  _(Label@2.5.1)_
```powerfx
(85)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **X**  _(Label@2.5.1)_
```powerfx
(620)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadAccuracy` . **Y**  _(Label@2.5.1)_
```powerfx
(213)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCount` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadCount` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadCount` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadCount` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadCount` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadCount` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadCount` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadCount` . **Height**  _(Label@2.5.1)_
```powerfx
(37)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCount` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCount` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colDValid)) & " тоолсон"
```

### `ScrDashboard/dPadRoot/dPadCount` . **Width**  _(Label@2.5.1)_
```powerfx
(110)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadCount` . **X**  _(Label@2.5.1)_
```powerfx
(730)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadCount` . **Y**  _(Label@2.5.1)_
```powerfx
(185)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadOwn` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadOwn` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Height**  _(Label@2.5.1)_
```powerfx
(40)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Text**  _(Label@2.5.1)_
```powerfx
"Өөрийн тооллого"
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Width**  _(Label@2.5.1)_
```powerfx
(110)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **X**  _(Label@2.5.1)_
```powerfx
(730)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadOwn` . **Y**  _(Label@2.5.1)_
```powerfx
(232)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(221)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
25*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(282)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(869)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(105)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceArt` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadVarianceArt` . **Fill**  _(Image@2.2.3)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadVarianceArt` . **Height**  _(Image@2.2.3)_
```powerfx
(221)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceArt` . **Image**  _(Image@2.2.3)_
```powerfx
If(varDPdfPendingV23,Substitute(Substitute(Substitute(Substitute(Substitute("data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' width='282' height='221'><defs><linearGradient id='g' x2='1' y2='1'><stop stop-color='#FA7020'/><stop offset='1' stop-color='#ED242B'/></linearGradient></defs><rect width='282' height='221' rx='25' fill='url(#g)'/><circle cx='248.16' cy='121.55000000000001' r='103.86999999999999' fill='none' stroke='#FFFFFF' stroke-opacity='.12' stroke-width='17'/></svg>"),"%23F5F4F2","%2316324F"),"%23858B94","%23526777"),"%23363A40","%23DFE8F0"),"%23FA7020","%23FFE1CD"),"%23ED242B","%23FFD1BF"),"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' width='282' height='221'><defs><linearGradient id='g' x2='1' y2='1'><stop stop-color='#FA7020'/><stop offset='1' stop-color='#ED242B'/></linearGradient></defs><rect width='282' height='221' rx='25' fill='url(#g)'/><circle cx='248.16' cy='121.55000000000001' r='103.86999999999999' fill='none' stroke='#FFFFFF' stroke-opacity='.12' stroke-width='17'/></svg>"))
```

### `ScrDashboard/dPadRoot/dPadVarianceArt` . **Width**  _(Image@2.2.3)_
```powerfx
(282)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceArt` . **X**  _(Image@2.2.3)_
```powerfx
(869)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceArt` . **Y**  _(Image@2.2.3)_
```powerfx
(105)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүтэй бараа"
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(246)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **X**  _(Label@2.5.1)_
```powerfx
(887)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(120)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Height**  _(Label@2.5.1)_
```powerfx
(58)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Size**  _(Label@2.5.1)_
```powerfx
35*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colDVariance)) & " / " & CountRows(colDValid)
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Width**  _(Label@2.5.1)_
```powerfx
(246)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **X**  _(Label@2.5.1)_
```powerfx
(887)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceTotal` . **Y**  _(Label@2.5.1)_
```powerfx
(154)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Height**  _(Label@2.5.1)_
```powerfx
(29)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Text**  _(Label@2.5.1)_
```powerfx
"дутуу " & CountRows(Filter(colDVariance,DVariance<0)) & "   илүү " & CountRows(Filter(colDVariance,DVariance>0)) & "   тайлбаргүй " & CountRows(Filter(colDVariance,DReason="Тайлбаргүй"))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Width**  _(Label@2.5.1)_
```powerfx
(246)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **X**  _(Label@2.5.1)_
```powerfx
(887)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceStats` . **Y**  _(Label@2.5.1)_
```powerfx
(284)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(456)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(384)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(122)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(340)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хөдөлгөөн — сараар · ₮"
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(354)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **X**  _(Label@2.5.1)_
```powerfx
(137)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(352)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Text**  _(Label@2.5.1)_
```powerfx
"● орлого   ● зарлага"
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Width**  _(Label@2.5.1)_
```powerfx
(354)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **X**  _(Label@2.5.1)_
```powerfx
(137)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyLegend` . **Y**  _(Label@2.5.1)_
```powerfx
(382)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,1)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(140.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome0` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,1)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,1)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(158.70499999999998)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense0` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,1)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,1)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **X**  _(Label@2.5.1)_
```powerfx
(140.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth0` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,2)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(183.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome1` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,2)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,2)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(202.20499999999998)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense1` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,2)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,2)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **X**  _(Label@2.5.1)_
```powerfx
(183.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth1` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,3)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(227.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,3)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,3)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(245.70499999999998)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,3)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,3)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **X**  _(Label@2.5.1)_
```powerfx
(227.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth2` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,4)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(270.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome3` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,4)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,4)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(289.205)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense3` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,4)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,4)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **X**  _(Label@2.5.1)_
```powerfx
(270.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth3` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,5)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(314.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome4` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,5)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,5)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(332.705)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense4` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,5)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,5)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **X**  _(Label@2.5.1)_
```powerfx
(314.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth4` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,6)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(357.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome5` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,6)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,6)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(376.205)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense5` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,6)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,6)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **X**  _(Label@2.5.1)_
```powerfx
(357.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth5` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,7)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(401.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome6` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,7)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,7)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(419.705)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense6` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,7)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,7)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **X**  _(Label@2.5.1)_
```powerfx
(401.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth6` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,8)).Income/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(444.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyIncome7` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,8)).Income/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#569DD8"),ColorValue("#454950"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(351)*Last(FirstN(colDMonths,8)).Expense/Max(1,Coalesce(varDMaxMonth,1))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
4*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(16.095)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(463.205)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyExpense7` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(765-(351)*Last(FirstN(colDMonths,8)).Expense/Max(1,Coalesce(varDMaxMonth,1)))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Height**  _(Label@2.5.1)_
```powerfx
(18)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Text**  _(Label@2.5.1)_
```powerfx
Text(Last(FirstN(colDMonths,8)).MonthDate,"mm")
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Width**  _(Label@2.5.1)_
```powerfx
(43.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **X**  _(Label@2.5.1)_
```powerfx
(444.5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyMonth7` . **Y**  _(Label@2.5.1)_
```powerfx
(771)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(53)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
If(varDIncomplete,"BC мөрийн хязгаарт хүрсэн",!varDLoaded,"BC шинэчлэх товчийг дарна уу.","Хөдөлгөөн алга")
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
!varDLoaded || varDIncomplete || Sum(colDMonths,Income+Expense)=0
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(348)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(140)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadMonthlyEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(568.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(456)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(309)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(520)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(340)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"TOP 5 зарлага · өртгийн дүнгээр"
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(279)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **X**  _(Label@2.5.1)_
```powerfx
(535)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(352)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(402)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDTop
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
73.0*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(291)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(529)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(387)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Height**  _(Label@2.5.1)_
```powerfx
(31)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(LookUp(colOfflineItems,number=ThisItem.ItemNo,displayName),ThisItem.ItemNo)
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Width**  _(Label@2.5.1)_
```powerfx
(177)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopItem` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Height**  _(Label@2.5.1)_
```powerfx
(29)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Size**  _(Label@2.5.1)_
```powerfx
9*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Qty,"#,##0.###") & " " & ThisItem.Uom
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Width**  _(Label@2.5.1)_
```powerfx
(86)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **X**  _(Label@2.5.1)_
```powerfx
(187)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopQty` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Height**  _(Label@2.5.1)_
```powerfx
(19)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Width**  _(Label@2.5.1)_
```powerfx
(267)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopLocation` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#DFE8F0"),ColorValue("#363A40"))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(259)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopTrack` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(62)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
2*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(259)*ThisItem.Amount/Max(1,Max(colDTop,Amount))*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopGallery/dPadTopBar` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(62)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
(37)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Зарлагын өгөгдөл алга"
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
IsEmpty(colDTop)
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
(273)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **X**  _(Label@2.5.1)_
```powerfx
(538)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadTopEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
(568.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(173)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(308)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(843)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(340)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Size**  _(Label@2.5.1)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүний шалтгаан"
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(278)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **X**  _(Label@2.5.1)_
```powerfx
(858)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(352)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(124)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDReasons
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
31*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(290)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(852)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(385)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.DReason
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Width**  _(Label@2.5.1)_
```powerfx
(88.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **X**  _(Label@2.5.1)_
```powerfx
(5)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsReason` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Text**  _(Label@2.5.1)_
```powerfx
Text(ThisItem.Total/Max(1,CountRows(colDVariance))*100,"0") & "%"
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Width**  _(Label@2.5.1)_
```powerfx
(39)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **X**  _(Label@2.5.1)_
```powerfx
(96.0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadReasonsGallery/dPadReasonsShare` . **Y**  _(Label@2.5.1)_
```powerfx
(2)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(269)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
22*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(308)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(843)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesCard` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(527)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Size**  _(Label@2.5.1)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Агуулахын төлөв · минимум"
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(278)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **X**  _(Label@2.5.1)_
```powerfx
(858)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(539)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(214)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDWarehouses
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
78*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(292)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(851)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(574)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFF1E8"),ColorValue("#23191A"))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(77)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
13*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(89.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesTile` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Height**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Size**  _(Label@2.5.1)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.locationCode
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Width**  _(Label@2.5.1)_
```powerfx
(73.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **X**  _(Label@2.5.1)_
```powerfx
(8)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesCode` . **Y**  _(Label@2.5.1)_
```powerfx
(7)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Shortage & " дутуу"
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Width**  _(Label@2.5.1)_
```powerfx
(73.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **X**  _(Label@2.5.1)_
```powerfx
(8)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesShort` . **Y**  _(Label@2.5.1)_
```powerfx
(34)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Height**  _(Label@2.5.1)_
```powerfx
(16)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Size**  _(Label@2.5.1)_
```powerfx
7*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.Configured & "/" & ThisItem.SKU & " мин"
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Width**  _(Label@2.5.1)_
```powerfx
(73.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **X**  _(Label@2.5.1)_
```powerfx
(8)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesScope` . **Y**  _(Label@2.5.1)_
```powerfx
(58)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(77)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,89,38,0.1)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varWLocation,ThisItem.locationCode);Navigate(Screen1,ScreenTransition.Fade)
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(89.33333333333333)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadWarehousesGallery/dPadWarehousesHit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(0)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadRead` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadRead` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadRead` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varDBusy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrDashboard/dPadRoot/dPadRead` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadRead` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadRead` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadRead` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadRead` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadRead` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadRead` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(dReadBC)
```

### `ScrDashboard/dPadRoot/dPadRead` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadRead` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadRead` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadRead` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadRead` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadRead` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"BC шинэчлэх"
```

### `ScrDashboard/dPadRoot/dPadRead` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPadRoot/dPadRead` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(142)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(416)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadRead` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(73)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(26)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadCapture` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadCapture` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadRoot/dPadCapture` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(dCapture)
```

### `ScrDashboard/dPadRoot/dPadCapture` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadCapture` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadCapture` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadRoot/dPadCapture` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
8*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Snapshot хадгалах"
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!varDPdfPendingV23 && (true)
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(154)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(251)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadCapture` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(73)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(221)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,255,255,0.05)
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDView,"variance")
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255,255,255,0.1)
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(282)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(869)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadRoot/dPadVarianceHit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(105)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadDrill` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadDrill` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(660)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height) && varDView="variance")
```

### `ScrDashboard/dPadDrill` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(600)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Width-600*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366))))/2
```

### `ScrDashboard/dPadDrill` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(Parent.Height-660*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790))))/2
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Height**  _(Label@2.5.1)_
```powerfx
(44)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Size**  _(Label@2.5.1)_
```powerfx
20*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүний шинжилгээ · өөрийн тооллого"
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Width**  _(Label@2.5.1)_
```powerfx
(496)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **X**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillTitle` . **Y**  _(Label@2.5.1)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(40)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDView,"overview")
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
21*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"×"
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(40)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(538)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillClose` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **Height**  _(Gallery@2.15.0)_
```powerfx
(466)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **Items**  _(Gallery@2.15.0)_
```powerfx
colDVariance
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **TemplateFill**  _(Gallery@2.15.0)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
6*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
76*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **Width**  _(Gallery@2.15.0)_
```powerfx
(568)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **X**  _(Gallery@2.15.0)_
```powerfx
(16)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery` . **Y**  _(Gallery@2.15.0)_
```powerfx
(90)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Height**  _(Label@2.5.1)_
```powerfx
(31)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Size**  _(Label@2.5.1)_
```powerfx
13*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(ThisItem.ItemName,ThisItem.ItemNo)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Width**  _(Label@2.5.1)_
```powerfx
(400)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillName` . **Y**  _(Label@2.5.1)_
```powerfx
(6)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Height**  _(Label@2.5.1)_
```powerfx
(25)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Size**  _(Label@2.5.1)_
```powerfx
10*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.LocationCode & " · " & ThisItem.DReason
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Width**  _(Label@2.5.1)_
```powerfx
(400)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **X**  _(Label@2.5.1)_
```powerfx
(13)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillReason` . **Y**  _(Label@2.5.1)_
```powerfx
(40)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#C34B20"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Height**  _(Label@2.5.1)_
```powerfx
(36)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Size**  _(Label@2.5.1)_
```powerfx
16*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Text**  _(Label@2.5.1)_
```powerfx
If(ThisItem.DVariance>0,"+","") & Text(ThisItem.DVariance,"#,##0.###")
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Width**  _(Label@2.5.1)_
```powerfx
(110)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **X**  _(Label@2.5.1)_
```powerfx
(430)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillGallery/dPadDrillQty` . **Y**  _(Label@2.5.1)_
```powerfx
(15)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,true);Set(varDExportKind,"CSV")
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Excel · мэйл"
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(173)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(22)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillExcel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(583)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(54)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,true);Set(varDExportKind,If(varDView="variance","CSV","PDF"))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Мэйл + хавсралт"
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(371)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(207)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dPadDrill/dPadDrillMail` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(583)*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Height/820),(ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dExportModal` . **Fill**  _(GroupContainer@1.5.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dExportModal` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Height*0.90,440*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrDashboard/dExportModal` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
24*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (varDExport)
```

### `ScrDashboard/dExportModal` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
Min(App.Width*0.92,680*(If(App.Width>=First(App.SizeBreakpoints).Value && App.Width>App.Height,Min(App.Width/1180,App.Height/820),Min(App.Width/640,App.Height/1136))))
```

### `ScrDashboard/dExportModal` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(App.Width-Self.Width)/2
```

### `ScrDashboard/dExportModal` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(App.Height-Self.Height)/2
```

### `ScrDashboard/dExportModal/dExportTitle` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dExportModal/dExportTitle` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportTitle` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dExportModal/dExportTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dExportModal/dExportTitle` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportTitle` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dExportModal/dExportTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/dExportModal/dExportTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.14
```

### `ScrDashboard/dExportModal/dExportTitle` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/24,Parent.Height/17)
```

### `ScrDashboard/dExportModal/dExportTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Dashboard илгээх"
```

### `ScrDashboard/dExportModal/dExportTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrDashboard/dExportModal/dExportTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrDashboard/dExportModal/dExportTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.05
```

### `ScrDashboard/dExportModal/dExportScope` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dExportModal/dExportScope` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportScope` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dExportModal/dExportScope` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dExportModal/dExportScope` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportScope` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dExportModal/dExportScope` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.13
```

### `ScrDashboard/dExportModal/dExportScope` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `ScrDashboard/dExportModal/dExportScope` . **Text**  _(Label@2.5.1)_
```powerfx
"Өөрийн тооллого · сонгосон хугацаа"
```

### `ScrDashboard/dExportModal/dExportScope` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrDashboard/dExportModal/dExportScope` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrDashboard/dExportModal/dExportScope` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.2
```

### `ScrDashboard/dExportModal/dRecipient` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dExportModal/dRecipient` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dExportModal/dRecipient` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
User().Email
```

### `ScrDashboard/dExportModal/dRecipient` . **DisplayMode**  _(Classic/TextInput@2.3.2)_
```powerfx
DisplayMode.View
```

### `ScrDashboard/dExportModal/dRecipient` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dExportModal/dRecipient` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dRecipient` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dExportModal/dRecipient` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Height*0.13
```

### `ScrDashboard/dExportModal/dRecipient` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Хүлээн авагч@tme.mn"
```

### `ScrDashboard/dExportModal/dRecipient` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dExportModal/dRecipient` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ScrDashboard/dExportModal/dRecipient` . **PaddingBottom**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dExportModal/dRecipient` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
12*(If((ScrDashboard.Width>=First(App.SizeBreakpoints).Value && ScrDashboard.Width>ScrDashboard.Height),(ScrDashboard.Width/1180),(ScrDashboard.Width/366)))
```

### `ScrDashboard/dExportModal/dRecipient` . **PaddingRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Width/640))
```

### `ScrDashboard/dExportModal/dRecipient` . **PaddingTop**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dExportModal/dRecipient` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `ScrDashboard/dExportModal/dRecipient` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Width*0.88
```

### `ScrDashboard/dExportModal/dRecipient` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Width*0.06
```

### `ScrDashboard/dExportModal/dRecipient` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
Parent.Height*0.36
```

### `ScrDashboard/dExportModal/dExportHint` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ScrDashboard/dExportModal/dExportHint` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportHint` . **Color**  _(Label@2.5.1)_
```powerfx
If(varDPdfPendingV23,ColorValue("#526777"),ColorValue("#66615B"))
```

### `ScrDashboard/dExportModal/dExportHint` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(0,0,0,0)
```

### `ScrDashboard/dExportModal/dExportHint` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportHint` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dExportModal/dExportHint` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.17
```

### `ScrDashboard/dExportModal/dExportHint` . **Size**  _(Label@2.5.1)_
```powerfx
Min(Parent.Width/32,Parent.Height/23)
```

### `ScrDashboard/dExportModal/dExportHint` . **Text**  _(Label@2.5.1)_
```powerfx
If(varDExportKind="CSV","Хураангуй + шүүсэн мөрүүдийн CSV хавсралт.","Хураангуй + харагдаж буй графиктай PDF хавсралт.") & Char(10) & "Зөвхөн өөрийн Microsoft 365 мэйлд илгээнэ."
```

### `ScrDashboard/dExportModal/dExportHint` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.88
```

### `ScrDashboard/dExportModal/dExportHint` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*0.06
```

### `ScrDashboard/dExportModal/dExportHint` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*0.53
```

### `ScrDashboard/dExportModal/dExportCancel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dExportModal/dExportCancel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dExportModal/dExportCancel` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dExportModal/dExportCancel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFFFFF"),ColorValue("#FFFFFF"))
```

### `ScrDashboard/dExportModal/dExportCancel` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportCancel` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dExportModal/dExportCancel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrDashboard/dExportModal/dExportCancel` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dExportModal/dExportCancel` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dExportModal/dExportCancel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dExportModal/dExportCancel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDExport,false)
```

### `ScrDashboard/dExportModal/dExportCancel` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportCancel` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportCancel` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dExportModal/dExportCancel` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dExportModal/dExportCancel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dExportModal/dExportCancel` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportCancel` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportCancel` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportCancel` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportCancel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrDashboard/dExportModal/dExportCancel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Болих"
```

### `ScrDashboard/dExportModal/dExportCancel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.29
```

### `ScrDashboard/dExportModal/dExportCancel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.06
```

### `ScrDashboard/dExportModal/dExportCancel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrDashboard/dExportModal/dExportSend` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#DFE4E1")
```

### `ScrDashboard/dExportModal/dExportSend` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#16324F"),ColorValue("#202225"))
```

### `ScrDashboard/dExportModal/dExportSend` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ScrDashboard/dExportModal/dExportSend` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(varDBusy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrDashboard/dExportModal/dExportSend` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPdfPendingV23,ColorValue("#FFE1CD"),ColorValue("#ED5F1C"))
```

### `ScrDashboard/dExportModal/dExportSend` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportSend` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dExportModal/dExportSend` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.15
```

### `ScrDashboard/dExportModal/dExportSend` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dExportModal/dExportSend` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dExportModal/dExportSend` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrDashboard/dExportModal/dExportSend` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(varDBusy || varDPdfPendingV23,Notify("Тайлан бэлтгэж байна…",NotificationType.Information),!Connection.Connected,Notify("Интернет холболт алга.",NotificationType.Warning),Set(varDBusy,true);Set(varDAttachmentNameV23,"Dashboard - " & If(varDView="variance","Зөрүүний тайлан",varDView="warehouse","Агуулах ба зарцуулалт","Хураангуй") & " " & Text(varDFrom,"yyyy-mm-dd") & " - " & Text(Today(),"yyyy-mm-dd"));Set(varDSummaryV23,"<h2>" & Substitute(Substitute(Substitute(Coalesce("Dashboard - " & If(varDView="variance","Зөрүүний тайлан",varDView="warehouse","Агуулах ба зарцуулалт","Хураангуй") & " " & Text(varDFrom,"yyyy-mm-dd") & " - " & Text(Today(),"yyyy-mm-dd"),""),"&","&amp;"),"<","&lt;"),">","&gt;") & "</h2><p>Хэрэглэгч: " & Substitute(Substitute(Substitute(Coalesce(User().FullName,""),"&","&amp;"),"<","&lt;"),">","&gt;") & " · " & User().Email & "</p><p>Хугацаа: " & Text(varDFrom,"yyyy-mm-dd") & " — " & Text(Today(),"yyyy-mm-dd") & "</p><p>Хуудас: Dashboard · " & varDView & "</p><p>Шүүлт: өөрийн тооллого · " & varDPeriod & "</p><p>Нийт мөр: " & CountRows(If(varDView="variance",colDVariance,colDLatest)) & "</p><p>Үлдэгдлийн үнэлгээ: " & Coalesce(Text(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank()),"#,##0"),"—") & " ₮</p><p>Тоолсон: " & CountRows(colDValid) & " · Зөрүүтэй: " & CountRows(colDVariance) & " · Нарийвчлал: " & Coalesce(Text(varDAccuracy,"0.0"),"—") & "%</p><p>BC зарцуулалт: " & If(varDLoaded && !varDIncomplete,"уншсан","баталгаажаагүй / дутуу") & "</p><p>Дэлгэрэнгүй тайланг хавсралтаас үзнэ үү.</p>");Set(varDExport,false);If(varDExportKind="CSV",With({_rows:If(varDView="variance",colDVariance,colDLatest)},If(IsEmpty(_rows),Notify("Илгээх мөр алга.",NotificationType.Warning),IfError(PA_ExportInventoryCSV.Run(JSON(ForAll(_rows As r,{'Огноо':If(IsBlank(r.CountDate),"",Text(r.CountDate,"yyyy-mm-dd hh:mm:ss")),'Барааны код':If(IsMatch(r.ItemNo,"[0-9]+"),"=" & Char(34) & r.ItemNo & Char(34),With({s:Coalesce(r.ItemNo,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s))),'Барааны нэр':With({s:Coalesce(r.ItemName,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Агуулах':With({s:Coalesce(r.LocationCode,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Үлдэгдэл':r.OpeningBalance,'Тоолсон':r.CountQty,'Зөрүү':If(IsBlank(r.CountQty),Blank(),r.CountQty-r.OpeningBalance),'Тоологч':With({s:Coalesce(r.Counter,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Шалтгаан':With({s:Coalesce(r.Reason,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s)),'Тайлбар':With({s:Coalesce(r.Comment,"")},If(Left(s,1) in ["=","+","-","@"],"'" & s,s))}),JSONFormat.Compact),User().Email,"[CSV2] " & varDAttachmentNameV23,varDSummaryV23),Notify("Илгээхэд алдаа: " & FirstError.Message,NotificationType.Error),Notify("Хураангуй болон CSV хавсралтыг илгээлээ.",NotificationType.Success))));Set(varDBusy,false),Set(varDPdfPendingV23,true)))
```

### `ScrDashboard/dExportModal/dExportSend` . **PaddingBottom**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportSend` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
(5)*((App.Height/1136))
```

### `ScrDashboard/dExportModal/dExportSend` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dExportModal/dExportSend` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/dExportModal/dExportSend` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#ED5F1C")
```

### `ScrDashboard/dExportModal/dExportSend` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportSend` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportSend` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportSend` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
18*(If(ScrDashboard.Width>=First(App.SizeBreakpoints).Value,Min(ScrDashboard.Width/1180,ScrDashboard.Height/820),Min(ScrDashboard.Width/366,ScrDashboard.Height/790)))
```

### `ScrDashboard/dExportModal/dExportSend` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
Min(Parent.Width/34,Parent.Height/25)
```

### `ScrDashboard/dExportModal/dExportSend` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Илгээх"
```

### `ScrDashboard/dExportModal/dExportSend` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.56
```

### `ScrDashboard/dExportModal/dExportSend` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0.38
```

### `ScrDashboard/dExportModal/dExportSend` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*0.78
```

### `ScrDashboard/dPdfTimerV23` . **OnTimerStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrDashboard/dPdfTimerV23` . **AutoStart**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ScrDashboard/dPdfTimerV23` . **AutoPause**  _(Timer@2.1.0)_
```powerfx
false
```

### `ScrDashboard/dPdfTimerV23` . **BorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ScrDashboard/dPdfTimerV23` . **BorderThickness**  _(Timer@2.1.0)_
```powerfx
(2)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrDashboard/dPdfTimerV23` . **Color**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrDashboard/dPdfTimerV23` . **DisabledBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 70%)
```

### `ScrDashboard/dPdfTimerV23` . **DisabledColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 90%)
```

### `ScrDashboard/dPdfTimerV23` . **DisabledFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.Fill, 70%)
```

### `ScrDashboard/dPdfTimerV23` . **Duration**  _(Timer@2.1.0)_
```powerfx
500
```

### `ScrDashboard/dPdfTimerV23` . **Fill**  _(Timer@2.1.0)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ScrDashboard/dPdfTimerV23` . **FocusedBorderThickness**  _(Timer@2.1.0)_
```powerfx
(4)*(Min(Min(App.Width,960)/640,App.Height/1136))
```

### `ScrDashboard/dPdfTimerV23` . **Font**  _(Timer@2.1.0)_
```powerfx
Font.'Open Sans'
```

### `ScrDashboard/dPdfTimerV23` . **Height**  _(Timer@2.1.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ScrDashboard/dPdfTimerV23` . **HoverBorderColor**  _(Timer@2.1.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ScrDashboard/dPdfTimerV23` . **HoverColor**  _(Timer@2.1.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ScrDashboard/dPdfTimerV23` . **HoverFill**  _(Timer@2.1.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ScrDashboard/dPdfTimerV23` . **OnTimerEnd**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),IfError(Set(varDPdfFileV23,PDF(ScrDashboard,{Size:"A4",Orientation:If(App.Width>App.Height,"Landscape","Portrait"),ExpandContainers:false}));If(IsBlank(varDPdfFileV23),Error({Kind:ErrorKind.Validation,Message:"PDF файл үүссэнгүй."}),PA_ExportInventoryCSV.Run(JSON(Table({PdfDataUri:Substitute(JSON(varDPdfFileV23,JSONFormat.IncludeBinaryData),Char(34),"")}),JSONFormat.Compact),User().Email,"[PDF] " & varDAttachmentNameV23,varDSummaryV23)),Notify("PDF үүсгэх эсвэл илгээхэд алдаа: " & FirstError.Message,NotificationType.Error),Notify("Хураангуй болон графиктай PDF тайланг илгээлээ.",NotificationType.Success));Set(varDPdfPendingV23,false);Set(varDBusy,false);Set(varDPdfFileV23,Blank())
)
```

### `ScrDashboard/dPdfTimerV23` . **PressedBorderColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPdfTimerV23` . **PressedColor**  _(Timer@2.1.0)_
```powerfx
Self.Fill
```

### `ScrDashboard/dPdfTimerV23` . **PressedFill**  _(Timer@2.1.0)_
```powerfx
Self.Color
```

### `ScrDashboard/dPdfTimerV23` . **Reset**  _(Timer@2.1.0)_
```powerfx
!varRptPdfPending
```

### `ScrDashboard/dPdfTimerV23` . **Size**  _(Timer@2.1.0)_
```powerfx
Max(12,(13)*(Min(Min(App.Width,960)/640,App.Height/1136)))
```

### `ScrDashboard/dPdfTimerV23` . **Start**  _(Timer@2.1.0)_
```powerfx
If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),varDPdfPendingV23
)
```

### `ScrDashboard/dPdfTimerV23` . **Visible**  _(Timer@2.1.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (false)
```

### `ScrDashboard/dPdfTimerV23` . **Width**  _(Timer@2.1.0)_
```powerfx
(1)*((Min(App.Width,960)/640))
```

### `ScrDashboard/dPdfTimerV23` . **X**  _(Timer@2.1.0)_
```powerfx
(0)*((Min(App.Width,960)/640))
```

### `ScrDashboard/dPdfTimerV23` . **Y**  _(Timer@2.1.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ScrDashboard/mobDBody` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*0/360
```

### `ScrDashboard/mobDBody` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*0/700
```

### `ScrDashboard/mobDBody` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*360/360
```

### `ScrDashboard/mobDBody` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*700/700
```

### `ScrDashboard/mobDBody` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDBody` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDBody` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 360 700'><rect x='0' y='0' width='360' height='700' fill='#F5F4F1' stroke='#F5F4F1' rx='0'/><rect x='14' y='58' width='332' height='116' fill='#FFFFFF' stroke='#E5E2DD' rx='15'/><rect x='14' y='188' width='332' height='207' fill='#FFFFFF' stroke='#E5E2DD' rx='15'/><rect x='14' y='408' width='160' height='92' fill='#FFFFFF' stroke='#E5E2DD' rx='15'/><rect x='184' y='408' width='162' height='92' fill='#FFF7E9' stroke='#F3BA77' rx='15'/><rect x='14' y='513' width='332' height='105' fill='#FFFFFF' stroke='#E5E2DD' rx='15'/><rect x='0' y='646' width='360' height='54' fill='#FFFFFF' stroke='#E5E2DD' rx='0'/></svg>")
```

### `ScrDashboard/mobDBody` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrDashboard/mobDTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*16/360
```

### `ScrDashboard/mobDTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*6/700
```

### `ScrDashboard/mobDTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*170/360
```

### `ScrDashboard/mobDTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*47/700
```

### `ScrDashboard/mobDTitle` . **Size**  _(Label@2.5.1)_
```powerfx
23*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Dashboard"
```

### `ScrDashboard/mobDTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDTitle` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDTitle` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDPeriod0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*210/360
```

### `ScrDashboard/mobDPeriod0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*13/700
```

### `ScrDashboard/mobDPeriod0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*62/360
```

### `ScrDashboard/mobDPeriod0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*32/700
```

### `ScrDashboard/mobDPeriod0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDPeriod0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDPeriod0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPeriod="7 хоног",Color.White,ColorValue("#EFEDE9"))
```

### `ScrDashboard/mobDPeriod0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDPeriod0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDPeriod0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDPeriod0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"7 хоног"
```

### `ScrDashboard/mobDPeriod0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"7 хоног");Select(dCalculate)
```

### `ScrDashboard/mobDPeriod0` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDPeriod0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDPeriod1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*275/360
```

### `ScrDashboard/mobDPeriod1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*13/700
```

### `ScrDashboard/mobDPeriod1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*38/360
```

### `ScrDashboard/mobDPeriod1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*32/700
```

### `ScrDashboard/mobDPeriod1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDPeriod1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDPeriod1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(varDPeriod="Сар",Color.White,ColorValue("#EFEDE9"))
```

### `ScrDashboard/mobDPeriod1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDPeriod1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDPeriod1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDPeriod1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Сар"
```

### `ScrDashboard/mobDPeriod1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varDPeriod,"Сар");Select(dCalculate)
```

### `ScrDashboard/mobDPeriod1` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDPeriod1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDMenu` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*318/360
```

### `ScrDashboard/mobDMenu` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*13/700
```

### `ScrDashboard/mobDMenu` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*30/360
```

### `ScrDashboard/mobDMenu` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*32/700
```

### `ScrDashboard/mobDMenu` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
16*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDMenu` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDMenu` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDMenu` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDMenu` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDMenu` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDMenu` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"⋯"
```

### `ScrDashboard/mobDMenu` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobDashboardMenu,!mobDashboardMenu)
```

### `ScrDashboard/mobDMenu` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDMenu` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDMenu` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
"Dashboard үйлдлүүд"
```

### `ScrDashboard/mobDValueTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*30/360
```

### `ScrDashboard/mobDValueTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*73/700
```

### `ScrDashboard/mobDValueTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*302/360
```

### `ScrDashboard/mobDValueTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*23/700
```

### `ScrDashboard/mobDValueTitle` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDValueTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrDashboard/mobDValueTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDValueTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDValueTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Нийт үлдэгдэл · локал үнэлгээ"
```

### `ScrDashboard/mobDValueTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDValueTitle` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDValueTitle` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDValue` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*30/360
```

### `ScrDashboard/mobDValue` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*94/700
```

### `ScrDashboard/mobDValue` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*302/360
```

### `ScrDashboard/mobDValue` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*45/700
```

### `ScrDashboard/mobDValue` . **Size**  _(Label@2.5.1)_
```powerfx
27*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDValue` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDValue` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDValue` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDValue` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())),"—","₮" & Text(If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank()),"#,##0"))
```

### `ScrDashboard/mobDValue` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDValue` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDValue` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDTrend` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*30/360
```

### `ScrDashboard/mobDTrend` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*140/700
```

### `ScrDashboard/mobDTrend` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*302/360
```

### `ScrDashboard/mobDTrend` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*22/700
```

### `ScrDashboard/mobDTrend` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDTrend` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrDashboard/mobDTrend` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDTrend` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDTrend` . **Text**  _(Label@2.5.1)_
```powerfx
With({p:Last(Filter(colDTrend,Day<Date(Year(Today()),Month(Today()),1))).Amount,v:If(varDStockReadyV17,Sum(colDStock,Qty*Cost),Blank())},If(!IsBlank(p) && p<>0 && !IsBlank(v),Text((v-p)/Abs(p)*100,"+0.0;-0.0;0.0") & "% өмнөх сараас",""))
```

### `ScrDashboard/mobDTrend` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDTrend` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDTrend` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDMonthTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*30/360
```

### `ScrDashboard/mobDMonthTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*198/700
```

### `ScrDashboard/mobDMonthTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*184/360
```

### `ScrDashboard/mobDMonthTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*27/700
```

### `ScrDashboard/mobDMonthTitle` . **Size**  _(Label@2.5.1)_
```powerfx
14*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDMonthTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDMonthTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDMonthTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDMonthTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хөдөлгөөн — сараар"
```

### `ScrDashboard/mobDMonthTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDMonthTitle` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDMonthTitle` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDIncome` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*219/360
```

### `ScrDashboard/mobDIncome` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*198/700
```

### `ScrDashboard/mobDIncome` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*53/360
```

### `ScrDashboard/mobDIncome` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*27/700
```

### `ScrDashboard/mobDIncome` . **Size**  _(Label@2.5.1)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDIncome` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDIncome` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDIncome` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDIncome` . **Text**  _(Label@2.5.1)_
```powerfx
"● Орлого"
```

### `ScrDashboard/mobDIncome` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDIncome` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDIncome` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDExpense` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*276/360
```

### `ScrDashboard/mobDExpense` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*198/700
```

### `ScrDashboard/mobDExpense` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*62/360
```

### `ScrDashboard/mobDExpense` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*27/700
```

### `ScrDashboard/mobDExpense` . **Size**  _(Label@2.5.1)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDExpense` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#EF601B")
```

### `ScrDashboard/mobDExpense` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDExpense` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDExpense` . **Text**  _(Label@2.5.1)_
```powerfx
"● Зарлага"
```

### `ScrDashboard/mobDExpense` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDExpense` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDExpense` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDChart` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*26/360
```

### `ScrDashboard/mobDChart` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*231/700
```

### `ScrDashboard/mobDChart` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*308/360
```

### `ScrDashboard/mobDChart` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*152/700
```

### `ScrDashboard/mobDChart` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDChart` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (varDLoaded && !varDIncomplete && Sum(colDMonths,Income+Expense)>0))
```

### `ScrDashboard/mobDChart` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 310 146'>" & Concat(LastN(colDMonths,6) As m,With({x:13+49*(m.Index-First(LastN(colDMonths,6)).Index),a:110*Coalesce(m.Income,0)/Max(1,Max(LastN(colDMonths,6),Max(Income,Expense))),b:110*Coalesce(m.Expense,0)/Max(1,Max(LastN(colDMonths,6),Max(Income,Expense)))},"<rect x='" & Text(x,"0","en-US") & "' y='" & Text(118-a,"0.0","en-US") & "' width='17' height='" & Text(a,"0.0","en-US") & "' rx='3' fill='#202225'/><rect x='" & Text(x+20,"0","en-US") & "' y='" & Text(118-b,"0.0","en-US") & "' width='17' height='" & Text(b,"0.0","en-US") & "' rx='3' fill='#F0601B'/><text x='" & Text(x+18,"0","en-US") & "' y='139' text-anchor='middle' fill='#65605b' font-size='10'>" & Text(m.MonthDate,"m") & "</text>")) & "</svg>")
```

### `ScrDashboard/mobDChart` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrDashboard/mobDRead` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*70/360
```

### `ScrDashboard/mobDRead` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*281/700
```

### `ScrDashboard/mobDRead` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*220/360
```

### `ScrDashboard/mobDRead` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*39/700
```

### `ScrDashboard/mobDRead` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDRead` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDRead` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDRead` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDRead` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDRead` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (!(varDLoaded && !varDIncomplete && Sum(colDMonths,Income+Expense)>0)))
```

### `ScrDashboard/mobDRead` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(varDBusy,"Түр хүлээнэ үү…",varDIncomplete,"BC мөрийн хязгаарт хүрсэн",varDLoaded,"Хөдөлгөөнгүй · шинэчлэх","BC хөдөлгөөн татах")
```

### `ScrDashboard/mobDRead` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(dReadBC)
```

### `ScrDashboard/mobDRead` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDRead` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDAccCaption` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*26/360
```

### `ScrDashboard/mobDAccCaption` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*418/700
```

### `ScrDashboard/mobDAccCaption` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*140/360
```

### `ScrDashboard/mobDAccCaption` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*24/700
```

### `ScrDashboard/mobDAccCaption` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDAccCaption` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrDashboard/mobDAccCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDAccCaption` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDAccCaption` . **Text**  _(Label@2.5.1)_
```powerfx
"Тооллогын нарийвчлал"
```

### `ScrDashboard/mobDAccCaption` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDAccCaption` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDAccCaption` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDAccValue` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*26/360
```

### `ScrDashboard/mobDAccValue` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*442/700
```

### `ScrDashboard/mobDAccValue` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*140/360
```

### `ScrDashboard/mobDAccValue` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*36/700
```

### `ScrDashboard/mobDAccValue` . **Size**  _(Label@2.5.1)_
```powerfx
21*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDAccValue` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDAccValue` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDAccValue` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDAccValue` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(varDAccuracy),"—",Text(varDAccuracy,"0.0") & "%")
```

### `ScrDashboard/mobDAccValue` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDAccValue` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDAccValue` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDAccTrack` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*26/360
```

### `ScrDashboard/mobDAccTrack` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*481/700
```

### `ScrDashboard/mobDAccTrack` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*136/360
```

### `ScrDashboard/mobDAccTrack` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*4/700
```

### `ScrDashboard/mobDAccTrack` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrDashboard/mobDAccTrack` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDAccTrack` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDAccBar` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*26/360
```

### `ScrDashboard/mobDAccBar` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*481/700
```

### `ScrDashboard/mobDAccBar` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*136/360*Min(1,Max(0,Coalesce(varDAccuracy,0)/100))
```

### `ScrDashboard/mobDAccBar` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*4/700
```

### `ScrDashboard/mobDAccBar` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrDashboard/mobDAccBar` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#139D50")
```

### `ScrDashboard/mobDAccBar` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDVarCaption` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*196/360
```

### `ScrDashboard/mobDVarCaption` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*418/700
```

### `ScrDashboard/mobDVarCaption` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*138/360
```

### `ScrDashboard/mobDVarCaption` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*24/700
```

### `ScrDashboard/mobDVarCaption` . **Size**  _(Label@2.5.1)_
```powerfx
11*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDVarCaption` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#95500B")
```

### `ScrDashboard/mobDVarCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDVarCaption` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDVarCaption` . **Text**  _(Label@2.5.1)_
```powerfx
"Зөрүүтэй бараа"
```

### `ScrDashboard/mobDVarCaption` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDVarCaption` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDVarCaption` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDVarCaption` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varDView,"variance")
```

### `ScrDashboard/mobDVarCaption` . **Tooltip**  _(Label@2.5.1)_
```powerfx
"Зөрүүтэй бараа"
```

### `ScrDashboard/mobDVarCount` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*196/360
```

### `ScrDashboard/mobDVarCount` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*442/700
```

### `ScrDashboard/mobDVarCount` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*138/360
```

### `ScrDashboard/mobDVarCount` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*40/700
```

### `ScrDashboard/mobDVarCount` . **Size**  _(Label@2.5.1)_
```powerfx
22*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDVarCount` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDVarCount` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDVarCount` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDVarCount` . **Text**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colDVariance),"#,##0")
```

### `ScrDashboard/mobDVarCount` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDVarCount` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDVarCount` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDVarCount` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Set(varDView,"variance")
```

### `ScrDashboard/mobDVarCount` . **Tooltip**  _(Label@2.5.1)_
```powerfx
Text(CountRows(colDVariance),"#,##0")
```

### `ScrDashboard/mobDTopTitle` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrDashboard/mobDTopTitle` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*520/700
```

### `ScrDashboard/mobDTopTitle` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*308/360
```

### `ScrDashboard/mobDTopTitle` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*27/700
```

### `ScrDashboard/mobDTopTitle` . **Size**  _(Label@2.5.1)_
```powerfx
14*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDTopTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDTopTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDTopTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23)
```

### `ScrDashboard/mobDTopTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Зарлага · өртгөөр эрэмбэлсэн"
```

### `ScrDashboard/mobDTopTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDTopTitle` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDTopTitle` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDTopName0` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrDashboard/mobDTopName0` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*550/700
```

### `ScrDashboard/mobDTopName0` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*207/360
```

### `ScrDashboard/mobDTopName0` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*26/700
```

### `ScrDashboard/mobDTopName0` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDTopName0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDTopName0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDTopName0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (CountRows(colDTop)>0))
```

### `ScrDashboard/mobDTopName0` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colDTop,1))},Coalesce(LookUp(colOfflineItems,number=r.ItemNo,displayName),r.ItemNo))
```

### `ScrDashboard/mobDTopName0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDTopName0` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDTopName0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDTopAmount0` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*236/360
```

### `ScrDashboard/mobDTopAmount0` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*550/700
```

### `ScrDashboard/mobDTopAmount0` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*94/360
```

### `ScrDashboard/mobDTopAmount0` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*26/700
```

### `ScrDashboard/mobDTopAmount0` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDTopAmount0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDTopAmount0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDTopAmount0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (CountRows(colDTop)>0))
```

### `ScrDashboard/mobDTopAmount0` . **Text**  _(Label@2.5.1)_
```powerfx
"₮" & Text(Last(FirstN(colDTop,1)).Amount,"#,##0")
```

### `ScrDashboard/mobDTopAmount0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDTopAmount0` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrDashboard/mobDTopAmount0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDTopName1` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrDashboard/mobDTopName1` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*579/700
```

### `ScrDashboard/mobDTopName1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*207/360
```

### `ScrDashboard/mobDTopName1` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*26/700
```

### `ScrDashboard/mobDTopName1` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDTopName1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDTopName1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDTopName1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (CountRows(colDTop)>1))
```

### `ScrDashboard/mobDTopName1` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(colDTop,2))},Coalesce(LookUp(colOfflineItems,number=r.ItemNo,displayName),r.ItemNo))
```

### `ScrDashboard/mobDTopName1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDTopName1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDTopName1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDTopAmount1` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*236/360
```

### `ScrDashboard/mobDTopAmount1` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*579/700
```

### `ScrDashboard/mobDTopAmount1` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*94/360
```

### `ScrDashboard/mobDTopAmount1` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*26/700
```

### `ScrDashboard/mobDTopAmount1` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDTopAmount1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDTopAmount1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDTopAmount1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (CountRows(colDTop)>1))
```

### `ScrDashboard/mobDTopAmount1` . **Text**  _(Label@2.5.1)_
```powerfx
"₮" & Text(Last(FirstN(colDTop,2)).Amount,"#,##0")
```

### `ScrDashboard/mobDTopAmount1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDTopAmount1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrDashboard/mobDTopAmount1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDNoTop` . **X**  _(Label@2.5.1)_
```powerfx
Parent.Width*28/360
```

### `ScrDashboard/mobDNoTop` . **Y**  _(Label@2.5.1)_
```powerfx
Parent.Height*550/700
```

### `ScrDashboard/mobDNoTop` . **Width**  _(Label@2.5.1)_
```powerfx
Parent.Width*298/360
```

### `ScrDashboard/mobDNoTop` . **Height**  _(Label@2.5.1)_
```powerfx
Parent.Height*42/700
```

### `ScrDashboard/mobDNoTop` . **Size**  _(Label@2.5.1)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDNoTop` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#635F59")
```

### `ScrDashboard/mobDNoTop` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNoTop` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (IsEmpty(colDTop)))
```

### `ScrDashboard/mobDNoTop` . **Text**  _(Label@2.5.1)_
```powerfx
"Сонгосон хугацаанд зарлагын дүн алга"
```

### `ScrDashboard/mobDNoTop` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrDashboard/mobDNoTop` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrDashboard/mobDNoTop` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrDashboard/mobDNavArt0` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*25/360
```

### `ScrDashboard/mobDNavArt0` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*654/700
```

### `ScrDashboard/mobDNavArt0` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*22/360
```

### `ScrDashboard/mobDNavArt0` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*20/700
```

### `ScrDashboard/mobDNavArt0` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavArt0` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|home|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavArt0` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M3 11l9-8 9 8v10h-6v-6H9v6H3z' fill='none' stroke='#635F59' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.6'/></svg>")
```

### `ScrDashboard/mobDNavArt0` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrDashboard/mobDNavHit0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*0/360
```

### `ScrDashboard/mobDNavHit0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*643/700
```

### `ScrDashboard/mobDNavHit0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*72/360
```

### `ScrDashboard/mobDNavHit0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*57/700
```

### `ScrDashboard/mobDNavHit0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDNavHit0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDNavHit0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|home|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavHit0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Нүүр"
```

### `ScrDashboard/mobDNavHit0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate('нүүр')
```

### `ScrDashboard/mobDNavHit0` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*30/700
```

### `ScrDashboard/mobDNavArt1` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*97/360
```

### `ScrDashboard/mobDNavArt1` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*654/700
```

### `ScrDashboard/mobDNavArt1` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*22/360
```

### `ScrDashboard/mobDNavArt1` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*20/700
```

### `ScrDashboard/mobDNavArt1` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavArt1` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavArt1` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M3 9l9-6 9 6v12H3z M6 12h12 M6 16h12' fill='none' stroke='#635F59' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.6'/></svg>")
```

### `ScrDashboard/mobDNavArt1` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrDashboard/mobDNavHit1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*72/360
```

### `ScrDashboard/mobDNavHit1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*643/700
```

### `ScrDashboard/mobDNavHit1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*72/360
```

### `ScrDashboard/mobDNavHit1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*57/700
```

### `ScrDashboard/mobDNavHit1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDNavHit1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDNavHit1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|stock|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavHit1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулах"
```

### `ScrDashboard/mobDNavHit1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(Screen1)
```

### `ScrDashboard/mobDNavHit1` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*30/700
```

### `ScrDashboard/mobDScanTile` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*156/360
```

### `ScrDashboard/mobDScanTile` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*631/700
```

### `ScrDashboard/mobDScanTile` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*48/360
```

### `ScrDashboard/mobDScanTile` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*46/700
```

### `ScrDashboard/mobDScanTile` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDScanTile` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDScanTile` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EF601B")
```

### `ScrDashboard/mobDScanTile` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDScanTile` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDScanTile` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDScanTile` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(scrWarehouses)
```

### `ScrDashboard/mobDScanTile` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDScanTile` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDNavArt2` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*169/360
```

### `ScrDashboard/mobDNavArt2` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*646/700
```

### `ScrDashboard/mobDNavArt2` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*22/360
```

### `ScrDashboard/mobDNavArt2` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*20/700
```

### `ScrDashboard/mobDNavArt2` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavArt2` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavArt2` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M3 8V3h5 M16 3h5v5 M21 16v5h-5 M8 21H3v-5 M9 8v8 M13 7v10 M16 8v8' fill='none' stroke='#FFFFFF' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.6'/></svg>")
```

### `ScrDashboard/mobDNavArt2` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrDashboard/mobDNavHit2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*144/360
```

### `ScrDashboard/mobDNavHit2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*643/700
```

### `ScrDashboard/mobDNavHit2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*72/360
```

### `ScrDashboard/mobDNavHit2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*57/700
```

### `ScrDashboard/mobDNavHit2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDNavHit2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDNavHit2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavHit2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Scan"
```

### `ScrDashboard/mobDNavHit2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Navigate(scrWarehouses)
```

### `ScrDashboard/mobDNavHit2` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*30/700
```

### `ScrDashboard/mobDNavArt3` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*241/360
```

### `ScrDashboard/mobDNavArt3` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*654/700
```

### `ScrDashboard/mobDNavArt3` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*22/360
```

### `ScrDashboard/mobDNavArt3` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*20/700
```

### `ScrDashboard/mobDNavArt3` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavArt3` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavArt3` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M3 4v17h18 M8 16v-6 M13 16V6 M18 16v-9' fill='none' stroke='#EF601B' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.6'/></svg>")
```

### `ScrDashboard/mobDNavArt3` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrDashboard/mobDNavHit3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*216/360
```

### `ScrDashboard/mobDNavHit3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*643/700
```

### `ScrDashboard/mobDNavHit3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*72/360
```

### `ScrDashboard/mobDNavHit3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*57/700
```

### `ScrDashboard/mobDNavHit3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDNavHit3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EF601B")
```

### `ScrDashboard/mobDNavHit3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && ((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))))
```

### `ScrDashboard/mobDNavHit3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Dashboard"
```

### `ScrDashboard/mobDNavHit3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
false
```

### `ScrDashboard/mobDNavHit3` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*30/700
```

### `ScrDashboard/mobDNavArt4` . **X**  _(Image@2.2.3)_
```powerfx
Parent.Width*313/360
```

### `ScrDashboard/mobDNavArt4` . **Y**  _(Image@2.2.3)_
```powerfx
Parent.Height*654/700
```

### `ScrDashboard/mobDNavArt4` . **Width**  _(Image@2.2.3)_
```powerfx
Parent.Width*22/360
```

### `ScrDashboard/mobDNavArt4` . **Height**  _(Image@2.2.3)_
```powerfx
Parent.Height*20/700
```

### `ScrDashboard/mobDNavArt4` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavArt4` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (true))
```

### `ScrDashboard/mobDNavArt4` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M8 8a4 4 0 1 0 8 0a4 4 0 1 0-8 0 M4 21a8 8 0 0 1 16 0' fill='none' stroke='#635F59' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.6'/></svg>")
```

### `ScrDashboard/mobDNavArt4` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrDashboard/mobDNavHit4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*288/360
```

### `ScrDashboard/mobDNavHit4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*643/700
```

### `ScrDashboard/mobDNavHit4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*72/360
```

### `ScrDashboard/mobDNavHit4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*57/700
```

### `ScrDashboard/mobDNavHit4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
10*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDNavHit4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDNavHit4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrDashboard/mobDNavHit4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (true))
```

### `ScrDashboard/mobDNavHit4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Би"
```

### `ScrDashboard/mobDNavHit4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess)
```

### `ScrDashboard/mobDNavHit4` . **PaddingTop**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*30/700
```

### `ScrDashboard/mobDOption0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*155/360
```

### `ScrDashboard/mobDOption0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*50/700
```

### `ScrDashboard/mobDOption0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*193/360
```

### `ScrDashboard/mobDOption0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*41/700
```

### `ScrDashboard/mobDOption0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDOption0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDOption0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDOption0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDOption0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDOption0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (mobDashboardMenu))
```

### `ScrDashboard/mobDOption0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"BC шинэчлэх"
```

### `ScrDashboard/mobDOption0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobDashboardMenu,false);Select(dReadBC)
```

### `ScrDashboard/mobDOption0` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDOption0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDOption1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*155/360
```

### `ScrDashboard/mobDOption1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*92/700
```

### `ScrDashboard/mobDOption1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*193/360
```

### `ScrDashboard/mobDOption1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*41/700
```

### `ScrDashboard/mobDOption1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDOption1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDOption1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDOption1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDOption1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDOption1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (mobDashboardMenu))
```

### `ScrDashboard/mobDOption1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Үнэлгээ хадгалах"
```

### `ScrDashboard/mobDOption1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobDashboardMenu,false);Select(dCapture)
```

### `ScrDashboard/mobDOption1` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDOption1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDOption2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*155/360
```

### `ScrDashboard/mobDOption2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*134/700
```

### `ScrDashboard/mobDOption2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*193/360
```

### `ScrDashboard/mobDOption2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*41/700
```

### `ScrDashboard/mobDOption2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDOption2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDOption2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDOption2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDOption2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDOption2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (mobDashboardMenu))
```

### `ScrDashboard/mobDOption2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Агуулахын хөдөлгөөн"
```

### `ScrDashboard/mobDOption2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobDashboardMenu,false);Set(varDView,"warehouse")
```

### `ScrDashboard/mobDOption2` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDOption2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDOption3` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*155/360
```

### `ScrDashboard/mobDOption3` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*176/700
```

### `ScrDashboard/mobDOption3` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*193/360
```

### `ScrDashboard/mobDOption3` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*41/700
```

### `ScrDashboard/mobDOption3` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDOption3` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDOption3` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDOption3` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDOption3` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDOption3` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (mobDashboardMenu))
```

### `ScrDashboard/mobDOption3` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"PDF · мэйл"
```

### `ScrDashboard/mobDOption3` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobDashboardMenu,false);Set(varDExport,true);Set(varDExportKind,If(varDView="variance","CSV","PDF"))
```

### `ScrDashboard/mobDOption3` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDOption3` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/mobDOption4` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*155/360
```

### `ScrDashboard/mobDOption4` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*218/700
```

### `ScrDashboard/mobDOption4` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Width*193/360
```

### `ScrDashboard/mobDOption4` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
Parent.Height*41/700
```

### `ScrDashboard/mobDOption4` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*Min(App.Width/360,App.Height/700)
```

### `ScrDashboard/mobDOption4` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1F2124")
```

### `ScrDashboard/mobDOption4` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFFFFF")
```

### `ScrDashboard/mobDOption4` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/mobDOption4` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/mobDOption4` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && ((App.Width<First(App.SizeBreakpoints).Value && varDView="overview" && !varDExport && !varDPdfPendingV23) && (mobDashboardMenu))
```

### `ScrDashboard/mobDOption4` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Өнөөдөр"
```

### `ScrDashboard/mobDOption4` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(mobDashboardMenu,false);Set(varDPeriod,"Live");Select(dCalculate)
```

### `ScrDashboard/mobDOption4` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrDashboard/mobDOption4` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E5E2DD")
```

### `ScrDashboard/pgDenied751` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrDashboard/pgDenied751` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrDashboard/pgDenied751` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrDashboard/pgDenied751` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrDashboard/pgDenied751` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrDashboard/pgDenied751` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrDashboard/pgDenied751` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrDashboard/pgDenied751` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrDashboard/pgDenied751` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|dashboard|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ScrDashboard/pgDenied751` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

