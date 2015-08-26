from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from .models import Message


class LatestEntriesFeed(Feed):
    title = _("Social Latest Entries")
    link = "/feeds/"
    description = _("Latest entries from all the workgroups")

    def items(self):
        return Message.objects.order_by('-pubDate')[:10]

    def item_title(self, item):
        return u'[{group}] {title}'.format(
            group=unicode(item.group),
            title=item.title,
        )

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('index')

    def item_guid(self, item):
        return unicode(item.pk)

    def item_pubdate(self, item):
        return item.pubDate
