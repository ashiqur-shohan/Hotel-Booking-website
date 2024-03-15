from django.contrib import admin
from .models import Booking
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

# admin.site.register(Booking)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        email_subject = "Booking Confirmation."
        email_body = render_to_string('booking_confirm.html',{'obj':obj})
        email = EmailMultiAlternatives(email_subject,'',to=[obj.account.user.email])
        email.attach_alternative(email_body,'text/html')
        email.send()
        super().save_model(request, obj, form, change)