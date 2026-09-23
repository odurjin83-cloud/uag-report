import os
import sqlite3
import csv
import io
import uuid
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, render_template_string, request, redirect, url_for, session, Response, send_file, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.dml.color import RGBColor

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --------------------------------------------------
# PDF fonts: reportlab's built-in base14 fonts (Helvetica etc.) do NOT
# include Cyrillic glyphs, so Mongolian text would render as blanks.
# We register a Unicode TTF (DejaVu Sans, which ships on most Linux
# systems) when we can find one, and fall back gracefully otherwise.
# --------------------------------------------------
_PDF_FONT_CANDIDATES = [
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
     "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"),
    ("C:\\Windows\\Fonts\\arial.ttf", "C:\\Windows\\Fonts\\arialbd.ttf"),
    ("/Library/Fonts/Arial.ttf", "/Library/Fonts/Arial Bold.ttf"),
    ("/System/Library/Fonts/Supplemental/Arial.ttf",
     "/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
]

def _register_pdf_fonts():
    for regular_path, bold_path in _PDF_FONT_CANDIDATES:
        if os.path.exists(regular_path) and os.path.exists(bold_path):
            try:
                pdfmetrics.registerFont(TTFont('UAGFont', regular_path))
                pdfmetrics.registerFont(TTFont('UAGFont-Bold', bold_path))
                return 'UAGFont', 'UAGFont-Bold'
            except Exception:
                continue
    # No Cyrillic-capable font found on this machine: fall back to the
    # built-in fonts. Mongolian text will not render correctly, but the
    # PDF will still generate instead of crashing.
    return 'Helvetica', 'Helvetica-Bold'

PDF_FONT, PDF_FONT_BOLD = _register_pdf_fonts()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "uag_master_system_key_2026_v4")
DB_NAME = "uag_reports_system.db"

# --------------------------------------------------
# Зураг (attachment) upload тохиргоо: ажлын гүйцэтгэлийг нотлох зураг
# хавсаргах боломж. Файлууд static/uploads/ дор өвөрмөц нэртэй (uuid)
# хадгалагдана, DB-д зөвхөн файлын нэрийг хадгална.
# --------------------------------------------------
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB нийт request хэмжээ
ALLOWED_IMAGE_EXT = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def _allowed_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXT

def _save_attachment(file_storage):
    """FileStorage -> saved unique filename (str) or None if empty/invalid."""
    if not file_storage or not file_storage.filename:
        return None
    original = secure_filename(file_storage.filename)
    if not original or not _allowed_image(original):
        return None
    ext = original.rsplit('.', 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex}.{ext}"
    file_storage.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_name))
    return unique_name

def _delete_attachment_file(filename):
    if not filename:
        return
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.isfile(path):
        try:
            os.remove(path)
        except OSError:
            pass

DEPARTMENTS = [
    "ЗОНХХэлтэс",
    "Хуулийн хэлтэс",
    "ХУТЗХэлтэс",
    "МТХэлтэс",
    "Кемпийн үйл ажиллагаа"
]

# --------------------------------------------------
# Chиг үүрэг (category) -> department mapping used to seed / migrate
# the categories table. This is the fix for the bug where every
# department's dropdown showed the same (originally ЗОНХХэлтэс-only)
# categories: each category now belongs to exactly one department.
# --------------------------------------------------
DEPARTMENT_CATEGORY_MAP = {
    "МТХэлтэс": [
        "Төв оффисийн ажлууд",
        "Төслийн талбайн ажлууд",
        "ERP / Help desk",
        "Дэд бүтэц / Интеграци",
    ],
    "ЗОНХХэлтэс": [
        "Архив, албан хэрэг хөтлөлт",
        "PR, олон нийт",
        "Газрын харилцаа",
        "Орон нутаг",
        "Үйл ажиллагаа, арга хэмжээ",
        "Захиргааны бусад ажил",
    ],
    "Хуулийн хэлтэс": [
        "Хууль зүйн зөвлөгөө",
        "Гэрээний хяналт",
        "Дүрэм, журам, тушаалын хяналт",
        "Хууль тогтоомжийн мэдээлэл",
    ],
    "ХУТЗХэлтэс": [
        "Тээвэр зохицуулалт",
        "Техникийн үзлэг, аюулгүй байдал",
        "Худалдан авалт, хангамж",
        "Тохижилт, үйлчилгээ",
    ],
    "Кемпийн үйл ажиллагаа": [
        "Төв кемп",
        "Анхуй кэмп",
        "Панво кэмп",
    ],
}

# Old (pre-fix) global categories that need to be re-tagged to the
# correct department instead of being deleted, so existing report rows
# that reference them by name keep working.
LEGACY_CATEGORY_DEPARTMENT = {
    "Архив, албан хэрэг": "ЗОНХХэлтэс",
    "PR, олон нийт": "ЗОНХХэлтэс",
    "Газрын харилцаа": "ЗОНХХэлтэс",
    "Орон нутаг": "ЗОНХХэлтэс",
    "Захиргааны бусад ажил": "ЗОНХХэлтэс",
    "Төв кемп": "Кемпийн үйл ажиллагаа",
}

PROGRESS_BUCKETS = ["25%", "50%", "75%", "100%"]

# --------------------------------------------------
# DATABASE INITIALIZATION & MIGRATION
# --------------------------------------------------

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user',
            department TEXT
        )
    ''')

    cursor.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'department' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN department TEXT")

    # Categories Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')

    # Bug fix: categories had no department column, so every department's
    # dropdown showed the exact same (globally shared) list. Add the
    # column and re-tag any pre-existing rows to their correct department.
    cursor.execute("PRAGMA table_info(categories)")
    cat_columns = [col[1] for col in cursor.fetchall()]
    if 'department' not in cat_columns:
        cursor.execute("ALTER TABLE categories ADD COLUMN department TEXT")

    # Re-tag legacy (pre-fix) rows that still have no department.
    cursor.execute("SELECT id, name FROM categories WHERE department IS NULL OR department = ''")
    for cat_id, name in cursor.fetchall():
        dept = LEGACY_CATEGORY_DEPARTMENT.get(name, "ЗОНХХэлтэс")
        cursor.execute("UPDATE categories SET department = ? WHERE id = ?", (dept, cat_id))

    # Reports Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT NOT NULL,
            report_date TEXT NOT NULL,
            func_area TEXT NOT NULL,
            task_desc TEXT NOT NULL,
            task_result TEXT,
            progress TEXT NOT NULL,
            assignee TEXT,
            status TEXT DEFAULT 'submitted',
            created_at TEXT
        )
    ''')

    # Bug fix / feature: ажлын гүйцэтгэлийг нотлох ЗУРАГ хавсаргах баганыг нэмэв.
    cursor.execute("PRAGMA table_info(reports)")
    rep_columns = [col[1] for col in cursor.fetchall()]
    if 'attachment' not in rep_columns:
        cursor.execute("ALTER TABLE reports ADD COLUMN attachment TEXT")

    # Seed Admin User
    cursor.execute("SELECT id FROM users WHERE email = 'admin@uag.mn'")
    if not cursor.fetchone():
        hashed_pw = generate_password_hash('123456')
        cursor.execute("INSERT INTO users (email, password, role, department) VALUES ('admin@uag.mn', ?, 'admin', 'Бүх хэлтэс')", (hashed_pw,))

    # Seed the correct per-department categories (idempotent: existing
    # names are left untouched thanks to INSERT OR IGNORE on the UNIQUE
    # name column).
    for dept, cats in DEPARTMENT_CATEGORY_MAP.items():
        for cat in cats:
            cursor.execute("INSERT OR IGNORE INTO categories (name, department) VALUES (?, ?)", (cat, dept))

    conn.commit()
    conn.close()

init_db()

# ---------------------------------------------------------
# SECURITY & AUTH DECORATORS
# ---------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session or session.get('role') != 'admin':
            return "Хандах эрх хүрэлцэхгүй байна!", 403
        return f(*args, **kwargs)
    return decorated_function

def parse_progress(value):
    """'75%' -> 75, tolerant of missing/odd values."""
    try:
        return int(str(value).replace('%', '').strip())
    except (TypeError, ValueError):
        return 0

def date_range_from_preset(preset, start_date, end_date):
    today = datetime.now().date()
    if preset == 'this_week':
        start_dt = today - timedelta(days=today.weekday())
        end_dt = start_dt + timedelta(days=6)
        return start_dt.strftime('%Y-%m-%d'), end_dt.strftime('%Y-%m-%d')
    elif preset == 'last_week':
        start_dt = today - timedelta(days=today.weekday() + 7)
        end_dt = start_dt + timedelta(days=6)
        return start_dt.strftime('%Y-%m-%d'), end_dt.strftime('%Y-%m-%d')
    elif preset == 'this_month':
        start_dt = today.replace(day=1)
        return start_dt.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d')
    return start_date, end_date

