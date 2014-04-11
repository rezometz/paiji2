from iptools import IpRangeList

from django.conf import settings

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


user_model = get_user_model()
try:
    groups = {}
    users = {}
    for groupname, ranges in settings.IP_AUTH_GROUPS.iteritems():
        (groups[groupname], created) = Group.objects.get_or_create(
            name=groupname,
        )
        (users[groupname], created) = user_model.objects.get_or_create(
            username=groupname,
        )
        groups[groupname].user_set.add(users[groupname])

except ImportError:
    pass


class IpAuthGroupMiddleware(object):
    def process_request(self, request):
        user = request.user

        if not user.is_authenticated():
            for groupname, ranges in settings.IP_AUTH_GROUPS.iteritems():
                ip_range = IpRangeList(*ranges)
                if request.META['REMOTE_ADDR'] in ip_range:
                    request.user = users[groupname]

