# Generated by Django 4.2 on 2023-04-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(null=True, upload_to='images/history/')),
                ('overview_title', models.CharField(default='업체개요', max_length=255)),
                ('date_company_founded', models.CharField(max_length=255)),
                ('date_corporation_founded', models.CharField(max_length=255)),
                ('CEO', models.CharField(max_length=255)),
                ('main_item', models.CharField(max_length=255)),
                ('num_employee', models.CharField(max_length=255)),
                ('head_office', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('timeline_img', models.ImageField(upload_to='images/history/')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(null=True, upload_to='images/introduction/')),
                ('greetings', models.TextField(default='인사말 예시')),
                ('intro_title', models.CharField(default='소개', max_length=255)),
                ('intro_context', models.TextField(default='소개 내용')),
                ('intro_image', models.ImageField(null=True, upload_to='images/')),
                ('mainvalues_title', models.CharField(default='핵심가치', max_length=255)),
                ('mainvalues_context', models.TextField(default='핵심가치 내용')),
                ('mainvalues_image', models.ImageField(null=True, upload_to='images/')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(null=True, upload_to='images/mainbusiness/')),
                ('greetings', models.TextField(default='주요업무 인트로')),
                ('title', models.CharField(default='제목', max_length=255)),
                ('business_list', models.TextField(default=' 쉼표 로 각 업무 구분,쉼표 로 각 업무 구분,쉼표 로 각 업무 구분')),
                ('work1_image', models.ImageField(blank=True, null=True, upload_to='images/mainbusiness/')),
                ('work2_image', models.ImageField(upload_to='images/mainbusiness/')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kr', models.CharField(blank=True, max_length=255, null=True)),
                ('name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/main/')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('brochure', models.FileField(blank=True, null=True, upload_to='files/main')),
                ('location_kr', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_kr_1', models.CharField(blank=True, max_length=255, null=True)),
                ('context_1', models.TextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='images/main/')),
                ('image_1_m', models.ImageField(blank=True, null=True, upload_to='images/main/')),
                ('comment_kr_2', models.CharField(blank=True, max_length=255, null=True)),
                ('context_2', models.TextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images/main/')),
                ('image_2_m', models.ImageField(blank=True, null=True, upload_to='images/main/')),
                ('comment_kr_3', models.CharField(blank=True, max_length=255, null=True)),
                ('context_3', models.TextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='images/main/')),
                ('image_3_m', models.ImageField(blank=True, null=True, upload_to='images/main/')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_image', models.ImageField(upload_to='images/map/')),
                ('map_location', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('fax_number', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart_image', models.ImageField(upload_to='images/organizationchart/')),
                ('chart_image_m', models.ImageField(null=True, upload_to='images/organizationchart/')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue_image', models.ImageField(upload_to='images/main/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
