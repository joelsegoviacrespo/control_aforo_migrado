# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from pymongo import MongoClient
import os
from decouple import config
from unipath import Path
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG', default=False)
DEBUG = config('DEBUG', default=True)

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '5.196.27.225', config('SERVER', default='127.0.0.1'),'aforo.softwaremediafactory.com']


CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'app',
    'camaras_historico',
    'cliente.apps.ClienteConfig',
    'instalacion.apps.InstalacionConfig',
    'camara_zona.apps.CamaraZonaConfig',
    'monitor.apps.MonitorConfig',
    'camaras.apps.CamarasConfig',
    'aforoInfo.apps.AforoinfoConfig',
    'valores.apps.ValoresConfig',
    'usuarios.apps.UsuariosConfig',
    'fondos.apps.FondosConfig',
    'posicion.apps.PosicionConfig',
    'espacios.apps.EspaciosConfig',
    'display.apps.DisplayConfig',     

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"   # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'instalacion.context_processors.side_menu_instalaciones',
            ],
        },
    },
]



WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {           
         'default': {
             'ENGINE': 'djongo',
             'NAME': 'aforo',
             'ENFORCE_SCHEMA': False,
             'CLIENT': {
                 'host': 'mongodb://user_aforo_mongo:Af0r0smfC10uDM0n4O@5.196.27.225:27227',
                 'port': 27227,
                 'username': 'user_aforo_mongo',
                 'password': 'Af0r0smfC10uDM0n4O',
                 'authSource': 'admin',
                 'authMechanism': 'SCRAM-SHA-1'
             }
        },
'DBCollection1': {
            'ENGINE': 'djongo',
            'NAME': 'aforo',
            'DB_IP': '5.196.27.225',
            'DB_Port': '27227',
            'CLIENT': {
                 'host': 'mongodb://user_aforo_mongo:Af0r0smfC10uDM0n4O@5.196.27.225:27227',
                 'port': 27227,
                 'username': 'user_aforo_mongo',
                 'password': 'Af0r0smfC10uDM0n4O',
                 'authSource': 'admin',
                 'authMechanism': 'SCRAM-SHA-1',
                 'db_collection1': 'cliente',
            }
        },    
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'mosayk')
MEDIA_URL = '/mosayk/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)


#Allow Log by email or console
ADMINS = (('Joel', 'joelsegoviacrespo@gmail.com'))
FTP_SETTINGS = {
    "ftp_url": "ftp.cluster028.hosting.ovh.net",
    "ftp_port": "21",     
    "ftp_user": "softwarext",
    "ftp_pass": "PjE4yQ3qAyzA", 
    "ftp_folder": "www/mosayk/",    
}
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': True,
#    'formatters': {
#        'verbose': {
#            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s'
#        }
#    },
#    'handlers': {
#        'gunicorn': {
#            'level': 'DEBUG',
#            'class': 'logging.handlers.RotatingFileHandler',
#            'formatter': 'verbose',
#            'filename': '/opt/gunicorn.errors',
#            'maxBytes': 1024 * 1024 * 100,  # 100 mb
#        }
#    },
#    'loggers': {
#        'gunicorn.errors': {
#            'level': 'DEBUG',
#            'handlers': ['gunicorn'],
#            'propagate': True,
#        },
#    }
#}

#EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
#EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'testsite_app'
#EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'


#Configuración conexión a la base de datos
DB_IP = config('DB_IP', default='5.196.27.225')
DB_IP ="5.196.27.225"
#DB_IP ="127.0.0.1"
DB_PORT = config('DB_PORT', default='27227')
DB_NAME = config('DB_NAME',default='aforo')
DB_COLLECTION2 = config('DB_COLLECTION1',default='cliente')
DB_USER_NAME = config('DB_USER_NAME',default='user_aforo_mongo')
DB_USER_PASSWORD = config('DB_USER_PASSWORD',default='Af0r0smfC10uDM0n4O')
DB_FULL = "mongodb://user_aforo_mongo:Af0r0smfC10uDM0n4O@5.196.27.225:27227/aforo?authSource=admin&authMechanism=SCRAM-SHA-256"
