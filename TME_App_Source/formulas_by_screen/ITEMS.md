# ITEMS — Power Fx formulas

### `ITEMS` . **OnVisible**  _(Screen)_
```powerfx
Set(pgAccess,Blank());If(Connection.Connected,IfError(Refresh(AssetUserAccess);Set(pgAccess,LookUp(AssetUserAccess,CompanyCode="TME-Inventory-Pages" && UserEmail=Lower(User().Email))),Set(pgAccess,Blank())));If((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode))),false
)
```

### `ITEMS` . **Fill**  _(Screen)_
```powerfx
RGBA(255,255,255,1)
```

### `ITEMS` . **Height**  _(Screen)_
```powerfx
App.Height
```

### `ITEMS` . **LoadingSpinnerColor**  _(Screen)_
```powerfx
RGBA(211, 66, 9, 1)
```

### `ITEMS` . **Width**  _(Screen)_
```powerfx
App.Width
```

### `ITEMS/BarcodeReader1` . **Visible**  _(BarcodeReader@1.0.25)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/BarcodeReader1` . **BorderFillColor**  _(BarcodeReader@1.0.25)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/BarcodeReader1` . **FillColor**  _(BarcodeReader@1.0.25)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/BarcodeReader1` . **Height**  _(BarcodeReader@1.0.25)_
```powerfx
(63)*((App.Height/1136))
```

### `ITEMS/BarcodeReader1` . **OnScan**  _(BarcodeReader@1.0.25)_
```powerfx
Set(
    varItem,
    LookUp(
        'items (v2.0)',
        number = First(Self.Barcodes).Value
    )
);
Set(
    varOpeningBalance,
    LookUp(
        'itemLedgerEntries (microsoft/analytics/v1.0)',
        'Item No.' = First(Self.Barcodes).Value
    ).Quantity
);
Set(varJustSelected, true);
Set(varBarcodeText, First(Self.Barcodes).Value);
Reset(txtSearch)
```

### `ITEMS/BarcodeReader1` . **Text**  _(BarcodeReader@1.0.25)_
```powerfx
"Код уншигч"
```

### `ITEMS/BarcodeReader1` . **TextColor**  _(BarcodeReader@1.0.25)_
```powerfx
RGBA(241, 244, 249, 1)
```

### `ITEMS/BarcodeReader1` . **Width**  _(BarcodeReader@1.0.25)_
```powerfx
(608)*((App.Width/640))
```

### `ITEMS/BarcodeReader1` . **X**  _(BarcodeReader@1.0.25)_
```powerfx
(17)*((App.Width/640))
```

### `ITEMS/BarcodeReader1` . **Y**  _(BarcodeReader@1.0.25)_
```powerfx
(9)*((App.Height/1136))
```

### `ITEMS/Icon12` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Icon12` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon12` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon12` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/Icon12` . **Fill**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Icon12` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon12` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(50)*((App.Height/1136))
```

### `ITEMS/Icon12` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Home
```

### `ITEMS/Icon12` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Navigate('нүүр')
```

### `ITEMS/Icon12` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(43)*((App.Width/640))
```

### `ITEMS/Icon12` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(576)*((App.Width/640))
```

### `ITEMS/Icon12` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*((App.Height/1136))
```

### `ITEMS/Icon5` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Icon5` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon5` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon5` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/Icon5` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon5` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(43)*((App.Height/1136))
```

### `ITEMS/Icon5` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ArrowLeft
```

### `ITEMS/Icon5` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx

Navigate(
    нүүр,
    ScreenTransition.CoverRight
)
```

### `ITEMS/Icon5` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(38)*((App.Width/640))
```

### `ITEMS/Icon5` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(27)*((App.Width/640))
```

### `ITEMS/Icon5` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(14)*((App.Height/1136))
```

