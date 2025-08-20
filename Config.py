"""
Configuration file with hardcoded sensitive information
"""

class Config:
    # SECURITY ISSUE: Hardcoded secrets in configuration
    SECRET_KEY = "super-secret-flask-key-12345"
    
    # Database configuration
    DB_HOST = "192.168.1.100"
    DB_USER = "admin"  
    DB_PASSWORD = "password123"
    DB_NAME = "security_demo"
    
    # AWS Configuration
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    # API Keys
    STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
    GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
    
    # Email settings
    MAIL_USERNAME = "support@company.com"
    MAIL_PASSWORD = "EmailPass2023!"
    
    # Social Media
    TWITTER_API_KEY = "abc123def456ghi789"
    TWITTER_API_SECRET = "xyz987uvw654rst321"

class ProductionConfig(Config):
    DEBUG = False
    ADMIN_USERNAME = "administrator"
    ADMIN_PASSWORD = "SuperSecretPassword2023!"