# Generated by Django 3.0.5 on 2020-10-18 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0019_auto_20201018_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petowner',
            old_name='adress',
            new_name='address',
        ),
    ]
