from django.db import models

# Create your models here.
class Product(models.Model):
    description=models.TextField()
    product_image=models.ImageField(upload_to='images/product/')
    product_features_image=models.ImageField(upload_to='images/product/')
    name=models.CharField(max_length=255, unique=True)
    is_need_detail=models.BooleanField(default=False)
    
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class ProductGoal(models.Model):
    
    goal_image=models.ImageField(upload_to='images/product')
    created_at=models.DateField(auto_now_add=True)
    
class Parts(models.Model):
    context=models.TextField(null=True, blank=True)
    parts_intro=models.ImageField(upload_to='images/product')
    sample=models.FileField(upload_to='files/product')
    
    created_at=models.DateField(auto_now=True)
    
class FacilityList(models.Model):
    image=models.ImageField(upload_to='images/facility_list')
    
    created_at=models.DateField(auto_now_add=True)
    
class Press(models.Model):
    image=models.ImageField(upload_to='images/product/press')
    context=models.TextField()
    name=models.CharField(max_length=255,null=True)
    
    company=models.CharField(max_length=255,null=True,blank=True)
    max_power=models.CharField(max_length=255,null=True,blank=True)
    stroke=models.CharField(max_length=255,null=True,blank=True)
    stroke_speed=models.CharField(max_length=255,null=True,blank=True)
    hydraulic_press=models.CharField(max_length=255,null=True,blank=True)
    quantity=models.CharField(max_length=255,null=True,blank=True)
    
    
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    