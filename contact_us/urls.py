
from django.urls import path
from .views import ContactView,about_us
urlpatterns = [
    path('contact_us',ContactView ,name='contact_us'),
    path('about_us',about_us,name='about'),
]