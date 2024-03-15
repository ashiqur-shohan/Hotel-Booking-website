from django.db import models
from account.models import Account
from hotel.models import Hotel
# Create your models here.

class Booking(models.Model):
    account = models.ForeignKey(Account,related_name='booking',on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,related_name='booking',on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)
    booking_date = models.DateField()
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.account.user.username} | {self.hotel.name}'