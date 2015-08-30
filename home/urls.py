from django.conf.urls import url  # , patterns
# from django.contrib.auth.decorators import login_required

from paiji2_social.views import MessageListView


urlpatterns = [
    url(
        r'^$',
        MessageListView.as_view(),
        name='index',
    ),
]
