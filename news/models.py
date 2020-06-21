from django.db import models


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

    def __str__(self):
        return f'{self.title}'
