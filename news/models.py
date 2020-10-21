from django.db import models
from django.db.models.signals import pre_save

from utils.utils import unique_slug_generator, TimeStampMixin

STATUS_CHOICES = (
    ('draft', 'Szkic'),
    ('published', 'Opublikowany'),
)


class Topic(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=True,
    )
    slug = models.SlugField(
        max_length=250,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name.title()


class Post(TimeStampMixin, models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='tytuł',
        help_text='',
    )
    date = models.DateField(
        auto_now=True,
        help_text='',
        verbose_name='data',
    )
    content = models.TextField(
        help_text='',
        verbose_name='treść',
    )
    slug = models.SlugField(
        max_length=250,
        blank=True,
        null=True,
    )
    img = models.ImageField(
        blank=True,
        upload_to='news/',
        verbose_name='obrazek',
    )
    status = models.CharField(
        max_length=15,
        verbose_name='status',
        help_text='status publikacji',
        choices=STATUS_CHOICES,
        default='draft',
    )
    pinned = models.BooleanField(
        null=False,
        blank=True,
        default=False,
        verbose_name='przypięty post'
    )
    topic = models.ForeignKey(
        Topic,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='wątek'
    )

    def __str__(self):
        return f'{self.title}'.title()


class FacebookPost(TimeStampMixin, models.Model):

    facebook_post_id = models.CharField(
        max_length=250,
        default=0,
    )
    facebook_permalink_url = models.CharField(
        max_length=400,
        null=True
    )

    status = models.CharField(
        max_length=15,
        verbose_name='status',
        help_text='status publikacji',
        choices=STATUS_CHOICES,
        default='draft',
    )

    pinned = models.BooleanField(
        null=False,
        blank=True,
        default=False,
        verbose_name='przypięty post',
    )

    class Meta:
        verbose_name = 'Facebook'
        verbose_name_plural = 'Facebook'

    def __str__(self):
        return f"FacebookPost: {self.facebook_post_id}"


def pre_save_receiver(instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Post)
pre_save.connect(pre_save_receiver, sender=Topic)
