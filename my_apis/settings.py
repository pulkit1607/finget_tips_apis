"""
Django settings for my_apis project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qzm)=u#tt+w6(a0@p3a)nqwnx+avdkuwl@74bmk0vl_gr+i!j6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'apis',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
    'rest_framework.authtoken',
    'storages',
    'django.contrib.postgres',
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

ROOT_URLCONF = 'my_apis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'my_apis.context_processor.form_context'
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

WSGI_APPLICATION = 'my_apis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DB_NAME', 'fingertips'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_USER', 'postgres'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'EXCEPTION_HANDLER': 'sides.exception.custom_exception_handler',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
    'DEFAULT_PARSER_CLASSES': (
       'rest_framework.parsers.JSONParser',
       'rest_framework.parsers.FormParser',
       'rest_framework.parsers.MultiPartParser',
    ),
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "api_key": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
    "JSON_EDITOR": True,
    "SHOW_REQUEST_HEADERS": True
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


# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'pulkitjain1607@gmail.com'
# EMAIL_HOST_PASSWORD = '27346504'
# DEFAULT_FROM_EMAIL = 'pulkitjain1607@gmail.com'
# DEFAULT_TO_EMAIL = 'pulkitjain1607@gmail.com'
# DEFAULT_FROM_EMAIL_NAME = 'ALP'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'fingertips')
# AWS_ACCESS_KEY_ID = 'AKIAIXW5DZXFD6PXCW2A'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join("static/"),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# TEST RAZORPAY CREDENTIALS
RAZORPAY_KEY_ID = "rzp_test_S7gxsV55dTOz1E"
RAZORPAY_KEY_KEY = "PsQyqccC4iZFH5wcewxIEu35"

#INSTAMOJO CREDENTIALS
PRIVATE_API_KEY = "17dc18b558c84e50dcf97dd2ade37624"
PRIVATE_AUTH_TOKEN = "1a733717bcd1fa397dd0d04d3bace0fa"
PRIVATE_SALT = "0e98c4c9b94f4b63916a087075e2f95e"

GOOGLE_MAPS_GEOLOCATION_KEY = "AIzaSyB8L5XklsbEJ-_R5v-YJe7Znl08m-4n2Zw"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mailqueued@gmail.com'
EMAIL_HOST_PASSWORD = 'pulkit1607'
DEFAULT_FROM_EMAIL = 'mailqueued@gmail.com'
DEFAULT_TO_EMAIL = 'mailqueued@gmail.com'
DEFAULT_FROM_EMAIL_NAME = 'QUEUED'