### `ITEMS/Container2_2` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Container2_2` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2_2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(315)*((App.Height/1136))
```

### `ITEMS/Container2_2` . **PaddingBottom**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Container2_2` . **PaddingLeft**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Container2_2` . **PaddingRight**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Container2_2` . **PaddingTop**  _(GroupContainer@1.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Container2_2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2_2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2_2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2_2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2_2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(607)*((App.Width/640))
```

### `ITEMS/Container2_2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(18)*((App.Width/640))
```

### `ITEMS/Container2_2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(706)*((App.Height/1136))
```

### `ITEMS/Container2_2/Rectangle2_2` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Container2_2/Rectangle2_2` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2_2/Rectangle2_2` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Container2_2/Rectangle2_2` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2_2/Rectangle2_2` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ITEMS/Container2_2/Rectangle2_2` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(206)*((App.Width/640))
```

### `ITEMS/Container2_2/Rectangle2_2` . **X**  _(Rectangle@2.3.0)_
```powerfx
(378)*((App.Width/640))
```

### `ITEMS/Container2_2/Rectangle2_2` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(36)*((App.Height/1136))
```

### `ITEMS/Container2` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Container2` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(129)*((App.Height/1136))
```

### `ITEMS/Container2` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container2` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(607)*((App.Width/640))
```

### `ITEMS/Container2` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(18)*((App.Width/640))
```

### `ITEMS/Container2` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(87)*((App.Height/1136))
```

### `ITEMS/Container6` . **Visible**  _(GroupContainer@1.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Container6` . **BorderColor**  _(GroupContainer@1.5.0)_
```powerfx
RGBA(109, 49, 162, 1)
```

### `ITEMS/Container6` . **BorderThickness**  _(GroupContainer@1.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container6` . **Height**  _(GroupContainer@1.5.0)_
```powerfx
(90)*((App.Height/1136))
```

### `ITEMS/Container6` . **RadiusBottomLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container6` . **RadiusBottomRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container6` . **RadiusTopLeft**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container6` . **RadiusTopRight**  _(GroupContainer@1.5.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Container6` . **Width**  _(GroupContainer@1.5.0)_
```powerfx
(127)*((App.Width/640))
```

### `ITEMS/Container6` . **X**  _(GroupContainer@1.5.0)_
```powerfx
(437)*((App.Width/640))
```

### `ITEMS/Container6` . **Y**  _(GroupContainer@1.5.0)_
```powerfx
(585)*((App.Height/1136))
```

### `ITEMS/galSuggestions` . **BorderColor**  _(Gallery@2.15.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/galSuggestions` . **Fill**  _(Gallery@2.15.0)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/galSuggestions` . **Height**  _(Gallery@2.15.0)_
```powerfx
(If(
    varJustSelected &&
    txtSearch.Text = varBarcodeText,
    42,
    300
))*((App.Height/1136))
```

### `ITEMS/galSuggestions` . **Items**  _(Gallery@2.15.0)_
```powerfx
If(
    varJustSelected &&
    txtSearch.Text = varBarcodeText,

    FirstN(
        Filter(
            'items (v2.0)',
            number = varBarcodeText
        ),
        1
    ),

    FirstN(
        Filter(
            'items (v2.0)',
            txtSearch.Text in number ||
            txtSearch.Text in 'Display Name'
        ),
        30
    )
)
```

### `ITEMS/galSuggestions` . **OnSelect**  _(Gallery@2.15.0)_
```powerfx
Set(varJustSelected, true);
Set(varItem, ThisItem);
Set(varBarcodeText, ThisItem.number);

Set(
    varOpeningBalance,
    LookUp(
        'itemLedgerEntries (microsoft/analytics/v1.0)',
        'Item No.' = ThisItem.number
    ).Quantity
);

Set(varNewPicture, Blank());

IfError(
    Set(
        varItemPicture,
        'PowerAppV2->Compose,Findonerecord(V3),Getanimage,fileordo...'.Run(
            ThisItem.number
        ).picture
    ),
    Set(varItemPicture, Blank())
)
```

### `ITEMS/galSuggestions` . **TemplatePadding**  _(Gallery@2.15.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/galSuggestions` . **TemplateSize**  _(Gallery@2.15.0)_
```powerfx
(42)*((App.Height/1136))
```

### `ITEMS/galSuggestions` . **Visible**  _(Gallery@2.15.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (Len(txtSearch.Text) > 0)
```

### `ITEMS/galSuggestions` . **Width**  _(Gallery@2.15.0)_
```powerfx
(538)*((App.Width/640))
```

### `ITEMS/galSuggestions` . **X**  _(Gallery@2.15.0)_
```powerfx
(56)*((App.Width/640))
```

### `ITEMS/galSuggestions` . **Y**  _(Gallery@2.15.0)_
```powerfx
(159)*((App.Height/1136))
```

### `ITEMS/galSuggestions/Title1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/galSuggestions/Title1` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/galSuggestions/Title1` . **Fill**  _(Label@2.5.1)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/galSuggestions/Title1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/galSuggestions/Title1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
If(ThisItem.IsSelected, FontWeight.Semibold, FontWeight.Normal)
```

### `ITEMS/galSuggestions/Title1` . **Height**  _(Label@2.5.1)_
```powerfx
(21)*((App.Height/1136))
```

### `ITEMS/galSuggestions/Title1` . **OnSelect**  _(Label@2.5.1)_
```powerfx
Select(Parent)
```

### `ITEMS/galSuggestions/Title1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/galSuggestions/Title1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/galSuggestions/Title1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/galSuggestions/Title1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/galSuggestions/Title1` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/galSuggestions/Title1` . **Text**  _(Label@2.5.1)_
```powerfx
ThisItem.number & " - " & Left(ThisItem.'Display Name', 30)
```

### `ITEMS/galSuggestions/Title1` . **VerticalAlign**  _(Label@2.5.1)_
```powerfx
VerticalAlign.Top
```

### `ITEMS/galSuggestions/Title1` . **Width**  _(Label@2.5.1)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - 86)*((App.Width/640))
```

### `ITEMS/galSuggestions/Title1` . **X**  _(Label@2.5.1)_
```powerfx
(16)*((App.Width/640))
```

### `ITEMS/galSuggestions/Title1` . **Y**  _(Label@2.5.1)_
```powerfx
(8)*((App.Height/1136))
```

### `ITEMS/galSuggestions/Rectangle1` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/galSuggestions/Rectangle1` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/galSuggestions/Rectangle1` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/galSuggestions/Rectangle1` . **Height**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Separator1.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ITEMS/galSuggestions/Rectangle1` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ITEMS/galSuggestions/Rectangle1` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
ThisItem.IsSelected
```

### `ITEMS/galSuggestions/Rectangle1` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(4)*((App.Width/640))
```

### `ITEMS/galSuggestions/Rectangle1` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/galSuggestions/Rectangle1` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/galSuggestions/NextArrow1` . **AccessibleLabel**  _(Classic/Icon@2.5.0)_
```powerfx
Self.Tooltip
```

### `ITEMS/galSuggestions/NextArrow1` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/galSuggestions/NextArrow1` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/galSuggestions/NextArrow1` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ITEMS/galSuggestions/NextArrow1` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/galSuggestions/NextArrow1` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(50)*((App.Height/1136))
```

### `ITEMS/galSuggestions/NextArrow1` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.ChevronRight
```

### `ITEMS/galSuggestions/NextArrow1` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Select(Parent)
```

### `ITEMS/galSuggestions/NextArrow1` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*((App.Height/1136))
```

### `ITEMS/galSuggestions/NextArrow1` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*((App.Width/640))
```

### `ITEMS/galSuggestions/NextArrow1` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*((App.Width/640))
```

### `ITEMS/galSuggestions/NextArrow1` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(12)*((App.Height/1136))
```

### `ITEMS/galSuggestions/NextArrow1` . **Tooltip**  _(Classic/Icon@2.5.0)_
```powerfx
"View item details"
```

### `ITEMS/galSuggestions/NextArrow1` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(50)*((App.Width/640))
```

### `ITEMS/galSuggestions/NextArrow1` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))) - (Self.Width/((App.Width/640))) - 12)*((App.Width/640))
```

### `ITEMS/galSuggestions/NextArrow1` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(((Parent.TemplateHeight/((App.Height/1136))) / 2) - ((Self.Height/((App.Height/1136))) / 2))*((App.Height/1136))
```

### `ITEMS/galSuggestions/Separator1` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/galSuggestions/Separator1` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/galSuggestions/Separator1` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/galSuggestions/Separator1` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(8)*((App.Height/1136))
```

### `ITEMS/galSuggestions/Separator1` . **OnSelect**  _(Rectangle@2.3.0)_
```powerfx
Select(Parent)
```

### `ITEMS/galSuggestions/Separator1` . **Width**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateWidth/((App.Width/640))))*((App.Width/640))
```

### `ITEMS/galSuggestions/Separator1` . **X**  _(Rectangle@2.3.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/galSuggestions/Separator1` . **Y**  _(Rectangle@2.3.0)_
```powerfx
((Parent.TemplateHeight/((App.Height/1136))) - (Self.Height/((App.Height/1136))))*((App.Height/1136))
```

### `ITEMS/txtCountQty` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/txtCountQty` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/txtCountQty` . **BorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtCountQty` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtCountQty` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/txtCountQty` . **Format**  _(Classic/TextInput@2.3.2)_
```powerfx
TextFormat.Number
```

### `ITEMS/txtCountQty` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(55)*((App.Height/1136))
```

### `ITEMS/txtCountQty` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"""Тоолох тоо оруулна уу"""
```

### `ITEMS/txtCountQty` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/txtCountQty` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ITEMS/txtCountQty` . **RadiusBottomLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtCountQty` . **RadiusBottomRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtCountQty` . **RadiusTopLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtCountQty` . **RadiusTopRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtCountQty` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtCountQty` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(569)*((App.Width/640))
```

### `ITEMS/txtCountQty` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/txtCountQty` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(885)*((App.Height/1136))
```

### `ITEMS/Label3_5` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label3_5` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_5` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_5` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_5` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_5` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label3_5` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*((App.Height/1136))
```

### `ITEMS/Label3_5` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_5` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_5` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_5` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_5` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_5` . **Text**  _(Label@2.5.1)_
```powerfx
"📦 Агуулахын үлдэгдэл:"
```

### `ITEMS/Label3_5` . **Width**  _(Label@2.5.1)_
```powerfx
(249)*((App.Width/640))
```

### `ITEMS/Label3_5` . **X**  _(Label@2.5.1)_
```powerfx
(38)*((App.Width/640))
```

### `ITEMS/Label3_5` . **Y**  _(Label@2.5.1)_
```powerfx
(750)*((App.Height/1136))
```

### `ITEMS/Label8_5` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label8_5` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label8_5` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label8_5` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_5` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/Label8_5` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_5` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label8_5` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ITEMS/Label8_5` . **Height**  _(Label@2.5.1)_
```powerfx
(32)*((App.Height/1136))
```

### `ITEMS/Label8_5` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_5` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_5` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_5` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_5` . **Size**  _(Label@2.5.1)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_5` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) || IsBlank(varItem),
    "-",
    Text(
        LookUp(
            'items (v2.0)',
            ThisRecord.number = varItem.number
        ).inventory,
        "#,##0"
    )
)
```

### `ITEMS/Label8_5` . **Width**  _(Label@2.5.1)_
```powerfx
(167)*((App.Width/640))
```

### `ITEMS/Label8_5` . **X**  _(Label@2.5.1)_
```powerfx
(433)*((App.Width/640))
```

### `ITEMS/Label8_5` . **Y**  _(Label@2.5.1)_
```powerfx
(748)*((App.Height/1136))
```

### `ITEMS/txtSearch` . **Visible**  _(Classic/TextInput@2.3.2)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/txtSearch` . **BorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/txtSearch` . **BorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtSearch` . **Default**  _(Classic/TextInput@2.3.2)_
```powerfx
varBarcodeText
```

