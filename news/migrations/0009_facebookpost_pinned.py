# Generated by Django 3.0.5 on 2020-10-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_post_pinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookpost',
            name='pinned',
            field=models.BooleanField(blank=True, default=False, verbose_name='przypięty post'),
        ),
    ]
