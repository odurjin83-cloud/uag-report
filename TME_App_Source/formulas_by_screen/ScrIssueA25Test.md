# ScrIssueA25Test — Power Fx formulas

### `ScrIssueA25Test` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title)),Set(issueDiscardPrompt,false);If(!(!IsBlank(a25Request) && (IsBlank(a25Document) || Coalesce(issueResumeReceipt,false)) && issueRequestOwner=Lower(User().Email)),Set(issueConfirm,false);Set(issueSubmissionMessage,"");Set(issuePartialDocument,Blank());Set(issueDraftMissing,false);Set(issueLookupMessage,"");Set(issueHasSearched,false);Set(issueSignedIn,false);Set(issueChoiceCode,"");Set(issueSearchPayload,"[]");ClearCollect(a25Matches,{code:"",fullName:"",division:"",dept:"",job:"",norm:""});Clear(a25Matches);If(!Coalesce(issueRecentReady,false),ClearCollect(issueRecent,{code:"",fullName:"",division:"",dept:"",job:"",norm:""});Clear(issueRecent);Set(issueRecentReady,true));ClearCollect(a25Stock,{number:"",displayName:"",blocked:false});Clear(a25Stock);ClearCollect(a25NormLines,{number:"",lifeTime:"",norm:""});Clear(a25NormLines);ClearCollect(a25Cart,{itemNo:"",title:"",quantity:1,norm:"",lifeTime:""});Set(a25Selected,{code:"",fullName:"",division:"",dept:"",job:"",norm:""});Set(a25Review,false);Clear(a25Cart);Set(a25ItemIndex,1);Set(a25CartIndex,1);Set(a25Request,Blank());Set(a25Document,Blank());Set(a25Index,1);Set(a25Busy,false);Reset(A25Query));Set(issueResumeReceipt,false)
)
```

### `ScrIssueA25Test` . **Fill**  _(Screen)_
```powerfx
ColorValue("#F5F4F1")
```

### `ScrIssueA25Test` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ScrIssueA25Test` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ScrIssueA25Test/cartFooterBand` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrIssueA25Test/cartFooterBand` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,650*Parent.Height/720,605*Parent.Height/680)
```

### `ScrIssueA25Test/cartFooterBand` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,360*Parent.Width/360,1100*Parent.Width/1100)
```

### `ScrIssueA25Test/cartFooterBand` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,70*Parent.Height/720,75*Parent.Height/680)
```

### `ScrIssueA25Test/cartFooterBand` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrIssueA25Test/cartFooterBand` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartFooterBand` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/cartFooterBand` . **BorderColor**  _(Label@2.5.1)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartHeaderBand` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrIssueA25Test/cartHeaderBand` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,0*Parent.Height/680)
```

### `ScrIssueA25Test/cartHeaderBand` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,360*Parent.Width/360,1100*Parent.Width/1100)
```

### `ScrIssueA25Test/cartHeaderBand` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,60*Parent.Height/720,62*Parent.Height/680)
```

### `ScrIssueA25Test/cartHeaderBand` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrIssueA25Test/cartHeaderBand` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartHeaderBand` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/cartHeaderBand` . **BorderColor**  _(Label@2.5.1)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/issuePickerHeader` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrIssueA25Test/issuePickerHeader` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,0*Parent.Height/680)
```

### `ScrIssueA25Test/issuePickerHeader` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,360*Parent.Width/360,1100*Parent.Width/1100)
```

### `ScrIssueA25Test/issuePickerHeader` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,60*Parent.Height/720,62*Parent.Height/680)
```

### `ScrIssueA25Test/issuePickerHeader` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issuePickerHeader` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issuePickerHeader` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issuePickerTrack` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrIssueA25Test/issuePickerTrack` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,60*Parent.Height/720,62*Parent.Height/680)
```

### `ScrIssueA25Test/issuePickerTrack` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,360*Parent.Width/360,1100*Parent.Width/1100)
```

### `ScrIssueA25Test/issuePickerTrack` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/720,49*Parent.Height/680)
```

### `ScrIssueA25Test/issuePickerTrack` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issuePickerTrack` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issuePickerTrack` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issuePickerFooter` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrIssueA25Test/issuePickerFooter` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,650*Parent.Height/720,605*Parent.Height/680)
```

### `ScrIssueA25Test/issuePickerFooter` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,360*Parent.Width/360,1100*Parent.Width/1100)
```

### `ScrIssueA25Test/issuePickerFooter` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,70*Parent.Height/720,75*Parent.Height/680)
```

### `ScrIssueA25Test/issuePickerFooter` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issuePickerFooter` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issuePickerFooter` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/A25Back` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
DisplayMode.Edit
```

### `ScrIssueA25Test/A25Back` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/A25Back` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/A25Back` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,281*Parent.Width/360,980*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Back` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Height/720,12*Parent.Height/680)
```

### `ScrIssueA25Test/A25Back` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,66*Parent.Width/360,95*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Back` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,34*Parent.Height/720,38*Parent.Height/680)
```

### `ScrIssueA25Test/A25Back` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Back` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/A25Back` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Back` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Back` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Back` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Back` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Back` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Гарах"
```

### `ScrIssueA25Test/A25Back` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueResumeReceipt,!IsBlank(a25Request) && IsBlank(a25Document));Set(issueDiscardPrompt,false);If(!Back(),Navigate(ScrPageMenu,ScreenTransition.None))
```

### `ScrIssueA25Test/A25Title` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/A25Title` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Title` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/A25Title` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/A25Title` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Title` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,0*Parent.Height/680)
```

### `ScrIssueA25Test/A25Title` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,156*Parent.Width/360,655*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Title` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,60*Parent.Height/720,62*Parent.Height/680)
```

### `ScrIssueA25Test/A25Title` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14,18)*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Title` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Title` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/A25Title` . **Text**  _(Label@2.5.1)_
```powerfx
"Хувцас олголт"
```

### `ScrIssueA25Test/A25Query` . **RadiusBottomRight**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Query` . **RadiusBottomLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Query` . **RadiusTopRight**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Query` . **RadiusTopLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Query` . **DisplayMode**  _(Classic/TextInput@2.3.2)_
```powerfx
If(a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/A25Query` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,588*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Query` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,153*Parent.Height/720,127*Parent.Height/680)
```

### `ScrIssueA25Test/A25Query` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,235*Parent.Width/360,367*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Query` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,44*Parent.Height/720,43*Parent.Height/680)
```

### `ScrIssueA25Test/A25Query` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Parent.Width/360,Parent.Height/720),15*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Query` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#202225")
```

### `ScrIssueA25Test/A25Query` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Query` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/A25Query` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Query` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Нэр эсвэл ажилтны код…"
```

### `ScrIssueA25Test/A25Query` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
Set(issueLookupMessage,"");Set(issueHasSearched,false);Set(issueChoiceCode,"");Set(a25Index,1);Clear(a25Matches);Set(issueSearchPayload,"[]")
```

### `ScrIssueA25Test/A25Query` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && (IsBlank(a25Selected.code) && (true)))
```

### `ScrIssueA25Test/A25Search` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Search` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Search` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Search` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Search` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,260*Parent.Width/360,967*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Search` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,153*Parent.Height/720,127*Parent.Height/680)
```

### `ScrIssueA25Test/A25Search` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,84*Parent.Width/360,109*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Search` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,44*Parent.Height/720,43*Parent.Height/680)
```

### `ScrIssueA25Test/A25Search` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Search` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Search` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Search` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/A25Search` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Search` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Search` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Search` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хайх"
```

### `ScrIssueA25Test/A25Search` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Len(Trim(A25Query.Text))>=2 && !Coalesce(a25Busy,false),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrIssueA25Test/A25Search` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueHasSearched,true);If(!a25Busy && Len(Trim(A25Query.Text))>=2,Set(a25Busy,true);Set(issueLookupMessage,"");Set(issueChoiceCode,"");Clear(a25Matches);Set(a25Index,1);Set(issueSearchPayload,"[]");IfError(With({payload:TMEIssueA25Test.Run(JSON({mode:"search",query:Trim(A25Query.Text)})).itemsjson},If(StartsWith(Trim(payload),"["),With({matches:ForAll(Table(ParseJSON(payload)) As e,{code:Text(e.Value.No),fullName:Trim(Text(e.Value.First_Name) & " " & Text(e.Value.Last_Name)),division:Text(e.Value.Division_Name),dept:Text(e.Value.Department_Name),job:Text(e.Value.Position_Name),norm:Text(e.Value.norm)})},ClearCollect(a25Matches,matches);Set(issueSearchPayload,payload);true),Set(issueLookupMessage,"Ажилтны жагсаалтыг уншиж чадсангүй. Холболтоо шалгаад дахин хайна уу.");false)),Set(issueLookupMessage,"Ажилтны жагсаалтыг уншиж чадсангүй. Холболтоо шалгаад дахин хайна уу.");false);Set(a25Busy,false))
```

### `ScrIssueA25Test/A25Search` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && (IsBlank(a25Selected.code) && (true)))
```

### `ScrIssueA25Test/A25Match0` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match0` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match0` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match0` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0)).code=issueChoiceCode,ColorValue("#EE5F1F"),ColorValue("#E4E1DC")),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/A25Match0` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0))},p.code & ", " & p.fullName & ", " & p.dept & ", " & p.job),"")
```

### `ScrIssueA25Test/A25Match0` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/A25Match0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Match0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,233*Parent.Height/720,219*Parent.Height/680)
```

### `ScrIssueA25Test/A25Match0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,520*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Match0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,82*Parent.Height/720,139*Parent.Height/680)
```

### `ScrIssueA25Test/A25Match0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrIssueA25Test/A25Match0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0)).code=issueChoiceCode,ColorValue("#FFF1E8"),Color.White),Color.White)
```

### `ScrIssueA25Test/A25Match0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/A25Match0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/A25Match0` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Match0` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Match0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0)
```

### `ScrIssueA25Test/A25Match0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!a25Busy && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,Set(issueLookupMessage,"");Set(issueChoiceCode,Text(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0)).code)))
```

### `ScrIssueA25Test/A25Match1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1)).code=issueChoiceCode,ColorValue("#EE5F1F"),ColorValue("#E4E1DC")),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/A25Match1` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1))},p.code & ", " & p.fullName & ", " & p.dept & ", " & p.job),"")
```

### `ScrIssueA25Test/A25Match1` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/A25Match1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,556*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Match1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,321*Parent.Height/720,219*Parent.Height/680)
```

### `ScrIssueA25Test/A25Match1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,520*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Match1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,82*Parent.Height/720,139*Parent.Height/680)
```

### `ScrIssueA25Test/A25Match1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrIssueA25Test/A25Match1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1)).code=issueChoiceCode,ColorValue("#FFF1E8"),Color.White),Color.White)
```

### `ScrIssueA25Test/A25Match1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/A25Match1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/A25Match1` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Match1` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Match1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1)
```

### `ScrIssueA25Test/A25Match1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!a25Busy && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,Set(issueLookupMessage,"");Set(issueChoiceCode,Text(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1)).code)))
```

### `ScrIssueA25Test/A25Match2` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match2` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match2` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match2` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Match2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2)).code=issueChoiceCode,ColorValue("#EE5F1F"),ColorValue("#E4E1DC")),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/A25Match2` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2))},p.code & ", " & p.fullName & ", " & p.dept & ", " & p.job),"")
```

### `ScrIssueA25Test/A25Match2` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/A25Match2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Match2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,409*Parent.Height/720,370*Parent.Height/680)
```

### `ScrIssueA25Test/A25Match2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,520*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Match2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,82*Parent.Height/720,139*Parent.Height/680)
```

### `ScrIssueA25Test/A25Match2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrIssueA25Test/A25Match2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2)).code=issueChoiceCode,ColorValue("#FFF1E8"),Color.White),Color.White)
```

### `ScrIssueA25Test/A25Match2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/A25Match2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/A25Match2` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Match2` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Match2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2)
```

### `ScrIssueA25Test/A25Match2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!a25Busy && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,Set(issueLookupMessage,"");Set(issueChoiceCode,Text(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2)).code)))
```

### `ScrIssueA25Test/A25Next` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),10*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Next` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),10*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Next` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),10*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Next` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),10*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Next` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Next` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,595*Parent.Height/720,537*Parent.Height/680)
```

### `ScrIssueA25Test/A25Next` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,186*Parent.Width/360,212*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Next` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,41*Parent.Height/720,44*Parent.Height/680)
```

### `ScrIssueA25Test/A25Next` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/A25Next` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Next` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Next` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Next` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Next` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Next` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Next` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн ажилтнууд  ›"
```

### `ScrIssueA25Test/A25Next` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>4)
```