# ---------------------------------------------------------
# HTML TEMPLATES & LAYOUT
# ---------------------------------------------------------
LAYOUT_HEADER = """
<!DOCTYPE html>
<html lang="mn" data-theme="{{ session.get('theme', 'dark') }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ҮАГ Систем</title>
    <!-- SheetJS (Excel боловсруулах сан) -->
    <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
    <style>
        :root {
            --bg-color: #f1f5f9;
            --card-bg: #ffffff;
            --text-color: #0f172a;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --primary-light: #eff6ff;
            --sidebar-bg: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
            --sidebar-border: rgba(255,255,255,0.08);
            --shadow-sm: 0 1px 2px rgba(15,23,42,0.06);
            --shadow-md: 0 4px 16px rgba(15,23,42,0.08);
            --radius: 14px;
        }

        [data-theme="dark"] {
            --bg-color: #0b1220;
            --card-bg: #161f2e;
            --text-color: #f1f5f9;
            --text-muted: #94a3b8;
            --border-color: #263042;
            --primary: #3b82f6;
            --primary-dark: #60a5fa;
            --primary-light: rgba(59,130,246,0.12);
            --sidebar-bg: linear-gradient(180deg, #0b1220 0%, #05080f 100%);
            --sidebar-border: rgba(255,255,255,0.06);
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 20px rgba(0,0,0,0.35);
        }

        * { box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg-color); color: var(--text-color); margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
        .wrapper { display: flex; min-height: 100vh; }
        .sidebar { width: 264px; background: var(--sidebar-bg); color: white; padding: 22px 18px; box-sizing: border-box; flex-shrink: 0; display: flex; flex-direction: column; justify-content: space-between; position: sticky; top: 0; height: 100vh; overflow-y: auto; }
        .sidebar h2 { font-size: 17px; letter-spacing: .2px; border-bottom: 1px solid var(--sidebar-border); padding-bottom: 16px; margin-top: 4px; margin-bottom: 14px; }
        .nav-link { display: flex; align-items: center; gap: 8px; color: #cbd5e1; padding: 10px 14px; border-radius: 10px; text-decoration: none; margin-bottom: 4px; font-size: 13.5px; font-weight: 500; transition: background .15s ease, color .15s ease, transform .1s ease; }
        .nav-link:hover { background: rgba(255,255,255,0.08); color: #fff; }
        .nav-link.active { background: var(--primary); color: white; box-shadow: 0 2px 10px rgba(37,99,235,0.4); }
        .content { flex: 1; padding: 28px 32px; box-sizing: border-box; overflow-x: auto; width: calc(100vw - 264px); }
        .card { background: var(--card-bg); border-radius: var(--radius); border: 1px solid var(--border-color); padding: 26px; margin-bottom: 22px; box-shadow: var(--shadow-sm); overflow: hidden; transition: box-shadow .2s ease; }
        .card h2, .card h3 { margin-top: 0; }
        .card h2 { font-size: 19px; }
        .card h3 { font-size: 16px; }

        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-top: 15px;
            table-layout: fixed;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow: hidden;
        }
        th, td {
            border-bottom: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            padding: 11px 10px;
            text-align: left;
            font-size: 13px;
            word-break: break-word;
            overflow-wrap: anywhere;
            vertical-align: middle;
        }
        th:last-child, td:last-child { border-right: none; }
        tr:last-child td { border-bottom: none; }
        th {
            background: var(--primary-light);
            color: var(--text-color);
            font-weight: 700;
            white-space: nowrap;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: .3px;
        }
        tbody tr { transition: background .12s ease; }
        tbody tr:hover { background: rgba(37,99,235,0.04); }

        input, select { width: 100%; padding: 9px 10px; border: 1px solid var(--border-color); border-radius: 8px; box-sizing: border-box; background: var(--card-bg); color: var(--text-color); font-family: inherit; font-size: 13.5px; transition: border-color .15s ease, box-shadow .15s ease; }
        input:focus, select:focus, textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px var(--primary-light); }

        textarea {
            width: 100%;
            padding: 8px 10px;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            box-sizing: border-box;
            background: var(--card-bg);
            color: var(--text-color);
            font-family: inherit;
            font-size: 13px;
            min-height: 42px;
            resize: none;
            overflow-y: hidden;
            line-height: 1.4;
        }

        .btn { padding: 9px 14px; border-radius: 8px; font-weight: 600; border: none; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 6px; font-size: 13px; text-align: center; white-space: nowrap; transition: transform .08s ease, filter .15s ease, box-shadow .15s ease; }
        .btn:hover { filter: brightness(1.08); }
        .btn:active { transform: translateY(1px); }
        .btn-primary { background: var(--primary); color: white; box-shadow: 0 2px 8px rgba(37,99,235,0.3); }
        .btn-success { background: #10b981; color: white; box-shadow: 0 2px 8px rgba(16,185,129,0.3); }
        .btn-warning { background: #f59e0b; color: white; box-shadow: 0 2px 8px rgba(245,158,11,0.3); }
        .btn-danger { background: #ef4444; color: white; box-shadow: 0 2px 8px rgba(239,68,68,0.3); }
        .btn-outline { background: transparent; border: 1px solid var(--border-color); color: var(--text-color); }
        .btn-outline:hover { background: var(--primary-light); border-color: var(--primary); }
        .btn-sm { padding: 5px 9px; font-size: 11px; margin: 2px; box-shadow: none; }

        .action-cell { display: flex; gap: 4px; align-items: center; justify-content: center; flex-wrap: nowrap; }

        .stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
        .stat-box { background: var(--primary-light); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid var(--border-color); }
        .stat-box h3 { margin: 0; font-size: 30px; color: var(--primary); font-weight: 800; }

        .badge { padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; display: inline-block; white-space: nowrap; }
        .badge-success { background: #d1fae5; color: #065f46; }
        .badge-info { background: #dbeafe; color: #1e40af; }
        .badge-locked { background: #475569; color: #f1f5f9; }
        .badge-admin { background: #fee2e2; color: #991b1b; }
        .badge-user { background: #e0e7ff; color: #3730a3; }

        .progress-bar-bg { width: 100%; background: #e2e8f0; height: 8px; border-radius: 4px; overflow: hidden; margin-top: 5px; }
        .progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--primary), var(--primary-dark)); }

        .filter-card { background: var(--primary-light); padding: 18px; border-radius: 12px; border: 1px solid var(--border-color); margin-top: 15px; }
        .quick-presets { display: flex; gap: 8px; margin-bottom: 12px; align-items: center; flex-wrap: wrap; }
        .preset-btn { background: var(--card-bg); border: 1px solid var(--border-color); padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; color: var(--text-color); text-decoration: none; transition: background .15s ease; }
        .preset-btn:hover { background: var(--primary-light); }
        .preset-btn.active { background: var(--primary); color: white; border-color: var(--primary); }

        .filter-form { display: flex; gap: 10px; flex-wrap: wrap; align-items: flex-end; }

        .attachment-thumb { width: 46px; height: 46px; object-fit: cover; border-radius: 8px; border: 1px solid var(--border-color); cursor: pointer; display: block; }
        .attachment-cell { display: flex; align-items: center; gap: 6px; }
        .attachment-empty { color: var(--text-muted); font-size: 12px; }
        .file-input-wrap { position: relative; }
        .file-input-wrap input[type=file] { padding: 6px; font-size: 11px; }
    </style>
</head>
<body>
<div class="wrapper">
    <div class="sidebar">
        <div>
            <h2>🏢 ҮАГ Систем</h2>
            <a href="/" class="nav-link {% if request.path == '/' %}active{% endif %}">📝 Тайлан оруулах</a>
            <a href="/analytics" class="nav-link {% if request.path == '/analytics' %}active{% endif %}">📊 Нийт Аналитик & Тооцоо</a>
            <a href="/report" class="nav-link {% if request.path == '/report' %}active{% endif %}">📑 Албан ёсны тайлан (PDF/PPTX)</a>

            <a href="/toggle_theme" class="nav-link" style="margin-top: 10px; background: rgba(255,255,255,0.05);">
                {% if session.get('theme') == 'light' %}🌙 Dark Theme{% else %}☀️ Light Theme{% endif %}
            </a>

            {% if session.get('role') == 'admin' %}
            <div style="font-size: 11px; text-transform: uppercase; color: #64748b; margin: 20px 0 5px 10px; font-weight: bold; letter-spacing: .5px;">АДМИН ПАНЕЛ</div>
            <a href="/admin?page=categories" class="nav-link {% if request.args.get('page') == 'categories' %}active{% endif %}">📋 Чиг үүрэг нэмэх</a>
            <a href="/admin?page=reports" class="nav-link {% if request.args.get('page') == 'reports' %}active{% endif %}">📂 Удирдлагын Нэгдсэн Тайлан</a>
            <a href="/admin?page=analytics" class="nav-link {% if request.args.get('page') == 'analytics' %}active{% endif %}">📊 Нэгдсэн Статистик</a>
            <a href="/admin?page=ai" class="nav-link {% if request.args.get('page') == 'ai' %}active{% endif %}">🤖 AI Дүгнэлт</a>
            <a href="/admin?page=others" class="nav-link {% if request.args.get('page') == 'others' %}active{% endif %}">👤 Хэрэглэгчдийн Удирдлага</a>
            {% endif %}
        </div>

        <div style="border-top: 1px solid var(--sidebar-border); padding-top: 15px; margin-top: 20px;">
            <div style="font-size: 12px; color: #94a3b8; font-weight: bold;">👤 {{ session.get('user') }}</div>
            <div style="font-size: 11px; color: #38bdf8; margin-top: 2px; margin-bottom: 10px;">🏢 {{ session.get('department', 'Бүх хэлтэс') }}</div>
            <a href="/logout" class="nav-link" style="color: #f87171; padding: 5px 0;">🚪 Гарах</a>
        </div>
    </div>
    <div class="content">
"""

