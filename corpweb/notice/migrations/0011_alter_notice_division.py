# Generated by Django 4.2 on 2023-04-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0010_alter_notice_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='division',
            field=models.CharField(choices=[('option0', '공지사항'), ('option1', '뉴스'), ('option2', '자료실')], max_length=255, null=True),
        ),
    ]