# Generated by Django 4.2 on 2023-04-08 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_introduction_background_mainbusiness_background_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='background',
        ),
        migrations.RemoveField(
            model_name='organizationchart',
            name='background',
        ),
    ]