LAYOUT_FOOTER = """
    </div>
</div>
<script>
    function autoResizeTextarea(el) {
        if (!el) return;
        el.style.height = 'auto';
        el.style.height = el.scrollHeight + 'px';
    }

    document.addEventListener('input', function (e) {
        if (e.target.tagName.toLowerCase() === 'textarea') {
            autoResizeTextarea(e.target);
        }
    });

    window.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('textarea').forEach(el => autoResizeTextarea(el));
    });

    function deleteAttachment(reportId, btnEl) {
        if (!confirm('Хавсаргасан зургийг устгах уу?')) return;
        fetch(`/report_attachment/delete/${reportId}`, { method: 'POST' })
            .then(r => r.json())
            .then(data => {
                if (data.ok) {
                    const cell = btnEl.closest('.attachment-cell');
                    if (cell) cell.outerHTML = '<span class="attachment-empty">—</span>';
                } else {
                    alert(data.error || 'Устгах явцад алдаа гарлаа.');
                }
            })
            .catch(() => alert('Сүлжээний алдаа гарлаа.'));
    }
</script>
</body>
</html>
"""

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="mn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Нэвтрэх - ҮАГ Систем</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: radial-gradient(circle at 20% 20%, #1e293b 0%, #0b1220 55%, #05080f 100%); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; color: #f8fafc; }
        .login-wrap { display: flex; flex-direction: column; align-items: center; gap: 18px; }
        .brand { display: flex; flex-direction: column; align-items: center; gap: 6px; color: #cbd5e1; }
        .brand .emoji { font-size: 34px; }
        .brand .title { font-size: 15px; font-weight: 700; letter-spacing: .4px; }
        .card { background: rgba(30,41,59,0.85); backdrop-filter: blur(6px); padding: 38px 34px; border-radius: 18px; box-shadow: 0 20px 50px rgba(0,0,0,0.45); width: 350px; border: 1px solid rgba(255,255,255,0.08); }
        .card h2 { text-align: center; margin: 0 0 22px; color: #f8fafc; font-size: 19px; }
        label { display: block; font-size: 12px; color: #94a3b8; font-weight: 600; margin-bottom: 6px; }
        .field { margin-bottom: 16px; }
        input { width: 100%; padding: 12px 13px; border: 1px solid #334155; border-radius: 9px; box-sizing: border-box; background: #0b1220; color: white; font-size: 14px; transition: border-color .15s ease, box-shadow .15s ease; }
        input:focus { outline: none; border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59,130,246,0.18); }
        button { width: 100%; padding: 12px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border: none; border-radius: 9px; font-weight: 700; cursor: pointer; font-size: 14px; margin-top: 6px; box-shadow: 0 6px 18px rgba(37,99,235,0.35); transition: filter .15s ease, transform .08s ease; }
        button:hover { filter: brightness(1.08); }
        button:active { transform: translateY(1px); }
        .error-msg { color: #f87171; font-size: 13px; text-align: center; background: rgba(248,113,113,0.1); border: 1px solid rgba(248,113,113,0.3); border-radius: 8px; padding: 8px; margin-bottom: 16px; }
    </style>
</head>
<body>
    <div class="login-wrap">
        <div class="brand">
            <div class="emoji">🏢</div>
            <div class="title">ҮАГ 7 ХОНОГИЙН ТАЙЛАН СИСТЕМ</div>
        </div>
        <div class="card">
            <h2>Системд нэвтрэх</h2>
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            <form method="POST">
                <div class="field">
                    <label>Имэйл хаяг</label>
                    <input type="email" name="email" value="admin@uag.mn" required placeholder="you@uag.mn">
                </div>
                <div class="field">
                    <label>Нууц үг</label>
                    <input type="password" name="password" value="123456" required placeholder="••••••">
                </div>
                <button type="submit">Нэвтрэх →</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

# ---------------------------------------------------------
# AUTH ROUTES
# ---------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT email, password, role, department FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and (check_password_hash(user[1], password) or user[1] == password):
            session['user'] = user[0]
            session['role'] = user[2]
            session['department'] = user[3] or "ЗОНХХэлтэс"
            return redirect(url_for('index'))
        else:
            return render_template_string(LOGIN_HTML, error="Имэйл эсвэл нууц үг буруу байна!")

    return render_template_string(LOGIN_HTML, error=None)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/toggle_theme')
@login_required
def toggle_theme():
    session['theme'] = 'dark' if session.get('theme') == 'light' else 'light'
    return redirect(request.referrer or url_for('index'))

# ---------------------------------------------------------
# USER DASHBOARD & REPORT ENTRY
# ---------------------------------------------------------
@app.route('/')
@login_required
def index():
    user_dept = session.get('department')
    user_role = session.get('role')

    # Шүүлтүүрийн параметрүүд
    # Bug fix: энгийн хэрэглэгч зөвхөн ӨӨРИЙН хэлтсийн ажлыг харна.
    # Админ л дурын хэлтсээр шүүх/бүгдийг харах эрхтэй.
    if user_role == 'admin':
        dept_filter = request.args.get('dept', '').strip()
    else:
        dept_filter = user_dept
    search_q = request.args.get('q', '').strip()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()
    preset = request.args.get('preset', '').strip()
    start_date, end_date = date_range_from_preset(preset, start_date, end_date)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Bug fix: категориудыг зөвхөн тухайн хэрэглэгчийн ХЭЛТСИЙН
    # чиг үүргээр шүүнэ (өмнө нь WHERE нөхцөлгүй бүх хэлтсийн категори
    # хамт харагдаж байсан). Админ бол бүх хэлтсийн категорийг харна.
    if user_role == 'admin':
        cursor.execute("SELECT name FROM categories ORDER BY department ASC, name ASC")
    else:
        cursor.execute("SELECT name FROM categories WHERE department = ? ORDER BY name ASC", (user_dept,))
    categories = [r[0] for r in cursor.fetchall()]

    # НИЙТЭЭРЭЭ ХАРЖ БОЛОХ SQL ЛОГИК
    sql = "SELECT id, department, report_date, func_area, task_desc, task_result, progress, assignee, status, created_at, attachment FROM reports WHERE 1=1"
    params = []

    if dept_filter:
        sql += " AND department = ?"
        params.append(dept_filter)

    if search_q:
        sql += " AND (task_desc LIKE ? OR assignee LIKE ? OR report_date LIKE ?)"
        params.extend([f"%{search_q}%", f"%{search_q}%", f"%{search_q}%"])

    if start_date:
        sql += " AND created_at >= ?"
        params.append(start_date)

    if end_date:
        sql += " AND created_at <= ?"
        params.append(end_date)

    sql += " ORDER BY id DESC"
    cursor.execute(sql, params)
    reports = cursor.fetchall()
    conn.close()

    cat_options = "".join([f'<option value="{c}">{c}</option>' for c in categories])
    dept_options = "".join([f'<option value="{d}" {"selected" if dept_filter==d else ""}>{d}</option>' for d in DEPARTMENTS])
    dept_filter_field = f"""
                <div style="flex: 1.5; min-width: 140px;">
                    <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Хэлтэс шүүх:</label>
                    <select name="dept">
                        <option value="">-- Бүх хэлтэс --</option>
                        {dept_options}
                    </select>
                </div>
    """ if user_role == 'admin' else ""
    saved_reports_title = "📂 Байгууллагын бүх тайлан" if user_role == 'admin' else f"📂 Миний хэлтсийн тайлангууд ({user_dept})"

    reports_rows = ""
    for r in reports:
        # Батлагдсан эсэхээр засах боломжийг удирах болон админ/хэрэглэгчийн эрх шалгах
        is_owner = (r[1] == user_dept) or (user_role == 'admin')

        if r[8] == 'approved':
            status_badge = '<span class="badge badge-success">Approved</span>'
            if user_role == 'admin':
                action_btn = f'<a href="/admin/toggle_report_status/{r[0]}?redirect=home" class="btn btn-warning btn-sm" title="Буцаан засах эрх нээх">🔓 Буцаах</a>'
            else:
                action_btn = '<span class="badge badge-locked" title="Батлагдсан тайлан">🔒 Батлагдсан</span>'
        else:
            status_badge = '<span class="badge badge-info">Submitted</span>'
            if is_owner:
                action_btn = f'<a href="/edit_report/{r[0]}" class="btn btn-warning btn-sm">✏️ Засах</a>'
            else:
                action_btn = '<span class="badge badge-info">-</span>'

        created_dt = r[9] if len(r) > 9 and r[9] else '-'
        attachment_name = r[10] if len(r) > 10 else None
        if attachment_name:
            can_delete_att = is_owner and r[8] != 'approved'
            del_att_btn = f'<button type="button" class="btn btn-danger btn-sm" title="Зураг устгах" onclick="deleteAttachment({r[0]}, this)">🗑</button>' if can_delete_att else ''
            attachment_cell = f'''<div class="attachment-cell">
                <a href="/static/uploads/{attachment_name}" target="_blank"><img class="attachment-thumb" src="/static/uploads/{attachment_name}" alt="хавсралт"></a>
                {del_att_btn}
            </div>'''
        else:
            attachment_cell = '<span class="attachment-empty">—</span>'

        reports_rows += f"""
        <tr id="report-row-{r[0]}">
            <td><b>{r[2]}</b><br><small style='color:#64748b;'>Огноо: {created_dt}</small></td>
            <td><b style="color:#2563eb;">{r[1]}</b></td>
            <td>{r[3]}</td>
            <td>{r[4]}</td>
            <td>{r[5] or '-'}</td>
            <td><b>{r[6]}</b></td>
            <td>{r[7] or '-'}</td>
            <td>{attachment_cell}</td>
            <td>{status_badge}</td>
            <td style="text-align: center;">{action_btn}</td>
        </tr>
        """

    content = f"""
    <div class="card">
        <h2>📝 7 Хоногийн Ажлын Бүртгэл Оруулах ({user_dept})</h2>

        <div style="display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap;">
            <button type="button" class="btn btn-outline" onclick="downloadTemplate()">📥 Excel загвар татах</button>
            <button type="button" class="btn btn-warning" onclick="document.getElementById('excelFileInput').click()">📤 Excel импортлох</button>
            <input type="file" id="excelFileInput" accept=".xlsx, .xls, .csv" style="display:none;" onchange="importExcel(event)">
            <button type="button" class="btn btn-primary" onclick="exportTableToExcel('savedReportsTable', 'Тайлангийн_түүх')">📊 Нийт Түүх Excel татах</button>
        </div>

        <form action="/save" method="POST" enctype="multipart/form-data">
            <div style="margin-bottom: 20px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
                <label style="font-weight: bold;">📅 Тайлант огноо сонгох:</label>
                <input type="date" id="reportDatePicker" onchange="syncDate()" style="width: 160px;">
                <input type="text" name="report_date" id="reportDateInput" style="width: 260px; font-weight: bold; background: rgba(37,99,235,0.1); color: var(--primary); text-align: center;" readonly required>
                <span style="margin-left:auto; font-size:13px; color:#64748b;">👤 Хариуцагч (автоматаар): <b style="color:var(--primary);">{session.get('user')}</b></span>
            </div>

            <table>
                <colgroup>
                    <col style="width: 17%;">
                    <col style="width: 29%;">
                    <col style="width: 23%;">
                    <col style="width: 11%;">
                    <col style="width: 15%;">
                    <col style="width: 5%;">
                </colgroup>
                <thead>
                    <tr>
                        <th>Чиг үүрэг</th>
                        <th>Ажлын мэдээлэл</th>
                        <th>Үр дүн</th>
                        <th>Явц</th>
                        <th>📎 Зураг</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody id="taskTable">
                    <tr>
                        <td><select name="func_area" required>{cat_options}</select></td>
                        <td><textarea name="task_desc" placeholder="Ажлын утга..." required></textarea></td>
                        <td><textarea name="task_result" placeholder="Үр дүн..."></textarea></td>
                        <td>
                            <select name="progress">
                                <option value="25%">25% - Эхэлсэн</option>
                                <option value="50%">50% - Хийгдэж байна</option>
                                <option value="75%">75% - Дуусах шатанд</option>
                                <option value="100%">100% - Дууссан</option>
                            </select>
                        </td>
                        <td class="file-input-wrap"><input type="file" name="attachment" accept="image/png,image/jpeg,image/gif,image/webp"></td>
                        <td><button type="button" class="btn btn-danger btn-sm" onclick="this.closest('tr').remove()">✕</button></td>
                    </tr>
                </tbody>
            </table>

            <div style="margin-top: 15px; display: flex; justify-content: space-between;">
                <button type="button" class="btn btn-outline" onclick="addRow()">+ Шинэ мөр нэмэх</button>
                <button type="submit" class="btn btn-success">💾 Хадгалах & Илгээх</button>
            </div>
        </form>
    </div>

    <div class="card">
        <h3>{saved_reports_title}</h3>

        <div class="filter-card">
            <div class="quick-presets">
                <span style="font-size:12px; font-weight:bold; color:#64748b; margin-right:5px;">⚡ Огнооны хурдан шүүлт:</span>
                <a href="/?preset=this_week&dept={dept_filter}&q={search_q}" class="preset-btn {'active' if preset=='this_week' else ''}">📅 Энэ 7 хоног</a>
                <a href="/?preset=last_week&dept={dept_filter}&q={search_q}" class="preset-btn {'active' if preset=='last_week' else ''}">⏮️ Өнгөрсөн 7 хоног</a>
                <a href="/?preset=this_month&dept={dept_filter}&q={search_q}" class="preset-btn {'active' if preset=='this_month' else ''}">🗓️ Энэ сар</a>
            </div>

            <form method="GET" action="/" class="filter-form">
                <div style="flex: 2; min-width: 170px;">
                    <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Хайх утга:</label>
                    <input type="text" name="q" value="{search_q}" placeholder="Ажлын утга, хариуцагчаар...">
                </div>
                {dept_filter_field}
                <div style="flex: 1; min-width: 135px;">
                    <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Эхлэх огноо:</label>
                    <input type="date" name="start_date" value="{start_date}">
                </div>

                <div style="flex: 1; min-width: 135px;">
                    <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Дуусах огноо:</label>
                    <input type="date" name="end_date" value="{end_date}">
                </div>

                <div style="display:flex; gap:6px;">
                    <button type="submit" class="btn btn-primary" style="width:auto;">🔍 Шүүх</button>
                    <a href="/" class="btn btn-outline" title="Шүүлтүүрийг арилгах">🔄</a>
                </div>
            </form>
        </div>

        <table id="savedReportsTable">
            <colgroup>
                <col style="width: 12%;">
                <col style="width: 9%;">
                <col style="width: 10%;">
                <col style="width: 21%;">
                <col style="width: 15%;">
                <col style="width: 5%;">
                <col style="width: 6%;">
                <col style="width: 7%;">
                <col style="width: 6%;">
                <col style="width: 9%;">
            </colgroup>
            <thead>
                <tr>
                    <th>Огноо</th>
                    <th>Хэлтэс</th>
                    <th>Чиг үүрэг</th>
                    <th>Ажлын мэдээлэл</th>
                    <th>Үр дүн</th>
                    <th>Явц</th>
                    <th>Хариуцагч</th>
                    <th>📎 Зураг</th>
                    <th>Төлөв</th>
                    <th>Үйлдэл</th>
                </tr>
            </thead>
            <tbody>
                {reports_rows if reports_rows else '<tr><td colspan="10" style="text-align:center; color:#94a3b8; padding:20px;">Сонгосон огноо болон шүүлтүүрт тохирох тайлан бүртгэгдээгүй байна.</td></tr>'}
            </tbody>
        </table>
    </div>

    <script>
        const categoriesList = {categories};

        function getWeekNumber(d) {{
            d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
            d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
            var yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
            var weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
            return weekNo;
        }}

        function syncDate() {{
            const dateVal = document.getElementById('reportDatePicker').value;
            if (!dateVal) return;
            const d = new Date(dateVal);
            const yyyy = d.getFullYear();
            const mm = String(d.getMonth() + 1).padStart(2, '0');
            const dd = String(d.getDate()).padStart(2, '0');
            const weekNum = getWeekNumber(d);
            document.getElementById('reportDateInput').value = `${{yyyy}}.${{mm}}.${{dd}} - ${{weekNum}}-р 7 хоног`;
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('reportDatePicker').value = today;
            syncDate();
        }});

        function addRowWithData(funcArea='', taskDesc='', taskResult='', progress='25%') {{
            const tbody = document.getElementById("taskTable");
            const tr = document.createElement("tr");

            let catOptionsHtml = categoriesList.map(c => `<option value="${{c}}" ${{c===funcArea?'selected':''}}>${{c}}</option>`).join('');

            let progOptions = ['25%', '50%', '75%', '100%'].map(p =>
                `<option value="${{p}}" ${{progress.includes(p)?'selected':''}}>${{p}} - ${{p==='100%'?'Дууссан':p==='75%'?'Дуусах шатанд':p==='50%'?'Хийгдэж байна':'Эхэлсэн'}}</option>`
            ).join('');

            tr.innerHTML = `
                <td><select name="func_area" required>${{catOptionsHtml}}</select></td>
                <td><textarea name="task_desc" placeholder="Ажлын утга..." required>${{taskDesc}}</textarea></td>
                <td><textarea name="task_result" placeholder="Үр дүн...">${{taskResult}}</textarea></td>
                <td><select name="progress">${{progOptions}}</select></td>
                <td class="file-input-wrap"><input type="file" name="attachment" accept="image/png,image/jpeg,image/gif,image/webp"></td>
                <td><button type="button" class="btn btn-danger btn-sm" onclick="this.closest('tr').remove()">✕</button></td>
            `;
            tbody.appendChild(tr);
            tr.querySelectorAll('textarea').forEach(el => autoResizeTextarea(el));
        }}

        function addRow() {{
            addRowWithData();
        }}

        function downloadTemplate() {{
            const headers = [["Чиг үүрэг", "Ажлын мэдээлэл", "Үр дүн", "Явц"]];
            const sampleRow = [
                [categoriesList[0] || "PR, олон нийт", "7 хоногийн ажлын гүйцэтгэлийг шалгах", "Амжилттай дууссан", "100%"]
            ];
            const ws = XLSX.utils.aoa_to_sheet([...headers, ...sampleRow]);
            const wb = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(wb, ws, "Тайлангийн_Загвар");
            XLSX.writeFile(wb, "UAG_Report_Template.xlsx");
        }}

        function importExcel(event) {{
            const file = event.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(e) {{
                const data = new Uint8Array(e.target.result);
                const workbook = XLSX.read(data, {{ type: 'array' }});
                const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
                const jsonData = XLSX.utils.sheet_to_json(firstSheet, {{ header: 1 }});

                if (jsonData.length <= 1) {{
                    alert("Excel файл хоосон байна!");
                    return;
                }}

                const tbody = document.getElementById("taskTable");
                tbody.innerHTML = "";

                const rows = jsonData.slice(1);
                let count = 0;
                rows.forEach(r => {{
                    if (!r || r.length === 0) return;
                    const funcArea = r[0] || categoriesList[0] || '';
                    const taskDesc = r[1] || '';
                    const taskResult = r[2] || '';
                    let progress = (r[3] !== undefined && r[3] !== null) ? String(r[3]).trim() : '25%';
                    if (!progress.includes('%')) progress += '%';

                    if (taskDesc) {{
                        addRowWithData(funcArea, taskDesc, taskResult, progress);
                        count++;
                    }}
                }});

                alert(`Амжилттай! ${{count}} мөр ажил Excel-ээс импортлогдлоо.`);
                document.getElementById('excelFileInput').value = "";
            }};
            reader.readAsArrayBuffer(file);
        }}

        function exportTableToExcel(tableId, filename) {{
            const table = document.getElementById(tableId);
            if (!table) return;
            const wb = XLSX.utils.table_to_book(table, {{ sheet: "Тайлан" }});
            XLSX.writeFile(wb, `${{filename}}_${{new Date().toISOString().slice(0,10)}}.xlsx`);
        }}
    </script>
    """
    return render_template_string(LAYOUT_HEADER + content + LAYOUT_FOOTER)

# ---------------------------------------------------------
# REPORT EDIT ROUTE (БАТЛАГДААГҮЙ ТАЙЛАНГ ЗАСАХ)
# ---------------------------------------------------------
@app.route('/edit_report/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_report(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, department, report_date, func_area, task_desc, task_result, progress, assignee, status, attachment FROM reports WHERE id = ?", (id,))
    rep = cursor.fetchone()

    if not rep:
        conn.close()
        return "Тайлан олдсонгүй!", 404

    user_dept = session.get('department')
    user_role = session.get('role')

    # Эрхийн шалгалт
    if user_role != 'admin' and rep[1] != user_dept:
        conn.close()
        return "Танд энэ тайланг засах эрх байхгүй!", 403

    # Батлагдсан тайланг засахыг хориглоно
    if rep[8] == 'approved':
        conn.close()
        return "<script>alert('Батлагдсан тайланг засах боломжгүй! Админд хандаж эрхээ нээлгэнэ үү.'); window.location.href='/';</script>"

    if request.method == 'POST':
        report_date = request.form.get('report_date')
        func_area = request.form.get('func_area')
        task_desc = request.form.get('task_desc')
        task_result = request.form.get('task_result')
        progress = request.form.get('progress')

        # Зураг солих / устгах
        remove_attachment = request.form.get('remove_attachment') == '1'
        new_file = request.files.get('attachment')
        new_filename = _save_attachment(new_file)
        existing_attachment = rep[9]

        if new_filename:
            if existing_attachment:
                _delete_attachment_file(existing_attachment)
            cursor.execute('''
                UPDATE reports
                SET report_date=?, func_area=?, task_desc=?, task_result=?, progress=?, attachment=?
                WHERE id=? AND status != 'approved'
            ''', (report_date, func_area, task_desc, task_result, progress, new_filename, id))
        elif remove_attachment and existing_attachment:
            _delete_attachment_file(existing_attachment)
            cursor.execute('''
                UPDATE reports
                SET report_date=?, func_area=?, task_desc=?, task_result=?, progress=?, attachment=NULL
                WHERE id=? AND status != 'approved'
            ''', (report_date, func_area, task_desc, task_result, progress, id))
        else:
            cursor.execute('''
                UPDATE reports
                SET report_date=?, func_area=?, task_desc=?, task_result=?, progress=?
                WHERE id=? AND status != 'approved'
            ''', (report_date, func_area, task_desc, task_result, progress, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    # Bug fix: тухайн ТАЙЛАНГ эзэмшиж буй хэлтсийн чиг үүргийг харуулна
    # (өмнө нь нэвтэрсэн хэрэглэгчийн бус, бүх хэлтсийн категори холилдон гарч байсан).
    cursor.execute("SELECT name FROM categories WHERE department = ? ORDER BY name ASC", (rep[1],))
    categories = [r[0] for r in cursor.fetchall()]
    conn.close()

    cat_options = "".join([f'<option value="{c}" {"selected" if c==rep[3] else ""}>{c}</option>' for c in categories])
    prog_options = "".join([f'<option value="{p}" {"selected" if p in rep[6] else ""}>{p}</option>' for p in ['25%', '50%', '75%', '100%']])

    existing_attachment = rep[9] if len(rep) > 9 else None
    if existing_attachment:
        attachment_block = f"""
            <div style="margin-bottom: 15px;">
                <label style="font-weight:bold; display:block; margin-bottom:5px;">📎 Одоогийн зураг:</label>
                <div style="display:flex; align-items:center; gap:10px;">
                    <a href="/static/uploads/{existing_attachment}" target="_blank"><img src="/static/uploads/{existing_attachment}" class="attachment-thumb" style="width:70px; height:70px;"></a>
                    <label style="display:flex; align-items:center; gap:5px; font-weight:normal; font-size:13px; cursor:pointer;">
                        <input type="checkbox" name="remove_attachment" value="1" style="width:auto;"> Зургийг устгах
                    </label>
                </div>
            </div>
            <div style="margin-bottom: 15px;">
                <label style="font-weight:bold; display:block; margin-bottom:5px;">Шинэ зургаар солих (сонголт):</label>
                <input type="file" name="attachment" accept="image/png,image/jpeg,image/gif,image/webp">
            </div>
        """
    else:
        attachment_block = """
            <div style="margin-bottom: 15px;">
                <label style="font-weight:bold; display:block; margin-bottom:5px;">📎 Зураг хавсаргах (сонголт):</label>
                <input type="file" name="attachment" accept="image/png,image/jpeg,image/gif,image/webp">
            </div>
        """

    edit_form = f"""
    <div class="card" style="max-width: 800px; margin: 30px auto;">
        <h2>✏️ Тайлан Шинэчлэн Засах (ID: #{rep[0]})</h2>
        <p style="color:#64748b; font-size:13px;">Хэлтэс: <b>{rep[1]}</b> | Одоогийн төлөв: <span class="badge badge-info">Илгээсэн</span></p>

        <form method="POST" enctype="multipart/form-data">
            <div style="margin-bottom: 15px;">
                <label style="font-weight:bold; display:block; margin-bottom:5px;">Тайлант огноо:</label>
                <input type="text" name="report_date" value="{rep[2]}" required>
            </div>

            <div style="margin-bottom: 15px;">
                <label style="font-weight:bold; display:block; margin-bottom:5px;">Чиг үүрэг:</label>
                <select name="func_area" required>{cat_options}</select>
            </div>

            <div style="margin-bottom: 15px;">
                <label style="font-weight:bold; display:block; margin-bottom:5px;">Ажлын мэдээлэл:</label>
                <textarea name="task_desc" required>{rep[4]}</textarea>
            </div>

            <div style="margin-bottom: 15px;">
                <label style="font-weight:bold; display:block; margin-bottom:5px;">Үр дүн:</label>
                <textarea name="task_result">{rep[5] or ''}</textarea>
            </div>

            <div style="display: flex; gap: 15px; margin-bottom: 20px;">
                <div style="flex:1;">
                    <label style="font-weight:bold; display:block; margin-bottom:5px;">Явц:</label>
                    <select name="progress">{prog_options}</select>
                </div>
                <div style="flex:1;">
                    <label style="font-weight:bold; display:block; margin-bottom:5px;">Хариуцагч:</label>
                    <input type="text" value="{rep[7] or ''}" readonly disabled style="background:#f1f5f9; color:#64748b;">
                </div>
            </div>

            {attachment_block}

            <div style="display: flex; gap: 10px; justify-content: flex-end;">
                <a href="/" class="btn btn-outline">Цуцлах</a>
                <button type="submit" class="btn btn-success">💾 Дахин Илгээх & Хадгалах</button>
            </div>
        </form>
    </div>
    """
    return render_template_string(LAYOUT_HEADER + edit_form + LAYOUT_FOOTER)

@app.route('/save', methods=['POST'])
@login_required
def save():
    user_dept = session.get('department', 'ЗОНХХэлтэс')
    assignee_email = session.get('user', '')
    report_date = request.form.get('report_date')
    func_areas = request.form.getlist('func_area')
    task_descs = request.form.getlist('task_desc')
    task_results = request.form.getlist('task_result')
    progresses = request.form.getlist('progress')
    # Мөр бүрийн зураг (empty file input ч мөрийн эрэмбийг зөрчихгүй indexed list буцаана)
    attachment_files = request.files.getlist('attachment')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for i in range(len(func_areas)):
        if func_areas[i] and task_descs[i]:
            saved_filename = None
            if i < len(attachment_files):
                saved_filename = _save_attachment(attachment_files[i])
            cursor.execute('''
                INSERT INTO reports (department, report_date, func_area, task_desc, task_result, progress, assignee, status, created_at, attachment)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'submitted', ?, ?)
            ''', (user_dept, report_date, func_areas[i], task_descs[i], task_results[i], progresses[i], assignee_email, datetime.now().strftime("%Y-%m-%d"), saved_filename))

    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/report_attachment/delete/<int:id>', methods=['POST'])
@login_required
def delete_report_attachment(id):
    """Тухайн тайлангийн мөрөнд хавсаргасан зургийг устгана (AJAX, JSON хариу)."""
    user_dept = session.get('department')
    user_role = session.get('role')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT department, status, attachment FROM reports WHERE id = ?", (id,))
    rep = cursor.fetchone()

    if not rep:
        conn.close()
        return jsonify(ok=False, error="Тайлан олдсонгүй."), 404

    dept, status, attachment = rep
    is_owner = (user_role == 'admin') or (dept == user_dept)
    if not is_owner:
        conn.close()
        return jsonify(ok=False, error="Танд энэ зургийг устгах эрх байхгүй."), 403
    if status == 'approved' and user_role != 'admin':
        conn.close()
        return jsonify(ok=False, error="Батлагдсан тайлангийн зургийг устгах боломжгүй."), 403

    if attachment:
        _delete_attachment_file(attachment)
        cursor.execute("UPDATE reports SET attachment = NULL WHERE id = ?", (id,))
        conn.commit()

    conn.close()
    return jsonify(ok=True)

# ---------------------------------------------------------
# ANALYTICS PAGE (НИЙТЭЭРЭЭ ХАРЖ БОЛОХ + ОГНООНЫ ШҮҮЛТҮҮР)
# ---------------------------------------------------------
@app.route('/analytics')
@login_required
def user_analytics():
    user_role = session.get('role')
    user_dept = session.get('department')

    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()
    preset = request.args.get('preset', '').strip()
    start_date, end_date = date_range_from_preset(preset, start_date, end_date)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Bug fix: энгийн хэрэглэгч зөвхөн өөрийн хэлтсийн статистикийг харна.
    # Админ бүх байгууллагын нэгтгэлийг харна.
    scope_depts = DEPARTMENTS if user_role == 'admin' else [user_dept]

    base_sql = "FROM reports WHERE 1=1"
    params = []
    if start_date:
        base_sql += " AND created_at >= ?"
        params.append(start_date)
    if end_date:
        base_sql += " AND created_at <= ?"
        params.append(end_date)

    if user_role == 'admin':
        cursor.execute(f"SELECT COUNT(*), AVG(CAST(REPLACE(progress, '%', '') AS INT)) {base_sql}", params)
    else:
        cursor.execute(f"SELECT COUNT(*), AVG(CAST(REPLACE(progress, '%', '') AS INT)) {base_sql} AND department = ?", params + [user_dept])
    total_count, avg_prog = cursor.fetchone()
    avg_prog = round(avg_prog or 0, 1)

    # Хэлтэс тус бүрийн дүн (админ: бүх хэлтэс, энгийн хэрэглэгч: зөвхөн өөрийнх)
    dept_stats_rows = ""
    for dept in scope_depts:
        dept_sql = base_sql + " AND department = ?"
        cursor.execute(f"SELECT COUNT(*), AVG(CAST(REPLACE(progress, '%', '') AS INT)) {dept_sql}", params + [dept])
        cnt, p_avg = cursor.fetchone()
        p_avg = round(p_avg or 0, 1)
        dept_stats_rows += f"""
        <tr>
            <td><b>{dept}</b></td>
            <td>{cnt} ажил</td>
            <td>
                <b>{p_avg}%</b>
                <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: {p_avg}%;"></div></div>
            </td>
        </tr>
        """

    conn.close()

    stats_title = "📊 Нийт Байгууллагын Тайлан Тооцоолол" if user_role == 'admin' else f"📊 {user_dept} — Тайлан Тооцоолол"
    detail_title = "📈 Гүйцэтгэлийн Нарийвчилсан Үзүүлэлт (Хэлтсээр)" if user_role == 'admin' else "📈 Гүйцэтгэлийн Нарийвчилсан Үзүүлэлт"

    body = f"""
    <div class="card">
        <h3>{stats_title}</h3>

        <div class="filter-card" style="margin-bottom: 20px;">
            <div class="quick-presets">
                <span style="font-size:12px; font-weight:bold; color:#64748b; margin-right:5px;">⚡ Огнооны хурдан шүүлт:</span>
                <a href="/analytics?preset=this_week" class="preset-btn {'active' if preset=='this_week' else ''}">📅 Энэ 7 хоног</a>
                <a href="/analytics?preset=last_week" class="preset-btn {'active' if preset=='last_week' else ''}">⏮️ Өнгөрсөн 7 хоног</a>
                <a href="/analytics?preset=this_month" class="preset-btn {'active' if preset=='this_month' else ''}">🗓️ Энэ сар</a>
            </div>

            <form method="GET" action="/analytics" class="filter-form">
                <div style="flex: 1; min-width: 150px;">
                    <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Эхлэх огноо:</label>
                    <input type="date" name="start_date" value="{start_date}">
                </div>

                <div style="flex: 1; min-width: 150px;">
                    <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Дуусах огноо:</label>
                    <input type="date" name="end_date" value="{end_date}">
                </div>

                <div style="display:flex; gap:6px;">
                    <button type="submit" class="btn btn-primary" style="width:auto;">🔍 Шүүж тооцоолох</button>
                    <a href="/analytics" class="btn btn-outline" title="Шүүлтүүрийг арилгах">🔄</a>
                </div>
            </form>
        </div>

        <div class="stat-grid" style="margin-bottom:20px;">
            <div class="stat-box"><h3>{total_count or 0}</h3><p>Нийт оруулсан ажил</p></div>
            <div class="stat-box"><h3>{avg_prog}%</h3><p>Дундаж гүйцэтгэл</p></div>
        </div>

        <h4>{detail_title}</h4>
        <table>
            <colgroup>
                <col style="width: 40%;">
                <col style="width: 25%;">
                <col style="width: 35%;">
            </colgroup>
            <thead><tr><th>Хэлтэс</th><th>Нийт ажил</th><th>Дундаж Биелэлт</th></tr></thead>
            <tbody>{dept_stats_rows}</tbody>
        </table>
    </div>
    """
    return render_template_string(LAYOUT_HEADER + body + LAYOUT_FOOTER)

# ---------------------------------------------------------
# UNIFIED PRINTABLE REPORT  (/report)
#
# A4-formatted report the browser can print / "Save as PDF" directly
# (native browser print keeps our exact @page CSS, so no extra PDF
# dependency is required), plus a PPTX export with real (not image)
# charts built via python-pptx. Regular users only ever see/export
# their own department; admins can see one, several, or all
# departments and get a 2-page company summary in front.
# ---------------------------------------------------------
def _scope_departments():
    """Returns (departments_in_scope, is_admin, requested_dept)."""
    user_role = session.get('role')
    user_dept = session.get('department')
    requested_dept = request.args.get('department', '').strip()

    if user_role != 'admin':
        return [user_dept], False, user_dept

    if requested_dept and requested_dept in DEPARTMENTS:
        return [requested_dept], True, requested_dept
    return list(DEPARTMENTS), True, ''

def _fetch_report_rows(conn, departments, start_date, end_date):
    placeholders = ",".join("?" for _ in departments)
    sql = f"""
        SELECT id, department, report_date, func_area, task_desc, task_result,
               progress, assignee, status, created_at
        FROM reports WHERE department IN ({placeholders})
    """
    params = list(departments)
    if start_date:
        sql += " AND created_at >= ?"
        params.append(start_date)
    if end_date:
        sql += " AND created_at <= ?"
        params.append(end_date)
    sql += " ORDER BY department, id"
    return conn.execute(sql, params).fetchall()

def _group_by_department(rows):
    by_dept = {}
    for r in rows:
        by_dept.setdefault(r[1], []).append(r)
    return by_dept

def _svg_trend_chart(rows, height=200):
    """Inline SVG line chart: average progress (%) per report date,
    in the order rows were recorded (created_at). No JS dependency,
    so it prints/exports to PDF exactly as shown on screen."""
    daily = {}
    order = []
    for r in sorted(rows, key=lambda x: (x[9] or '', x[0])):
        d = r[9] or '—'
        if d not in daily:
            daily[d] = []
            order.append(d)
        daily[d].append(parse_progress(r[6]))
    if len(order) < 2:
        return ""

    # Cap to the most recent 12 points so labels stay legible.
    order = order[-12:]
    values = [round(sum(daily[d]) / len(daily[d]), 1) for d in order]

    width, padding = 720, 44
    n = len(values)
    step = (width - 2 * padding) / max(n - 1, 1)
    top_pad = 26

    def xy(i, v):
        x = padding + i * step
        y = top_pad + (height - top_pad - 30) * (1 - v / 100)
        return x, y

    points = [xy(i, v) for i, v in enumerate(values)]
    path = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)

    gridlines = "".join(
        f'<line x1="{padding}" y1="{top_pad + (height - top_pad - 30) * (1 - gv / 100):.1f}" '
        f'x2="{width - padding}" y2="{top_pad + (height - top_pad - 30) * (1 - gv / 100):.1f}" '
        f'stroke="#e2e8f0" stroke-width="1"/>'
        f'<text x="4" y="{top_pad + (height - top_pad - 30) * (1 - gv / 100) + 4:.1f}" font-size="10" fill="#94a3b8">{gv}%</text>'
        for gv in [0, 25, 50, 75, 100]
    )
    circles = "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#2563eb"/>'
        f'<text x="{x:.1f}" y="{y - 10:.1f}" font-size="11" text-anchor="middle" font-weight="600" fill="#1e293b">{values[i]}%</text>'
        for i, (x, y) in enumerate(points)
    )
    x_labels = "".join(
        f'<text x="{x:.1f}" y="{height - 8}" font-size="10" text-anchor="middle" fill="#64748b">{order[i]}</text>'
        for i, (x, y) in enumerate(points)
    )

    return f"""
    <div style="margin-bottom:20px;">
        <h4 style="margin-bottom:8px;">📈 Гүйцэтгэлийн трэнд (өдрөөр, дундаж биелэлт %)</h4>
        <svg viewBox="0 0 {width} {height}" style="width:100%; height:auto; background:#fff;">
            {gridlines}
            <polyline points="{path}" fill="none" stroke="#2563eb" stroke-width="3"/>
            {circles}
            {x_labels}
        </svg>
    </div>
    """

def _category_breakdown_bars(d_rows):
    """Chиг үүрэг (category) -> average completion %, rendered as
    horizontal bars, for a single department's task table."""
    by_cat = {}
    for r in d_rows:
        by_cat.setdefault(r[3], []).append(parse_progress(r[6]))
    if not by_cat:
        return ""
    rows_html = ""
    for cat, vals in sorted(by_cat.items()):
        avg = round(sum(vals) / len(vals), 1)
        rows_html += f"""
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <div style="width:34%; font-size:13px; font-weight:600;">{cat}</div>
            <div style="flex:1; background:#e2e8f0; height:14px; border-radius:6px; overflow:hidden;">
                <div style="width:{avg}%; background:#2563eb; height:100%;"></div>
            </div>
            <div style="width:60px; text-align:right; font-size:13px; font-weight:700; color:#2563eb;">{avg}%</div>
        </div>
        """
    return f"""
    <div style="margin-bottom:20px;">
        <h4 style="margin-bottom:8px;">📊 Чиг үүргээр биелэлт</h4>
        {rows_html}
    </div>
    """

@app.route('/report')
@login_required
def unified_report():
    departments, is_admin, requested_dept = _scope_departments()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()
    preset = request.args.get('preset', '').strip()
    # Bug fix: анх нээхэд (шүүлтгүй үед) яг тухайн ЦАГИЙН БҮС дэх өнөөдрийг агуулсан
    # календарын 7 хоног (Даваа-Ням) автоматаар сонгогдоно — "7 хоногийн тайлан" гэдэг
    # утгандаа нийцүүлэн, зөвхөн нэг өдөр биш бүтэн долоо хоногийг харуулна.
    if not start_date and not end_date and not preset:
        preset = 'this_week'
    start_date, end_date = date_range_from_preset(preset, start_date, end_date)

    conn = sqlite3.connect(DB_NAME)
    rows = _fetch_report_rows(conn, departments, start_date, end_date)
    conn.close()

    by_dept = _group_by_department(rows)
    total_count = len(rows)
    avg_prog = round(sum(parse_progress(r[6]) for r in rows) / total_count, 1) if total_count else 0
    done_count = sum(1 for r in rows if parse_progress(r[6]) >= 100)
    attention_rows = [r for r in rows if parse_progress(r[6]) < 100]

    export_qs = f"start_date={start_date}&end_date={end_date}" + (f"&department={requested_dept}" if requested_dept else "")

    # ---- top (no-print) controls ----
    dept_selector = ""
    if is_admin:
        opts = '<option value="">-- Бүх хэлтэс (нэгтгэл) --</option>' + "".join(
            f'<option value="{d}" {"selected" if d==requested_dept else ""}>{d}</option>' for d in DEPARTMENTS
        )
        dept_selector = f"""
        <div style="flex: 1; min-width: 200px;">
            <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Хэлтэс:</label>
            <select name="department">{opts}</select>
        </div>
        """

    controls = f"""
    <div class="card no-print">
        <h2 style="margin-top:0;">📑 Албан ёсны 7 хоногийн тайлан</h2>
        <p style="color:#64748b; font-size:13px;">Доор бэлдсэн А4 хуудаснуудыг шууд хэвлэх эсвэл "PDF-ээр хадгалах"-ыг сонгож татаж авах боломжтой (хэвлэх цонх). PPTX хувилбар слайд бүрдээ график агуулна.</p>
        <div class="quick-presets no-print" style="margin-bottom:10px;">
            <span style="font-size:12px; font-weight:bold; color:#64748b; margin-right:5px;">⚡ Огнооны хурдан шүүлт (Даваа–Ням):</span>
            <a href="/report?preset=this_week{('&department='+requested_dept) if requested_dept else ''}" class="preset-btn {'active' if preset=='this_week' else ''}">📅 Энэ 7 хоног ({start_date} — {end_date})</a>
            <a href="/report?preset=last_week{('&department='+requested_dept) if requested_dept else ''}" class="preset-btn {'active' if preset=='last_week' else ''}">⏮️ Өнгөрсөн 7 хоног</a>
        </div>
        <form method="GET" action="/report" class="filter-form">
            <div style="flex: 1; min-width: 150px;">
                <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Эхлэх огноо:</label>
                <input type="date" name="start_date" value="{start_date}">
            </div>
            <div style="flex: 1; min-width: 150px;">
                <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Дуусах огноо:</label>
                <input type="date" name="end_date" value="{end_date}">
            </div>
            {dept_selector}
            <div style="display:flex; gap:6px;">
                <button type="submit" class="btn btn-primary" style="width:auto;">🔍 Шүүх</button>
            </div>
        </form>
        <div style="margin-top:16px; display:flex; gap:10px; flex-wrap:wrap;">
            <a href="/report/export_pdf?{export_qs}" class="btn btn-danger">📄 PDF татах</a>
            <a href="/report/export_pptx?{export_qs}" class="btn btn-success">📊 PPTX татах (график бүхий)</a>
            <button type="button" class="btn btn-outline" onclick="window.print()">🖨️ Хэвлэх (browser)</button>
        </div>
    </div>
    """

    # ---- A4 pages ----
    pages_html = ""
    show_summary_page = is_admin and not requested_dept and len(departments) > 1

    if show_summary_page:
        bars = ""
        for dept in DEPARTMENTS:
            d_rows = by_dept.get(dept, [])
            d_avg = round(sum(parse_progress(r[6]) for r in d_rows) / len(d_rows), 1) if d_rows else 0
            bars += f"""
            <tr>
                <td style="border:1px solid #cbd5e1; padding:6px;"><b>{dept}</b></td>
                <td style="border:1px solid #cbd5e1; padding:6px;">{len(d_rows)}</td>
                <td style="border:1px solid #cbd5e1; padding:6px;">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <div style="flex:1; background:#e2e8f0; height:10px; border-radius:4px; overflow:hidden;">
                            <div style="width:{d_avg}%; background:#2563eb; height:100%;"></div>
                        </div>
                        <span style="font-size:12px; white-space:nowrap;">{d_avg}%</span>
                    </div>
                </td>
            </tr>
            """

        attention_html = "".join(
            f"<tr><td style='border:1px solid #cbd5e1; padding:6px;'>{r[1]}</td>"
            f"<td style='border:1px solid #cbd5e1; padding:6px;'>{r[3]}</td>"
            f"<td style='border:1px solid #cbd5e1; padding:6px;'>{r[4]}</td>"
            f"<td style='border:1px solid #cbd5e1; padding:6px;'>{r[6]}</td></tr>"
            for r in attention_rows[:25]
        ) or "<tr><td colspan='4' style='padding:6px; color:#64748b;'>Анхаарал шаардах (дуусаагүй) ажил алга.</td></tr>"

        pages_html += f"""
        <div class="a4-page">
            <div class="a4-header">
                <div><b>ЦЭЦЭНС МАЙНИНГ ЭНД ЭНЕРЖИ ХХК</b><br>Үйл ажиллагааны газар — 7 хоногийн нэгдсэн тайлан</div>
                <div style="text-align:right;">{start_date or '—'} — {end_date or '—'}</div>
            </div>
            <div class="a4-kpis">
                <div class="a4-kpi"><div class="a4-kpi-num">{total_count}</div><div>Нийт ажил</div></div>
                <div class="a4-kpi"><div class="a4-kpi-num">{avg_prog}%</div><div>Дундаж биелэлт</div></div>
                <div class="a4-kpi"><div class="a4-kpi-num">{done_count}</div><div>Дууссан ажил (100%)</div></div>
                <div class="a4-kpi"><div class="a4-kpi-num">{len(attention_rows)}</div><div>Анхаарал шаардах ажил</div></div>
            </div>
            {_svg_trend_chart(rows)}
            <h4>Хэлтсүүдийн гүйцэтгэлийн харьцуулалт</h4>
            <table style="width:100%; border-collapse:collapse; font-size:14px;">
                <thead><tr>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left;">Хэлтэс</th>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left;">Ажлын тоо</th>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left;">Дундаж биелэлт</th>
                </tr></thead>
                <tbody>{bars}</tbody>
            </table>
        </div>
        <div class="a4-page">
            <div class="a4-header">
                <div><b>ЦЭЦЭНС МАЙНИНГ ЭНД ЭНЕРЖИ ХХК</b><br>Шийдвэрлүүлэх шаардлагатай тулгамдсан асуудлууд (дуусаагүй, биелэлт 25–75%)</div>
                <div style="text-align:right;">{start_date or '—'} — {end_date or '—'}</div>
            </div>
            <table style="width:100%; border-collapse:collapse; font-size:12px;">
                <thead><tr>
                    <th style="border:1px solid #cbd5e1; padding:6px; background:#f1f5f9; text-align:left;">Хэлтэс</th>
                    <th style="border:1px solid #cbd5e1; padding:6px; background:#f1f5f9; text-align:left;">Чиг үүрэг</th>
                    <th style="border:1px solid #cbd5e1; padding:6px; background:#f1f5f9; text-align:left;">Ажил</th>
                    <th style="border:1px solid #cbd5e1; padding:6px; background:#f1f5f9; text-align:left;">Явц</th>
                </tr></thead>
                <tbody>{attention_html}</tbody>
            </table>
        </div>
        """

    for dept in departments:
        d_rows = by_dept.get(dept, [])
        d_avg = round(sum(parse_progress(r[6]) for r in d_rows) / len(d_rows), 1) if d_rows else 0
        task_rows_html = "".join(
            f"""<tr>
                <td style="border:1px solid #cbd5e1; padding:8px; font-size:13px;">{r[3]}</td>
                <td style="border:1px solid #cbd5e1; padding:8px; font-size:13px;">{r[4]}</td>
                <td style="border:1px solid #cbd5e1; padding:8px; font-size:15px; font-weight:600; color:#0f172a;">{r[5] or '-'}</td>
                <td style="border:1px solid #cbd5e1; padding:8px; font-size:13px; white-space:nowrap;">{r[6]}</td>
                <td style="border:1px solid #cbd5e1; padding:8px; font-size:13px;">{r[7] or '-'}</td>
            </tr>"""
            for r in d_rows
        ) or "<tr><td colspan='5' style='padding:8px; color:#64748b;'>Сонгосон хугацаанд бүртгэгдсэн ажил алга.</td></tr>"

        pages_html += f"""
        <div class="a4-page">
            <div class="a4-header">
                <div><b>{dept}</b><br>7 хоногийн ажлын тайлан</div>
                <div style="text-align:right;">{start_date or '—'} — {end_date or '—'}</div>
            </div>
            <div class="a4-kpis">
                <div class="a4-kpi"><div class="a4-kpi-num">{len(d_rows)}</div><div>Ажлын тоо</div></div>
                <div class="a4-kpi"><div class="a4-kpi-num">{d_avg}%</div><div>Дундаж биелэлт</div></div>
                <div class="a4-kpi"><div class="a4-kpi-num">{sum(1 for r in d_rows if parse_progress(r[6])>=100)}</div><div>Дууссан</div></div>
            </div>
            {_svg_trend_chart(d_rows)}
            {_category_breakdown_bars(d_rows)}
            <table style="width:100%; border-collapse:collapse; table-layout:fixed;">
                <colgroup>
                    <col style="width:14%;">
                    <col style="width:23%;">
                    <col style="width:35%;">
                    <col style="width:8%;">
                    <col style="width:20%;">
                </colgroup>
                <thead><tr>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left; font-size:13px;">Чиг үүрэг</th>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left; font-size:13px;">Ажлын мэдээлэл</th>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left; font-size:13px;">Үр дүн</th>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left; font-size:13px;">Явц</th>
                    <th style="border:1px solid #cbd5e1; padding:8px; background:#f1f5f9; text-align:left; font-size:13px;">Хариуцагч</th>
                </tr></thead>
                <tbody>{task_rows_html}</tbody>
            </table>
        </div>
        """

    extra_style = """
    <style>
        @media print {
            @page { size: A4 portrait; margin: 12mm; }
            .no-print { display: none !important; }
            .sidebar { display: none !important; }
            .content { width: 100% !important; padding: 0 !important; }
        }
        .a4-page {
            max-width: 210mm;
            min-height: 150mm;
            margin: 0 auto 24px;
            background: #fff;
            color: #0f172a;
            padding: 14mm;
            box-sizing: border-box;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            page-break-after: always;
        }
        .a4-header { display:flex; justify-content:space-between; align-items:flex-start; border-bottom:2px solid #2563eb; padding-bottom:10px; margin-bottom:16px; font-size:14px; }
        .a4-kpis { display:flex; gap:14px; margin-bottom:20px; flex-wrap:wrap; }
        .a4-kpi { flex:1; min-width:130px; background:#f1f5f9; border-radius:10px; padding:16px 10px; text-align:center; }
        .a4-kpi-num { font-size:30px; font-weight:bold; color:#2563eb; line-height:1.1; }
        .a4-kpi div:last-child { font-size:13px; color:#334155; margin-top:4px; }
    </style>
    """

    return render_template_string(LAYOUT_HEADER + extra_style + controls + pages_html + LAYOUT_FOOTER)


def _add_chart_slide_kpis(prs, total_count, avg_prog, done_count, attention_count, period_label):
    slide = prs.slides.add_slide(prs.slide_layouts[5] if len(prs.slide_layouts) > 5 else prs.slide_layouts[1])
    slide.shapes.title.text = "Нэгдсэн үзүүлэлт (KPI)"
    box = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(9), Inches(0.5))
    box.text_frame.text = f"Тайлант хугацаа: {period_label}"

    kpi_labels = ["Нийт ажил", "Дундаж биелэлт (%)", "Дууссан ажил", "Анхаарал шаардах ажил"]
    kpi_values = [total_count, avg_prog, done_count, attention_count]
    left = Inches(0.5)
    top = Inches(2.0)
    width = Inches(2.1)
    height = Inches(1.3)
    for i, (label, val) in enumerate(zip(kpi_labels, kpi_values)):
        tb = slide.shapes.add_textbox(left + Inches(2.3 * i), top, width, height)
        tf = tb.text_frame
        tf.text = str(val)
        tf.paragraphs[0].font.size = Pt(32)
        tf.paragraphs[0].font.bold = True
        tf.paragraphs[0].font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
        p2 = tf.add_paragraph()
        p2.text = label
        p2.font.size = Pt(12)
    return slide


def _add_department_bar_chart(prs, by_dept):
    slide = prs.slides.add_slide(prs.slide_layouts[5] if len(prs.slide_layouts) > 5 else prs.slide_layouts[1])
    slide.shapes.title.text = "Хэлтсүүдийн дундаж биелэлт (%)"

    chart_data = CategoryChartData()
    chart_data.categories = list(DEPARTMENTS)
    values = []
    for dept in DEPARTMENTS:
        d_rows = by_dept.get(dept, [])
        avg = round(sum(parse_progress(r[6]) for r in d_rows) / len(d_rows), 1) if d_rows else 0
        values.append(avg)
    chart_data.add_series('Дундаж биелэлт (%)', values)

    x, y, cx, cy = Inches(0.6), Inches(1.4), Inches(8.8), Inches(5.0)
    graphic_frame = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data)
    chart = graphic_frame.chart
    chart.has_legend = False
    return slide


def _add_status_pie_chart(prs, rows, title_suffix=""):
    slide = prs.slides.add_slide(prs.slide_layouts[5] if len(prs.slide_layouts) > 5 else prs.slide_layouts[1])
    slide.shapes.title.text = f"Явцын хуваарилалт {title_suffix}".strip()

    bucket_counts = {b: 0 for b in PROGRESS_BUCKETS}
    for r in rows:
        p = parse_progress(r[6])
        if p >= 100:
            bucket_counts["100%"] += 1
        elif p >= 75:
            bucket_counts["75%"] += 1
        elif p >= 50:
            bucket_counts["50%"] += 1
        else:
            bucket_counts["25%"] += 1

    chart_data = CategoryChartData()
    chart_data.categories = list(bucket_counts.keys())
    chart_data.add_series('Ажлын тоо', list(bucket_counts.values()))

    x, y, cx, cy = Inches(1.5), Inches(1.4), Inches(6.5), Inches(5.0)
    graphic_frame = slide.shapes.add_chart(XL_CHART_TYPE.PIE, x, y, cx, cy, chart_data)
    chart = graphic_frame.chart
    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.RIGHT
    chart.legend.include_in_layout = False
    return slide


def _add_department_task_table_slides(prs, dept, d_rows, rows_per_slide=4):
    """Renders a department's tasks as real PowerPoint TABLES instead of
    a giant wall of bullet text. The previous version dumped every task
    into one text placeholder, which PowerPoint then auto-shrinks to an
    unreadable size once there are more than a handful of rows. A table
    keeps each field in its own column at a fixed, readable font size,
    and long departments are split across several "(page X/Y)" slides
    instead of overflowing one slide."""
    blank_layout = prs.slide_layouts[6] if len(prs.slide_layouts) > 6 else prs.slide_layouts[5]

    if not d_rows:
        slide = prs.slides.add_slide(blank_layout)
        tb = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.6))
        tb.text_frame.text = dept
        tb.text_frame.paragraphs[0].font.size = Pt(28)
        tb.text_frame.paragraphs[0].font.bold = True
        msg = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(0.6))
        msg.text_frame.text = "Сонгосон хугацаанд бүртгэгдсэн ажил алга."
        return

    chunks = [d_rows[i:i + rows_per_slide] for i in range(0, len(d_rows), rows_per_slide)]
    total_pages = len(chunks)
    headers = ["Чиг үүрэг", "Ажлын мэдээлэл", "Үр дүн", "Явц", "Хариуцагч"]
    col_widths = [Inches(1.7), Inches(3.3), Inches(2.6), Inches(0.8), Inches(1.1)]

    for page_idx, chunk in enumerate(chunks, start=1):
        slide = prs.slides.add_slide(blank_layout)
        title_text = dept if total_pages == 1 else f"{dept} ({page_idx}/{total_pages})"
        tb = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
        tb.text_frame.text = title_text
        tb.text_frame.paragraphs[0].font.size = Pt(24)
        tb.text_frame.paragraphs[0].font.bold = True
        tb.text_frame.paragraphs[0].font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        rows_n = len(chunk) + 1
        cols_n = len(headers)
        left, top, width, height = Inches(0.4), Inches(1.1), Inches(9.5), Inches(5.8)
        graphic_frame = slide.shapes.add_table(rows_n, cols_n, left, top, width, height)
        table = graphic_frame.table
        for c, w in enumerate(col_widths):
            table.columns[c].width = w

        for c, h in enumerate(headers):
            cell = table.cell(0, c)
            cell.text = h
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(0x25, 0x63, 0xEB)
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        for r_idx, r in enumerate(chunk, start=1):
            values = [r[3], r[4], r[5] or '-', r[6], r[7] or '-']
            for c_idx, val in enumerate(values):
                cell = table.cell(r_idx, c_idx)
                cell.text_frame.word_wrap = True
                cell.text = str(val)
                for p in cell.text_frame.paragraphs:
                    p.font.size = Pt(10)


