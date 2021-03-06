"""
Django settings for eLegislative project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as messages
import os
# http://whitenoise.evans.io/en/stable/index.html



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = os.path.join(BASE_DIR, 'elegislative_app/templates')
STATIC_DIR = os.path.join(BASE_DIR, 'elegislative_app/static')
MEDIA_DIR = os.path.join(BASE_DIR, 'elegislative_app/media')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0=8_446=toqa#ix8sv_6rtmk54ajx1paa_fp+xfz_zt_ch2+r%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
 
    # 'jet.dashboard',
    # 'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'elegislative_app',
    'import_export',
    'django_cleanup', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'eLegislative.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'eLegislative.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'elms',
#         'USER': 'lloydgarcia77',
#         'PASSWORD': 'qweQWE123!',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'elegislative_system_db',
#         'USER': 'root',
#         'PASSWORD': 'r00t@passw0rd77',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Singapore'

DATETIME_FORMAT = '%b %d %Y %a %I:%M %p'

USE_I18N = True

USE_L10N = True

USE_TZ = False
# https://docs.djangoproject.com/en/3.2/releases/3.2/
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
 

AUTH_USER_MODEL = 'elegislative_app.User'
# for jet
X_FRAME_OPTIONS = 'SAMEORIGIN'

STATIC_URL = '/static/'
# STATIC_ROOT = STATIC_DIR
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

 
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# -------Using Gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 
EMAIL_HOST_USER = 'lloydgarcia77@gmail.com'
EMAIL_HOST_PASSWORD = 'LloydQueen77'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_FROM = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Go Daddy
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_HOST_USER = 'info@lits.com.ph'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = '@Helios2o18'
# EMAIL_PORT = 587
# EMAIL_USE_SSL = False
# EMAIL_USE_TLS = True
# from cryptography.fernet import Fernet
# Fernet.generate_key()
ENCRYPT_KEY = b'xlNVkz4loCnsQWGmKEMjj7De5fj0d_N0_yeKxGJxDSk='


NOTIFICATION_TAGS = (
    ('None','None'),
    ('Agenda','Agenda'),
    ('Resolution','Resolution'),
    ('Ordinance','Ordinance'),
    ('MOM','MOM'),
    ('CRO','CRO'),
    ('CRR','CRR'),
    ('CMRO','CMRO'),
    ('CMRR','CMRR'),
    ('Announcement','Announcement'),
)
# https://pypi.org/project/dj-database-url/
# db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES['default'].update(db_from_env) 

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1200 # set just 10 seconds to test
SESSION_SAVE_EVERY_REQUEST = True

DATA_UPLOAD_MAX_MEMORY_SIZE = None
# DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880 # 5MB 