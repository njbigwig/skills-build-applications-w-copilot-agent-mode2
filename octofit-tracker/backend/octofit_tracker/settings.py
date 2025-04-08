# Add 'octofit_tracker' to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'octofit_tracker',
]

# Add MongoDB database configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Enable CORS
INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
] + MIDDLEWARE

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'
]
CORS_ALLOW_HEADERS = [
    'content-type', 'authorization', 'x-csrftoken', 'x-requested-with'
]

# Allow all hosts
ALLOWED_HOSTS = ['*']