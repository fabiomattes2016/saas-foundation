import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')  # Use a default value for development, but override in production

if os.getenv("DEBUG") == '1':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [".railway.app", ".railway.app."]  # Allow all subdomains of railway.app in development

if DEBUG:
    ALLOWED_HOSTS += ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commando',
    'compressor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cfehome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line to specify the templates directory
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

WSGI_APPLICATION = 'cfehome.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "postgres"),
        'USER': os.getenv("DB_USER", "postgres"),
        'PASSWORD': os.getenv("DB_PASSWORD", ""),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-us')
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_BASE_DIR = BASE_DIR / 'static'
STATICFILES_BASE_DIR.mkdir(exist_ok=True, parents=True)

STATICFILES_VENDOR_DIR = STATICFILES_BASE_DIR / 'vendors'

STATICFILES_DIRS = [
    STATICFILES_BASE_DIR
]

if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'prod-cdn'
else:
    STATIC_ROOT = BASE_DIR.parent / 'dev-cdn'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

VENDORS_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.3.0/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.3.0/dist/flowbite.min.js"
}

# COMPRESS_ROOT = BASE_DIR / 'static'
# COMPRESS_ENABLED = True
# STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)