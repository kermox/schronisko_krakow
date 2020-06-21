from django.db import models
from schronisko_krakow.utils import random_string_generator, unique_slug_generator
from django.db.models.signals import pre_save

STATUS_CHOICES = (
    ('draft', 'Szkic'),
    ('published', 'Opublikowany'),
)


class Post(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name='tytuł',
        help_text='',
    )
    date = models.DateField(
        auto_now=True,
        verbose_name='data',
        help_text='',
    )
    content = models.TextField(
        verbose_name='treść',
        help_text='',
    )
    slug = models.SlugField(
        blank=True,
        null=True,
    )
    img = models.ImageField(
        blank=True,
        upload_to='posts/',
        verbose_name='obrazek',
    )
    status = models.CharField(
        max_length=15,
        verbose_name='status',
        help_text='status publikacji',
        choices=STATUS_CHOICES,
        default='draft',
    )

    def __str__(self):
        return f'{self.title}'


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Post)
