from .base import *

DEBUG = True


# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
EC2_DEPLOY = os.path.dirname(BASE_DIR)
MEDIA_ROOT = os.path.join(EC2_DEPLOY,'.media')
MEDIA_URL ='/media/'

# wsgi
WSGI_APPLICATION = 'config.wsgi.local.application'

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# JSON_DIR =os.path.join(EC2_DEPLOY,'.secrets')
# json_data = open(f'{JSON_DIR}/base.json').read()
# data = json.loads(json_data)
# SECRET_KEY = data["SECRET_KEY"]
print(DATABASES)
