from django.db import models
from django.core.validators import EmailValidator


class EmailTemplate(models.Model):
    title = models.CharField(
        max_length=250,
        blank=True,
        null=False,
        verbose_name='Tytuł'
    )
    body = models.TextField(
        blank=True,
        null=False,
        verbose_name='Treść'
    )

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __str__(self):
        return self.email_body[0:20]


class EmailBase(models.Model):
    email_address = models.EmailField(blank=False, null=True,
                                      validators=[
                                          EmailValidator(message='Przepraszamy, podany adress jest niepoprawny.')])

    def __str__(self):
        return self.email_address