### `ScrIssueA25Test/A25Next` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(a25Index,If(Coalesce(a25Index,1)+4>CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches)),1,Coalesce(a25Index,1)+4))
```

### `ScrIssueA25Test/A25Employee` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/A25Employee` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Employee` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,108*Parent.Height/720,119*Parent.Height/680)
```

### `ScrIssueA25Test/A25Employee` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,785*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Employee` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,46*Parent.Height/720,49*Parent.Height/680)
```

### `ScrIssueA25Test/A25Employee` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Employee` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Employee` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/A25Employee` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/A25Employee` . **Text**  _(Label@2.5.1)_
```powerfx
a25Selected.fullName & "   ·   " & a25Selected.code & If(App.Width<First(App.SizeBreakpoints).Value,"",Char(10) & Concat(Filter(Table({t:a25Selected.division},{t:a25Selected.dept},{t:a25Selected.job}),!IsBlank(t)),t," · "))
```

### `ScrIssueA25Test/A25Change` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/A25Change` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,234*Parent.Width/360,877*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Change` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,157*Parent.Height/720,122*Parent.Height/680)
```

### `ScrIssueA25Test/A25Change` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,110*Parent.Width/360,196*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Change` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,31*Parent.Height/720,37*Parent.Height/680)
```

### `ScrIssueA25Test/A25Change` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Change` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/A25Change` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Change` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Change` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Change` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Change` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Change` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document))
```

### `ScrIssueA25Test/A25Change` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(Coalesce(a25Busy,false),DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/A25Change` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Ажилтан солих"
```

### `ScrIssueA25Test/A25Change` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueConfirm,false);Set(issueSubmissionMessage,"");Set(a25Selected,Blank()); Set(a25Review,false); Clear(a25Cart); Set(a25ItemIndex,1); Set(a25Request,Blank()); Set(a25Document,Blank());Set(issueConfirm,false);Set(issueSubmissionMessage,"")
```

### `ScrIssueA25Test/A25ItemQuery` . **DelayOutput**  _(Classic/TextInput@2.3.2)_
```powerfx
false
```

### `ScrIssueA25Test/A25ItemQuery` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25ItemQuery` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,201*Parent.Height/720,226*Parent.Height/680)
```

### `ScrIssueA25Test/A25ItemQuery` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,656*Parent.Width/1100)
```

### `ScrIssueA25Test/A25ItemQuery` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,43*Parent.Height/720,43*Parent.Height/680)
```

### `ScrIssueA25Test/A25ItemQuery` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25ItemQuery` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25ItemQuery` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25ItemQuery` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/A25ItemQuery` . **PaddingLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Width/360,14*Parent.Width/1100)
```

### `ScrIssueA25Test/A25ItemQuery` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document))
```

### `ScrIssueA25Test/A25ItemQuery` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Хувцасны нэр эсвэл барааны код"
```

### `ScrIssueA25Test/A25ItemQuery` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
Set(a25ItemIndex,1)
```

### `ScrIssueA25Test/A25Item0` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/A25Item0` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,8*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item0` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Parent.Width/360,17*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item0` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0)).number in a25Cart.itemNo,false),ColorValue("#EE5F1F"),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/A25Item0` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/A25Item0` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/A25Item0` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item0` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,256*Parent.Height/720,285*Parent.Height/680)
```

### `ScrIssueA25Test/A25Item0` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,321*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item0` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,68*Parent.Height/720,101*Parent.Height/680)
```

### `ScrIssueA25Test/A25Item0` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Item0` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Item0` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0)).number in a25Cart.itemNo,false),ColorValue("#FFF1E8"),Color.White)
```

### `ScrIssueA25Test/A25Item0` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Item0` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Item0` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Item0` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Item0` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0)
```

### `ScrIssueA25Test/A25Item0` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0))},i.displayName & Char(10) & i.number & "   ·   " & If(i.blocked,"BC-д хаалттай",With({m:LookUp(a25NormLines,number=i.number,lifeTime)},If(IsBlank(m),"Хугацааг гараар оруулна","А/25 · " & Substitute(m,"M"," сар")))) & If(i.number in a25Cart.itemNo,"   ✓","")),"")
```

### `ScrIssueA25Test/A25Item0` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+0))},If(i.blocked,Notify("BC-д хаалттай бараа",NotificationType.Warning),If(IsBlank(LookUp(a25Cart,itemNo=i.number)),With({r:LookUp(a25NormLines,number=i.number)},Collect(a25Cart,{itemNo:i.number,title:i.displayName,quantity:1,norm:Coalesce(r.norm,""),lifeTime:Coalesce(r.lifeTime,"")}));Set(a25Request,Blank())))))
```

### `ScrIssueA25Test/A25Item1` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/A25Item1` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,8*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item1` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Parent.Width/360,17*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1)).number in a25Cart.itemNo,false),ColorValue("#EE5F1F"),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/A25Item1` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/A25Item1` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/A25Item1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,361*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,334*Parent.Height/720,285*Parent.Height/680)
```

### `ScrIssueA25Test/A25Item1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,321*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,68*Parent.Height/720,101*Parent.Height/680)
```

### `ScrIssueA25Test/A25Item1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Item1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Item1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1)).number in a25Cart.itemNo,false),ColorValue("#FFF1E8"),Color.White)
```

### `ScrIssueA25Test/A25Item1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Item1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Item1` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Item1` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Item1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1)
```

### `ScrIssueA25Test/A25Item1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1))},i.displayName & Char(10) & i.number & "   ·   " & If(i.blocked,"BC-д хаалттай",With({m:LookUp(a25NormLines,number=i.number,lifeTime)},If(IsBlank(m),"Хугацааг гараар оруулна","А/25 · " & Substitute(m,"M"," сар")))) & If(i.number in a25Cart.itemNo,"   ✓","")),"")
```

### `ScrIssueA25Test/A25Item1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+1))},If(i.blocked,Notify("BC-д хаалттай бараа",NotificationType.Warning),If(IsBlank(LookUp(a25Cart,itemNo=i.number)),With({r:LookUp(a25NormLines,number=i.number)},Collect(a25Cart,{itemNo:i.number,title:i.displayName,quantity:1,norm:Coalesce(r.norm,""),lifeTime:Coalesce(r.lifeTime,"")}));Set(a25Request,Blank())))))
```

### `ScrIssueA25Test/A25Item2` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/A25Item2` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,8*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item2` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Parent.Width/360,17*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item2` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2)).number in a25Cart.itemNo,false),ColorValue("#EE5F1F"),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/A25Item2` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/A25Item2` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/A25Item2` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item2` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,412*Parent.Height/720,399*Parent.Height/680)
```

### `ScrIssueA25Test/A25Item2` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,321*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Item2` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,68*Parent.Height/720,101*Parent.Height/680)
```

### `ScrIssueA25Test/A25Item2` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Item2` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Item2` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2)).number in a25Cart.itemNo,false),ColorValue("#FFF1E8"),Color.White)
```

### `ScrIssueA25Test/A25Item2` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Item2` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Item2` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Item2` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Item2` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2)
```

### `ScrIssueA25Test/A25Item2` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2))},i.displayName & Char(10) & i.number & "   ·   " & If(i.blocked,"BC-д хаалттай",With({m:LookUp(a25NormLines,number=i.number,lifeTime)},If(IsBlank(m),"Хугацааг гараар оруулна","А/25 · " & Substitute(m,"M"," сар")))) & If(i.number in a25Cart.itemNo,"   ✓","")),"")
```

### `ScrIssueA25Test/A25Item2` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+2))},If(i.blocked,Notify("BC-д хаалттай бараа",NotificationType.Warning),If(IsBlank(LookUp(a25Cart,itemNo=i.number)),With({r:LookUp(a25NormLines,number=i.number)},Collect(a25Cart,{itemNo:i.number,title:i.displayName,quantity:1,norm:Coalesce(r.norm,""),lifeTime:Coalesce(r.lifeTime,"")}));Set(a25Request,Blank())))))
```

### `ScrIssueA25Test/A25NoItems` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/A25NoItems` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,25*Parent.Width/1100)
```

### `ScrIssueA25Test/A25NoItems` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,275*Parent.Height/720,302*Parent.Height/680)
```

### `ScrIssueA25Test/A25NoItems` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,653*Parent.Width/1100)
```

### `ScrIssueA25Test/A25NoItems` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,56*Parent.Height/720,58*Parent.Height/680)
```

### `ScrIssueA25Test/A25NoItems` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25NoItems` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/A25NoItems` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))=0)
```

### `ScrIssueA25Test/A25NoItems` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsEmpty(a25Stock),"Бүлэгт бараа олдсонгүй.","Ийм нэр, кодтой хувцас олдсонгүй")
```

### `ScrIssueA25Test/A25Other` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Other` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,578*Parent.Height/720,525*Parent.Height/680)
```

### `ScrIssueA25Test/A25Other` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,656*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Other` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,42*Parent.Height/720,40*Parent.Height/680)
```

### `ScrIssueA25Test/A25Other` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Other` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Other` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Other` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Other` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Other` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Other` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Other` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>4)
```

### `ScrIssueA25Test/A25Other` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн бараа  →     " & RoundUp(If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)/4,0) & " / " & RoundUp(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))/4,0)
```

### `ScrIssueA25Test/A25Other` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
With({firstRow:If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1),filterKey:("catalog|" & Lower(Trim(A25ItemQuery.Text)))},Set(a25ItemIndex,If(firstRow+4>CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),1,firstRow+4));Set(issuePagedCatalogQuery,filterKey))
```

### `ScrIssueA25Test/A25Basket` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(IsEmpty(a25Cart) || a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/A25Basket` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,180*Parent.Width/360,783*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Basket` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/A25Basket` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,164*Parent.Width/360,291*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Basket` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/A25Basket` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Basket` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Basket` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/A25Basket` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Basket` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Basket` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/A25Basket` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Basket` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document))
```

### `ScrIssueA25Test/A25Basket` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Сагс харах  →"
```

### `ScrIssueA25Test/A25Basket` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueConfirm,false);Set(issueSubmissionMessage,"");Set(a25Review,true);Set(a25CartIndex,1);Reset(A25Months)
```

### `ScrIssueA25Test/A25CartLine` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,18*Parent.Width/1100)
```

### `ScrIssueA25Test/A25CartLine` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/A25CartLine` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25CartLine` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25CartLine` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,219*Parent.Height/720,245*Parent.Height/680)
```

### `ScrIssueA25Test/A25CartLine` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,645*Parent.Width/1100)
```

### `ScrIssueA25Test/A25CartLine` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,107*Parent.Height/720,124*Parent.Height/680)
```

### `ScrIssueA25Test/A25CartLine` . **Size**  _(Label@2.5.1)_
```powerfx
16*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25CartLine` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25CartLine` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/A25CartLine` . **Text**  _(Label@2.5.1)_
```powerfx
If(!IsEmpty(a25Cart),With({r:Last(FirstN(a25Cart,Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart))))},r.title & Char(10) & r.itemNo & "    ·    " & r.quantity & " ш" & Char(10) & If(IsBlank(r.norm),"А/25 хугацаа оноогдоогүй","А/25 норм · " & r.norm)))
```

### `ScrIssueA25Test/A25Less` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(!Coalesce(a25Busy,false) && IsBlank(a25Request),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrIssueA25Test/A25Less` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Less` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,449*Parent.Height/720,390*Parent.Height/680)
```

### `ScrIssueA25Test/A25Less` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,146*Parent.Width/360,190*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Less` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,39*Parent.Height/720,43*Parent.Height/680)
```

### `ScrIssueA25Test/A25Less` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Less` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/A25Less` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/A25Less` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Less` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Less` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Less` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Less` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/A25Less` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Сагснаас хасах"
```

### `ScrIssueA25Test/A25Less` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If((Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false)) && !Coalesce(a25Busy,false) && IsBlank(a25Request) && !IsEmpty(a25Cart),With({r:Last(FirstN(a25Cart,Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart))))},If(r.quantity=1,Remove(a25Cart,r),Patch(a25Cart,r,{quantity:r.quantity-1})));Set(a25CartIndex,Max(1,Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart))));If(IsEmpty(a25Cart),Set(a25Review,false));Reset(A25Months))
```

### `ScrIssueA25Test/A25CartNext` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,170*Parent.Width/360,230*Parent.Width/1100)
```

### `ScrIssueA25Test/A25CartNext` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,449*Parent.Height/720,390*Parent.Height/680)
```

### `ScrIssueA25Test/A25CartNext` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,174*Parent.Width/360,254*Parent.Width/1100)
```

### `ScrIssueA25Test/A25CartNext` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,39*Parent.Height/720,43*Parent.Height/680)
```

### `ScrIssueA25Test/A25CartNext` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25CartNext` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25CartNext` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25CartNext` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25CartNext` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25CartNext` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25CartNext` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25CartNext` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false) && CountRows(a25Cart)>1)
```

### `ScrIssueA25Test/A25CartNext` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн мөр  →    " & Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart)) & "/" & CountRows(a25Cart)
```

