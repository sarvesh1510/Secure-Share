# app.py

from flask import Flask, request, send_from_directory, render_template, redirect, url_for, flash, session, jsonify
import os, random, hashlib, mimetypes, base64
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from functools import wraps
from io import BytesIO
import qrcode

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

# ================= CONFIG =================
UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

app.config.update(
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH=MAX_FILE_SIZE,
    FILE_EXPIRATION=timedelta(hours=24),
    ALLOWED_EXTENSIONS={
        'png','jpg','jpeg','gif','pdf','txt','zip',
        'doc','docx','xls','xlsx','ppt','pptx',
        'mp3','mp4','mov','avi','csv','json','html','css','js'
    }
)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= TEMP STORAGE =================
file_records = {}

# ================= HELPERS =================
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_code():
    return str(random.randint(100000, 999999))

def generate_file_id():
    return f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000,9999)}"

def clean_expired_files():
    now = datetime.now()
    expired = [fid for fid, rec in file_records.items() if now > rec['expires_at']]
    
    for fid in expired:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_records[fid]['filename']))
        except:
            pass
        file_records.pop(fid, None)

def hash_file(filepath):
    sha = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()

# ================= ROUTES =================
@app.route('/')
def home():
    clean_expired_files()
    return render_template('index.html')

@app.route('/upload_page')
def upload_page():
    return render_template('upload_page.html')

# ===== FILE UPLOAD =====
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')

    if not file or file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('upload_page'))

    if not allowed_file(file.filename):
        flash('File type not allowed', 'error')
        return redirect(url_for('upload_page'))

    file_code = generate_code()
    file_id = generate_file_id()

    original_name = secure_filename(file.filename)
    ext = original_name.rsplit('.', 1)[1].lower()
    stored_name = f"{file_id}.{ext}"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], stored_name)
    file.save(filepath)

    file_records[file_code] = {
        'filename': stored_name,
        'original_filename': original_name,
        'upload_time': datetime.now(),
        'expires_at': datetime.now() + app.config['FILE_EXPIRATION'],
        'download_count': 0,
        'file_size': os.path.getsize(filepath),
        'file_hash': hash_file(filepath),
        'mime_type': mimetypes.guess_type(original_name)[0] or 'application/octet-stream'
    }

    # QR Code
    qr_url = url_for('download_file', file_code=file_code, _external=True)
    qr = qrcode.make(qr_url)
    buffer = BytesIO()
    qr.save(buffer)
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render_template(
        'upload_success.html',
        qr_code=qr_base64,
        file_code=file_code,
        file_name=original_name,
        file_size=file_records[file_code]['file_size'],
        expires_at=file_records[file_code]['expires_at'].strftime('%Y-%m-%d %H:%M:%S')
    )

# ===== ENTER CODE =====
@app.route('/enter_code', methods=['GET', 'POST'])
def enter_code():
    if request.method == 'POST':
        code = request.form.get('code', '').strip()

        if code not in file_records:
            flash('Invalid code', 'error')
            return redirect(url_for('enter_code'))

        if datetime.now() > file_records[code]['expires_at']:
            flash('File expired', 'error')
            return redirect(url_for('enter_code'))

        return redirect(url_for('download_file', file_code=code))

    return render_template('enter_code.html')

# ===== DOWNLOAD PAGE =====
@app.route('/download/<file_code>')
def download_file(file_code):
    record = file_records.get(file_code)

    if not record:
        flash('Invalid file code', 'error')
        return redirect(url_for('enter_code'))

    if datetime.now() > record['expires_at']:
        flash('File expired', 'error')
        return redirect(url_for('enter_code'))

    record['download_count'] += 1

    return render_template(
        'download_file.html',
        file_code=file_code,
        file_name=record['original_filename'],
        file_size=record['file_size'],
        expires_at=record['expires_at'].strftime('%Y-%m-%d %H:%M:%S')
    )

# ===== SERVE FILE =====
@app.route('/download_file/<file_code>')
def serve_file(file_code):
    record = file_records.get(file_code)
    if not record:
        return "File not found", 404

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        record['filename'],
        as_attachment=True,
        download_name=record['original_filename']
    )

# ===== API =====
@app.route('/api/check_code/<file_code>')
def check_code(file_code):
    record = file_records.get(file_code)

    if not record:
        return jsonify({'valid': False})

    if datetime.now() > record['expires_at']:
        return jsonify({'valid': False, 'reason': 'expired'})

    return jsonify({
        'valid': True,
        'filename': record['original_filename'],
        'size': record['file_size']
    })

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)
