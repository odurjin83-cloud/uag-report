# ҮАГ Систем — Deploy хийх заавар

Энэ апп нь **Flask (Python) + SQLite + зураг upload** ашигладаг тул **Netlify дээр
ажиллахгүй** (Netlify зөвхөн статик сайт болон богино хугацааны serverless функц
дэмждэг тул өгөгдлийн сан болон хавсаргасан зургийг байнга хадгалж чадахгүй).

Үүний оронд Python апп-ыг шууд дэмждэг үнэгүй/хямд хостинг ашиглахыг санал болгож
байна: **Render.com** (хамгийн хялбар), эсвэл **Railway.app** / **PythonAnywhere**.

---

## Render.com дээр deploy хийх (санал болгож буй арга)

1. https://render.com дээр бүртгүүлнэ (GitHub-аар нэвтэрч болно).
2. Энэ zip доторх файлуудыг GitHub дээрх шинэ repo-д хуулна (эсвэл Render дээр
   "Deploy from a Git repository" сонголтын оронд шууд zip-аас **"Public Git
   repository"**-г алгасаад доорх **"Blueprint" биш, энгийн Web Service**-ийг
   ашиглана):
   - New → Web Service → холбогдох GitHub repo-г сонгоно.
3. Тохиргоо:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (Procfile-д бас бичигдсэн)
   - **Environment**: Python 3
4. "Environment Variables" хэсэгт (заавал биш ч санал болгож байна):
   - `SECRET_KEY` = өөрийн санамсаргүй урт тэмдэгт мөр
5. **Deploy** дарна. Хэдэн минутын дараа `https://<app-name>.onrender.com`
   хаягаар апп ажиллана.

> ⚠️ Анхаар: Render-ийн үнэгүй төлөвлөгөө дээр диск нь "ephemeral" (сэргэхэд
> устдаг) тул `uag_reports_system.db` болон `static/uploads/` доtorh зургууд
> apп дахин deploy/restart хийх бүрт устаж болзошгүй. Байнгын хадгалалт хэрэгтэй
> бол Render-ийн **Persistent Disk**-г нэмж холбох (Settings → Disks) эсвэл
> өгөгдлийн санг PostgreSQL мэт удирдлагатай DB руу шилжүүлэх шаардлагатай.

## Railway.app / PythonAnywhere дээр

- **Railway**: GitHub repo-г холбоод "Deploy" дарахад л Procfile-г танина.
- **PythonAnywhere**: Web tab → Flask app бүртгээд, `app.py`-г заана. Файлын
  сан (uploads) болон SQLite нь PythonAnywhere дээр байнга хадгалагдана (энэ нь
  Render-ийн үнэгүй төлөвлөгөөнөөс давуу тал).

---

## Локал компьютер дээр турших

```bash
pip install -r requirements.txt
python app.py
```

Апп `http://127.0.0.1:5000` дээр ажиллана.
Анхны админ хэрэглэгч: **admin@uag.mn** / **123456**

---

## Netlify тухай нэмэлт тайлбар

Хэрэв ирээдүйд Netlify (эсвэл Vercel гэх мэт "serverless-first" платформ) дээр
заавал байршуулах шаардлагатай бол дараах том өөрчлөлтүүд хэрэгтэй болно:
- SQLite-г Postgres/Supabase/Turso зэрэг удирдлагатай DB руу шилжүүлэх
- `static/uploads/`-д хадгалдаг зургийг S3, Cloudinary зэрэг гадаад storage руу
  шилжүүлэх
- Flask route-уудыг Netlify Functions (эсвэл FastAPI+Mangum маягийн) хэлбэрт
  дахин зохион байгуулах

Энэ бол цоо шинэ архитектур зохион байгуулалт шаардсан том ажил тул одоогийн
zip-д ороогүй болно.