### `ScrIssueA25Test/A25CartNext` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If((Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false)) && !Coalesce(a25Busy,false) && IsBlank(a25Request) && CountRows(a25Cart)>1,Set(a25CartIndex,Mod(Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart)),CountRows(a25Cart))+1);Reset(A25Months))
```

### `ScrIssueA25Test/A25Continue` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(!Coalesce(a25Busy,false) && IsBlank(a25Request),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrIssueA25Test/A25Continue` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Continue` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/A25Continue` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,121*Parent.Width/360,183*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Continue` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/A25Continue` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Continue` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Continue` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Continue` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25Continue` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25Continue` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#292C30")
```

### `ScrIssueA25Test/A25Continue` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25Continue` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/A25Continue` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹  Хувцас нэмэх"
```

### `ScrIssueA25Test/A25Continue` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(a25Review,false)
```

### `ScrIssueA25Test/A25Months` . **DisplayMode**  _(Classic/TextInput@2.3.2)_
```powerfx
If(!Coalesce(a25Busy,false) && IsBlank(a25Request) && !IsEmpty(a25Cart),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrIssueA25Test/A25Months` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,695*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Months` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,379*Parent.Height/720,288*Parent.Height/680)
```

### `ScrIssueA25Test/A25Months` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,378*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Months` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,50*Parent.Height/720,53*Parent.Height/680)
```

### `ScrIssueA25Test/A25Months` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
17*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Months` . **Color**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Months` . **Fill**  _(Classic/TextInput@2.3.2)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Months` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/A25Months` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/A25Months` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
Coalesce(Substitute(Last(FirstN(a25Cart,Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart)))).lifeTime,"M",""),"")
```

### `ScrIssueA25Test/A25Months` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Сарын тоо"
```

### `ScrIssueA25Test/A25Months` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
If((Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false)) && !Coalesce(a25Busy,false) && IsBlank(a25Request) && !IsEmpty(a25Cart),With({m:Trim(Self.Text),r:Last(FirstN(a25Cart,Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart))))},If(IsMatch(m,"[1-9][0-9]{0,2}"),Patch(a25Cart,r,{lifeTime:m & "M"}),Patch(a25Cart,r,{lifeTime:""});If(!IsBlank(m),Notify("Хугацааг сараар оруулна уу.",NotificationType.Warning)))))
```

### `ScrIssueA25Test/A25OK` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,130*Parent.Width/360,755*Parent.Width/1100)
```

### `ScrIssueA25Test/A25OK` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/A25OK` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,214*Parent.Width/360,319*Parent.Width/1100)
```

### `ScrIssueA25Test/A25OK` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/A25OK` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25OK` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25OK` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/A25OK` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A7421D")
```

### `ScrIssueA25Test/A25OK` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#853411")
```

### `ScrIssueA25Test/A25OK` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/A25OK` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A5A9B0")
```

### `ScrIssueA25Test/A25OK` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && !Coalesce(issueDraftMissing,false))
```

### `ScrIssueA25Test/A25OK` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy,"BC-д илгээж байна…",!IsBlank(a25Request),"Дахин оролдох","ОК · BC-д ноорог үүсгэх")
```

### `ScrIssueA25Test/A25OK` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(a25Document) && CountIf(a25Cart,IsBlank(lifeTime))=0 && !Coalesce(a25Busy,false) && Connection.Connected,DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrIssueA25Test/A25OK` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If((Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && !Coalesce(issueDraftMissing,false)) && !a25Busy && Connection.Connected && !IsEmpty(a25Cart) && CountIf(a25Cart,IsBlank(lifeTime))=0,Set(a25Busy,true);Set(issueSubmissionMessage,"");If(IsBlank(a25Request),Set(issuePartialDocument,Blank());Set(issueDraftMissing,false);Set(issueRequestOwner,Lower(User().Email));Set(a25Request,Text(GUID())));IfError(With({reply:ParseJSON(TMEIssueA25Test.Run(JSON({mode:"issue",id:a25Request,employeeNo:a25Selected.code,norm:a25Selected.norm,lines:ShowColumns(a25Cart,itemNo,quantity,norm,lifeTime)})).itemsjson)},With({documentNo:Trim(Text(reply.document)),partialNo:Trim(Text(reply.partialDocument)),message:Text(reply.message)},If(Text(reply.code)="draft_unavailable" && Lower(Text(reply.retryable))="false" && Lower(Text(reply.ok))="false",Set(issueDraftMissing,true);Set(issueSubmissionMessage,Coalesce(message,"Өмнөх хүсэлтийн ноорог BC-д олдсонгүй."));false,!IsBlank(partialNo),Set(issuePartialDocument,partialNo);Set(issueSubmissionMessage,If(partialNo in message,message,"Ноорог " & partialNo & " · " & Coalesce(message,"Бүх мөр хадгалагдсан эсэх баталгаажаагүй. Ижил хүсэлтээр дахин оролдоно уу.")));false,IsBlank(documentNo) || Lower(Text(reply.ok))="false",Set(issueSubmissionMessage,Coalesce(message,"BC-д бүх мөр хадгалагдсан эсэх нь тодорхойгүй байна. Зарим мөр ноорогт орсон байж болно. Ижил хүсэлтээр дахин оролдоно уу."));false,Set(a25Document,documentNo);true))),Set(issueSubmissionMessage,Coalesce(IfError(If(FirstError.Details.HttpStatusCode=422,With({remote:ParseJSON(FirstError.Details.HttpResponse).error},If(Text(remote.code)="A25Department",Text(remote.message)))),Blank()),"BC-д бүх мөр хадгалагдсан эсэх нь тодорхойгүй байна. Зарим мөр ноорогт орсон байж болно. Ижил хүсэлтээр дахин оролдоно уу."));false);Set(a25Busy,false);If(!IsBlank(a25Document) && IsBlank(LookUp(issueRecent,code=a25Selected.code)),Collect(issueRecent,a25Selected)))
```

### `ScrIssueA25Test/A25Result` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Parent.Width/360,18*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Result` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/A25Result` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/A25Result` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Result` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,272*Parent.Height/720,280*Parent.Height/680)
```

### `ScrIssueA25Test/A25Result` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1051*Parent.Width/1100)
```

### `ScrIssueA25Test/A25Result` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,109*Parent.Height/720,116*Parent.Height/680)
```

### `ScrIssueA25Test/A25Result` . **Size**  _(Label@2.5.1)_
```powerfx
23*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/A25Result` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/A25Result` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !IsBlank(a25Document))
```

### `ScrIssueA25Test/A25Result` . **Text**  _(Label@2.5.1)_
```powerfx
"Ноорог үүссэн" & Char(10) & a25Document
```

### `ScrIssueA25Test/issueBrandPanel` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,0*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandPanel` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,0*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandPanel` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,360*Parent.Width/360,529*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandPanel` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,266*Parent.Height/720,680*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandPanel` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrIssueA25Test/issueBrandPanel` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueBrandPanel` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueBrandLogo` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Width/360,48*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandLogo` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,20*Parent.Height/720,35*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandLogo` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,115*Parent.Width/360,155*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandLogo` . **Height**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,46*Parent.Height/720,79*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandLogo` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueBrandLogo` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueBrandLogo` . **Image**  _(Image@2.2.3)_
```powerfx
'Buuruljuut logo 3-6-03 2'
```

### `ScrIssueA25Test/issueBrandTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Width/360,50*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,101*Parent.Height/720,261*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,310*Parent.Width/360,437*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,58*Parent.Height/720,146*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,31*Min(Parent.Width/360,Parent.Height/720),53*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueBrandTitle` . **Color**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issueBrandTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueBrandTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueBrandTitle` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"Хувцас олголт","Хувцас" & Char(10) & "олголт")
```

### `ScrIssueA25Test/issueBrandTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueBrandHint` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,26*Parent.Width/360,53*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandHint` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,164*Parent.Height/720,415*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandHint` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,290*Parent.Width/360,416*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandHint` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,66*Parent.Height/720,86*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandHint` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),16*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueBrandHint` . **Color**  _(Label@2.5.1)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issueBrandHint` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueBrandHint` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueBrandHint` . **Text**  _(Label@2.5.1)_
```powerfx
"Байгууллагын бүртгэлээрээ нэвтэрч, ажилтанд олгох хувцсыг сонгоно уу."
```

### `ScrIssueA25Test/issueAccountTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Parent.Width/360,575*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,312*Parent.Height/720,193*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,316*Parent.Width/360,490*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,46*Parent.Height/720,57*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,23*Min(Parent.Width/360,Parent.Height/720),28*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueAccountTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueAccountTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueAccountTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Бүртгэлээ сонгоно уу"
```

### `ScrIssueA25Test/issueAccountTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueAccount` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/issueAccount` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
User().FullName & ", " & User().Email & ". Энэ бүртгэлээр үргэлжлүүлэх."
```

### `ScrIssueA25Test/issueAccount` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Parent.Width/360,575*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccount` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,374*Parent.Height/720,269*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccount` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,316*Parent.Width/360,482*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccount` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,89*Parent.Height/720,106*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccount` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#242528")
```

### `ScrIssueA25Test/issueAccount` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issueAccount` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),15*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccount` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),15*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccount` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),15*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccount` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),15*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccount` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/issueAccount` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/issueAccount` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueAccount` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/issueAccount` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueSignedIn,true)
```

### `ScrIssueA25Test/issueEntryBack` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/issueEntryBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Parent.Width/360,575*Parent.Width/1100)
```

### `ScrIssueA25Test/issueEntryBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,476*Parent.Height/720,395*Parent.Height/680)
```

### `ScrIssueA25Test/issueEntryBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,114*Parent.Width/360,118*Parent.Width/1100)
```

### `ScrIssueA25Test/issueEntryBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,47*Parent.Height/720,46*Parent.Height/680)
```

### `ScrIssueA25Test/issueEntryBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueEntryBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueEntryBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueEntryBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/issueEntryBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/issueEntryBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueEntryBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"←  Буцах"
```

### `ScrIssueA25Test/issueEntryBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Back()
```

### `ScrIssueA25Test/issueTopLogo` . **RadiusBottomRight**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Min(Parent.Width/360,Parent.Height/720),9*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueTopLogo` . **RadiusBottomLeft**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Min(Parent.Width/360,Parent.Height/720),9*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueTopLogo` . **RadiusTopRight**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Min(Parent.Width/360,Parent.Height/720),9*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueTopLogo` . **RadiusTopLeft**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,9*Min(Parent.Width/360,Parent.Height/720),9*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueTopLogo` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,23*Parent.Width/1100)
```