### `ITEMS/txtSearch` . **FocusedBorderThickness**  _(Classic/TextInput@2.3.2)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtSearch` . **Font**  _(Classic/TextInput@2.3.2)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/txtSearch` . **Height**  _(Classic/TextInput@2.3.2)_
```powerfx
(48)*((App.Height/1136))
```

### `ITEMS/txtSearch` . **HintText**  _(Classic/TextInput@2.3.2)_
```powerfx
"Код оруулж хайх..."
```

### `ITEMS/txtSearch` . **HoverBorderColor**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/txtSearch` . **HoverFill**  _(Classic/TextInput@2.3.2)_
```powerfx
RGBA(255, 211, 205, 1)
```

### `ITEMS/txtSearch` . **OnChange**  _(Classic/TextInput@2.3.2)_
```powerfx
If(
    varJustSelected,
    false,
    
    With(
        {
            found:
                LookUp(
                    'items (v2.0)',
                    number = txtSearch.Text
                )
        },
        If(
            IsBlank(Trim(txtSearch.Text)) || IsBlank(found),

            Set(varItem, Blank());
            Set(varOpeningBalance, Blank()),

            Set(varItem, found);
            Set(
                varOpeningBalance,
                LookUp(
                    'itemLedgerEntries (microsoft/analytics/v1.0)',
                    'Item No.' = found.number
                ).Quantity
            )
        )
    )
)
```

### `ITEMS/txtSearch` . **RadiusBottomLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtSearch` . **RadiusBottomRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtSearch` . **RadiusTopLeft**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtSearch` . **RadiusTopRight**  _(Classic/TextInput@2.3.2)_
```powerfx
(5)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtSearch` . **Size**  _(Classic/TextInput@2.3.2)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/txtSearch` . **Width**  _(Classic/TextInput@2.3.2)_
```powerfx
(537)*((App.Width/640))
```

### `ITEMS/txtSearch` . **X**  _(Classic/TextInput@2.3.2)_
```powerfx
(56)*((App.Width/640))
```

### `ITEMS/txtSearch` . **Y**  _(Classic/TextInput@2.3.2)_
```powerfx
(111)*((App.Height/1136))
```

### `ITEMS/Label3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3` . **Height**  _(Label@2.5.1)_
```powerfx
(39)*((App.Height/1136))
```

### `ITEMS/Label3` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3` . **Text**  _(Label@2.5.1)_
```powerfx
"Барааны Нэр"
```

### `ITEMS/Label3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label3` . **Width**  _(Label@2.5.1)_
```powerfx
(135)*((App.Width/640))
```

### `ITEMS/Label3` . **X**  _(Label@2.5.1)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/Label3` . **Y**  _(Label@2.5.1)_
```powerfx
(258)*((App.Height/1136))
```

### `ITEMS/Label3_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_1` . **Height**  _(Label@2.5.1)_
```powerfx
(34)*((App.Height/1136))
```

### `ITEMS/Label3_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_1` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_1` . **Text**  _(Label@2.5.1)_
```powerfx
"Барааны Код"
```

### `ITEMS/Label3_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label3_1` . **Width**  _(Label@2.5.1)_
```powerfx
(251)*((App.Width/640))
```

### `ITEMS/Label3_1` . **X**  _(Label@2.5.1)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/Label3_1` . **Y**  _(Label@2.5.1)_
```powerfx
(297)*((App.Height/1136))
```

### `ITEMS/Label3_2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_2` . **Height**  _(Label@2.5.1)_
```powerfx
(14)*((App.Height/1136))
```

### `ITEMS/Label3_2` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_2` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_2` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_2` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_2` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_2` . **Text**  _(Label@2.5.1)_
```powerfx
"Барааны төрөл"
```

### `ITEMS/Label3_2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label3_2` . **Width**  _(Label@2.5.1)_
```powerfx
(271)*((App.Width/640))
```

### `ITEMS/Label3_2` . **X**  _(Label@2.5.1)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/Label3_2` . **Y**  _(Label@2.5.1)_
```powerfx
(338)*((App.Height/1136))
```

### `ITEMS/Label3_3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_3` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*((App.Height/1136))
```

### `ITEMS/Label3_3` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_3` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_3` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_3` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_3` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_3` . **Text**  _(Label@2.5.1)_
```powerfx
"Байршил"
```

### `ITEMS/Label3_3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label3_3` . **Width**  _(Label@2.5.1)_
```powerfx
(271)*((App.Width/640))
```

### `ITEMS/Label3_3` . **X**  _(Label@2.5.1)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/Label3_3` . **Y**  _(Label@2.5.1)_
```powerfx
(364)*((App.Height/1136))
```

