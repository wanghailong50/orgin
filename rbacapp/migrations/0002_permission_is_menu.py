# Generated by Django 2.0.6 on 2020-04-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbacapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='是否为菜单'),
        ),
    ]