### `ScrIssueA25Test/issueTopLogo` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Parent.Height/720,10*Parent.Height/680)
```

### `ScrIssueA25Test/issueTopLogo` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,35*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueTopLogo` . **Height**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,35*Parent.Height/720,42*Parent.Height/680)
```

### `ScrIssueA25Test/issueTopLogo` . **Fill**  _(Image@2.2.3)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueTopLogo` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueTopLogo` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAALaElEQVR4nO2bCWxcxRnH/9/MO/bw7npxDiAhARPbMQ7iMEdLCwlKOQo9qKrlaEEhlKutGqkUkBBRowjaUtGKSi0gGUg4G4qpVI4eQmqbtIJWlDSEgiG2Ywg5ICSxvd5d27vvzXzVPK9LIKKVNokr2/OLrJf31u/tvO+b75wxYLFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi+UgYICin68vSPcvW/BTzp3gjV+bjoIVE/6NOQgCeMjH8mzavWkoGVxhzs11TEMmdNaZWW6+cNfyBTMSoH8lfTGrVFFvZ2LeSbivq1QdEGMacVhnHa+C2N+1rF8MaS4nBa7MxOTsUlkFaU82DgwHX52uVnBYX5hWQxvBjithyXoozkGyxpWh0mzMgRksBV8Z3XDC9Jr9h1UBJrjuu7D5jh1LFzZEcl612CECD6Sb2wTRiSMhg5mckZAJjDOHr2qcZxRmrAbTiEP+suMCHBrg+XEhVqYT+tn+XHsG2KDNdUfr01OecDWgiSBCZlXnyVTg0snRA7qmVzZ06GdbVy4SoFK6lQCddOVZujK0zlyP0k2iUw4YBBkToZMwDTl85k40zxck8oEebUg4n+/H5tVRoGUcb4LCgb/O881x/QeLrQXUAudycizYdkbnmnTW+BwCy0JZq5iDW/Nfb2kxfj/KRccFj6o6mLKYpESWXWPsOmQWQJ2dyszwnsICJ3owkcmAzOCMn0fCFS6zXikO+EaqjoSqn2zAZMO8t0kgJlwBRrjmuLe1ZUV+0cI7tp14Yrb5D73lyBKYBwTBpJoMAoUKDIFWDe0rM+fNVUQ+aeyoURh76mJMurbK9e3u0DeabptwBaxfvDi6n4RoSLvuygwHm/aduvA6MyOEEL2hEXKU7QM6EjTFCVTSHwkCFCX/RNhpzpbM2jB5aoFqWyUfFm7SjO9PuAKWfPjfrnIQKiaaX+/Kjr2fbnkgIP1uQekhR0CauR5EYuWjCLRbjQUHGr/ZTCMwv4FJRGTlndW6hfUKYjxXy3Mif10zG8Zye01qc4lFaKb4YBiqhrRz7UAQ1JHEZl+IswMohJpBDrLMHFQUykLA1wwWgCgGOhCKN022ajhqKr67YAYTdgqHJtYCxtsL5jjj9e4tAG+OC2ORoIKxBoEvgPF2YHoNZpIzdNIxX8dmwFtj0rSJWMUdgoJ+oy5W3x09c/XkUMB403CwOFp0KvoL6Y7utyZUAVHkB3RnLieQywlmPO6a1AeggEEJKeuY4JW17ktIMg6HTfBlwkIwusWYUtiRRILF09SxMRj3qZhEzOvcMZJ6vO8DriYVE6aA/tbW+e+1tBzb2NcnTAra0LXl3oEw3JaUQhrF6DE5fhaE9UaqJhSPGufP1CwEXi6FquRLIYtlnQ9d9dhkcz/7Y4QfZXsTqQBN+lsZT7x53Ejx74OLWh/ob2v5lHBwS1RSEWhEsa5zxVzWyA5r/bc6R0gNDpMuCQL9FqAn4ylXaOj7j+joe9d0SWvNpf/f1Cr86N5ab3y/qakx5jtdMYIvSUAxo8T6WY5zqT4prhiSWokYSHrQFcH3Oz5yMR9HVgSPkpSNUgVJJcS6pHYvwENdA9XBTEoLOBhErW2HI3t6+kLW95i+Ql6p0ZLSOuvKL0lNdYOhfibjCqnHCi7pS1zKzL8AYURp3lcYHhiKP7S1d3SYl9JDXf3VeDLthF+7C+rsNLIViuUP8qHemJEiZtrLA0qpuEtfdAg6r9S6mCDjUyjpydnQyOdVmCPQ7496fHfJ5M8znugdmq6L8QelgE5zX3u7nNXVNSwRXD6s9fYjpHSMVopK64QUXxFEc0a0up+At2HST6Ilsx7p+2262HOjecb+iy88jZVwSF5866JFs2dq9WTMpyXDnkbo6TCZlI7weOcI4654HR89yjwvrbqXmerxv7gbitoS08gd1VQJ72ttvUxKbg8YxxEjBR0MVECvKK3fdwhLko48ckQzkoLmMKubf7iuu/HqZfO99LH/8fVRo3TPNS2pGQC2Z0rhMem0otVdleiDxYsd2rAhxDSgJgvY29pye4Pn3mmaamVmuNW+c1Hw68rXf3d9pDlOJ7Gjj67Peql8ufKT+qe7b4lSzU6op3KQl3ZC5a9pupgYnmJqkMQCQr2hWDZl1/Q8bDqM6NgYTnVrqNkF7T2hZbkvxH0CFBthVTHt5bgvXOUzApffcuP0GjzsZke/wy4N39O5pWO1aYp+uD+Iedn8+qKT8hUqpxCzZK0vZ5a/diWWhpp31T/c86Px38UUhWpNQ031u7ut5awE0T0JIc8wle+IYIS+RixBEDGCcliNCn1XwzPdK8cD7ScJs//6xoyjsAgsVzqSpGL13UDwjuxRfSVajSnrjmrKgozwX2lvd2e/seWl1OtvnTkYVC4uKf2MBr/DzGFZM4aVRsAsj4jJ2wdzzWOdwlUfVThXFzSMSzqioy9fCeQ7DNpUDnmP1vS0VOL5/u2NC02pP774M9Wo1QVVvT4w0NZyLiDOE+BTQpdH4XM/+SD2SZLPmhzaXoF6ZPZverd+kjvh6jgKVzQ3hDH+sUuYw6a+Y70uu2brbzCFqTkG7GtpucBzxJ1EOM0zBRcDgcOomC6/hwpiKJPLMdcnT/p4s0zht+ubtkYLvh/v+XBVMYUbG2epinOXK3huqLjNl6J+ROlnJbAitbZ3b3XAUyoe1Lwgww7qJCGpohNEvSDT9UyaNQEXvuPCH5UMDf0Oa3ouHHFeiYqvXLQ/9EBzWgWB97IDBQz5UtDMUOP3ZcU7BLBN6SDYf4vjVOKgX6jY1nZ+BeEFzHQqezwDPgIRRyhj2KkcHmQXJF287fgcwsHzdWt7NkfC3n/hJQdh0tP8DY1NHNCFLtE1ibh7cmkkfElrviS9tnfPwbR8p6QCTFA0ff/9r+06ecHMVMK5FT6fHniYJTw+0vMpG8+4GC5XdhekviTmY0+mo7fv467kg6sWNnuOyoF4mefQ5nKIl+MOXVIO9T/Ta3pXVAdrFfAxJdDGdjinbUTwXlvLuQmPHogn6PjAZ7APxGKEijTLXvqFsuRXM2l5QXE0fHN70bvu6NRwQ7aQeG8gOxqXgTSrZAuFwL2B1h2+J79JGn9KPNh98f9KX6e1Cxq3gn2tzZfWu+6vRJwQuAoUAyrmD49c3hQI/gd5aPB8fNmJkVMKwht8R15fDrFWMx9P4GES+Awx9gB0hivhjYb8y2za+95QofLzzNreFeMVNKYgB7crojorhRRBSeufBWWVjtIZjV0ei78ozTnPpYtIYm7MAQYr6lEQXRdzRXs5DP/sCPoOg14Em90SaGOJP8QTzlVhKaS9+fBzLtH5r+dO8Kizq4IpymHLKvZc1HLzjJi8u0AhUgmJQa1+xx6Xsr7MDY6Ge6Wg51K+XJ4vh38l0GjSFecVKupOT4qbQ8X9mbU9cz4p1kwlDtYCIqIq1eyS27NHYOZMnfd3nOQT3W02pDiCuFBWPxUxbI474rFQMxPRFmbMMVuaon8EV3qCKVA7A62vBfDw4PKmxkyxZxuegp56yeeHHJLy3szQqH3c1qbMkZW8zhG0sxjoR0PwOemnum/R4MtcAaWM/IEOBo6N5rbAy2DqMQ8hiET9mt4nBNFSAS4Yv7//TuqpyGF5vfzShc15KfbOe6Gr35wPfm1eFtJ/LZNx5g6Wwvvqiz0rhlILtqXjzpxCWZ0jFIaSSfnq0HDw5fQxW5+frLsjauGwNLgyf3yr2wifV8ExjTalUnWeoLnFUvhgffHkFWZmM9CfH1abUnN6XjTFWb4U3uYG/Gp1qdKZilXvhGFiQnU7YiTE9y9fNHvgyqaro8+q68D55U0rhq5tOnv/axaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFhwM/wbva0OdzwsPMgAAAABJRU5ErkJggg=="
```

### `ScrIssueA25Test/issueTopTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,62*Parent.Width/360,78*Parent.Width/1100)
```

### `ScrIssueA25Test/issueTopTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,6*Parent.Height/720,8*Parent.Height/680)
```

### `ScrIssueA25Test/issueTopTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,185*Parent.Width/360,280*Parent.Width/1100)
```

### `ScrIssueA25Test/issueTopTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,43*Parent.Height/720,44*Parent.Height/680)
```

### `ScrIssueA25Test/issueTopTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(Parent.Width/360,Parent.Height/720),19*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueTopTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrIssueA25Test/issueTopTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueTopTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueTopTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Хувцас олголт"
```

### `ScrIssueA25Test/issueTopTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueTopUser` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,218*Parent.Width/360,654*Parent.Width/1100)
```

### `ScrIssueA25Test/issueTopUser` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,6*Parent.Height/720,8*Parent.Height/680)
```

### `ScrIssueA25Test/issueTopUser` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,67*Parent.Width/360,305*Parent.Width/1100)
```

### `ScrIssueA25Test/issueTopUser` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,43*Parent.Height/720,44*Parent.Height/680)
```

### `ScrIssueA25Test/issueTopUser` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueTopUser` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueTopUser` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueTopUser` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueTopUser` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,Upper(Left(User().FullName,1)),User().FullName)
```

### `ScrIssueA25Test/issueTopUser` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrIssueA25Test/issueExit` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,287*Parent.Width/360,979*Parent.Width/1100)
```

### `ScrIssueA25Test/issueExit` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,8*Parent.Height/720,9*Parent.Height/680)
```

### `ScrIssueA25Test/issueExit` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,58*Parent.Width/360,98*Parent.Width/1100)
```

### `ScrIssueA25Test/issueExit` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,39*Parent.Height/720,42*Parent.Height/680)
```

### `ScrIssueA25Test/issueExit` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueExit` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueExit` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueExit` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/issueExit` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/issueExit` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueExit` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Буцах"
```

### `ScrIssueA25Test/issueExit` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueSignedIn,false)
```

### `ScrIssueA25Test/issueSteps` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/issueSteps` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,23*Parent.Width/1100)
```

### `ScrIssueA25Test/issueSteps` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,61*Parent.Height/720,62*Parent.Height/680)
```

### `ScrIssueA25Test/issueSteps` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,326*Parent.Width/360,1053*Parent.Width/1100)
```

### `ScrIssueA25Test/issueSteps` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/720,49*Parent.Height/680)
```

### `ScrIssueA25Test/issueSteps` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),15*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueSteps` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueSteps` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueSteps` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueSteps` . **Text**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,"1 / 5     Ажилтан","❶  Ажилтан          ②  Хувцас          ③  Тоо, хугацаа          ④  Баталгаажуулах          ⑤  Дууссан")
```

### `ScrIssueA25Test/issueSelectTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/issueSelectTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,108*Parent.Height/720,125*Parent.Height/680)
```

### `ScrIssueA25Test/issueSelectTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,330*Parent.Width/360,450*Parent.Width/1100)
```

### `ScrIssueA25Test/issueSelectTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,38*Parent.Height/720,48*Parent.Height/680)
```

### `ScrIssueA25Test/issueSelectTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Min(Parent.Width/360,Parent.Height/720),27*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueSelectTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#242528")
```

### `ScrIssueA25Test/issueSelectTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueSelectTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueSelectTitle` . **Text**  _(Label@2.5.1)_
```powerfx
"Ажилтан сонгох"
```

### `ScrIssueA25Test/issueSelectTitle` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueResultsTitle` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,25*Parent.Width/1100)
```

### `ScrIssueA25Test/issueResultsTitle` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,201*Parent.Height/720,179*Parent.Height/680)
```

### `ScrIssueA25Test/issueResultsTitle` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,660*Parent.Width/1100)
```

### `ScrIssueA25Test/issueResultsTitle` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,29*Parent.Height/720,30*Parent.Height/680)
```

### `ScrIssueA25Test/issueResultsTitle` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,11*Min(Parent.Width/360,Parent.Height/720),13*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueResultsTitle` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueResultsTitle` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueResultsTitle` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueResultsTitle` . **Text**  _(Label@2.5.1)_
```powerfx
If(IsBlank(Trim(A25Query.Text)),"Энэ удаагийн олголтууд","Хайлтын үр дүн")
```

### `ScrIssueA25Test/issueFourth` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3)).code=issueChoiceCode,ColorValue("#EE5F1F"),ColorValue("#E4E1DC")),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/issueFourth` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3))},p.code & ", " & p.fullName & ", " & p.dept & ", " & p.job),"")
```

### `ScrIssueA25Test/issueFourth` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,556*Parent.Width/1100)
```

### `ScrIssueA25Test/issueFourth` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,497*Parent.Height/720,370*Parent.Height/680)
```

### `ScrIssueA25Test/issueFourth` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,520*Parent.Width/1100)
```

### `ScrIssueA25Test/issueFourth` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,82*Parent.Height/720,139*Parent.Height/680)
```

### `ScrIssueA25Test/issueFourth` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrIssueA25Test/issueFourth` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,If(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3)).code=issueChoiceCode,ColorValue("#FFF1E8"),Color.White),Color.White)
```

### `ScrIssueA25Test/issueFourth` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueFourth` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueFourth` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueFourth` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueFourth` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/issueFourth` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/issueFourth` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3)
```