### `ITEMS/Label8` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label8` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label8` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label8` . **Height**  _(Label@2.5.1)_
```powerfx
(36)*((App.Height/1136))
```

### `ITEMS/Label8` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8` . **Size**  _(Label@2.5.1)_
```powerfx
(Max(8, Min(16, 16 - (Len(varItem.'Display Name') - 10) * 0.15)))*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) || IsBlank(varItem),
    "-",
    varItem.'Display Name'
)
```

### `ITEMS/Label8` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label8` . **Width**  _(Label@2.5.1)_
```powerfx
(332)*((App.Width/640))
```

### `ITEMS/Label8` . **X**  _(Label@2.5.1)_
```powerfx
(273)*((App.Width/640))
```

### `ITEMS/Label8` . **Y**  _(Label@2.5.1)_
```powerfx
(258)*((App.Height/1136))
```

### `ITEMS/Label8_2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label8_2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label8_2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_2` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Label8_2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label8_2` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label8_2` . **Height**  _(Label@2.5.1)_
```powerfx
(28)*((App.Height/1136))
```

### `ITEMS/Label8_2` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_2` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_2` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_2` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_2` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_2` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) || IsBlank(varItem),
    "-",
    varItem.'Type'
)
```

### `ITEMS/Label8_2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label8_2` . **Width**  _(Label@2.5.1)_
```powerfx
(168)*((App.Width/640))
```

### `ITEMS/Label8_2` . **X**  _(Label@2.5.1)_
```powerfx
(437)*((App.Width/640))
```

### `ITEMS/Label8_2` . **Y**  _(Label@2.5.1)_
```powerfx
(327)*((App.Height/1136))
```

### `ITEMS/Label8_3` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label8_3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label8_3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_3` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Label8_3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label8_3` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label8_3` . **Height**  _(Label@2.5.1)_
```powerfx
(26)*((App.Height/1136))
```

### `ITEMS/Label8_3` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_3` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_3` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_3` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_3` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_3` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) || IsBlank(varItem),
    "-",
    LookUp(
        'itemLedgerEntries (microsoft/analytics/v1.0)',
        'Item No.' = varItem.number
    ).'Location Code'
)
```

### `ITEMS/Label8_3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label8_3` . **Width**  _(Label@2.5.1)_
```powerfx
(168)*((App.Width/640))
```

### `ITEMS/Label8_3` . **X**  _(Label@2.5.1)_
```powerfx
(437)*((App.Width/640))
```

### `ITEMS/Label8_3` . **Y**  _(Label@2.5.1)_
```powerfx
(359)*((App.Height/1136))
```

### `ITEMS/Label8_4` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label8_4` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label8_4` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_4` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Label8_4` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_4` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label8_4` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label8_4` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*((App.Height/1136))
```

### `ITEMS/Label8_4` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_4` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_4` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_4` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_4` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_4` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) || IsBlank(varItem),
    "-",
    LookUp(
        'itemLedgerEntries (microsoft/analytics/v1.0)',
        'Item No.' = varItem.number
    ).'Unit of Measure Code'
)
```

### `ITEMS/Label8_4` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label8_4` . **Width**  _(Label@2.5.1)_
```powerfx
(168)*((App.Width/640))
```

### `ITEMS/Label8_4` . **X**  _(Label@2.5.1)_
```powerfx
(437)*((App.Width/640))
```

### `ITEMS/Label8_4` . **Y**  _(Label@2.5.1)_
```powerfx
(389)*((App.Height/1136))
```

### `ITEMS/Label9` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label9` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label9` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Label9` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label9` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label9` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label9` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*((App.Height/1136))
```

### `ITEMS/Label9` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label9` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label9` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label9` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label9` . **Size**  _(Label@2.5.1)_
```powerfx
(18)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label9` . **Text**  _(Label@2.5.1)_
```powerfx
"📋 Барааны мэдээлэл"
```

### `ITEMS/Label9` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label9` . **Width**  _(Label@2.5.1)_
```powerfx
(327)*((App.Width/640))
```

### `ITEMS/Label9` . **X**  _(Label@2.5.1)_
```powerfx
(30)*((App.Width/640))
```

### `ITEMS/Label9` . **Y**  _(Label@2.5.1)_
```powerfx
(228)*((App.Height/1136))
```

### `ITEMS/Rectangle3` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Rectangle3` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/Rectangle3` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ITEMS/Rectangle3` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Rectangle3` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(564)*((App.Width/640))
```

### `ITEMS/Rectangle3` . **X**  _(Rectangle@2.3.0)_
```powerfx
(41
)*((App.Width/640))
```

### `ITEMS/Rectangle3` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(294)*((App.Height/1136))
```

### `ITEMS/Rectangle3_1` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Rectangle3_1` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_1` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/Rectangle3_1` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_1` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ITEMS/Rectangle3_1` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Rectangle3_1` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(564)*((App.Width/640))
```

### `ITEMS/Rectangle3_1` . **X**  _(Rectangle@2.3.0)_
```powerfx
(41)*((App.Width/640))
```

### `ITEMS/Rectangle3_1` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(327)*((App.Height/1136))
```

### `ITEMS/Rectangle3_2` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Rectangle3_2` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_2` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/Rectangle3_2` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_2` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ITEMS/Rectangle3_2` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Rectangle3_2` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(564)*((App.Width/640))
```

### `ITEMS/Rectangle3_2` . **X**  _(Rectangle@2.3.0)_
```powerfx
(41)*((App.Width/640))
```

### `ITEMS/Rectangle3_2` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(359)*((App.Height/1136))
```

### `ITEMS/Rectangle3_3` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Rectangle3_3` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_3` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/Rectangle3_3` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_3` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ITEMS/Rectangle3_3` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Rectangle3_3` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(564)*((App.Width/640))
```

### `ITEMS/Rectangle3_3` . **X**  _(Rectangle@2.3.0)_
```powerfx
(41)*((App.Width/640))
```

### `ITEMS/Rectangle3_3` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(389)*((App.Height/1136))
```

### `ITEMS/Rectangle3_4` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Rectangle3_4` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_4` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/Rectangle3_4` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_4` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ITEMS/Rectangle3_4` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Rectangle3_4` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(564)*((App.Width/640))
```

### `ITEMS/Rectangle3_4` . **X**  _(Rectangle@2.3.0)_
```powerfx
(41)*((App.Width/640))
```

### `ITEMS/Rectangle3_4` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(418)*((App.Height/1136))
```

### `ITEMS/Label3_4` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_4` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_4` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_4` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_4` . **Height**  _(Label@2.5.1)_
```powerfx
(20)*((App.Height/1136))
```

### `ITEMS/Label3_4` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_4` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_4` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_4` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_4` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_4` . **Text**  _(Label@2.5.1)_
```powerfx
"Tавиур"
```

### `ITEMS/Label3_4` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label3_4` . **Width**  _(Label@2.5.1)_
```powerfx
(271)*((App.Width/640))
```

