from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^rezo/', include('rezo.urls')),
    url(r'^bulletin/', include('bulletin_board.urls')),
    url(r'^cov/', include('cov.urls')),

    url(r'^', include('home.urls'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
