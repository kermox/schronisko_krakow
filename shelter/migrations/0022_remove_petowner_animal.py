# Generated by Django 3.0.5 on 2020-10-18 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0021_auto_20201018_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petowner',
            name='animal',
        ),
    ]
