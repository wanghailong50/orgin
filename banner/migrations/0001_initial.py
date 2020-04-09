# Generated by Django 2.0.6 on 2020-04-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('loaddata', models.DateField(auto_now_add=True, null=True)),
                ('isshow', models.CharField(max_length=20)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='pics')),
            ],
        ),
    ]