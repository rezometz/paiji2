from django.conf.urls.static import static
from django.conf import settings

from .urls import urlpatterns


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
