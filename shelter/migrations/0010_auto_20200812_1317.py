# Generated by Django 3.0.5 on 2020-08-12 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0009_animalgallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalgallery',
            old_name='photos',
            new_name='photo',
        ),
    ]