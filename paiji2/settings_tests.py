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


INSTALLED_APPS += (
    # 'debug_toolbar',

    # paiji2 apps

    'paiji2_utils',
    'paiji2_weather',
    'paiji2_infoconcert',
    'paiji2_survey',
    'paiji2_carpooling',
    'paiji2_mettis',
    'paiji2_shoutbox',
    'mptt',
    'paiji2_forum',
    'paiji2_comic',
    'django_markdown',
    'paiji2_social',
)

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
        'NAME': ':memory:',
    }
}

# Admins
ADMINS = (('Paiji developers', 'paiji-dev@rezometz.org'))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

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

OPENWEATHERMAP_API_KEY = ''
