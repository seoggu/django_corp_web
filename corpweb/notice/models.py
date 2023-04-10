from django.db import models

# Create your models here.
class Notice(models.Model):
    
    CHOICES={
        ('option0','공지사항'),
        ('option1','뉴스'),
        ('option2','자료실')
    }
    
    title=models.CharField(max_length=255)
    context=models.TextField()
    
    file=models.FileField(upload_to='files/notice/', null=True, blank=True)
    image=models.ImageField(upload_to='images/notice/', null=True, blank=True)
    
    division=models.CharField(max_length=255, choices=CHOICES, null=True)
    
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

