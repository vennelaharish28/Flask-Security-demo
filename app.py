"""
Flask Security Demo Application
"""

from flask import Flask, render_template, request, jsonify, session
import sqlite3
import requests
from datetime import datetime

app = Flask(__name__)

# SECURITY ISSUE #1: Hardcoded secret key
app.secret_key = "super-secret-flask-key-12345"

# SECURITY ISSUE #2: Hardcoded database credentials
DB_USER = "admin"
DB_PASSWORD = "password123"
DB_HOST = "192.168.1.100"
DB_PORT = "5432"

# SECURITY ISSUE #3: Hardcoded API keys
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

# SECURITY ISSUE #4: Hardcoded email credentials
EMAIL_USER = "support@company.com"
EMAIL_PASS = "EmailPass2023!"
SMTP_SERVER = "smtp.company.com"

# SECURITY ISSUE #5: Database connection string with credentials
DATABASE_URL = "postgresql://admin:password123@192.168.1.100:5432/myapp_db"

# SECURITY ISSUE #6: JWT Secret
JWT_SECRET = "my-super-secret-jwt-key-dont-tell-anyone"

# SECURITY ISSUE #7: Encryption key
ENCRYPTION_KEY = "16ByteSecretKey!"

# SECURITY ISSUE #8: Internal IP addresses and ports
REDIS_HOST = "10.0.0.50"
REDIS_PORT = 6379
REDIS_PASSWORD = "redis_secret_pass"

# SECURITY ISSUE #9: Third-party service credentials
TWILIO_ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
TWILIO_AUTH_TOKEN = "your_auth_token"
SENDGRID_API_KEY = "SG.1234567890.abcdefghijklmnopqrstuvwxyz"

# SECURITY ISSUE #10: Social media API keys
TWITTER_API_KEY = "abc123def456ghi789"
TWITTER_API_SECRET = "xyz987uvw654rst321"
FACEBOOK_APP_ID = "1234567890123456"
FACEBOOK_APP_SECRET = "abcdef1234567890abcdef1234567890"

class DatabaseManager:
    def __init__(self):
        self.connection_string = f"sqlite:///app.db?user={DB_USER}&password={DB_PASSWORD}"
    
    def authenticate_user(self, username, password):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        return result

@app.route('/')
def home():
    return """
    <html>
    <head><title>Flask Security Demo</title></head>
    <body>
        <h1>🔐 Flask Security Demo Application</h1>
        <p>This application contains intentional security vulnerabilities for educational purposes.</p>
        <h2>Available Endpoints:</h2>
        <ul>
            <li><a href="/admin">/admin</a> - Admin panel with credentials</li>
            <li><a href="/config">/config</a> - Configuration exposure</li>
            <li><a href="/api/keys">/api/keys</a> - API keys exposure</li>
            <li><a href="/debug">/debug</a> - Debug information</li>
            <li><a href="/backup">/backup</a> - Backup configuration</li>
        </ul>
        <p><strong>⚠️ WARNING: This is for testing security tools only!</strong></p>
    </body>
    </html>
    """

@app.route('/admin')
def admin():
    admin_user = "administrator"
    admin_pass = "SuperSecretPassword2023!"
    
    return f"""
    <html>
    <head><title>Admin Panel</title></head>
    <body>
        <h1>🔑 Admin Panel</h1>
        <p>Default admin credentials:</p>
        <p><strong>Username:</strong> {admin_user}</p>
        <p><strong>Password:</strong> {admin_pass}</p>
        <p><strong>Database:</strong> {DATABASE_URL}</p>
        <p><a href="/">← Back to Home</a></p>
    </body>
    </html>
    """

@app.route('/config')
def show_config():
    config = {
        'database_host': DB_HOST,
        'database_user': DB_USER,
        'database_password': DB_PASSWORD,
        'aws_key': AWS_ACCESS_KEY,
        'jwt_secret': JWT_SECRET,
        'stripe_key': STRIPE_SECRET_KEY
    }
    return jsonify(config)

@app.route('/api/keys')
def api_keys():
    keys = {
        'aws_access': AWS_ACCESS_KEY,
        'aws_secret': AWS_SECRET_KEY,
        'github': GITHUB_TOKEN,
        'stripe': STRIPE_SECRET_KEY,
        'sendgrid': SENDGRID_API_KEY,
        'twilio_sid': TWILIO_ACCOUNT_SID,
        'twilio_token': TWILIO_AUTH_TOKEN
    }
    return jsonify(keys)

@app.route('/debug')
def debug_info():
    debug_data = {
        'environment': 'production',
        'secret_key': app.secret_key,
        'database_url': DATABASE_URL,
        'internal_ips': [REDIS_HOST, DB_HOST],
        'all_secrets': {
            'email_password': EMAIL_PASS,
            'redis_password': REDIS_PASSWORD,
            'encryption_key': ENCRYPTION_KEY
        }
    }
    return jsonify(debug_data)

@app.route('/backup')
def backup():
    backup_server = "192.168.1.200"
    backup_user = "backup_admin"
    backup_pass = "BackupPass123!"
    
    return f"""
    <html>
    <head><title>Backup Configuration</title></head>
    <body>
        <h2>💾 Backup Configuration</h2>
        <p><strong>Server:</strong> {backup_server}</p>
        <p><strong>Username:</strong> {backup_user}</p>
        <p><strong>Password:</strong> {backup_pass}</p>
        <p><a href="/">← Back to Home</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    print(f"Starting server with database: {DATABASE_URL}")
    print(f"Using AWS credentials: {AWS_ACCESS_KEY}")
   app.run(host='127.0.0.1', port=8080, debug=True)