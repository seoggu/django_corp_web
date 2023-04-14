# Generated by Django 4.2 on 2023-04-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_remove_maininfo_brochure_remove_maininfo_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maininfo',
            name='brochure',
            field=models.FileField(blank=True, null=True, upload_to='files/main'),
        ),
        migrations.AddField(
            model_name='maininfo',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='fax_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/main/'),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]