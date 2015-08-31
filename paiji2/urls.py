from django.conf.urls import patterns, include, url

from django.contrib import admin

from modular_blocks import modules
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from paiji2.views import confirm_language


admin.autodiscover()
modules.autodiscover()


urlpatterns = [
    url(
        r'^i18n/confirm-language/(?P<code>[\w-]+)$',
        confirm_language,
        name="set_language",
    ),
] + i18n_patterns(
    '',
    # url(r'^', include('home.urls'), name='home'),
    url(r'^', include('paiji2_social.urls')),
    url(r'^rezo/', include('rezo.urls')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^calendar/', include('backbone_calendar.urls')),
    url(r'^forum/', include('paiji2_forum.urls', namespace='forum')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'carpooling/', include('paiji2_carpooling.urls')),
) + modules.get_i18n_patterns()
