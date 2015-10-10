# example settings for the dev server #

# Import common settings from settings_common.py
try:
    from settings_common import *
except ImportError:
    print "The settings_common.py file does not exist."
    print "Your installation is improperly configured."
    exit()


INSTALLED_APPS += (
    # 'debug_toolbar',

    # paiji2 apps

    'paiji2_utils',
    # 'paiji2_weather',
    # 'paiji2_infoconcert',
    'paiji2_survey',
    'paiji2_carpooling',
    # 'paiji2_mettis',
    'paiji2_shoutbox',
    'mptt',
    'paiji2_forum',
    'paiji2_comic',
    'django_markdown',
    'paiji2_social',
)

# URLs

ROOT_URLCONF = 'paiji2.dev_urls'  # to serve media files

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

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

# irc links in the navbar
IRC = {
    'enabled': True,
    'public': True,
    'nickname': 'Yseult',
    'irclc_url': 'irc.lc',
    'servers': (
        # {
        #     'name': 'Name',
        #     'url': 'server_url.domain',
        #     'channel': (
        #         'channel1',
        #         'channel2'
        #     ),
        # },
        {
            'name': 'Debian',
            'url': 'irc.debian.org',
            'channels': (
                'debian',
                'xen',
            ),
        },
        {
            'name': 'Freenode',
            'url': 'irc.freenode.net',
            'channels': (
                'freenode',
                'ubuntu',
                'debian',
            ),
        },
    ),
}

HTMLVALIDATOR_ENABLED = True
HTMLVALIDATOR_FAILFAST = True
HTMLVALIDATOR_DUMPDIR = os.path.join(BASE_DIR, 'validation_errors')
HTMLVALIDATOR_VNU_URL = 'https://validator.nu/'

# testing when the test server is running
if HTMLVALIDATOR_ENABLED:
    MIDDLEWARE_CLASSES += ("htmlvalidator.middleware.HTMLValidator",)

# email conf
EMAIL_HOST = 'smtp.myserver.net'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'me@myserver.net'  # important
EMAIL_HOST_USER = 'me'
EMAIL_HOST_PASSWORD = 'alibaba'
EMAIL_USE_TLS = True

REZO_MAIL = 'test-rezo@mydomain.td'

# paiji2-weather
OPENWEATHERMAP_API_KEY = ''
