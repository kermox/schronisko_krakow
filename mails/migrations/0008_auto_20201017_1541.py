# Generated by Django 3.0.5 on 2020-10-17 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0007_auto_20201017_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailbase',
            options={'verbose_name': 'Addresses', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='emailtemplates',
            options={'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
        migrations.AddField(
            model_name='emailbase',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='emailbase',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='emailtemplates',
            name='email_title',
            field=models.CharField(blank=True, max_length=250, verbose_name='Tytuł'),
        ),
    ]
