from django.test import TestCase

from news.models import FacebookPost, Post, Topic


class TestModels(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='test title',
            content='test content',
        )
        self.topic = Topic.objects.create(
            name='test topic'
        )

    def test_post_is_assigned_slug_on_creation(self):
        self.assertEquals(self.post.slug, 'test-title')

    def test_topic_is_assigned_slug_on_creation(self):
        self.assertEquals(self.topic.slug, 'test-topic')
