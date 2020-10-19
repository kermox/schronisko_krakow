from django.test import TestCase, Client
from django.urls import reverse

from news.models import Post, Topic




class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.news_list_url = reverse('news-list')
        self.news_detail_url = reverse('news-detail', args=['post_1'])
        self.news_topic_detail_url = reverse('news-topic-detail', args=['topic_1'])
        self.news_update_facebook_url = reverse('admin:news_facebookpost_changelist')

        Post.objects.create(
            title='post_1',
            content='some test content',
        )

        Topic.objects.create(
            name='topic_1'
        )

    def test_news_post_GET(self):

        response = self.client.get(self.news_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news-list.html')

    def test_news_detail_GET(self):

        response = self.client.get(self.news_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news-detail.html')

    def test_topic_GET(self):

        response = self.client.get(self.news_topic_detail_url, args=['topic_1'])

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news-topic-detail.html')

    def test_facebook_update_POST(self):

        response = self.client.get(self.news_update_facebook_url)

        self.assertEquals(response.status_code, 302)
