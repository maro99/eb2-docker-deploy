from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# Static
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
# EC2_DEPLOY = os.path.dirname(BASE_DIR)
# MEDIA_ROOT = os.path.join(EC2_DEPLOY,'.media')
# MEDIA_URL ='/media/'

# wsgi
WSGI_APPLICATION = 'config.wsgi.dev.application'

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'