@app.route('/report/export_pptx')
@login_required
def export_report_pptx():
    departments, is_admin, requested_dept = _scope_departments()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()

    conn = sqlite3.connect(DB_NAME)
    rows = _fetch_report_rows(conn, departments, start_date, end_date)
    conn.close()
    by_dept = _group_by_department(rows)

    total_count = len(rows)
    avg_prog = round(sum(parse_progress(r[6]) for r in rows) / total_count, 1) if total_count else 0
    done_count = sum(1 for r in rows if parse_progress(r[6]) >= 100)
    attention_count = sum(1 for r in rows if parse_progress(r[6]) < 100)
    period_label = f"{start_date or '—'} — {end_date or '—'}"

    prs = Presentation()

    # Title slide
    title_slide = prs.slides.add_slide(prs.slide_layouts[0])
    title_slide.shapes.title.text = "ҮАГ 7 Хоногийн Тайлан"
    subtitle_text = requested_dept if requested_dept else "Нэгдсэн тайлан (бүх хэлтэс)"
    title_slide.placeholders[1].text = f"{subtitle_text}\n{period_label}"

    # Company-wide KPI + charts only make sense when more than one
    # department is in scope (admin, no department filter).
    if is_admin and not requested_dept and len(departments) > 1:
        _add_chart_slide_kpis(prs, total_count, avg_prog, done_count, attention_count, period_label)
        _add_department_bar_chart(prs, by_dept)
        _add_status_pie_chart(prs, rows, "(бүх хэлтэс)")

    for dept in departments:
        d_rows = by_dept.get(dept, [])
        if len(departments) == 1:
            # single-department scope: show its own KPI + status pie too
            d_total = len(d_rows)
            d_avg = round(sum(parse_progress(r[6]) for r in d_rows) / d_total, 1) if d_total else 0
            d_done = sum(1 for r in d_rows if parse_progress(r[6]) >= 100)
            d_attention = sum(1 for r in d_rows if parse_progress(r[6]) < 100)
            _add_chart_slide_kpis(prs, d_total, d_avg, d_done, d_attention, period_label)
            if d_rows:
                _add_status_pie_chart(prs, d_rows, f"({dept})")
        _add_department_task_table_slides(prs, dept, d_rows)

    suffix = requested_dept if requested_dept else "Company"
    fname = f"UAG_Report_{suffix}_{datetime.now().strftime('%Y%m%d')}.pptx".replace(" ", "_")
    output_path = os.path.join(os.getcwd(), fname)
    prs.save(output_path)
    return send_file(output_path, as_attachment=True, download_name=fname)


