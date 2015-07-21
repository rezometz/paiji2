from django.conf.urls import patterns, include, url

from django.contrib import admin

from modular_blocks import modules
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
modules.autodiscover()


urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^rezo/', include('rezo.urls')),

    url(r'^social/', include('social.urls')),

    url(r'^', include('home.urls'), name='home'),

    url(r'^calendar/', include('backbone_calendar.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^forum/', include('forum.urls', namespace='forum')),

    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += modules.get_patterns()
