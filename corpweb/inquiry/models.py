from django.db import models

# Create your models here.
class Inquiry(models.Model):
    
    name=models.CharField(max_length=255, null=False)
    email=models.EmailField(null=False)
    context=models.TextField(null=False)
    
    created_at= created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} | {self.email} | {self.context} | {self.created_at}'