from django.db import models
from account.models import Account
from hotel.models import Hotel
# Create your models here.

STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]


class Review(models.Model):
    account = models.ForeignKey(Account,related_name='review',on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,related_name='review',on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.CharField(choices = STAR_CHOICES,max_length=10,null=True,default='⭐⭐⭐⭐⭐')

    def __str__(self):
        return f'{self.account.user.username} | {self.hotel.name} | {self.rating}'