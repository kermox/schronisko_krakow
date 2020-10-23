from django.contrib.staticfiles.testing import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver

from news.models import Post, Topic


class TestNewsAppPages(LiveServerTestCase):

    def setUp(self):
        topic = Topic.objects.create(
            name='topic name'
        )

        Post.objects.create(
            title='no topic post',
            content='some test content',
            status='published'
        )
        Post.objects.create(
            title='topic post',
            content='some test content',
            status='published',
            topic=topic
        )

        self.browser = webdriver.Chrome('functional_tests/chromedriver')


    def tearDown(self):
        self.browser.close()

    def test_news_posts_are_displayed(self):
        self.browser.get(self.live_server_url + reverse('news-list'))

        post = self.browser.find_element_by_class_name('card')

        self.assertTrue(post)

    def test_news_topics_are_displayed(self):
        self.browser.get(self.live_server_url + reverse('news-list'))

        topic_link = self.browser.find_element_by_link_text('topic name'.upper())

        self.assertTrue(topic_link)

    def test_news_topics_links_redirect_to_topic_detail(self):
        self.browser.get(self.live_server_url + reverse('news-list'))

        topic_url = self.live_server_url + reverse('news-topic-detail', args=['topic-name'])

        topic_link = self.browser.find_element_by_link_text('topic name'.upper())
        topic_link_clicked = topic_link.click()

        self.assertEquals(self.browser.current_url, topic_url)

    def test_news_topics_posts_are_displayed(self):
        self.browser.get(self.live_server_url + reverse('news-topic-detail', args=['topic-name']))

        post = self.browser.find_element_by_class_name('card')

        self.assertTrue(post)