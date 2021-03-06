# -*- encoding: utf-8 -*- #
"""
Django settings for paiji2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.conf import global_settings
import django.conf.locale
from django.core.urlresolvers import reverse
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# URLs

ROOT_URLCONF = 'paiji2.urls'

LOGIN_URL = '/rezo/sign-in'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

REDIRECT_URL = '/'


# used by paiji_utils
# to define some template tags
def PROFILE_URL(user):
    return reverse(
        'user-profile',
        kwargs={
            'pk': user.pk,
        },
    )

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
    'djangobower',
    'bootstrap3',
    'modular_blocks',
    'rezo',
)

MIDDLEWARE_CLASSES = (
    # uncomment to cache the entire site
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # uncomment to cache the entire site
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'rezo.context_processors.get_admin_email',
)

WSGI_APPLICATION = 'paiji2.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('fr', 'french'),
    ('en', 'english'),
    # ('la', 'latine'),
    # ('de', 'german'),
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

django.conf.locale.LANG_INFO.update(LATINE_LANG_INFO)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'home', 'locale'),
    os.path.join(BASE_DIR, 'homepage_alert', 'locale'),
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


BOWER_INSTALLED_APPS = (
    'bootstrap',
    'components-font-awesome',
    'morris.js',
    'weather-icons',
    'jquery-ui',
    'flag-icon-css',
)

KEY_CACHE_WEATHER = 'paiji2_weather_data'
KEY_CACHE_FTPS = 'paiji2_ftps_data'

AUTH_USER_MODEL = 'rezo.User'

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/paiji2_cache',
        'TIMEOUT': 86400,
    }
}

CACHE_MIDDLEWARE_ALIAS = 'paiji2_cache'
CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = ''


SUIT_CONFIG = {
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'homepage_alert': 'icon-exclamation-sign',
        'paiji2_carpooling': 'icon-road',
        'paiji2_social': 'icon-user',
        'backbone_calendar': 'icon-calendar',
        'paiji2_survey': 'icon-tasks',
        }
}

TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'advimage,advlink,table,\
        searchreplace,contextmenu,template,paste,save,autosave,media',
    'mode': 'exact',
    'theme': 'advanced',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    # Theme options
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,|,\
        justifyleft,justifycenter,justifyright,justifyfull,|,\
        styleselect,formatselect,fontsizeselect",
    'theme_advanced_buttons2': "bullist,numlist,|,\
        outdent,indent,blockquote,|,\
        undo,redo,|,\
        link,unlink,anchor,image,cleanup,help,code,|,\
        forecolor",
    'theme_advanced_buttons3': "tablecontrols,|,\
        removeformat,visualaid,|,\
        sub,sup,|,charmap,emotions,iespell,media,advhr",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_statusbar_location': "bottom",
    'gecko_spellcheck': True,
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
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
METTIS_STOPS = [
    {
        'line': 'LIGNE B',
        'direction': 'CITE U',
        'from_stop': 'GRAHAM BELL',
        'url_1': '999',
        'url_2': 'CITE+U%7C999',
        'url_3': 21366,
    }
]

ADMIN_EMAIL = 'paiji-dev@rezometz.org'

TEMPLATE_DIRS = global_settings.TEMPLATE_DIRS + (
    os.path.join(BASE_DIR, 'paiji2', 'templates'),
)

# paiji2_social
MIN_ROOM_UPDATE_DELTA = timedelta(days=3)

# django_markdown
MARKDOWN_PROTECT_PREVIEW = False
MARKDOWN_EXTENSIONS = ['extra', 'codehilite']

# paiji2_comic
FORTUNE_PATH = '/usr/games/fortune'
