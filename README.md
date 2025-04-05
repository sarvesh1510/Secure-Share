#  Secure Share File Sharing App with QR Code and Expiry

This project is a Flask-based secure file sharing web application that allows users to upload files, generate a unique access code, and download them via a secure link or QR code. Files are stored temporarily and automatically expire after 24 hours.

## Features

-  Upload files with unique access codes
-  Supports various file formats (images, documents, media, etc.)
-  File download tracking
-  Automatic file expiration after 24 hours
-  QR code generation for easy sharing
-  Simple admin login dashboard
-  REST API endpoint to verify file codes

---

##  Tech Stack

- Python 3.x
- Flask
- HTML, CSS (Bootstrap optional)
- JavaScript
- QRCode (Python lib)
- SHA256 for file hashing
- SQLite or in-memory Python dict for session/file handling


