from django.db import models

# Create your models here.
class Introduction(models.Model):
    background=models.ImageField(upload_to='images/introduction/', null=True)
    greetings = models.TextField(default='인사말 예시')
    
    intro_title = models.CharField(max_length=255, default='소개')
    intro_context = models.TextField(default='소개 내용')
    intro_image=models.ImageField(upload_to='images/', null=True)
    
    mainvalues_title = models.CharField(max_length=255, default='핵심가치')
    mainvalues_context = models.TextField(default='핵심가치 내용')
    mainvalues_image=models.ImageField(upload_to='images/', null=True)
    
    created_at = models.DateField(auto_now_add=True, null=True)
    
class History(models.Model):
    background=models.ImageField(upload_to='images/history/', null=True)
    overview_title=models.CharField(max_length=255, default='업체개요')
    date_company_founded=models.CharField(max_length=255)
    date_corporation_founded=models.CharField(max_length=255)
    CEO =models.CharField(max_length=255)
    main_item=models.CharField(max_length=255)
    num_employee=models.CharField(max_length=255)
    head_office=models.CharField(max_length=255)
    email=models.EmailField()
    
    timeline_img=models.ImageField(upload_to='images/history/')
    
    created_at = models.DateField(auto_now_add=True, null=True)
    
class MainBusiness(models.Model):
    background=models.ImageField(upload_to='images/mainbusiness/', null=True)
    greetings = models.TextField(default='주요업무 인트로')
    
    title=models.CharField(max_length=255, default='제목')
    business_list=models.TextField(default=' 쉼표 로 각 업무 구분,쉼표 로 각 업무 구분,쉼표 로 각 업무 구분')
    
    work1_image=models.ImageField(upload_to='images/mainbusiness/',null=True, blank=True)
    work2_image=models.ImageField(upload_to='images/mainbusiness/')
    
    created_at = models.DateField(auto_now_add=True, null=True)
    
class OrganizationChart(models.Model):
    chart_image=models.ImageField(upload_to='images/organizationchart/')
    
    chart_image_m = models.ImageField(upload_to='images/organizationchart/', null=True)
    
    created_at = models.DateField(auto_now_add=True, null=True)


class Map(models.Model):
    map_image=models.ImageField(upload_to='images/map/')
    
    map_location=models.CharField(max_length=255, null=True)
    
    phone_number=models.CharField(max_length=255, null=True)
    
    fax_number=models.CharField(max_length=255, null=True)
    
    created_at = models.DateField(auto_now_add=True, null=True)
    
class MainInfo(models.Model):
    name_kr=models.CharField(max_length=255,null=True,blank=True)
    name_en=models.CharField(max_length=255,null=True,blank=True)
    
    
    logo=models.ImageField(upload_to='images/main/',null=True,blank=True)
    phone_number=models.CharField(max_length=50,null=True,blank=True)
    fax_number=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    brochure=models.FileField(upload_to='files/main',null=True,blank=True)
    
    location_kr=models.CharField(max_length=255,null=True,blank=True)

    
    created_at=models.DateField(auto_now_add=True,null=True,blank=True)
    
    
class MainSlide(models.Model):

    comment_kr_1=models.CharField(max_length=255, null=True, blank=True)
    context_1=models.TextField(null=True, blank=True)
    image_1=models.ImageField(upload_to='images/main/', null=True, blank=True)
    image_1_m=models.ImageField(upload_to='images/main/', null=True, blank=True)
    
    comment_kr_2=models.CharField(max_length=255, null=True, blank=True)
    context_2=models.TextField(null=True, blank=True)
    image_2=models.ImageField(upload_to='images/main/', null=True, blank=True)
    image_2_m=models.ImageField(upload_to='images/main/', null=True, blank=True)
    
    comment_kr_3=models.CharField(max_length=255, null=True, blank=True)
    context_3=models.TextField(null=True, blank=True)
    image_3=models.ImageField(upload_to='images/main/', null=True, blank=True)
    image_3_m=models.ImageField(upload_to='images/main/', null=True, blank=True)
    
    created_at=models.DateField(auto_now_add=True,null=True,blank=True)
    
class Revenue(models.Model):
    
    revenue_image=models.ImageField(upload_to='images/main/')
    
    created_at=models.DateField(auto_now_add=True)
    
