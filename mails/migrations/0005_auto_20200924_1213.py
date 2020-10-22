# Generated by Django 3.0.5 on 2020-09-24 12:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0004_auto_20200924_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddresses',
            name='email_address',
            field=models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator(message='Przepraszamy, podany adress jest niepoprawny.')]),
        ),
    ]
