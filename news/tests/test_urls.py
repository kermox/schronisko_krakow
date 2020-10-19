from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import NewsListView, NewsDetailView, TopicDetailView, update_facebook_posts


class TestUrls(SimpleTestCase):

    def test_news_list_url_resolves(self):
        url = reverse('news-list')
        self.assertEquals(resolve(url).func.view_class, NewsListView)

    def test_news_detail_url_resolves(self):
        url = reverse('news-detail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, NewsDetailView)

    def test_topic_detail_url_resolves(self):
        url = reverse('news-topic-detail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, TopicDetailView)

    def test_update_facebook_post_url_resolves(self):
        url = reverse('news-update')
        self.assertEquals(resolve(url).func, update_facebook_posts)