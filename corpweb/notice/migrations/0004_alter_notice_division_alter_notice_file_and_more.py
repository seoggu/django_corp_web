# Generated by Django 4.2 on 2023-04-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_notice_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='division',
            field=models.CharField(choices=[('option1', '뉴스'), ('option0', '공지사항'), ('option2', '자료실')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/notice/'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/notice/'),
        ),
    ]
