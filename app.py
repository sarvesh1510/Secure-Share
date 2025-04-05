from flask import Flask, request, send_from_directory, render_template, redirect, url_for, flash, session, jsonify
import os
import random
import qrcode
import base64
from io import BytesIO
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
import hashlib
import mimetypes
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure random key in production

# Configuration
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB file size limit
app.config['ALLOWED_EXTENSIONS'] = {
    'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'zip', 
    'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'mp3', 
    'mp4', 'mov', 'avi', 'csv', 'json', 'html', 'css', 'js'
}
app.config['FILE_EXPIRATION'] = timedelta(hours=24)  # Files expire after 24 hours

# Database simulation (replace with real database in production)
file_records = {}
user_sessions = {}

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_code():
    """Generate a secure 6-digit code"""
    return str(random.randint(100000, 999999))

def generate_file_id():
    """Generate a unique file ID with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{timestamp}_{random.randint(1000, 9999)}"

def clean_expired_files():
    """Remove expired files from storage and records"""
    now = datetime.now()
    expired_files = [
        file_id for file_id, record in file_records.items()
        if now > record['expires_at']
    ]
    
    for file_id in expired_files:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_records[file_id]['filename']))
            del file_records[file_id]
        except:
            continue

def login_required(f):
    """Decorator for admin/protected routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    """Home page with file sharing options"""
    clean_expired_files()  # Clean up before showing the page
    return render_template('index.html')

@app.route('/upload_page')
def upload_page():
    """File upload page"""
    return render_template('upload_page.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads with enhanced features"""
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('upload_page'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('upload_page'))
    
    if not allowed_file(file.filename):
        flash('File type not allowed', 'error')
        return redirect(url_for('upload_page'))
    
    # Generate unique identifiers
    file_code = generate_code()
    file_id = generate_file_id()
    
    # Secure the filename
    original_filename = secure_filename(file.filename)
    file_ext = original_filename.rsplit('.', 1)[1].lower()
    stored_filename = f"{file_id}.{file_ext}"
    
    # Save file
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], stored_filename))
    
    # Calculate file hash
    file_hash = hashlib.sha256()
    with open(os.path.join(app.config['UPLOAD_FOLDER'], stored_filename), 'rb') as f:
        while chunk := f.read(8192):
            file_hash.update(chunk)
    
    # Store file record
    file_records[file_code] = {
        'filename': stored_filename,
        'original_filename': original_filename,
        'upload_time': datetime.now(),
        'expires_at': datetime.now() + app.config['FILE_EXPIRATION'],
        'download_count': 0,
        'file_size': os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], stored_filename)),
        'file_hash': file_hash.hexdigest(),
        'mime_type': mimetypes.guess_type(original_filename)[0] or 'application/octet-stream'
    }
    
    # Generate QR code
    qr_data = url_for('download_file', file_code=file_code, _external=True)
    qr_code = qrcode.make(qr_data)
    img_stream = BytesIO()
    qr_code.save(img_stream)
    img_stream.seek(0)
    qr_code_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')
    
    return render_template('upload_success.html', 
                         qr_code=qr_code_base64, 
                         file_code=file_code,
                         file_name=original_filename,
                         file_size=file_records[file_code]['file_size'],
                         expires_at=file_records[file_code]['expires_at'].strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/enter_code', methods=['GET', 'POST'])
def enter_code():
    """Handle code entry for file download"""
    if request.method == 'POST':
        access_code = request.form.get('code', '').strip()
        if access_code in file_records:
            if datetime.now() > file_records[access_code]['expires_at']:
                flash('This file has expired', 'error')
                return redirect(url_for('enter_code'))
            return redirect(url_for('download_file', file_code=access_code))
        flash('Invalid code', 'error')
    return render_template('enter_code.html')

@app.route('/download/<file_code>', methods=['GET'])
def download_file(file_code):
    """Serve files with download tracking"""
    if file_code not in file_records:
        flash('Invalid file code', 'error')
        return redirect(url_for('enter_code'))
    
    record = file_records[file_code]
    
    if datetime.now() > record['expires_at']:
        flash('This file has expired', 'error')
        return redirect(url_for('enter_code'))
    
    # Increment download count
    file_records[file_code]['download_count'] += 1
    
    return render_template('download_file.html', 
                         file_code=file_code,
                         file_name=record['original_filename'],
                         file_size=record['file_size'],
                         expires_at=record['expires_at'].strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/download_file/<file_code>', methods=['GET'])
def serve_file(file_code):
    """Serve the actual file for download"""
    if file_code not in file_records:
        return "File not found", 404
    
    record = file_records[file_code]
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        record['filename'],
        as_attachment=True,
        download_name=record['original_filename']
    )

@app.route('/api/check_code/<file_code>', methods=['GET'])
def check_code(file_code):
    """API endpoint to check if a code is valid"""
    if file_code in file_records:
        if datetime.now() > file_records[file_code]['expires_at']:
            return jsonify({'valid': False, 'reason': 'expired'})
        return jsonify({
            'valid': True,
            'filename': file_records[file_code]['original_filename'],
            'size': file_records[file_code]['file_size'],
            'expires': file_records[file_code]['expires_at'].isoformat()
        })
    return jsonify({'valid': False, 'reason': 'not_found'})

# Admin routes (protected)
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # In production, use proper authentication with hashed passwords
        if username == 'admin' and password == 'securepassword':
            session['user_id'] = 'admin'
            return redirect(url_for('admin_dashboard'))
        flash('Invalid credentials', 'error')
    return render_template('admin_login.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')