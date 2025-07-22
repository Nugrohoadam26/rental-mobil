import os
from pathlib import Path

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-ganti-ini-di-produksi'
DEBUG = True
ALLOWED_HOSTS = []

# APLIKASI TERINSTAL
INSTALLED_APPS = [
    'jazzmin',  # Untuk tampilan admin lebih baik
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rental',
    'django.contrib.humanize',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rental_mobil.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'rental', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rental_mobil.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# VALIDASI PASSWORD (Kosongkan saat pengembangan)
AUTH_PASSWORD_VALIDATORS = []

# LOKALISASI
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# FILE STATIS & MEDIA
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'rental', 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# LOGIN / LOGOUT
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'daftar_mobil'
LOGOUT_REDIRECT_URL = 'login'

# AUTO FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


