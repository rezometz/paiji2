from django.conf.urls import patterns, include, url

from django.contrib import admin

from modular_blocks import modules
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()
modules.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^i18n/', include('django.conf.urls.i18n')),
) + i18n_patterns(
    '',
    url(r'^rezo/', include('rezo.urls')),
    url(r'^social/', include('social.urls')),
    url(r'^', include('home.urls'), name='home'),
    url(r'^admin', include(admin.site.urls)),
    url(r'^calendar/', include('backbone_calendar.urls')),
    url(r'^forum/', include('paiji2_forum.urls', namespace='forum')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'carpooling/', include('paiji2_carpooling.urls')),
) + modules.get_i18n_patterns()
