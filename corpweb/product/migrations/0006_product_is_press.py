# Generated by Django 4.2 on 2023-04-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productgoal_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_press',
            field=models.BooleanField(default=False),
        ),
    ]
