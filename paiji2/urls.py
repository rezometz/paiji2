from django.conf.urls import patterns, include, url

from django.contrib import admin

from modular_blocks import modules


admin.autodiscover()
modules.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^rezo/', include('rezo.urls')),

    url(r'^', include('home.urls'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += modules.get_patterns()
