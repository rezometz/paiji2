"""
Django settings for paiji2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.conf import global_settings


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


LOGIN_URL = 'sign-in'

# Application definition
INSTALLED_APPS = (
        'suit',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_gravatar',
        'graphos',
        'tinymce',
        'home',
        'homepage_alert',
        'backbone_calendar',

        # paiji2 apps
        'paiji2_weather',
        'paiji2_infoconcert',
        'paiji2_survey',
        'paiji2_carpooling',
        'paiji2_mettis',
        'paiji2_shoutbox',
        'paiji2_forum',
        'mptt',

        'modular_blocks',
        'djangobower',
        #        'debug_toolbar',
        'bootstrap3',
        'rezo',
        'social',
 )

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        )

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'rezo.context_processors.get_admin_email',
        )

ROOT_URLCONF = 'paiji2.urls'

WSGI_APPLICATION = 'paiji2.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('fr', 'french'),
    ('en', 'english'),
    #('la', 'latine'),
    #('de', 'german'),
)

# adds latine language
LATINE_LANG_INFO = {
    'la': {
        'bidi': False,
        'code': 'la',
        'name': 'Latine',
        'name_local': 'Latina',
    },
}

import django.conf.locale
django.conf.locale.LANG_INFO.update(LATINE_LANG_INFO)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'home', 'locale'),
    os.path.join(BASE_DIR, 'homepage_alert', 'locale'),
    os.path.join(BASE_DIR, 'social', 'locale'),
    os.path.join(BASE_DIR, 'rezo', 'locale'),
)


TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + (
        'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

BOWER_INSTALLED_APPS = (
    'bootstrap',
    'components-font-awesome',
    'morris.js',
    'weather-icons',
    'jquery-ui',
)

KEY_CACHE_WEATHER = 'paiji2_weather_data'
KEY_CACHE_FTPS = 'paiji2_ftps_data'

AUTH_USER_MODEL = 'rezo.User'

# Cache
# https://docs.djangoproject.com/en/dev/topics/cache/

CACHE_MIDDLEWARE_ALIAS = 'paiji2_cache'
CACHE_MIDDLEWARE_SECONDS = 300
CACHE_MIDDLEWARE_KEY_PREFIX = ''

SUIT_CONFIG = {
        'MENU_ICONS': {
            'sites': 'icon-leaf',
            'auth': 'icon-lock',
            'backbone_calendar': 'icon-calendar',
            'cov': 'icon-road',
            'homepage_alert': 'icon-exclamation-sign',
            'social': 'icon-user',
            'survey': 'icon-tasks',
            }
        }

TINYMCE_DEFAULT_CONFIG = {
        'plugins': 'advimage,advlink,table,searchreplace,contextmenu,template,paste,save,autosave,media',
        'mode':'exact',
        'theme': 'advanced',
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 10,
        #Theme options
        'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontsizeselect",
        'theme_advanced_buttons2' : "bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,forecolor",
        'theme_advanced_buttons3' : "tablecontrols,|,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
        'theme_advanced_toolbar_location' : "top",
        'theme_advanced_statusbar_location' : "bottom",

        'gecko_spellcheck' : True,
        }

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# modular blocks - rezo user model initialisation
SIDEBAR_LEFT = [
    u'bulletin-board',
    u'weather',
]
SIDEBAR_RIGHT = [
    u'rezo-account',
    u'cov',
    u'survey-form',
]

# paiji2_mettis
METTIS_STOPS = [{'line': 'LIGNE B', 'direction':'CITE U', 'from_stop':'GRAHAM BELL', 'url_1':'999', 'url_2':'CITE+U%7C999', 'url_3': 21366}]


ADMIN_EMAIL = 'paiji-dev@rezometz.org'
