from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 70)
    image = models.ImageField(upload_to="hotel/images")
    price = models.DecimalField(max_digits=5, decimal_places=0)
    description = models.TextField(null=True)
    def __str__(self):
        return f'{self.name} | {self.location}'