### `ITEMS/Label3_4` . **X**  _(Label@2.5.1)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/Label3_4` . **Y**  _(Label@2.5.1)_
```powerfx
(394)*((App.Height/1136))
```

### `ITEMS/Rectangle2` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Rectangle2` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Rectangle2` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle2` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/Rectangle2` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle2` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(40)*((App.Height/1136))
```

### `ITEMS/Rectangle2` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(206)*((App.Width/640))
```

### `ITEMS/Rectangle2` . **X**  _(Rectangle@2.3.0)_
```powerfx
(396)*((App.Width/640))
```

### `ITEMS/Rectangle2` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(788)*((App.Height/1136))
```

### `ITEMS/Label3_6` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label3_6` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_6` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_6` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_6` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_6` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label3_6` . **Height**  _(Label@2.5.1)_
```powerfx
(37)*((App.Height/1136))
```

### `ITEMS/Label3_6` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_6` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_6` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_6` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_6` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_6` . **Text**  _(Label@2.5.1)_
```powerfx
"✅ Тоологдсон тоо"
```

### `ITEMS/Label3_6` . **Width**  _(Label@2.5.1)_
```powerfx
(235)*((App.Width/640))
```

### `ITEMS/Label3_6` . **X**  _(Label@2.5.1)_
```powerfx
(38)*((App.Width/640))
```

### `ITEMS/Label3_6` . **Y**  _(Label@2.5.1)_
```powerfx
(791)*((App.Height/1136))
```

### `ITEMS/Label3_7` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label3_7` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label3_7` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_7` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_7` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/Label3_7` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_7` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_7` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ITEMS/Label3_7` . **Height**  _(Label@2.5.1)_
```powerfx
(36)*((App.Height/1136))
```

### `ITEMS/Label3_7` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_7` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_7` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_7` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_7` . **Size**  _(Label@2.5.1)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_7` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(varItem) || CountRows(Filter(InventoryCount, ItemNo = varItem.number)) = 0,
    "-",
    Text(
        Sum(
            Filter(
                InventoryCount,
                ItemNo = varItem.number
            ),
            CountQty
        ),
        "#,##0"
    )
)
```

### `ITEMS/Label3_7` . **Width**  _(Label@2.5.1)_
```powerfx
(192)*((App.Width/640))
```

### `ITEMS/Label3_7` . **X**  _(Label@2.5.1)_
```powerfx
(408)*((App.Width/640))
```

### `ITEMS/Label3_7` . **Y**  _(Label@2.5.1)_
```powerfx
(791)*((App.Height/1136))
```

### `ITEMS/Button1` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Button1` . **BorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.Fill, -15%)
```

### `ITEMS/Button1` . **BorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Button1` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/Button1` . **DisabledBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(166, 166, 166, 1)
```

### `ITEMS/Button1` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Button1` . **FocusedBorderThickness**  _(Classic/Button@2.2.0)_
```powerfx
(4)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Button1` . **Font**  _(Classic/Button@2.2.0)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Button1` . **Height**  _(Classic/Button@2.2.0)_
```powerfx
(58)*((App.Height/1136))
```

### `ITEMS/Button1` . **HoverBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(Self.BorderColor, 20%)
```

### `ITEMS/Button1` . **HoverColor**  _(Classic/Button@2.2.0)_
```powerfx
RGBA(255, 255, 255, 1)
```

### `ITEMS/Button1` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorFade(RGBA(211, 66, 9, 1), -20%)
```

### `ITEMS/Button1` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Notify("Тооллого бүртгэхдээ агуулахаа сонгож, нэгдсэн тооллогын дэлгэцийг ашиглана уу.",NotificationType.Information);Navigate(scrWarehouses,ScreenTransition.None)
```

### `ITEMS/Button1` . **PressedBorderColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ITEMS/Button1` . **PressedColor**  _(Classic/Button@2.2.0)_
```powerfx
Self.Fill
```

### `ITEMS/Button1` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
Self.Color
```

### `ITEMS/Button1` . **RadiusBottomLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Button1` . **RadiusBottomRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Button1` . **RadiusTopLeft**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Button1` . **RadiusTopRight**  _(Classic/Button@2.2.0)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Button1` . **Size**  _(Classic/Button@2.2.0)_
```powerfx
(24)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Button1` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Хадгалах"
```

### `ITEMS/Button1` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
(569)*((App.Width/640))
```

### `ITEMS/Button1` . **X**  _(Classic/Button@2.2.0)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/Button1` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
(951)*((App.Height/1136))
```

### `ITEMS/Label9_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label9_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label9_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label9_1` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Label9_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label9_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label9_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label9_1` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((App.Height/1136))
```

### `ITEMS/Label9_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label9_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label9_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label9_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label9_1` . **Size**  _(Label@2.5.1)_
```powerfx
(18)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label9_1` . **Text**  _(Label@2.5.1)_
```powerfx
"📊 Тооллогын мэдээлэл"
```

### `ITEMS/Label9_1` . **Width**  _(Label@2.5.1)_
```powerfx
(484)*((App.Width/640))
```

### `ITEMS/Label9_1` . **X**  _(Label@2.5.1)_
```powerfx
(32)*((App.Width/640))
```

### `ITEMS/Label9_1` . **Y**  _(Label@2.5.1)_
```powerfx
(706)*((App.Height/1136))
```

### `ITEMS/Label10` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label10` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label10` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label10` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label10` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label10` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label10` . **Height**  _(Label@2.5.1)_
```powerfx
(30)*((App.Height/1136))
```

### `ITEMS/Label10` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label10` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label10` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label10` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label10` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label10` . **Text**  _(Label@2.5.1)_
```powerfx
"🔢 Тооллого Зөрүү"
```

### `ITEMS/Label10` . **Width**  _(Label@2.5.1)_
```powerfx
(249)*((App.Width/640))
```

### `ITEMS/Label10` . **X**  _(Label@2.5.1)_
```powerfx
(38)*((App.Width/640))
```

### `ITEMS/Label10` . **Y**  _(Label@2.5.1)_
```powerfx
(838)*((App.Height/1136))
```

### `ITEMS/Icon13` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Icon13` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon13` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon13` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(109, 49, 162, 1)
```

### `ITEMS/Icon13` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon13` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ITEMS/Icon13` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Save
```

### `ITEMS/Icon13` . **OnSelect**  _(Classic/Icon@2.5.0)_
```powerfx
Set(
    varUploadPicture,
    Substitute(
        JSON(
            Image8.Image,
            JSONFormat.IncludeBinaryData
        ),
        """",
        ""
    )
);

If(
    StartsWith(varUploadPicture, "data:image"),
    
    IfError(
        'PowerAppV2->Getrecord(V3)'.Run(
            varItem.number,
            varUploadPicture
        ),
        
        Notify(
            "Зураг хадгалахад алдаа гарлаа",
            NotificationType.Error
        ),
        
        Notify(
            "Зураг BC-д амжилттай хадгалагдлаа",
            NotificationType.Success
        )
    ),
    
    Notify(
        "Зураг Base64 формат руу хөрвөөгүй байна",
        NotificationType.Error
    )
)
```

