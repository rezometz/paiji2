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
        'graphos',
        'tinymce',
        'home',
        'homepage_alert',
        'backbone_calendar',
        'weather',
        'cov',
        'modular_blocks',
        'bulletin_board',
        'infoconcert',
        'debug_toolbar',
        'south',
        'bootstrap3',
        'rezo',
        'survey',
        'social',
        )

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        )

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        )

ROOT_URLCONF = 'paiji2.urls'

WSGI_APPLICATION = 'paiji2.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

KEY_CACHE_WEATHER = 'paiji2_weather_data'


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