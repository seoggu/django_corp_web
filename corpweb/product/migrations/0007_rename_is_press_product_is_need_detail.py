# Generated by Django 4.2 on 2023-04-16 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_is_press'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_press',
            new_name='is_need_detail',
        ),
    ]