### `ITEMS/Icon13` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(52)*((App.Width/640))
```

### `ITEMS/Icon13` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(473)*((App.Width/640))
```

### `ITEMS/Icon13` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(591)*((App.Height/1136))
```

### `ITEMS/Image8` . **Visible**  _(Image@2.2.3)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Image8` . **BorderColor**  _(Image@2.2.3)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Image8` . **BorderThickness**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Image8` . **FocusedBorderThickness**  _(Image@2.2.3)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Image8` . **Height**  _(Image@2.2.3)_
```powerfx
(194)*((App.Height/1136))
```

### `ITEMS/Image8` . **Image**  _(Image@2.2.3)_
```powerfx
If(
    !IsBlank(varNewPicture),
    varNewPicture,
    varItemPicture
)
```

### `ITEMS/Image8` . **OnSelect**  _(Image@2.2.3)_
```powerfx
If(
    !IsBlank(varNewPicture),
    varNewPicture,
    varItemPicture
)
```

### `ITEMS/Image8` . **PaddingBottom**  _(Image@2.2.3)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Image8` . **PaddingLeft**  _(Image@2.2.3)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Image8` . **PaddingRight**  _(Image@2.2.3)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Image8` . **PaddingTop**  _(Image@2.2.3)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Image8` . **RadiusBottomLeft**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Image8` . **RadiusBottomRight**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Image8` . **RadiusTopLeft**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Image8` . **RadiusTopRight**  _(Image@2.2.3)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Image8` . **Width**  _(Image@2.2.3)_
```powerfx
(307)*((App.Width/640))
```

### `ITEMS/Image8` . **X**  _(Image@2.2.3)_
```powerfx
(63)*((App.Width/640))
```

### `ITEMS/Image8` . **Y**  _(Image@2.2.3)_
```powerfx
(481)*((App.Height/1136))
```

### `ITEMS/AddMediaButton2` . **Visible**  _(AddMedia@2.2.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/AddMediaButton2` . **Align**  _(AddMedia@2.2.1)_
```powerfx
Align.Right
```

### `ITEMS/AddMediaButton2` . **BorderColor**  _(AddMedia@2.2.1)_
```powerfx
RGBA(111,73,224,1)
```

### `ITEMS/AddMediaButton2` . **BorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/AddMediaButton2` . **ChangePictureText**  _(AddMedia@2.2.1)_
```powerfx
"ЗУРАГ АВАХ"
```

### `ITEMS/AddMediaButton2` . **Color**  _(AddMedia@2.2.1)_
```powerfx
Color.White
```

### `ITEMS/AddMediaButton2` . **Fill**  _(AddMedia@2.2.1)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/AddMediaButton2` . **FocusedBorderThickness**  _(AddMedia@2.2.1)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/AddMediaButton2` . **Height**  _(AddMedia@2.2.1)_
```powerfx
(49)*((App.Height/1136))
```

### `ITEMS/AddMediaButton2` . **OnChange**  _(AddMedia@2.2.1)_
```powerfx
Set(varNewPicture, AddMediaButton2.Media)
```

### `ITEMS/AddMediaButton2` . **Size**  _(AddMedia@2.2.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/AddMediaButton2` . **Text**  _(AddMedia@2.2.1)_
```powerfx
"ЗУРАГ АВАХ"
```

### `ITEMS/AddMediaButton2` . **Width**  _(AddMedia@2.2.1)_
```powerfx
(111)*((App.Width/640))
```

### `ITEMS/AddMediaButton2` . **X**  _(AddMedia@2.2.1)_
```powerfx
(444)*((App.Width/640))
```

### `ITEMS/AddMediaButton2` . **Y**  _(AddMedia@2.2.1)_
```powerfx
(525)*((App.Height/1136))
```

### `ITEMS/Icon16` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Icon16` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ITEMS/Icon16` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.History
```

### `ITEMS/Icon16` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Width/640))
```

### `ITEMS/Icon16` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(211)*((App.Width/640))
```

### `ITEMS/Icon16` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(1036)*((App.Height/1136))
```

### `ITEMS/Icon16_1` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Icon16_1` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16_1` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16_1` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16_1` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16_1` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ITEMS/Icon16_1` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.TrendingUpwards
```

### `ITEMS/Icon16_1` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Icon16_1` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Icon16_1` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Icon16_1` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Icon16_1` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Width/640))
```

### `ITEMS/Icon16_1` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(375)*((App.Width/640))
```

### `ITEMS/Icon16_1` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(1036)*((App.Height/1136))
```

### `ITEMS/Icon16_2` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Icon16_2` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16_2` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16_2` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16_2` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16_2` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ITEMS/Icon16_2` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Settings
```

### `ITEMS/Icon16_2` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Icon16_2` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Icon16_2` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Icon16_2` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Icon16_2` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Width/640))
```

### `ITEMS/Icon16_2` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(549)*((App.Width/640))
```

### `ITEMS/Icon16_2` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(1036)*((App.Height/1136))
```

### `ITEMS/Icon16_3` . **Visible**  _(Classic/Icon@2.5.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Icon16_3` . **BorderColor**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16_3` . **BorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16_3` . **Color**  _(Classic/Icon@2.5.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Icon16_3` . **FocusedBorderThickness**  _(Classic/Icon@2.5.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Icon16_3` . **Height**  _(Classic/Icon@2.5.0)_
```powerfx
(44)*((App.Height/1136))
```

### `ITEMS/Icon16_3` . **Icon**  _(Classic/Icon@2.5.0)_
```powerfx
Icon.Scan
```

### `ITEMS/Icon16_3` . **PaddingBottom**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Icon16_3` . **PaddingLeft**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Icon16_3` . **PaddingRight**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Width/640))
```

### `ITEMS/Icon16_3` . **PaddingTop**  _(Classic/Icon@2.5.0)_
```powerfx
(0)*((App.Height/1136))
```

### `ITEMS/Icon16_3` . **Width**  _(Classic/Icon@2.5.0)_
```powerfx
(32)*((App.Width/640))
```

### `ITEMS/Icon16_3` . **X**  _(Classic/Icon@2.5.0)_
```powerfx
(55)*((App.Width/640))
```

### `ITEMS/Icon16_3` . **Y**  _(Classic/Icon@2.5.0)_
```powerfx
(1036)*((App.Height/1136))
```

### `ITEMS/Label17` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label17` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label17` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label17` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label17` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(109, 49, 162, 1)
```

### `ITEMS/Label17` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label17` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label17` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label17` . **Height**  _(Label@2.5.1)_
```powerfx
(49)*((App.Height/1136))
```

