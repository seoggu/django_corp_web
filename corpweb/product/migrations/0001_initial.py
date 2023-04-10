# Generated by Django 4.2 on 2023-04-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('product_image', models.ImageField(upload_to='images/product/')),
                ('product_features_image', models.ImageField(upload_to='images/product/')),
                ('product_name', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
