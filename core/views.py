from django.shortcuts import render
from hotel.models import Hotel
# Create your views here.

def home(request):
    data = Hotel.objects.all()
    return render(request,'home.html',{'data':data})