# ---------------------------------------------------------
# REAL PDF EXPORT (reportlab)
#
# The /report page can already be "printed to PDF" from the browser,
# but that depends on the person choosing the right print settings.
# This route builds an actual .pdf file server-side and sends it as a
# download, so "PDF татах" always works the same way for everyone.
# Long task tables split across pages automatically (reportlab's Table
# flowable does this on its own inside SimpleDocTemplate).
# ---------------------------------------------------------
def _pdf_esc(value):
    text = str(value) if value is not None else ""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def _pdf_styles():
    styles = getSampleStyleSheet()
    return {
        'title': ParagraphStyle('UAGTitle', fontName=PDF_FONT_BOLD, fontSize=18, leading=22, textColor=colors.HexColor('#0F172A')),
        'subtitle': ParagraphStyle('UAGSubtitle', fontName=PDF_FONT, fontSize=11, leading=14, textColor=colors.HexColor('#64748B')),
        'h2': ParagraphStyle('UAGH2', fontName=PDF_FONT_BOLD, fontSize=15, leading=18, textColor=colors.HexColor('#1E293B'), spaceBefore=6, spaceAfter=8),
        'kpi_num': ParagraphStyle('UAGKpiNum', fontName=PDF_FONT_BOLD, fontSize=20, leading=24, textColor=colors.HexColor('#2563EB'), alignment=1),
        'kpi_label': ParagraphStyle('UAGKpiLabel', fontName=PDF_FONT, fontSize=9, leading=11, textColor=colors.HexColor('#334155'), alignment=1),
        'cell': ParagraphStyle('UAGCell', fontName=PDF_FONT, fontSize=9, leading=12),
        'cell_bold': ParagraphStyle('UAGCellBold', fontName=PDF_FONT_BOLD, fontSize=9, leading=12),
        'th': ParagraphStyle('UAGTh', fontName=PDF_FONT_BOLD, fontSize=9.5, leading=12, textColor=colors.white),
    }