### `ScrIssueA25Test/issueFourth` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/issueFourth` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!a25Busy && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,Set(issueLookupMessage,"");Set(issueChoiceCode,Text(Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3)).code)))
```

### `ScrIssueA25Test/issueEmpty` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,24*Parent.Width/360,35*Parent.Width/1100)
```

### `ScrIssueA25Test/issueEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,245*Parent.Height/720,227*Parent.Height/680)
```

### `ScrIssueA25Test/issueEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,308*Parent.Width/360,827*Parent.Width/1100)
```

### `ScrIssueA25Test/issueEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,72*Parent.Height/720,60*Parent.Height/680)
```

### `ScrIssueA25Test/issueEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),16*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code) && IsEmpty(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches)))
```

### `ScrIssueA25Test/issueEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
If(a25Busy,"Ажилтны мэдээллийг уншиж байна…",!IsBlank(issueLookupMessage),issueLookupMessage,issueHasSearched && !IsBlank(Trim(A25Query.Text)),"Ажилтан олдсонгүй. Нэр эсвэл кодоо шалгана уу.","Нэр эсвэл кодын эхний хоёр тэмдэгтийг оруулаад Хайх дарна уу.")
```

### `ScrIssueA25Test/issueChoiceCaption` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/issueChoiceCaption` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,657*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/issueChoiceCaption` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,157*Parent.Width/360,678*Parent.Width/1100)
```

### `ScrIssueA25Test/issueChoiceCaption` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,55*Parent.Height/720,49*Parent.Height/680)
```

### `ScrIssueA25Test/issueChoiceCaption` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),15*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueChoiceCaption` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueChoiceCaption` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueChoiceCaption` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueChoiceCaption` . **Text**  _(Label@2.5.1)_
```powerfx
"Сонгосон: " & Coalesce(LookUp(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),code=issueChoiceCode,fullName),"—")
```

### `ScrIssueA25Test/issueProceed` . **DisabledColor**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issueProceed` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F7C59F")
```

### `ScrIssueA25Test/issueProceed` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,182*Parent.Width/360,818*Parent.Width/1100)
```

### `ScrIssueA25Test/issueProceed` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,659*Parent.Height/720,619*Parent.Height/680)
```

### `ScrIssueA25Test/issueProceed` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,162*Parent.Width/360,258*Parent.Width/1100)
```

### `ScrIssueA25Test/issueProceed` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,48*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/issueProceed` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,14*Min(Parent.Width/360,Parent.Height/720),16*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueProceed` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/issueProceed` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/issueProceed` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueProceed` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueProceed` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueProceed` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueProceed` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueProceed` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueProceed` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/issueProceed` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy && !IsBlank(issueChoiceCode),"Ачаалж байна…",!IsBlank(issueChoiceCode) && !IsBlank(issueLookupMessage),"Дахин оролдох","Үргэлжлүүлэх  →")
```

### `ScrIssueA25Test/issueProceed` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(issueChoiceCode) || a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/issueProceed` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueConfirm,false);Set(issueSubmissionMessage,"");If(!a25Busy && !IsBlank(issueChoiceCode),Set(a25Busy,true);Set(issueLookupMessage,"");Set(a25Selected,{code:"",fullName:"",division:"",dept:"",job:"",norm:""});Set(a25Review,false);Clear(a25Cart);Set(a25ItemIndex,1);Set(a25CartIndex,1);Set(a25Request,Blank());Set(a25Document,Blank());Clear(a25NormLines);Clear(a25Stock);IfError(With({payload:If(IsBlank(LookUp(a25Matches,code=issueChoiceCode,code)),TMEIssueA25Test.Run(JSON({mode:"search",query:issueChoiceCode})).itemsjson,issueSearchPayload)},With({person:LookUp(Table(ParseJSON(payload)) As e,Text(e.Value.No)=issueChoiceCode,e.Value)},If(IsBlank(Text(person.No)),Set(issueLookupMessage,"Сонгосон ажилтан BC-д олдсонгүй. Дахин хайна уу.");false,With({catalogPayload:TMEIssueA25Test.Run(JSON({mode:"catalog"})).itemsjson},If(StartsWith(Trim(catalogPayload),"["),With({norms:ForAll(Table(person.eligible) As p,{number:Text(p.Value.number),lifeTime:Text(p.Value.lifeTime),norm:Text(p.Value.norm)}),stock:ForAll(Table(ParseJSON(catalogPayload)) As item,{number:Text(item.Value.number),displayName:Text(item.Value.displayName),blocked:Boolean(item.Value.blocked)})},ClearCollect(a25NormLines,norms);ClearCollect(a25Stock,stock);Set(a25Selected,{code:Text(person.No),fullName:Trim(Text(person.First_Name) & " " & Text(person.Last_Name)),division:Text(person.Division_Name),dept:Text(person.Department_Name),job:Text(person.Position_Name),norm:Text(person.norm)});true),Set(issueLookupMessage,"Ажилтны мэдээлэл, хувцасны жагсаалтыг ачаалж чадсангүй. Үргэлжлүүлэх товчоор дахин оролдоно уу.");false))))),Clear(a25NormLines);Clear(a25Stock);Set(issueLookupMessage,"Ажилтны мэдээлэл, хувцасны жагсаалтыг ачаалж чадсангүй. Үргэлжлүүлэх товчоор дахин оролдоно уу.");false);If(!IsBlank(issueLookupMessage),Notify(issueLookupMessage,NotificationType.Warning));Set(a25Busy,false))
```

### `ScrIssueA25Test/issueBrandAccent` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,26*Parent.Width/360,53*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandAccent` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,90*Parent.Height/720,248*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandAccent` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,34*Parent.Width/360,54*Parent.Width/1100)
```

### `ScrIssueA25Test/issueBrandAccent` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,3*Parent.Height/720,4*Parent.Height/680)
```

### `ScrIssueA25Test/issueBrandAccent` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueBrandAccent` . **Fill**  _(Label@2.5.1)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/issueBrandAccent` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueIdentityProvider` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,26*Parent.Width/360,53*Parent.Width/1100)
```

### `ScrIssueA25Test/issueIdentityProvider` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,232*Parent.Height/720,619*Parent.Height/680)
```

### `ScrIssueA25Test/issueIdentityProvider` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,276*Parent.Width/360,456*Parent.Width/1100)
```

### `ScrIssueA25Test/issueIdentityProvider` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Parent.Height/720,35*Parent.Height/680)
```

### `ScrIssueA25Test/issueIdentityProvider` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),13*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueIdentityProvider` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#FFBC8F")
```

### `ScrIssueA25Test/issueIdentityProvider` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueIdentityProvider` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueIdentityProvider` . **Text**  _(Label@2.5.1)_
```powerfx
"Power Apps · Microsoft Entra ID"
```

### `ScrIssueA25Test/issueAccountAvatar` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,35*Parent.Width/360,595*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountAvatar` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,394*Parent.Height/720,295*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountAvatar` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Width/360,54*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountAvatar` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,54*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountAvatar` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Min(Parent.Width/360,Parent.Height/720),19*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountAvatar` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueAccountAvatar` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF1E8")
```

### `ScrIssueA25Test/issueAccountAvatar` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,30*Min(Parent.Width/360,Parent.Height/720),30*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountAvatar` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,30*Min(Parent.Width/360,Parent.Height/720),30*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountAvatar` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,30*Min(Parent.Width/360,Parent.Height/720),30*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountAvatar` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,30*Min(Parent.Width/360,Parent.Height/720),30*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountAvatar` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/issueAccountAvatar` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/issueAccountAvatar` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueAccountAvatar` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
Upper(Left(Coalesce(User().FullName,User().Email),1))
```

### `ScrIssueA25Test/issueAccountAvatar` . **Tooltip**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ бүртгэлээр үргэлжлүүлэх"
```

### `ScrIssueA25Test/issueAccountAvatar` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Select(issueAccount)
```

### `ScrIssueA25Test/issueAccountName` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,91*Parent.Width/360,668*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountName` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,386*Parent.Height/720,286*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountName` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,206*Parent.Width/360,327*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountName` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,31*Parent.Height/720,39*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountName` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),18*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountName` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueAccountName` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueAccountName` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueAccountName` . **Text**  _(Label@2.5.1)_
```powerfx
Coalesce(User().FullName,User().Email)
```

### `ScrIssueA25Test/issueAccountName` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/issueAccountName` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueAccount)
```

### `ScrIssueA25Test/issueAccountName` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueAccountEmail` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,91*Parent.Width/360,668*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountEmail` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,418*Parent.Height/720,326*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountEmail` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,206*Parent.Width/360,334*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountEmail` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,29*Parent.Height/720,27*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountEmail` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Min(Parent.Width/360,Parent.Height/720),14*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountEmail` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueAccountEmail` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueAccountEmail` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueAccountEmail` . **Text**  _(Label@2.5.1)_
```powerfx
User().Email
```

### `ScrIssueA25Test/issueAccountEmail` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueAccount)
```

### `ScrIssueA25Test/issueAccountEmail` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueAccountChevron` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,303*Parent.Width/360,1006*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountChevron` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,398*Parent.Height/720,298*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountChevron` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,22*Parent.Width/360,30*Parent.Width/1100)
```

### `ScrIssueA25Test/issueAccountChevron` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,35*Parent.Height/720,45*Parent.Height/680)
```

### `ScrIssueA25Test/issueAccountChevron` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,20*Min(Parent.Width/360,Parent.Height/720),24*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueAccountChevron` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueAccountChevron` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueAccountChevron` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (!Coalesce(issueSignedIn,false))
```

### `ScrIssueA25Test/issueAccountChevron` . **Text**  _(Label@2.5.1)_
```powerfx
"›"
```

### `ScrIssueA25Test/issueAccountChevron` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueAccount)
```

### `ScrIssueA25Test/issueAccountChevron` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrIssueA25Test/issueRowCode0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,238*Parent.Height/720,228*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode0` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,237*Parent.Width/360,405*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode0` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Parent.Height/720,25*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode0` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),11*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCode0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCode0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCode0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0)
```

### `ScrIssueA25Test/issueRowCode0` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0))},p.code),"")
```

### `ScrIssueA25Test/issueRowCode0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match0)
```

### `ScrIssueA25Test/issueRowCode0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowName0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,254*Parent.Height/720,254*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName0` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,268*Parent.Width/360,441*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName0` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,39*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName0` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),21*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowName0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowName0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowName0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0)
```

### `ScrIssueA25Test/issueRowName0` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0))},p.fullName),"")
```

### `ScrIssueA25Test/issueRowName0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueRowName0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match0)
```

### `ScrIssueA25Test/issueRowName0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowDept0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,280*Parent.Height/720,297*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept0` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept0` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,23*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept0` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),13*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowDept0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowDept0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowDept0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0)
```

### `ScrIssueA25Test/issueRowDept0` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0))},p.dept),"")
```

### `ScrIssueA25Test/issueRowDept0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match0)
```

### `ScrIssueA25Test/issueRowDept0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowPosition0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,296*Parent.Height/720,323*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition0` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition0` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,24*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition0` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowPosition0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueRowPosition0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowPosition0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0)
```

### `ScrIssueA25Test/issueRowPosition0` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0))},p.job & If(!IsBlank(p.job) && !IsBlank(p.division)," · ","") & p.division),"")
```

### `ScrIssueA25Test/issueRowPosition0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match0)
```

### `ScrIssueA25Test/issueRowPosition0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowCheck0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,307*Parent.Width/360,495*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,241*Parent.Height/720,232*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck0` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,26*Parent.Width/360,31*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck0` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,31*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck0` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(Parent.Width/360,Parent.Height/720),20*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCheck0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCheck0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCheck0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0)
```

### `ScrIssueA25Test/issueRowCheck0` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+0,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+0))},If(p.code=issueChoiceCode,"●","○")),"")
```

### `ScrIssueA25Test/issueRowCheck0` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrIssueA25Test/issueRowCheck0` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match0)
```

### `ScrIssueA25Test/issueRowCheck0` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowCode1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,326*Parent.Height/720,228*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,237*Parent.Width/360,405*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Parent.Height/720,25*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode1` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),11*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCode1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCode1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCode1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1)
```

### `ScrIssueA25Test/issueRowCode1` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1))},p.code),"")
```

### `ScrIssueA25Test/issueRowCode1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match1)
```

### `ScrIssueA25Test/issueRowCode1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowName1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,342*Parent.Height/720,254*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,268*Parent.Width/360,441*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,39*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName1` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),21*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowName1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowName1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowName1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1)
```

