# Generated by Django 3.0.5 on 2020-10-17 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0008_auto_20201017_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator(message='Proszę podać prawidłowy adress.')])),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Tytuł')),
                ('body', models.TextField(blank=True, verbose_name='Treść')),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
        ),
        migrations.DeleteModel(
            name='EmailBase',
        ),
        migrations.DeleteModel(
            name='EmailTemplates',
        ),
    ]
