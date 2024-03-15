from django.urls import path, include
from .views import UserRegistrationView,UserLoginView,user_logout,deposite,active,AccountUpdateView,UserPasswordChangeView
urlpatterns = [
    path('registration',UserRegistrationView.as_view(),name='registration'),
    path('registration/active/<uid64>/<token>/',active,name='active'),
    path('login',UserLoginView.as_view(),name='login'),
    path('update',AccountUpdateView.as_view(),name='update'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('logout',user_logout,name='logout'),
    path('deposite',deposite,name='deposite'),
]