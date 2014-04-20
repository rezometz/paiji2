from iptools import IpRangeList

from django.conf import settings

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

groups = {}
users = {}

class IpAuthGroupMiddleware(object):
    def __init__(self):
        user_model = get_user_model()
        try:
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

    def process_request(self, request):
        user = request.user

        if not user.is_authenticated():
            for groupname, ranges in settings.IP_AUTH_GROUPS.iteritems():
                ip_range = IpRangeList(*ranges)
                if request.META['REMOTE_ADDR'] in ip_range:
                    request.user = users[groupname]


from django.db import models
class UserAuthGroupMixin(models.Model):
    
    def is_authenticated(self):
        return not self in users.itervalues()

    class Meta:
        abstract = True