def _pdf_kpi_table(styles, kpi_pairs):
    """kpi_pairs: list of (value, label). Rendered as a row of boxed KPI cards."""
    row = [[Paragraph(_pdf_esc(v), styles['kpi_num']), ] for v, l in kpi_pairs]
    numbers = [Paragraph(_pdf_esc(v), styles['kpi_num']) for v, l in kpi_pairs]
    labels = [Paragraph(_pdf_esc(l), styles['kpi_label']) for v, l in kpi_pairs]
    col_w = (170 * mm) / len(kpi_pairs)
    t = Table([numbers, labels], colWidths=[col_w] * len(kpi_pairs))
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F1F5F9')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#E2E8F0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.75, colors.white),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t

def _pdf_task_table(styles, d_rows):
    header = [Paragraph(h, styles['th']) for h in ["Чиг үүрэг", "Ажлын мэдээлэл", "Үр дүн", "Явц", "Хариуцагч"]]
    data = [header]
    for r in d_rows:
        data.append([
            Paragraph(_pdf_esc(r[3]), styles['cell']),
            Paragraph(_pdf_esc(r[4]), styles['cell']),
            Paragraph(_pdf_esc(r[5] or '-'), styles['cell_bold']),
            Paragraph(_pdf_esc(r[6]), styles['cell']),
            Paragraph(_pdf_esc(r[7] or '-'), styles['cell']),
        ])
    col_widths = [26 * mm, 52 * mm, 45 * mm, 16 * mm, 25 * mm]
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563EB')),
        ('GRID', (0, 0), (-1, -1), 0.6, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')]),
    ]))
    return t