### `ScrIssueA25Test/issueRowName1` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1))},p.fullName),"")
```

### `ScrIssueA25Test/issueRowName1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueRowName1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match1)
```

### `ScrIssueA25Test/issueRowName1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowDept1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,368*Parent.Height/720,297*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,23*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept1` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),13*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowDept1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowDept1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowDept1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1)
```

### `ScrIssueA25Test/issueRowDept1` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1))},p.dept),"")
```

### `ScrIssueA25Test/issueRowDept1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match1)
```

### `ScrIssueA25Test/issueRowDept1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowPosition1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,384*Parent.Height/720,323*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,24*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition1` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowPosition1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueRowPosition1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowPosition1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1)
```

### `ScrIssueA25Test/issueRowPosition1` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1))},p.job & If(!IsBlank(p.job) && !IsBlank(p.division)," · ","") & p.division),"")
```

### `ScrIssueA25Test/issueRowPosition1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match1)
```

### `ScrIssueA25Test/issueRowPosition1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowCheck1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,307*Parent.Width/360,1027*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Height/720,232*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,26*Parent.Width/360,31*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,31*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck1` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(Parent.Width/360,Parent.Height/720),20*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCheck1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCheck1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCheck1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1)
```

### `ScrIssueA25Test/issueRowCheck1` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+1,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+1))},If(p.code=issueChoiceCode,"●","○")),"")
```

### `ScrIssueA25Test/issueRowCheck1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrIssueA25Test/issueRowCheck1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match1)
```

### `ScrIssueA25Test/issueRowCheck1` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowCode2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,414*Parent.Height/720,379*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode2` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,237*Parent.Width/360,405*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode2` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Parent.Height/720,25*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode2` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),11*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCode2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCode2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCode2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2)
```

### `ScrIssueA25Test/issueRowCode2` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2))},p.code),"")
```

### `ScrIssueA25Test/issueRowCode2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match2)
```

### `ScrIssueA25Test/issueRowCode2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowName2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,430*Parent.Height/720,405*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName2` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,268*Parent.Width/360,441*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName2` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,39*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName2` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),21*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowName2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowName2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowName2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2)
```

### `ScrIssueA25Test/issueRowName2` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2))},p.fullName),"")
```

### `ScrIssueA25Test/issueRowName2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueRowName2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match2)
```

### `ScrIssueA25Test/issueRowName2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowDept2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,456*Parent.Height/720,448*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept2` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept2` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,23*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept2` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),13*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowDept2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowDept2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowDept2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2)
```

### `ScrIssueA25Test/issueRowDept2` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2))},p.dept),"")
```

### `ScrIssueA25Test/issueRowDept2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match2)
```

### `ScrIssueA25Test/issueRowDept2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowPosition2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,42*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,472*Parent.Height/720,474*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition2` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition2` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,24*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition2` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowPosition2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueRowPosition2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowPosition2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2)
```

### `ScrIssueA25Test/issueRowPosition2` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2))},p.job & If(!IsBlank(p.job) && !IsBlank(p.division)," · ","") & p.division),"")
```

### `ScrIssueA25Test/issueRowPosition2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match2)
```

### `ScrIssueA25Test/issueRowPosition2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowCheck2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,307*Parent.Width/360,495*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,417*Parent.Height/720,383*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck2` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,26*Parent.Width/360,31*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck2` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,31*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck2` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(Parent.Width/360,Parent.Height/720),20*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCheck2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCheck2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCheck2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2)
```

### `ScrIssueA25Test/issueRowCheck2` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+2,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+2))},If(p.code=issueChoiceCode,"●","○")),"")
```

### `ScrIssueA25Test/issueRowCheck2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrIssueA25Test/issueRowCheck2` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(A25Match2)
```

### `ScrIssueA25Test/issueRowCheck2` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowCode3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,502*Parent.Height/720,379*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode3` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,237*Parent.Width/360,405*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCode3` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,17*Parent.Height/720,25*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCode3` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),11*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCode3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCode3` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCode3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3)
```

### `ScrIssueA25Test/issueRowCode3` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3))},p.code),"")
```

### `ScrIssueA25Test/issueRowCode3` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueFourth)
```

### `ScrIssueA25Test/issueRowCode3` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowName3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,518*Parent.Height/720,405*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName3` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,268*Parent.Width/360,441*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowName3` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,39*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowName3` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,15*Min(Parent.Width/360,Parent.Height/720),21*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowName3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowName3` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowName3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3)
```

### `ScrIssueA25Test/issueRowName3` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3))},p.fullName),"")
```

### `ScrIssueA25Test/issueRowName3` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ScrIssueA25Test/issueRowName3` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueFourth)
```

### `ScrIssueA25Test/issueRowName3` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowDept3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,544*Parent.Height/720,448*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept3` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowDept3` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,23*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowDept3` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),13*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowDept3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/issueRowDept3` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowDept3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3)
```

### `ScrIssueA25Test/issueRowDept3` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3))},p.dept),"")
```

### `ScrIssueA25Test/issueRowDept3` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueFourth)
```

### `ScrIssueA25Test/issueRowDept3` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowPosition3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,28*Parent.Width/360,574*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,560*Parent.Height/720,474*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition3` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,295*Parent.Width/360,489*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowPosition3` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Height/720,24*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowPosition3` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,10*Min(Parent.Width/360,Parent.Height/720),12*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowPosition3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#68655F")
```

### `ScrIssueA25Test/issueRowPosition3` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowPosition3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3)
```

### `ScrIssueA25Test/issueRowPosition3` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3))},p.job & If(!IsBlank(p.job) && !IsBlank(p.division)," · ","") & p.division),"")
```

### `ScrIssueA25Test/issueRowPosition3` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueFourth)
```

### `ScrIssueA25Test/issueRowPosition3` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/issueRowCheck3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,307*Parent.Width/360,1027*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,505*Parent.Height/720,383*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck3` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,26*Parent.Width/360,31*Parent.Width/1100)
```

### `ScrIssueA25Test/issueRowCheck3` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,25*Parent.Height/720,31*Parent.Height/680)
```

### `ScrIssueA25Test/issueRowCheck3` . **Size**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Min(Parent.Width/360,Parent.Height/720),20*Min(Parent.Width/1100,Parent.Height/680))
```

### `ScrIssueA25Test/issueRowCheck3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/issueRowCheck3` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/issueRowCheck3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && ((Coalesce(issueSignedIn,false) && IsBlank(a25Selected.code)) && CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3)
```

### `ScrIssueA25Test/issueRowCheck3` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches))>=Max(1,Coalesce(a25Index,1))+3,With({p:Last(FirstN(If(IsBlank(Trim(A25Query.Text)),issueRecent,a25Matches),Max(1,Coalesce(a25Index,1))+3))},If(p.code=issueChoiceCode,"●","○")),"")
```

### `ScrIssueA25Test/issueRowCheck3` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ScrIssueA25Test/issueRowCheck3` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(issueFourth)
```

### `ScrIssueA25Test/issueRowCheck3` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/cartIssuedBy` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,157*Parent.Width/360,663*Parent.Width/1100)
```

### `ScrIssueA25Test/cartIssuedBy` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,12*Parent.Height/720,12*Parent.Height/680)
```

### `ScrIssueA25Test/cartIssuedBy` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,114*Parent.Width/360,294*Parent.Width/1100)
```

### `ScrIssueA25Test/cartIssuedBy` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,35*Parent.Height/720,39*Parent.Height/680)
```

### `ScrIssueA25Test/cartIssuedBy` . **Size**  _(Label@2.5.1)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartIssuedBy` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/cartIssuedBy` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartIssuedBy` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/cartIssuedBy` . **Text**  _(Label@2.5.1)_
```powerfx
User().FullName
```

### `ScrIssueA25Test/cartIssuedBy` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartIssuedBy` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ScrIssueA25Test/cartIssuedBy` . **Wrap**  _(Label@2.5.1)_
```powerfx
false
```

### `ScrIssueA25Test/cartStage` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartStage` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,66*Parent.Height/720,67*Parent.Height/680)
```

### `ScrIssueA25Test/cartStage` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1052*Parent.Width/1100)
```

### `ScrIssueA25Test/cartStage` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,32*Parent.Height/720,39*Parent.Height/680)
```

### `ScrIssueA25Test/cartStage` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartStage` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartStage` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartStage` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code))
```

### `ScrIssueA25Test/cartStage` . **Text**  _(Label@2.5.1)_
```powerfx
With({k:If(!IsBlank(a25Document),5,!a25Review,2,Coalesce(issueConfirm,false),4,3)},If(App.Width<First(App.SizeBreakpoints).Value,Switch(k,2,"2 / 5   Хувцас",3,"3 / 5   Тоо, хугацаа",4,"4 / 5   Баталгаажуулах","5 / 5   Дууссан"),Concat(Table({n:1,t:"Ажилтан"},{n:2,t:"Хувцас"},{n:3,t:"Тоо, хугацаа"},{n:4,t:"Баталгаажуулах"},{n:5,t:"Дууссан"}) As s,If(s.n=k,"●  ",s.n<k,"✓  ","○  ") & s.t,"          ───          ")))
```

### `ScrIssueA25Test/cartStage` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartPickHeading` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPickHeading` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,157*Parent.Height/720,176*Parent.Height/680)
```

### `ScrIssueA25Test/cartPickHeading` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,215*Parent.Width/360,617*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPickHeading` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,33*Parent.Height/720,40*Parent.Height/680)
```

### `ScrIssueA25Test/cartPickHeading` . **Size**  _(Label@2.5.1)_
```powerfx
21*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPickHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartPickHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPickHeading` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document))
```

### `ScrIssueA25Test/cartPickHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"Хувцас сонгох"
```

### `ScrIssueA25Test/cartPickHeading` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartFourthItem` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,361*Parent.Width/1100)
```

### `ScrIssueA25Test/cartFourthItem` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,490*Parent.Height/720,399*Parent.Height/680)
```

### `ScrIssueA25Test/cartFourthItem` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,321*Parent.Width/1100)
```

### `ScrIssueA25Test/cartFourthItem` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,68*Parent.Height/720,101*Parent.Height/680)
```

### `ScrIssueA25Test/cartFourthItem` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartFourthItem` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartFourthItem` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3)).number in a25Cart.itemNo,false),ColorValue("#FFF1E8"),Color.White)
```

### `ScrIssueA25Test/cartFourthItem` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartFourthItem` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartFourthItem` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3)
```

### `ScrIssueA25Test/cartFourthItem` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3))},i.displayName & Char(10) & i.number & "   ·   " & If(i.blocked,"BC-д хаалттай",With({m:LookUp(a25NormLines,number=i.number,lifeTime)},If(IsBlank(m),"Хугацааг гараар оруулна","А/25 · " & Substitute(m,"M"," сар")))) & If(i.number in a25Cart.itemNo,"   ✓","")),"")
```

### `ScrIssueA25Test/cartFourthItem` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3,With({i:Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3))},If(i.blocked,Notify("BC-д хаалттай бараа",NotificationType.Warning),If(IsBlank(LookUp(a25Cart,itemNo=i.number)),With({r:LookUp(a25NormLines,number=i.number)},Collect(a25Cart,{itemNo:i.number,title:i.displayName,quantity:1,norm:Coalesce(r.norm,""),lifeTime:Coalesce(r.lifeTime,"")}));Set(a25Request,Blank())))))
```

### `ScrIssueA25Test/cartFourthItem` . **Align**  _(Classic/Button@2.2.0)_
```powerfx
Align.Left
```

### `ScrIssueA25Test/cartFourthItem` . **FontWeight**  _(Classic/Button@2.2.0)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartFourthItem` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
If(If(CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))))>=If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3,Last(FirstN(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text))),If(("catalog|" & Lower(Trim(A25ItemQuery.Text)))=Coalesce(issuePagedCatalogQuery,"unpaged") && Coalesce(a25ItemIndex,1)>=1 && Coalesce(a25ItemIndex,1)<=CountRows(Filter(a25Stock,IsBlank(Trim(A25ItemQuery.Text)) || Trim(A25ItemQuery.Text) in displayName || StartsWith(number,Trim(A25ItemQuery.Text)))),Coalesce(a25ItemIndex,1),1)+3)).number in a25Cart.itemNo,false),ColorValue("#EE5F1F"),ColorValue("#E4E1DC"))
```

### `ScrIssueA25Test/cartFourthItem` . **PaddingLeft**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,13*Parent.Width/360,17*Parent.Width/1100)
```

