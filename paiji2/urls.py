from django.conf.urls import patterns, include, url

from django.contrib import admin

from modular_blocks import modules
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
modules.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^rezo/', include('rezo.urls')),

    url(r'^social/', include('social.urls')),

    url(r'^', include('home.urls'), name='home'),

    url(r'^calendar/', include('backbone_calendar.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^tinymce/', include('tinymce.urls')),
)

urlpatterns += modules.get_patterns()