def _generate_report_pdf(output_path, departments, is_admin, requested_dept, rows, by_dept, start_date, end_date):
    styles = _pdf_styles()
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=15 * mm, rightMargin=15 * mm, topMargin=15 * mm, bottomMargin=15 * mm,
        title="ҮАГ 7 Хоногийн Тайлан",
    )
    story = []
    period_label = f"{start_date or '—'} — {end_date or '—'}"

    total_count = len(rows)
    avg_prog = round(sum(parse_progress(r[6]) for r in rows) / total_count, 1) if total_count else 0
    done_count = sum(1 for r in rows if parse_progress(r[6]) >= 100)
    attention_rows = [r for r in rows if parse_progress(r[6]) < 100]

    story.append(Paragraph("ЦЭЦЭНС МАЙНИНГ ЭНД ЭНЕРЖИ ХХК", styles['title']))
    story.append(Paragraph(f"Үйл ажиллагааны газар — 7 хоногийн тайлан &nbsp;|&nbsp; {period_label}", styles['subtitle']))
    story.append(Spacer(1, 10 * mm))

    show_summary = is_admin and not requested_dept and len(departments) > 1
    if show_summary:
        story.append(Paragraph("Нэгдсэн үзүүлэлт", styles['h2']))
        story.append(_pdf_kpi_table(styles, [
            (str(total_count), "Нийт ажил"),
            (f"{avg_prog}%", "Дундаж биелэлт"),
            (str(done_count), "Дууссан ажил"),
            (str(len(attention_rows)), "Анхаарал шаардах"),
        ]))
        story.append(Spacer(1, 8 * mm))

        story.append(Paragraph("Хэлтсүүдийн гүйцэтгэлийн харьцуулалт", styles['h2']))
        dept_header = [Paragraph(h, styles['th']) for h in ["Хэлтэс", "Ажлын тоо", "Дундаж биелэлт"]]
        dept_data = [dept_header]
        for dept in DEPARTMENTS:
            d_rows = by_dept.get(dept, [])
            d_avg = round(sum(parse_progress(r[6]) for r in d_rows) / len(d_rows), 1) if d_rows else 0
            dept_data.append([
                Paragraph(_pdf_esc(dept), styles['cell_bold']),
                Paragraph(str(len(d_rows)), styles['cell']),
                Paragraph(f"{d_avg}%", styles['cell_bold']),
            ])
        dept_table = Table(dept_data, colWidths=[80 * mm, 40 * mm, 40 * mm], repeatRows=1)
        dept_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563EB')),
            ('GRID', (0, 0), (-1, -1), 0.6, colors.HexColor('#CBD5E1')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')]),
        ]))
        story.append(dept_table)
        story.append(PageBreak())

        story.append(Paragraph("Шийдвэрлүүлэх шаардлагатай (дуусаагүй, биелэлт 25–75%)", styles['h2']))
        if attention_rows:
            att_header = [Paragraph(h, styles['th']) for h in ["Хэлтэс", "Чиг үүрэг", "Ажил", "Явц"]]
            att_data = [att_header]
            for r in attention_rows[:30]:
                att_data.append([
                    Paragraph(_pdf_esc(r[1]), styles['cell']),
                    Paragraph(_pdf_esc(r[3]), styles['cell']),
                    Paragraph(_pdf_esc(r[4]), styles['cell']),
                    Paragraph(_pdf_esc(r[6]), styles['cell_bold']),
                ])
            att_table = Table(att_data, colWidths=[35 * mm, 35 * mm, 70 * mm, 20 * mm], repeatRows=1)
            att_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EF4444')),
                ('GRID', (0, 0), (-1, -1), 0.6, colors.HexColor('#CBD5E1')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FEF2F2')]),
            ]))
            story.append(att_table)
        else:
            story.append(Paragraph("Анхаарал шаардах ажил алга.", styles['cell']))
        story.append(PageBreak())

    for i, dept in enumerate(departments):
        d_rows = by_dept.get(dept, [])
        d_total = len(d_rows)
        d_avg = round(sum(parse_progress(r[6]) for r in d_rows) / d_total, 1) if d_total else 0
        d_done = sum(1 for r in d_rows if parse_progress(r[6]) >= 100)

        story.append(Paragraph(dept, styles['h2']))
        story.append(_pdf_kpi_table(styles, [
            (str(d_total), "Ажлын тоо"),
            (f"{d_avg}%", "Дундаж биелэлт"),
            (str(d_done), "Дууссан"),
        ]))
        story.append(Spacer(1, 6 * mm))

        if d_rows:
            story.append(_pdf_task_table(styles, d_rows))
        else:
            story.append(Paragraph("Сонгосон хугацаанд бүртгэгдсэн ажил алга.", styles['cell']))

        if i < len(departments) - 1:
            story.append(PageBreak())

    doc.build(story)


@app.route('/report/export_pdf')
@login_required
def export_report_pdf():
    departments, is_admin, requested_dept = _scope_departments()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()

    conn = sqlite3.connect(DB_NAME)
    rows = _fetch_report_rows(conn, departments, start_date, end_date)
    conn.close()
    by_dept = _group_by_department(rows)

    suffix = requested_dept if requested_dept else "Company"
    fname = f"UAG_Report_{suffix}_{datetime.now().strftime('%Y%m%d')}.pdf".replace(" ", "_")
    output_path = os.path.join(os.getcwd(), fname)

    _generate_report_pdf(output_path, departments, is_admin, requested_dept, rows, by_dept, start_date, end_date)
    return send_file(output_path, as_attachment=True, download_name=fname, mimetype='application/pdf')


