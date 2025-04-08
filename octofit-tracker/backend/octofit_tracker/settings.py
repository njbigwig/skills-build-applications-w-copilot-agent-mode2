# Add 'octofit_tracker' to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'octofit_tracker',
]

# Configure database based on environment
import os
from pathlib import Path

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

if os.getenv('DJANGO_DB_ENGINE') == 'djongo':
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': os.getenv('MONGO_DB_NAME', 'octofit_db'),
            'HOST': os.getenv('MONGO_HOST', 'localhost'),
            'PORT': int(os.getenv('MONGO_PORT', 27017)),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Enable CORS
INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE = [
    # Base middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    'https://example.com',
    'https://api.example.com',
]
CORS_ALLOW_METHODS = [
    'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'
]
CORS_ALLOW_HEADERS = [
    'content-type', 'authorization', 'x-csrftoken', 'x-requested-with'
]

# Allow all hosts

if os.getenv('DJANGO_ENV') == 'production':
    ALLOWED_HOSTS = ['example.com', 'api.example.com']
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']