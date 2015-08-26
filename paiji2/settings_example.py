# Import common settings from settings_common.py
try:
    from settings_common import *
except ImportError:
    print "The settings_common.py file does not exist."
    print "Your installation is improperly configured."
    exit()

# from django.conf import global_settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# INSTALLED_APPS += ('debug_toolbar',)

SECRET_KEY = 'mysecretkey'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# IP_AUTH_GROUPS is used to create group base upon ip range
# To use it, you need to enable the IpAuthGroupMiddleware
# See below
IP_AUTH_GROUPS = {
    # 'local': ['127.0.0.1', ],
    # 'school': ['192.168.0.0/16', '10.8.0.0/16', ],
}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Admins
ADMINS = (('Paiji developers', 'paiji-dev@rezometz.org'))

STATIC_ROOT = os.path.join(BASE_DIR, '/static')
