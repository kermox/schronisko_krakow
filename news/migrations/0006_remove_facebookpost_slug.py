# Generated by Django 3.0.5 on 2020-08-14 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200814_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookpost',
            name='slug',
        ),
    ]
