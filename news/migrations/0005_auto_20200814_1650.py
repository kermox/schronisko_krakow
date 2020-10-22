# Generated by Django 3.0.5 on 2020-08-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200814_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookpost',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.AddField(
            model_name='facebookpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='facebookpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