### `ScrIssueA25Test/cartFourthItem` . **PaddingRight**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,8*Parent.Width/360,12*Parent.Width/1100)
```

### `ScrIssueA25Test/cartFourthItem` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/cartPreviewPanel` . **X**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,704*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewPanel` . **Y**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,184*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewPanel` . **Width**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,370*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewPanel` . **Height**  _(Image@2.2.3)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,385*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewPanel` . **Fill**  _(Image@2.2.3)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewPanel` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value))
```

### `ScrIssueA25Test/cartPreviewPanel` . **Image**  _(Image@2.2.3)_
```powerfx
"data:image/svg+xml;utf8," & EncodeUrl("<svg xmlns='http://www.w3.org/2000/svg' width='100%' height='100%'><rect x='0.5' y='0.5' width='99.6%' height='99%' rx='13' fill='white' stroke='#E4E1DC'/></svg>")
```

### `ScrIssueA25Test/cartPreviewPanel` . **ImagePosition**  _(Image@2.2.3)_
```powerfx
ImagePosition.Stretch
```

### `ScrIssueA25Test/cartPreviewHeading` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,726*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewHeading` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,208*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewHeading` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,327*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewHeading` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,35*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewHeading` . **Size**  _(Label@2.5.1)_
```powerfx
18*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPreviewHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartPreviewHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewHeading` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value))
```

### `ScrIssueA25Test/cartPreviewHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"Олгох хувцас"
```

### `ScrIssueA25Test/cartPreviewHeading` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartPreviewEmpty` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,726*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,258*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,326*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,86*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value) && IsEmpty(a25Cart))
```

### `ScrIssueA25Test/cartPreviewEmpty` . **Text**  _(Label@2.5.1)_
```powerfx
"Сонгосон хувцас энд харагдана."
```

### `ScrIssueA25Test/cartPreviewEmpty` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartPreviewItem0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,726*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,257*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem0` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,323*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem0` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,56*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem0` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPreviewItem0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartPreviewItem0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewItem0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value) && CountRows(a25Cart)>0)
```

### `ScrIssueA25Test/cartPreviewItem0` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(a25Cart,1))},r.title & Char(10) & r.quantity & " ш    ·    " & Coalesce(Substitute(r.lifeTime,"M"," сар"),"Хугацаа оруулна уу"))
```

### `ScrIssueA25Test/cartPreviewItem0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartPreviewItem1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,726*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,319*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,323*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,56*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem1` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPreviewItem1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartPreviewItem1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewItem1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value) && CountRows(a25Cart)>1)
```

### `ScrIssueA25Test/cartPreviewItem1` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(a25Cart,2))},r.title & Char(10) & r.quantity & " ш    ·    " & Coalesce(Substitute(r.lifeTime,"M"," сар"),"Хугацаа оруулна уу"))
```

### `ScrIssueA25Test/cartPreviewItem1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartPreviewItem2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,726*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,381*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem2` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,323*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem2` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,56*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem2` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPreviewItem2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartPreviewItem2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewItem2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value) && CountRows(a25Cart)>2)
```

### `ScrIssueA25Test/cartPreviewItem2` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(a25Cart,3))},r.title & Char(10) & r.quantity & " ш    ·    " & Coalesce(Substitute(r.lifeTime,"M"," сар"),"Хугацаа оруулна уу"))
```

### `ScrIssueA25Test/cartPreviewItem2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartPreviewItem3` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,726*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem3` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,443*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem3` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,323*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewItem3` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,56*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewItem3` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPreviewItem3` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartPreviewItem3` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewItem3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value) && CountRows(a25Cart)>3)
```

### `ScrIssueA25Test/cartPreviewItem3` . **Text**  _(Label@2.5.1)_
```powerfx
With({r:Last(FirstN(a25Cart,4))},r.title & Char(10) & r.quantity & " ш    ·    " & Coalesce(Substitute(r.lifeTime,"M"," сар"),"Хугацаа оруулна уу"))
```

### `ScrIssueA25Test/cartPreviewItem3` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartPreviewMore` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,726*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewMore` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,514*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewMore` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Width/360,322*Parent.Width/1100)
```

### `ScrIssueA25Test/cartPreviewMore` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,0*Parent.Height/720,34*Parent.Height/680)
```

### `ScrIssueA25Test/cartPreviewMore` . **Size**  _(Label@2.5.1)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartPreviewMore` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/cartPreviewMore` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartPreviewMore` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document) && !(App.Width<First(App.SizeBreakpoints).Value) && CountRows(a25Cart)>4)
```

### `ScrIssueA25Test/cartPreviewMore` . **Text**  _(Label@2.5.1)_
```powerfx
"+ " & (CountRows(a25Cart)-4) & " хувцас"
```

### `ScrIssueA25Test/cartPreviewMore` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartTotals` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartTotals` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/cartTotals` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,153*Parent.Width/360,693*Parent.Width/1100)
```

### `ScrIssueA25Test/cartTotals` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,44*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/cartTotals` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartTotals` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartTotals` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartTotals` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !Coalesce(a25Review,false) && IsBlank(a25Document))
```

### `ScrIssueA25Test/cartTotals` . **Text**  _(Label@2.5.1)_
```powerfx
"Сагс · " & CountRows(a25Cart) & " төрөл   " & Coalesce(Sum(a25Cart,quantity),0) & " ш"
```

### `ScrIssueA25Test/cartTotals` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartEditHeading` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartEditHeading` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,164*Parent.Height/720,178*Parent.Height/680)
```

### `ScrIssueA25Test/cartEditHeading` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,860*Parent.Width/1100)
```

### `ScrIssueA25Test/cartEditHeading` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,48*Parent.Height/680)
```

### `ScrIssueA25Test/cartEditHeading` . **Size**  _(Label@2.5.1)_
```powerfx
22*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartEditHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartEditHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartEditHeading` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/cartEditHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"Тоо, хугацаа"
```

### `ScrIssueA25Test/cartEditHeading` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartMonthLabel` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,695*Parent.Width/1100)
```

### `ScrIssueA25Test/cartMonthLabel` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,344*Parent.Height/720,245*Parent.Height/680)
```

### `ScrIssueA25Test/cartMonthLabel` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,378*Parent.Width/1100)
```

### `ScrIssueA25Test/cartMonthLabel` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,30*Parent.Height/720,35*Parent.Height/680)
```

### `ScrIssueA25Test/cartMonthLabel` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartMonthLabel` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartMonthLabel` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartMonthLabel` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/cartMonthLabel` . **Text**  _(Label@2.5.1)_
```powerfx
"Эдлэх хугацаа (сар)"
```

### `ScrIssueA25Test/cartMonthLabel` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartEditTotal` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartEditTotal` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,510*Parent.Height/720,470*Parent.Height/680)
```

### `ScrIssueA25Test/cartEditTotal` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,645*Parent.Width/1100)
```

### `ScrIssueA25Test/cartEditTotal` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,52*Parent.Height/720,54*Parent.Height/680)
```

### `ScrIssueA25Test/cartEditTotal` . **Size**  _(Label@2.5.1)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartEditTotal` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/cartEditTotal` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartEditTotal` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/cartEditTotal` . **Text**  _(Label@2.5.1)_
```powerfx
CountRows(a25Cart) & " нэрийн хувцас   ·   " & Sum(a25Cart,quantity) & " ширхэг"
```

### `ScrIssueA25Test/cartEditTotal` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartAdvance` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,145*Parent.Width/360,781*Parent.Width/1100)
```

### `ScrIssueA25Test/cartAdvance` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/cartAdvance` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,199*Parent.Width/360,293*Parent.Width/1100)
```

### `ScrIssueA25Test/cartAdvance` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/cartAdvance` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartAdvance` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartAdvance` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/cartAdvance` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartAdvance` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartAdvance` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false))
```

### `ScrIssueA25Test/cartAdvance` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Баталгаажуулах  →"
```

### `ScrIssueA25Test/cartAdvance` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If((Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && !Coalesce(issueConfirm,false)) && !Coalesce(a25Busy,false) && IsBlank(a25Request) && !IsEmpty(a25Cart),With({r:Last(FirstN(a25Cart,Min(Max(1,Coalesce(a25CartIndex,1)),CountRows(a25Cart)))),m:Trim(A25Months.Text)},If(!IsMatch(m,"[1-9][0-9]{0,2}"),Notify("Эдлэх хугацааг 1–999 сарын хооронд оруулна уу.",NotificationType.Warning),Patch(a25Cart,r,{lifeTime:m & "M"});If(CountIf(a25Cart,IsBlank(lifeTime))>0,Notify("Сагсны бүх мөрийн хугацааг оруулна уу.",NotificationType.Warning),Set(issueCheckPage,0);Set(issueConfirm,true)))))
```

### `ScrIssueA25Test/cartAdvance` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartAdvance` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/cartAdvance` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(!Coalesce(a25Busy,false) && IsBlank(a25Request) && !IsEmpty(a25Cart),DisplayMode.Edit,DisplayMode.Disabled)
```

### `ScrIssueA25Test/cartConfirmHeading` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartConfirmHeading` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,167*Parent.Height/720,178*Parent.Height/680)
```

### `ScrIssueA25Test/cartConfirmHeading` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1049*Parent.Width/1100)
```

### `ScrIssueA25Test/cartConfirmHeading` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,41*Parent.Height/720,48*Parent.Height/680)
```

### `ScrIssueA25Test/cartConfirmHeading` . **Size**  _(Label@2.5.1)_
```powerfx
22*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartConfirmHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartConfirmHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartConfirmHeading` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false))
```

### `ScrIssueA25Test/cartConfirmHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"Олголтоо шалгана уу"
```

### `ScrIssueA25Test/cartConfirmHeading` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartCheckRow0` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckRow0` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,225*Parent.Height/720,245*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckRow0` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1050*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckRow0` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,73*Parent.Height/720,67*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckRow0` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartCheckRow0` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartCheckRow0` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartCheckRow0` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && CountRows(a25Cart)>=3*Max(0,Coalesce(issueCheckPage,0))+1)
```

### `ScrIssueA25Test/cartCheckRow0` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(a25Cart)>=3*Max(0,Coalesce(issueCheckPage,0))+1,With({r:Last(FirstN(a25Cart,3*Max(0,Coalesce(issueCheckPage,0))+1))},r.title & Char(10) & r.itemNo & "    ·    " & r.quantity & " ш    ·    " & Substitute(r.lifeTime,"M"," сар")),"")
```

### `ScrIssueA25Test/cartCheckRow0` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartCheckRow0` . **BorderColor**  _(Label@2.5.1)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartCheckRow1` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckRow1` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,306*Parent.Height/720,321*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckRow1` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1050*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckRow1` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,73*Parent.Height/720,67*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckRow1` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartCheckRow1` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartCheckRow1` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartCheckRow1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && CountRows(a25Cart)>=3*Max(0,Coalesce(issueCheckPage,0))+2)
```

### `ScrIssueA25Test/cartCheckRow1` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(a25Cart)>=3*Max(0,Coalesce(issueCheckPage,0))+2,With({r:Last(FirstN(a25Cart,3*Max(0,Coalesce(issueCheckPage,0))+2))},r.title & Char(10) & r.itemNo & "    ·    " & r.quantity & " ш    ·    " & Substitute(r.lifeTime,"M"," сар")),"")
```

### `ScrIssueA25Test/cartCheckRow1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartCheckRow1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartCheckRow2` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckRow2` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,387*Parent.Height/720,397*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckRow2` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1050*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckRow2` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,73*Parent.Height/720,67*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckRow2` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartCheckRow2` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartCheckRow2` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartCheckRow2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && CountRows(a25Cart)>=3*Max(0,Coalesce(issueCheckPage,0))+3)
```

### `ScrIssueA25Test/cartCheckRow2` . **Text**  _(Label@2.5.1)_
```powerfx
If(CountRows(a25Cart)>=3*Max(0,Coalesce(issueCheckPage,0))+3,With({r:Last(FirstN(a25Cart,3*Max(0,Coalesce(issueCheckPage,0))+3))},r.title & Char(10) & r.itemNo & "    ·    " & r.quantity & " ш    ·    " & Substitute(r.lifeTime,"M"," сар")),"")
```

### `ScrIssueA25Test/cartCheckRow2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartCheckRow2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartCheckMore` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckMore` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,477*Parent.Height/720,480*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckMore` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,278*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckMore` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,39*Parent.Height/720,41*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckMore` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartCheckMore` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartCheckMore` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartCheckMore` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartCheckMore` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartCheckMore` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && CountRows(a25Cart)>3)
```

### `ScrIssueA25Test/cartCheckMore` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн мөрүүд   " & (Coalesce(issueCheckPage,0)+1) & "/" & RoundUp(CountRows(a25Cart)/3,0)
```

