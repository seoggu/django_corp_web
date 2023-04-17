# Generated by Django 4.2 on 2023-04-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_press_company_press_max_power_press_max_stroke_speed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='press',
            old_name='max_stroke_speed',
            new_name='hydraulic_press',
        ),
        migrations.RenameField(
            model_name='press',
            old_name='weight',
            new_name='stroke',
        ),
        migrations.AddField(
            model_name='press',
            name='stroke_speed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]