### `ITEMS/Label17` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label17` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label17` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label17` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label17` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label17` . **Text**  _(Label@2.5.1)_
```powerfx
"ЗУРАГ UPLOAD"
```

### `ITEMS/Label17` . **Width**  _(Label@2.5.1)_
```powerfx
(143)*((App.Width/640))
```

### `ITEMS/Label17` . **X**  _(Label@2.5.1)_
```powerfx
(421)*((App.Width/640))
```

### `ITEMS/Label17` . **Y**  _(Label@2.5.1)_
```powerfx
(629)*((App.Height/1136))
```

### `ITEMS/Label18` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label18` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label18` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label18` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label18` . **Color**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(varItem),
    RGBA(100,100,100,1),
    With(
        {
            openingQty:
                LookUp(
                    'itemLedgerEntries (microsoft/analytics/v1.0)',
                    'Item No.' = varItem.number
                ).Quantity,
            countedQty:
                Sum(
                    Filter(
                        InventoryCount,
                        ItemNo = varItem.number
                    ),
                    CountQty
                )
        },
        With(
            {
                diff: countedQty - openingQty
            },
            If(
                diff = 0,
                RGBA(22,163,74,1),
                diff > 0,
                RGBA(217,119,6,1),
                RGBA(220,38,38,1)
            )
        )
    )
)
```

### `ITEMS/Label18` . **Fill**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(varItem),
    RGBA(245,245,245,1),
    With(
        {
            openingQty:
                LookUp(
                    'itemLedgerEntries (microsoft/analytics/v1.0)',
                    'Item No.' = varItem.number
                ).Quantity,
            countedQty:
                Sum(
                    Filter(
                        InventoryCount,
                        ItemNo = varItem.number
                    ),
                    CountQty
                )
        },
        With(
            {
                diff: countedQty - openingQty
            },
            If(
                diff = 0,
                RGBA(220,252,231,1),
                diff > 0,
                RGBA(255,243,205,1),
                RGBA(254,226,226,1)
            )
        )
    )
)
```

### `ITEMS/Label18` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label18` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label18` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ITEMS/Label18` . **Height**  _(Label@2.5.1)_
```powerfx
(39)*((App.Height/1136))
```

### `ITEMS/Label18` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label18` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label18` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label18` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label18` . **Size**  _(Label@2.5.1)_
```powerfx
(21)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label18` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) ||
    IsBlank(varItem) ||
    CountRows(
        Filter(
            InventoryCount,
            ItemNo = varItem.number
        )
    ) = 0,
    "-",
    With(
        {
            openingQty:
                LookUp(
                    'itemLedgerEntries (microsoft/analytics/v1.0)',
                    'Item No.' = varItem.number
                ).Quantity,

            countedQty:
                Sum(
                    Filter(
                        InventoryCount,
                        ItemNo = varItem.number
                    ),
                    CountQty
                )
        },
        With(
            {
                diff: countedQty - openingQty
            },
            If(
                diff > 0,
                "+" & Text(diff, "#,##0"),
                Text(diff, "#,##0")
            )
        )
    )
)
```

### `ITEMS/Label18` . **Width**  _(Label@2.5.1)_
```powerfx
(206)*((App.Width/640))
```

### `ITEMS/Label18` . **X**  _(Label@2.5.1)_
```powerfx
(396)*((App.Width/640))
```

### `ITEMS/Label18` . **Y**  _(Label@2.5.1)_
```powerfx
(833)*((App.Height/1136))
```

### `ITEMS/Label19_2` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label19_2` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ITEMS/Label19_2` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label19_2` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_2` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_2` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label19_2` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((App.Height/1136))
```

### `ITEMS/Label19_2` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19_2` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19_2` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19_2` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19_2` . **Size**  _(Label@2.5.1)_
```powerfx
(16)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_2` . **Text**  _(Label@2.5.1)_
```powerfx
"Тайлан"
```

### `ITEMS/Label19_2` . **Width**  _(Label@2.5.1)_
```powerfx
(87)*((App.Width/640))
```

### `ITEMS/Label19_2` . **X**  _(Label@2.5.1)_
```powerfx
(346)*((App.Width/640))
```

### `ITEMS/Label19_2` . **Y**  _(Label@2.5.1)_
```powerfx
(1080)*((App.Height/1136))
```

### `ITEMS/Label19` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label19` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ITEMS/Label19` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label19` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label19` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((App.Height/1136))
```

### `ITEMS/Label19` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19` . **Size**  _(Label@2.5.1)_
```powerfx
(16)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19` . **Text**  _(Label@2.5.1)_
```powerfx
"theme"
```

### `ITEMS/Label19` . **Width**  _(Label@2.5.1)_
```powerfx
(97)*((App.Width/640))
```

### `ITEMS/Label19` . **X**  _(Label@2.5.1)_
```powerfx
(24)*((App.Width/640))
```

### `ITEMS/Label19` . **Y**  _(Label@2.5.1)_
```powerfx
(1080)*((App.Height/1136))
```

### `ITEMS/Label19_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label19_1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ITEMS/Label19_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label19_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label19_1` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((App.Height/1136))
```

### `ITEMS/Label19_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19_1` . **Size**  _(Label@2.5.1)_
```powerfx
(16)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_1` . **Text**  _(Label@2.5.1)_
```powerfx
"Түүх"
```

### `ITEMS/Label19_1` . **Width**  _(Label@2.5.1)_
```powerfx
(77)*((App.Width/640))
```

### `ITEMS/Label19_1` . **X**  _(Label@2.5.1)_
```powerfx
(187)*((App.Width/640))
```

### `ITEMS/Label19_1` . **Y**  _(Label@2.5.1)_
```powerfx
(1080)*((App.Height/1136))
```

### `ITEMS/Label19_3` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (true)
```

### `ITEMS/Label19_3` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Center
```

### `ITEMS/Label19_3` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label19_3` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_3` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_3` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label19_3` . **Height**  _(Label@2.5.1)_
```powerfx
(38)*((App.Height/1136))
```

### `ITEMS/Label19_3` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19_3` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19_3` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label19_3` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label19_3` . **Size**  _(Label@2.5.1)_
```powerfx
(16)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label19_3` . **Text**  _(Label@2.5.1)_
```powerfx
"Тохиргоо"
```

### `ITEMS/Label19_3` . **Width**  _(Label@2.5.1)_
```powerfx
(120)*((App.Width/640))
```

### `ITEMS/Label19_3` . **X**  _(Label@2.5.1)_
```powerfx
(504)*((App.Width/640))
```

### `ITEMS/Label19_3` . **Y**  _(Label@2.5.1)_
```powerfx
(1080)*((App.Height/1136))
```

### `ITEMS/Rectangle3_5` . **BorderColor**  _(Rectangle@2.3.0)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Rectangle3_5` . **BorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_5` . **Fill**  _(Rectangle@2.3.0)_
```powerfx
RGBA(204, 231, 246, 1)
```

### `ITEMS/Rectangle3_5` . **FocusedBorderThickness**  _(Rectangle@2.3.0)_
```powerfx
(2)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Rectangle3_5` . **Height**  _(Rectangle@2.3.0)_
```powerfx
(1)*((App.Height/1136))
```

### `ITEMS/Rectangle3_5` . **Visible**  _(Rectangle@2.3.0)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Rectangle3_5` . **Width**  _(Rectangle@2.3.0)_
```powerfx
(564)*((App.Width/640))
```