### `ScrIssueA25Test/cartCheckMore` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(CountRows(a25Cart)>3,Set(issueCheckPage,Mod(Coalesce(issueCheckPage,0)+1,RoundUp(CountRows(a25Cart)/3,0))))
```

### `ScrIssueA25Test/cartCheckMore` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartCheckMore` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/cartCheckTotals` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckTotals` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,523*Parent.Height/720,531*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckTotals` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1020*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckTotals` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,37*Parent.Height/720,38*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckTotals` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartCheckTotals` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartCheckTotals` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartCheckTotals` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false))
```

### `ScrIssueA25Test/cartCheckTotals` . **Text**  _(Label@2.5.1)_
```powerfx
"CAMP агуулах   ·   " & CountRows(a25Cart) & " төрөл   ·   " & Sum(a25Cart,quantity) & " ш"
```

### `ScrIssueA25Test/cartCheckTotals` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartSubmitError` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartSubmitError` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,563*Parent.Height/720,566*Parent.Height/680)
```

### `ScrIssueA25Test/cartSubmitError` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1049*Parent.Width/1100)
```

### `ScrIssueA25Test/cartSubmitError` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,90*Parent.Height/720,46*Parent.Height/680)
```

### `ScrIssueA25Test/cartSubmitError` . **Size**  _(Label@2.5.1)_
```powerfx
12*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartSubmitError` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#A64210")
```

### `ScrIssueA25Test/cartSubmitError` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartSubmitError` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && !IsBlank(issueSubmissionMessage))
```

### `ScrIssueA25Test/cartSubmitError` . **Text**  _(Label@2.5.1)_
```powerfx
issueSubmissionMessage
```

### `ScrIssueA25Test/cartSubmitError` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartSubmitError` . **Tooltip**  _(Label@2.5.1)_
```powerfx
issueSubmissionMessage
```

### `ScrIssueA25Test/cartSubmitError` . **Wrap**  _(Label@2.5.1)_
```powerfx
true
```

### `ScrIssueA25Test/cartCheckBack` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckBack` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckBack` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,105*Parent.Width/360,184*Parent.Width/1100)
```

### `ScrIssueA25Test/cartCheckBack` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/cartCheckBack` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
13*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartCheckBack` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartCheckBack` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartCheckBack` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartCheckBack` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartCheckBack` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && !Coalesce(issueDraftMissing,false))
```

### `ScrIssueA25Test/cartCheckBack` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
If(IsBlank(a25Request),"‹  Засах","Хүсэлт хаах")
```

### `ScrIssueA25Test/cartCheckBack` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If(!a25Busy,If(IsBlank(a25Request),Set(issueConfirm,false);Reset(A25Months),Set(issueDiscardPrompt,true)))
```

### `ScrIssueA25Test/cartCheckBack` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartCheckBack` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/cartCheckBack` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

### `ScrIssueA25Test/cartDoneMark` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDoneMark` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,197*Parent.Height/720,200*Parent.Height/680)
```

### `ScrIssueA25Test/cartDoneMark` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,329*Parent.Width/360,1049*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDoneMark` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,69*Parent.Height/720,72*Parent.Height/680)
```

### `ScrIssueA25Test/cartDoneMark` . **Size**  _(Label@2.5.1)_
```powerfx
32*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartDoneMark` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#167844")
```

### `ScrIssueA25Test/cartDoneMark` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartDoneMark` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !IsBlank(a25Document))
```

### `ScrIssueA25Test/cartDoneMark` . **Text**  _(Label@2.5.1)_
```powerfx
"✓"
```

### `ScrIssueA25Test/cartDoneMark` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartIssuedTotal` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartIssuedTotal` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,400*Parent.Height/720,420*Parent.Height/680)
```

### `ScrIssueA25Test/cartIssuedTotal` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1052*Parent.Width/1100)
```

### `ScrIssueA25Test/cartIssuedTotal` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,76*Parent.Height/720,58*Parent.Height/680)
```

### `ScrIssueA25Test/cartIssuedTotal` . **Size**  _(Label@2.5.1)_
```powerfx
15*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartIssuedTotal` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartIssuedTotal` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartIssuedTotal` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !IsBlank(a25Document))
```

### `ScrIssueA25Test/cartIssuedTotal` . **Text**  _(Label@2.5.1)_
```powerfx
a25Selected.fullName & "   ·   " & CountRows(a25Cart) & " төрөл   ·   " & Sum(a25Cart,quantity) & " ширхэг"
```

### `ScrIssueA25Test/cartIssuedTotal` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartNew` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,114*Parent.Width/360,790*Parent.Width/1100)
```

### `ScrIssueA25Test/cartNew` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/cartNew` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,230*Parent.Width/360,283*Parent.Width/1100)
```

### `ScrIssueA25Test/cartNew` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/cartNew` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartNew` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartNew` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/cartNew` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartNew` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartNew` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && !IsBlank(a25Document))
```

### `ScrIssueA25Test/cartNew` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Дараагийн ажилтан  →"
```

### `ScrIssueA25Test/cartNew` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueConfirm,false);Set(issueSubmissionMessage,"");Set(a25Selected,Blank()); Set(a25Review,false); Clear(a25Cart); Set(a25ItemIndex,1); Set(a25Request,Blank()); Set(a25Document,Blank());Set(issueConfirm,false);Set(issueSubmissionMessage,"");Set(issueChoiceCode,"");Reset(A25Query);Reset(A25ItemQuery);Set(a25Index,1);Clear(a25Matches)
```

### `ScrIssueA25Test/cartNew` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartNew` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/pgDenied1367` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ScrIssueA25Test/pgDenied1367` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ScrIssueA25Test/pgDenied1367` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ScrIssueA25Test/pgDenied1367` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/pgDenied1367` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ScrIssueA25Test/pgDenied1367` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/pgDenied1367` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/pgDenied1367` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ScrIssueA25Test/pgDenied1367` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))
```

### `ScrIssueA25Test/pgDenied1367` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

### `ScrIssueA25Test/cartStartNew` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,755*Parent.Width/1100)
```

### `ScrIssueA25Test/cartStartNew` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/cartStartNew` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,319*Parent.Width/1100)
```

### `ScrIssueA25Test/cartStartNew` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/cartStartNew` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartStartNew` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartStartNew` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/cartStartNew` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartStartNew` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartStartNew` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && Coalesce(issueDraftMissing,false))
```

### `ScrIssueA25Test/cartStartNew` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Шинэ хүсэлт эхлүүлэх"
```

### `ScrIssueA25Test/cartStartNew` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If((((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && !Coalesce(issueDiscardPrompt,false) && Coalesce(issueDraftMissing,false))) && !a25Busy,Set(issueDiscardPrompt,true))
```

### `ScrIssueA25Test/cartStartNew` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartStartNew` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/cartDiscardHeading` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardHeading` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,172*Parent.Height/720,178*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardHeading` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1020*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardHeading` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,67*Parent.Height/720,60*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardHeading` . **Size**  _(Label@2.5.1)_
```powerfx
22*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartDiscardHeading` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartDiscardHeading` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartDiscardHeading` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && Coalesce(issueDiscardPrompt,false) && !IsBlank(a25Request) && IsBlank(a25Document))
```

### `ScrIssueA25Test/cartDiscardHeading` . **Text**  _(Label@2.5.1)_
```powerfx
"Энэ хүсэлтийг апп дээр хаах уу?"
```

### `ScrIssueA25Test/cartDiscardHeading` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ScrIssueA25Test/cartDiscardHint` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardHint` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,249*Parent.Height/720,259*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardHint` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1020*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardHint` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,103*Parent.Height/720,65*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardHint` . **Size**  _(Label@2.5.1)_
```powerfx
15*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartDiscardHint` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#645F59")
```

### `ScrIssueA25Test/cartDiscardHint` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartDiscardHint` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && Coalesce(issueDiscardPrompt,false) && !IsBlank(a25Request) && IsBlank(a25Document))
```

### `ScrIssueA25Test/cartDiscardHint` . **Text**  _(Label@2.5.1)_
```powerfx
"Хаахад сагс цэвэрлэгдэнэ. Дараагийн олголт тусдаа хүсэлт болно. Дахин олгохын өмнө BC дэх нооргоо шалгана уу."
```

### `ScrIssueA25Test/cartDiscardHint` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartDiscardHint` . **Wrap**  _(Label@2.5.1)_
```powerfx
true
```

### `ScrIssueA25Test/cartDiscardReference` . **X**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardReference` . **Y**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,370*Parent.Height/720,345*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardReference` . **Width**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,328*Parent.Width/360,1020*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardReference` . **Height**  _(Label@2.5.1)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,104*Parent.Height/720,88*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardReference` . **Size**  _(Label@2.5.1)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartDiscardReference` . **Color**  _(Label@2.5.1)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartDiscardReference` . **Fill**  _(Label@2.5.1)_
```powerfx
Color.Transparent
```

### `ScrIssueA25Test/cartDiscardReference` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && Coalesce(issueDiscardPrompt,false) && !IsBlank(a25Request) && IsBlank(a25Document))
```

### `ScrIssueA25Test/cartDiscardReference` . **Text**  _(Label@2.5.1)_
```powerfx
If(!IsBlank(issuePartialDocument),If(issueDraftMissing,"Өмнөх BC ноорог   ","BC ноорог   ") & issuePartialDocument & Char(10),"") & "Хүсэлтийн дугаар" & Char(10) & a25Request
```

### `ScrIssueA25Test/cartDiscardReference` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Normal
```

### `ScrIssueA25Test/cartDiscardReference` . **Wrap**  _(Label@2.5.1)_
```powerfx
true
```

### `ScrIssueA25Test/cartDiscardCancel` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,16*Parent.Width/360,24*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardCancel` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardCancel` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,116*Parent.Width/360,184*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardCancel` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardCancel` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartDiscardCancel` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#1E2124")
```

### `ScrIssueA25Test/cartDiscardCancel` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartDiscardCancel` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartDiscardCancel` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartDiscardCancel` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && Coalesce(issueDiscardPrompt,false) && !IsBlank(a25Request) && IsBlank(a25Document))
```

### `ScrIssueA25Test/cartDiscardCancel` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"‹  Буцах"
```

### `ScrIssueA25Test/cartDiscardCancel` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(issueDiscardPrompt,false)
```

### `ScrIssueA25Test/cartDiscardCancel` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartDiscardCancel` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/cartDiscardConfirm` . **X**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,143*Parent.Width/360,755*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,662*Parent.Height/720,616*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,201*Parent.Width/360,319*Parent.Width/1100)
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
If(App.Width<First(App.SizeBreakpoints).Value,45*Parent.Height/720,47*Parent.Height/680)
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
14*If(App.Width<First(App.SizeBreakpoints).Value,Min(App.Width/360,App.Height/720),Min(App.Width/1100,App.Height/680))
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#EE5F1F")
```

### `ScrIssueA25Test/cartDiscardConfirm` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ScrIssueA25Test/cartDiscardConfirm` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && Coalesce(issueDiscardPrompt,false) && !IsBlank(a25Request) && IsBlank(a25Document))
```

### `ScrIssueA25Test/cartDiscardConfirm` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хааж, сагс цэвэрлэх"
```

### `ScrIssueA25Test/cartDiscardConfirm` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
If((((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|issue|" in pgAccess.Title))) && (Coalesce(issueSignedIn,false) && !IsBlank(a25Selected.code) && Coalesce(a25Review,false) && IsBlank(a25Document) && Coalesce(issueConfirm,false) && Coalesce(issueDiscardPrompt,false) && !IsBlank(a25Request) && IsBlank(a25Document))) && !a25Busy,Set(a25Selected,{code:"",fullName:"",division:"",dept:"",job:"",norm:""});Set(a25Review,false);Clear(a25Cart);Set(a25ItemIndex,1);Set(a25CartIndex,1);Set(a25Request,Blank());Set(a25Document,Blank());Set(issueRequestOwner,Blank());Set(issuePartialDocument,Blank());Set(issueDraftMissing,false);Set(issueResumeReceipt,false);Set(issueDiscardPrompt,false);Set(issueConfirm,false);Set(issueSubmissionMessage,"");Set(issueLookupMessage,"");Set(issueChoiceCode,"");Set(issueSearchPayload,"[]");Set(issueHasSearched,false);Set(a25Index,1);Clear(a25Matches);Clear(a25NormLines);Clear(a25Stock);Reset(A25Query);Reset(A25ItemQuery))
```

### `ScrIssueA25Test/cartDiscardConfirm` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#E4E1DC")
```

### `ScrIssueA25Test/cartDiscardConfirm` . **DisabledFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#F4C8AC")
```

### `ScrIssueA25Test/cartDiscardConfirm` . **DisplayMode**  _(Classic/Button@2.2.0)_
```powerfx
If(a25Busy,DisplayMode.Disabled,DisplayMode.Edit)
```

