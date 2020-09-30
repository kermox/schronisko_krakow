from django.db import models
from django.core.validators import EmailValidator


class EmailTemplates(models.Model):
    email_body = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.email_body[0:20]


class EmailBase(models.Model):
    email_address = models.EmailField(blank=False, null=True,
                                      validators=[
                                          EmailValidator(message='Przepraszamy, podany adress jest niepoprawny.')])

    def __str__(self):
        return self.email_address
