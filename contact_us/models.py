from django.db import models

# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    body = models.TextField()
    timestamp = models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        verbose_name_plural = "Contact_Us"