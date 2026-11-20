# Засвар 2 — Flow талд эрхээр шүүх (техникийн шаардлага)

**Асуудал:** `App.OnStart` (`App.pa.yaml:438–452`) болон `нүүр`, `ScrCountHome`, `ScrAccess.phoneProfileSync` дээр
`ClearCollect(colOfflineStock,colAutoStockV16)` / `ClearCollect(colOfflineBins,colAutoBinsV16)` нь flow-оос ирсэн **бүх мөрийг**
санах ойд хадгалдаг. Аппын эрхийн шүүлт зөвхөн дискэнд бичих хуулбарт (`colAclAutoStockV16Disk`) үйлчилнэ.
Аппын шүүлт аюулгүй байдлын хил биш — хэрэглэгч Monitor/хөгжүүлэгчийн хэрэгслээр хүсэлтийн хариуг харж чадна.
**Хил нь flow/сервер байх ёстой.**

Хамаарах flow-ууд: `PA_GetStockFromExcel`, `PA_GetAllBinsOffline` (заавал), `PA_GetItemsSnapshot` (өртгийн талбарын хувьд, сонголттой).

## 1. Хэрэглэгчийг тодорхойлох
- Хэрэглэгчийг **параметрээр БҮҮ авна**. Power Apps (V2) trigger-ийн толгойгоос авна:
  `toLower(trim(triggerOutputs()?['headers']?['x-ms-user-email']))`
- Хоосон бол → `403`-тэй адил хариу (`{"ok":false,"code":"no_identity","stockjson":"[]","rowCount":0}`), өгөгдөл буцаахгүй.

## 2. Эрхийг серверээс унших
- SharePoint `AssetUserAccess`-ээс: `CompanyCode = 'TME-Inventory-Pages'` ба `UserEmail = <дээрх и-мэйл>`.
- Шаардлага: `Active = true`, `ExpiresAt` хоосон эсвэл `> utcNow()`, `Title`-д `|count|` (эсвэл тооллого/үлдэгдэлтэй холбоотой хуудасны түлхүүр) байна.
- Зөвшөөрөгдсөн агуулах: `LocationCode = "*"` → бүгд; эсвэл `"|A|B|"` хэлбэрээс жагсаалт.
- Олдохгүй / идэвхгүй / хугацаа дууссан → `{"ok":false,"code":"denied", ... ,"rowCount":0}`; **ямар ч мөр буцаахгүй**.
- **Hard-code админ и-мэйлийг flow-д бүү хуулаарай.** Админыг `AssetUserAccess`-д `LocationCode="*"` мөрөөр (эсвэл Entra ID бүлгээр) тодорхойлно. (Аппын кодын hard-code-ийг дараагийн шатанд арилгана.)

## 3. Шүүлтийг flow дотор хийх
- Excel-ийн мөрүүдийг (Filter array) `locationCode` нь зөвшөөрөгдсөн жагсаалтад байгаагаар шүүнэ. Зөвхөн шүүсэн мөрийг `stockjson`/`binsjson`-д хийнэ.
- Харьцуулалтыг `toUpper(trim(...))`-ээр хийнэ (аппын `Upper(...)` дүрэмтэй ижил).

## 4. Хариуны гэрээ (апп дараагийн шатанд шалгана)
```json
{
  "ok": true,
  "stockjson": "[{\"itemNo\":\"00123\",\"locationCode\":\"P-MAIN\",\"quantity\":12.5}]",
  "rowCount": 4287,
  "asOf": "2026-11-20T09:00:00Z",
  "scope": "|P-MAIN|P-OM|",
  "source": "Excel"
}
```
- `rowCount` = **шүүсний дараах** мөрийн тоо. `asOf` = Excel өгөгдөл үүссэн бодит цаг (flow ажилласан цаг биш).
- `itemNo`-г **string** хэлбэрээр (тэргүүлэх 0 хадгалагдана).

## 5. Өгөгдлийн чанар (олдвор 3-тай холбоотой)
- Excel "List rows" дээр **Pagination ON**, Threshold ≥ нийт мөрийн тоо (жишээ 100000).
- `itemNo + locationCode (+ binCode)` давхардсан мөрийг илрүүлнэ:
  - Тавиураар хуваасан үлдэгдэл бол түлхүүрт `binCode` орно — давхардал биш.
  - Жинхэнэ давхардал (ижил түлхүүр, тавиургүй) бол `{"ok":false,"code":"duplicate_rows","duplicates":[...]}` буцааж, апп хуучин баталгаатай snapshot-оо хэвээр үлдээнэ.
- Хоосон `itemNo`/`locationCode` мөрийг хасаж, тоог `skipped`-д буцаана.

## 6. Холболт ба ажиллуулах эрх
- Flow-ийн Excel/SharePoint холболт эзэмшигчийн нэрээр ажиллавал хэрэглэгч flow-ийг өөр параметрээр дуудаж бусдын өгөгдлийг авч чадахгүй байх ёстой — тиймээс 1–3-р алхам заавал.
- Run-only users тохиргоог зөвхөн шаардлагатай бүлэгт өгнө.

## 7. Хүлээн авах тест (дэлгэцийг биш, flow-ийн хариуг шалгана)
1. Зөвхөн нэг агуулахын эрхтэй туршилтын хэрэглэгчээр апп нээнэ → Power Automate → Run history → тухайн run-ий **Response output**-ыг нээнэ → өөр агуулахын **нэг ч** мөр байхгүй.
2. Эрхийг идэвхгүй болгоод дахин ажиллуулна → `denied`, `rowCount: 0`.
3. `ExpiresAt`-ийг өнгөрсөн болгоно → `denied`.
4. `LocationCode="*"` админ хэрэглэгч → бүх мөр, `rowCount` = Excel-ийн нийт (давхардалгүй) мөр.
5. Excel-д нэг мөрийг санаатай давхардуулна → `duplicate_rows`.

## Хавсралт — Зарлагын `TMEA25IssueAsCaller`
- `enqueue` горимд ижил `id` дахин ирвэл **шинэ ноорог үүсгэхгүй**, өмнөх хүсэлтийн төлөвийг буцаана (idempotency). Аппын durable outbox үүн дээр тулгуурладаг.