### `ITEMS/Rectangle3_5` . **X**  _(Rectangle@2.3.0)_
```powerfx
(40)*((App.Width/640))
```

### `ITEMS/Rectangle3_5` . **Y**  _(Rectangle@2.3.0)_
```powerfx
(445)*((App.Height/1136))
```

### `ITEMS/Label8_1` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label8_1` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label8_1` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_1` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_1` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label8_1` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Bold
```

### `ITEMS/Label8_1` . **Height**  _(Label@2.5.1)_
```powerfx
(33)*((App.Height/1136))
```

### `ITEMS/Label8_1` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_1` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_1` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_1` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_1` . **Size**  _(Label@2.5.1)_
```powerfx
(14)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_1` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) || IsBlank(varItem),
    "-",
    varItem.number
)
```

### `ITEMS/Label8_1` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label8_1` . **Width**  _(Label@2.5.1)_
```powerfx
(167)*((App.Width/640))
```

### `ITEMS/Label8_1` . **X**  _(Label@2.5.1)_
```powerfx
(438)*((App.Width/640))
```

### `ITEMS/Label8_1` . **Y**  _(Label@2.5.1)_
```powerfx
(297)*((App.Height/1136))
```

### `ITEMS/Label3_25` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label3_25` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_25` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_25` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label3_25` . **Height**  _(Label@2.5.1)_
```powerfx
(14)*((App.Height/1136))
```

### `ITEMS/Label3_25` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_25` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_25` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label3_25` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label3_25` . **Size**  _(Label@2.5.1)_
```powerfx
(12)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label3_25` . **Text**  _(Label@2.5.1)_
```powerfx
"Хэмжих нэгж"
```

### `ITEMS/Label3_25` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label3_25` . **Width**  _(Label@2.5.1)_
```powerfx
(271)*((App.Width/640))
```

### `ITEMS/Label3_25` . **X**  _(Label@2.5.1)_
```powerfx
(36)*((App.Width/640))
```

### `ITEMS/Label3_25` . **Y**  _(Label@2.5.1)_
```powerfx
(425)*((App.Height/1136))
```

### `ITEMS/Label8_23` . **Align**  _(Label@2.5.1)_
```powerfx
Align.Right
```

### `ITEMS/Label8_23` . **BorderColor**  _(Label@2.5.1)_
```powerfx
RGBA(131, 24, 75, 1)
```

### `ITEMS/Label8_23` . **BorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_23` . **Color**  _(Label@2.5.1)_
```powerfx
RGBA(9, 33, 98, 1)
```

### `ITEMS/Label8_23` . **FocusedBorderThickness**  _(Label@2.5.1)_
```powerfx
(0)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_23` . **Font**  _(Label@2.5.1)_
```powerfx
Font.'Open Sans'
```

### `ITEMS/Label8_23` . **FontWeight**  _(Label@2.5.1)_
```powerfx
FontWeight.Semibold
```

### `ITEMS/Label8_23` . **Height**  _(Label@2.5.1)_
```powerfx
(27)*((App.Height/1136))
```

### `ITEMS/Label8_23` . **PaddingBottom**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_23` . **PaddingLeft**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_23` . **PaddingRight**  _(Label@2.5.1)_
```powerfx
(5)*((App.Width/640))
```

### `ITEMS/Label8_23` . **PaddingTop**  _(Label@2.5.1)_
```powerfx
(5)*((App.Height/1136))
```

### `ITEMS/Label8_23` . **Size**  _(Label@2.5.1)_
```powerfx
(10)*(Min(App.Width/640,App.Height/1136))
```

### `ITEMS/Label8_23` . **Text**  _(Label@2.5.1)_
```powerfx
If(
    IsBlank(Trim(txtSearch.Text)) || IsBlank(varItem),
    "-",
    LookUp(
        'itemLedgerEntries (microsoft/analytics/v1.0)',
        'Item No.' = varItem.number
    ).'Unit of Measure Code'
)
```

### `ITEMS/Label8_23` . **Visible**  _(Label@2.5.1)_
```powerfx
((Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))) && (IsBlank(Trim(txtSearch.Text)) ||
(
    varJustSelected &&
    txtSearch.Text = varBarcodeText
))
```

### `ITEMS/Label8_23` . **Width**  _(Label@2.5.1)_
```powerfx
(168)*((App.Width/640))
```

### `ITEMS/Label8_23` . **X**  _(Label@2.5.1)_
```powerfx
(437)*((App.Width/640))
```

### `ITEMS/Label8_23` . **Y**  _(Label@2.5.1)_
```powerfx
(419)*((App.Height/1136))
```

### `ITEMS/pgDenied1148` . **X**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Width-320)/2)
```

### `ITEMS/pgDenied1148` . **Y**  _(Classic/Button@2.2.0)_
```powerfx
Max(12,(Parent.Height-76)/2)
```

### `ITEMS/pgDenied1148` . **Width**  _(Classic/Button@2.2.0)_
```powerfx
Min(320,Parent.Width-24)
```

### `ITEMS/pgDenied1148` . **Color**  _(Classic/Button@2.2.0)_
```powerfx
Color.White
```

### `ITEMS/pgDenied1148` . **Fill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#202225")
```

### `ITEMS/pgDenied1148` . **HoverFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFF0E6")
```

### `ITEMS/pgDenied1148` . **PressedFill**  _(Classic/Button@2.2.0)_
```powerfx
ColorValue("#FFD8C2")
```

### `ITEMS/pgDenied1148` . **Text**  _(Classic/Button@2.2.0)_
```powerfx
"Энэ хуудасны эрх холбогдоогүй · Профайл"
```

### `ITEMS/pgDenied1148` . **Visible**  _(Classic/Button@2.2.0)_
```powerfx
!(Lower(User().Email)="od.u@tme.mn" || (pgAccess.Active && (IsBlank(pgAccess.ExpiresAt) || pgAccess.ExpiresAt>Now()) && "|count|" in pgAccess.Title && !IsBlank(pgAccess.LocationCode)))
```

### `ITEMS/pgDenied1148` . **OnSelect**  _(Classic/Button@2.2.0)_
```powerfx
Set(varPView,"profile");Navigate(ScrAccess,ScreenTransition.Fade)
```

