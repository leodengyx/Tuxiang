from base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tuxiang',
        'USER': 'dba_tuxiang',
        'PASSWORD': '84253416',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AUTH_PROFILE_MODULE = "users.UserProfile"

# Project Application definition
PROJECT_APPS = [
    #'rest_framework'
    'users',
    'photos',
    'albums',
]

INSTALLED_APPS += PROJECT_APPS