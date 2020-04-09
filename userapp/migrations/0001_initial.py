# Generated by Django 2.0.6 on 2020-04-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('religious_name', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('salt', models.CharField(max_length=20, null=True)),
                ('danger', models.CharField(max_length=20, null=True)),
                ('head_pic', models.ImageField(null=True, upload_to='pics')),
                ('address', models.CharField(max_length=20, null=True)),
                ('signature', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('qq', models.CharField(max_length=20, null=True)),
                ('resever', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]