# ---------------------------------------------------------
# ADMIN CONTROLLER & MANAGEMENT
# ---------------------------------------------------------
@app.route('/admin')
@admin_required
def admin():
    page = request.args.get('page', 'categories')
    search_q = request.args.get('q', '').strip()
    dept_filter = request.args.get('dept', '').strip()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()
    preset = request.args.get('preset', '').strip()
    start_date, end_date = date_range_from_preset(preset, start_date, end_date)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    body = ""

    if page == 'categories':
        # Bug fix: categories are now grouped by department, and the
        # add-category form requires picking a department so a new
        # category is never accidentally shared across all departments.
        cursor.execute("SELECT id, name, department FROM categories ORDER BY department ASC, id DESC")
        cats = cursor.fetchall()

        cats_by_dept = {}
        for c in cats:
            cats_by_dept.setdefault(c[2] or "—", []).append(c)

        dept_sections = ""
        for dept in DEPARTMENTS:
            dept_cats = cats_by_dept.get(dept, [])
            items = "".join(
                f"<li style='margin-bottom:8px;'><b>{c[1]}</b> "
                f"<a href='/admin/delete_category/{c[0]}' style='color:red; margin-left: 15px; font-size:12px;' onclick='return confirm(\"Устгах уу?\")'>[Устгах]</a></li>"
                for c in dept_cats
            ) or "<li style='color:#94a3b8;'>Чиг үүрэг бүртгэгдээгүй байна.</li>"
            dept_sections += f"""
            <div style="margin-bottom:18px;">
                <h4 style="margin-bottom:6px; color:#2563eb;">{dept}</h4>
                <ul style="padding-left:20px; margin-top:0;">{items}</ul>
            </div>
            """

        dept_options_add = "".join([f'<option value="{d}">{d}</option>' for d in DEPARTMENTS])

        body = f"""
        <div class="card">
            <h3>➕ Шинэ "Чиг үүрэг" нэмэх</h3>
            <p style="color:#64748b; font-size:13px;">Чиг үүрэг тухайн хэлтэст л харагдах тул аль хэлтэст зориулж нэмэхээ сонгоно уу.</p>
            <form action="/admin/add_category" method="POST" style="display: flex; gap: 10px;">
                <select name="department" required style="flex: 1;">
                    <option value="">-- Хэлтэс сонгох --</option>
                    {dept_options_add}
                </select>
                <input type="text" name="category_name" placeholder="Дропдаунд нэмэх Чиг үүргийн нэр..." required style="flex:2;">
                <button type="submit" class="btn btn-primary" style="width:auto;">Нэмэх</button>
            </form>
        </div>
        <div class="card">
            <h3>📋 Идэвхтэй Чиг үүргүүд (хэлтсээр)</h3>
            {dept_sections}
        </div>
        """

    elif page == 'reports':
        sql = "SELECT id, department, report_date, func_area, task_desc, task_result, progress, assignee, status, created_at, attachment FROM reports WHERE 1=1"
        params = []

        if search_q:
            sql += " AND (task_desc LIKE ? OR assignee LIKE ? OR report_date LIKE ?)"
            params.extend([f"%{search_q}%", f"%{search_q}%", f"%{search_q}%"])
        if dept_filter:
            sql += " AND department = ?"
            params.append(dept_filter)
        if start_date:
            sql += " AND created_at >= ?"
            params.append(start_date)
        if end_date:
            sql += " AND created_at <= ?"
            params.append(end_date)

        sql += " ORDER BY id DESC"
        cursor.execute(sql, params)
        reps = cursor.fetchall()

        dept_options = "".join([f'<option value="{d}" {"selected" if dept_filter==d else ""}>{d}</option>' for d in DEPARTMENTS])

        reps_rows = ""
        for r in reps:
            st = '<span class="badge badge-info">Submitted</span>' if r[8] == 'submitted' else '<span class="badge badge-success">Approved</span>'
            created_dt = r[9] if len(r) > 9 and r[9] else '-'
            attachment_name = r[10] if len(r) > 10 else None
            if attachment_name:
                attachment_cell = f'''<div class="attachment-cell">
                    <a href="/static/uploads/{attachment_name}" target="_blank"><img class="attachment-thumb" src="/static/uploads/{attachment_name}" alt="хавсралт"></a>
                    <button type="button" class="btn btn-danger btn-sm" title="Зураг устгах" onclick="deleteAttachment({r[0]}, this)">🗑</button>
                </div>'''
            else:
                attachment_cell = '<span class="attachment-empty">—</span>'
            reps_rows += f"""
            <tr>
                <td><b>{r[2]}</b><br><small style="color:#64748b;">Огноо: {created_dt}</small></td>
                <td><b>{r[1]}</b></td>
                <td>{r[3]}</td>
                <td>{r[4]}</td>
                <td>{r[5] or '-'}</td>
                <td><b>{r[6]}</b></td>
                <td>{r[7] or '-'}</td>
                <td>{attachment_cell}</td>
                <td>{st}</td>
                <td>
                    <div class="action-cell">
                        <a href="/admin/toggle_report_status/{r[0]}" class="btn btn-warning btn-sm" title="Төлөв солих / Баталгаажуулах эсвэл Буцаах">Төлөв</a>
                        <a href="/admin/delete_report/{r[0]}" class="btn btn-danger btn-sm" onclick="return confirm('Устгах уу?')" title="Устгах">✕</a>
                    </div>
                </td>
            </tr>
            """

        export_url = f"/admin/export_csv?q={search_q}&dept={dept_filter}&start_date={start_date}&end_date={end_date}"
        report_pdf_url = f"/report?start_date={start_date}&end_date={end_date}" + (f"&department={dept_filter}" if dept_filter else "")

        body = f"""
        <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <h3>📂 Удирдлагын Нэгдсэн Тайлангийн Жоорогнол</h3>
                <div style="display:flex; gap:8px; flex-wrap:wrap;">
                    <a href="{report_pdf_url}" class="btn btn-primary">📑 PDF/PPTX бэлэн тайлан руу очих</a>
                    <a href="{export_url}" class="btn btn-success">📥 Шүүсэн тайланг Excel (CSV) Татах</a>
                </div>
            </div>

            <div class="filter-card">
                <div class="quick-presets">
                    <span style="font-size:12px; font-weight:bold; color:#64748b; margin-right:5px;">⚡ Хурдан шүүлт:</span>
                    <a href="/admin?page=reports&preset=this_week&dept={dept_filter}&q={search_q}" class="preset-btn {'active' if preset=='this_week' else ''}">📅 Энэ 7 хоног</a>
                    <a href="/admin?page=reports&preset=last_week&dept={dept_filter}&q={search_q}" class="preset-btn {'active' if preset=='last_week' else ''}">⏮️ Өнгөрсөн 7 хоног</a>
                    <a href="/admin?page=reports&preset=this_month&dept={dept_filter}&q={search_q}" class="preset-btn {'active' if preset=='this_month' else ''}">🗓️ Энэ сар</a>
                </div>

                <form method="GET" action="/admin" class="filter-form">
                    <input type="hidden" name="page" value="reports">

                    <div style="flex: 2; min-width: 170px;">
                        <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Хайх утга:</label>
                        <input type="text" name="q" value="{search_q}" placeholder="Ажлын утга, хариуцагчаар...">
                    </div>

                    <div style="flex: 1.5; min-width: 140px;">
                        <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Хэлтэс:</label>
                        <select name="dept">
                            <option value="">-- Бүх хэлтэс --</option>
                            {dept_options}
                        </select>
                    </div>

                    <div style="flex: 1; min-width: 135px;">
                        <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Эхлэх огноо:</label>
                        <input type="date" name="start_date" value="{start_date}">
                    </div>

                    <div style="flex: 1; min-width: 135px;">
                        <label style="font-size:12px; font-weight:bold; display:block; margin-bottom:4px;">Дуусах огноо:</label>
                        <input type="date" name="end_date" value="{end_date}">
                    </div>

                    <div style="display:flex; gap:6px;">
                        <button type="submit" class="btn btn-primary" style="width:auto;">🔍 Шүүх</button>
                        <a href="/admin?page=reports" class="btn btn-outline" title="Шүүлтүүрийг арилгах">🔄</a>
                    </div>
                </form>
            </div>

            <table>
                <colgroup>
                    <col style="width: 11%;">
                    <col style="width: 8%;">
                    <col style="width: 9%;">
                    <col style="width: 21%;">
                    <col style="width: 15%;">
                    <col style="width: 5%;">
                    <col style="width: 7%;">
                    <col style="width: 7%;">
                    <col style="width: 6%;">
                    <col style="width: 8%;">
                </colgroup>
                <thead>
                    <tr>
                        <th>Тайлант огноо</th>
                        <th>Хэлтэс</th>
                        <th>Чиг үүрэг</th>
                        <th>Ажил</th>
                        <th>Үр дүн</th>
                        <th>Явц</th>
                        <th>Хариуцагч</th>
                        <th>📎 Зураг</th>
                        <th>Төлөв</th>
                        <th>Үйлдэл</th>
                    </tr>
                </thead>
                <tbody>{reps_rows if reps_rows else '<tr><td colspan="10" style="text-align:center; padding: 25px; color: #94a3b8;">Сонгосон огноо болон шүүлтүүрт тохирох тайлан олдсонгүй.</td></tr>'}</tbody>
            </table>
        </div>
        """

    elif page == 'analytics':
        return redirect(url_for('user_analytics'))

    elif page == 'ai':
        cursor.execute("SELECT department, func_area, task_desc, progress FROM reports")
        reps = cursor.fetchall()

        dept_summary = {}
        for r in reps:
            dept_summary.setdefault(r[0], []).append(f"• <b>[{r[1]}]</b> {r[2]} - <i>Явц: {r[3]}</i>")

        ai_output = "<b>🤖 AI Автомат Дүгнэлт ба Зөвлөмж:</b><br><br>"
        if reps:
            for dept, tasks in dept_summary.items():
                ai_output += f"<div style='margin-bottom:12px;'><b>📌 {dept} ({len(tasks)} ажил):</b><br>" + "<br>".join(tasks) + "</div>"
            ai_output += "<hr style='border:0; border-top:1px solid #e2e8f0; margin:15px 0;'><b style='color:#2563eb;'>💡 AI Системийн Нэгдсэн Зөвлөмж:</b><br>• Гүйцэтгэлийн хувь 50%-иас доош байгаа ажлуудад онцгой анхаарч хугацааг нарийвчлах.<br>• Хэлтсүүдийн хоорондын ажлын ачааллыг тэнцвэржүүлж, чиг үүргүүдийг тодорхой болгох."
        else:
            ai_output += "Одоогоор шинжлэх тайлангийн өгөгдөл байхгүй байна."

        body = f"""
        <div class="card">
            <h3>🤖 AI Тайлан & Анализ Боловсруулагч</h3>
            <div style="background: rgba(37, 99, 235, 0.05); padding: 20px; border-radius: 8px; border-left: 4px solid #2563eb; line-height:1.6;">
                {ai_output}
            </div>
        </div>
        """

    elif page == 'others':
        cursor.execute("SELECT id, email, role, department FROM users ORDER BY id ASC")
        users_list = cursor.fetchall()

        users_rows = ""
        for u in users_list:
            role_badge = f'<span class="badge badge-admin">admin</span>' if u[2] == 'admin' else '<span class="badge badge-user">user</span>'
            users_rows += f"""
            <tr>
                <td>{u[0]}</td>
                <td><b>{u[1]}</b></td>
                <td><b style="color:#2563eb;">{u[3] or "Бүх хэлтэс"}</b></td>
                <td>{role_badge}</td>
                <td><a href='/admin/delete_user/{u[0]}' class='btn btn-danger btn-sm' onclick='return confirm("Устгах уу?")'>Устгах</a></td>
            </tr>
            """

        dept_options_add = "".join([f'<option value="{d}">{d}</option>' for d in DEPARTMENTS])

        body = f"""
        <div class="card">
            <h3>👤 Хэрэглэгчдийн Удирдлага</h3>
            <form action="/admin/add_user" method="POST" style="display: grid; grid-template-columns: 2fr 2fr 2fr 1fr 1fr; gap: 10px; margin-bottom:20px; align-items: center;">
                <input type="email" name="email" placeholder="Шинэ хэрэглэгчийн имэйл..." required>
                <input type="password" name="password" placeholder="Нууц үг..." required>
                <select name="department" required>
                    <option value="">-- Хэсэг нэгж сонгох --</option>
                    {dept_options_add}
                </select>
                <select name="role">
                    <option value="user">User</option>
                    <option value="admin">Admin</option>
                </select>
                <button type="submit" class="btn btn-primary" style="padding:10px;">+ Нэмэх</button>
            </form>

            <table>
                <colgroup>
                    <col style="width: 10%;">
                    <col style="width: 30%;">
                    <col style="width: 30%;">
                    <col style="width: 15%;">
                    <col style="width: 15%;">
                </colgroup>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Имэйл</th>
                        <th>Хэсэг нэгж</th>
                        <th>Эрх</th>
                        <th>Үйлдэл</th>
                    </tr>
                </thead>
                <tbody>{users_rows}</tbody>
            </table>
        </div>
        """

    conn.close()
    return render_template_string(LAYOUT_HEADER + body + LAYOUT_FOOTER)

# ---------------------------------------------------------
# ADMIN ACTIONS
# ---------------------------------------------------------
@app.route('/admin/add_category', methods=['POST'])
@admin_required
def add_category():
    cat_name = request.form.get('category_name', '').strip()
    department = request.form.get('department', '').strip()
    if cat_name and department in DEPARTMENTS:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO categories (name, department) VALUES (?, ?)", (cat_name, department))
        conn.commit()
        conn.close()
    return redirect('/admin?page=categories')

@app.route('/admin/delete_category/<int:id>')
@admin_required
def delete_category(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categories WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/admin?page=categories')

@app.route('/admin/delete_report/<int:id>')
@admin_required
def delete_report(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reports WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/admin?page=reports')

@app.route('/admin/toggle_report_status/<int:id>')
@admin_required
def toggle_report_status(id):
    redirect_target = request.args.get('redirect', '')
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM reports WHERE id = ?", (id,))
    res = cursor.fetchone()
    if res:
        new_status = 'approved' if res[0] == 'submitted' else 'submitted'
        cursor.execute("UPDATE reports SET status = ? WHERE id = ?", (new_status, id))
        conn.commit()
    conn.close()

    if redirect_target == 'home':
        return redirect(url_for('index'))
    return redirect('/admin?page=reports')

@app.route('/admin/add_user', methods=['POST'])
@admin_required
def add_user():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '').strip()
    department = request.form.get('department', '').strip()
    role = request.form.get('role', 'user')

    if email and password:
        hashed_pw = generate_password_hash(password)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password, role, department) VALUES (?, ?, ?, ?)", (email, hashed_pw, role, department))
            conn.commit()
        except sqlite3.IntegrityError:
            pass
        conn.close()

    return redirect('/admin?page=others')

@app.route('/admin/delete_user/<int:id>')
@admin_required
def delete_user(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/admin?page=others')

@app.route('/admin/export_csv')
@admin_required
def export_csv():
    search_q = request.args.get('q', '').strip()
    dept_filter = request.args.get('dept', '').strip()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    sql = "SELECT report_date, department, func_area, task_desc, task_result, progress, assignee, status, created_at FROM reports WHERE 1=1"
    params = []

    if search_q:
        sql += " AND (task_desc LIKE ? OR assignee LIKE ? OR report_date LIKE ?)"
        params.extend([f"%{search_q}%", f"%{search_q}%", f"%{search_q}%"])
    if dept_filter:
        sql += " AND department = ?"
        params.append(dept_filter)
    if start_date:
        sql += " AND created_at >= ?"
        params.append(start_date)
    if end_date:
        sql += " AND created_at <= ?"
        params.append(end_date)

    sql += " ORDER BY id DESC"
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    conn.close()

    output = io.StringIO()
    output.write('﻿')
    writer = csv.writer(output)
    writer.writerow(['Тайлант огноо', 'Хэлтэс', 'Чиг үүрэг', 'Ажлын мэдээлэл', 'Үр дүн', 'Явц', 'Хариуцагч', 'Төлөв', 'Системд бүртгэсэн огноо'])

    for r in rows:
        writer.writerow(r)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": f"attachment; filename=uag_reports_export_{datetime.now().strftime('%Y%m%d')}.csv"}
    )

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print("-------------------------------------------------------")
    print(f"ҮАГ Систем ажиллаж байна: http://127.0.0.1:{port}")
    print("Админ имэйл: admin@uag.mn | Нууц үг: 123456")
    print("-------------------------------------------------------")
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
