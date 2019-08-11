from django.contrib.syndication.views import Feed
from blogging.models import Post


class LatestPosts(Feed):
    title = 'Latest Posts'
    link = ''
    description = 'Contents on latest published posts'
    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        return published.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return "Posted by {} - {}, text: {}".format(item.author, item.published_date, item.text)


'''
from django.urls import reverse

class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])
'''