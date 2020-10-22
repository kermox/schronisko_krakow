# Generated by Django 3.0.5 on 2020-09-24 12:12

import django.core.validators
from django.db import migrations, models

import mails.models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0003_auto_20200923_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddresses',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator(
                message='Przepraszamy, podany adress jest niepoprawny.')]),
        ),
    ]
