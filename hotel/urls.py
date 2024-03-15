from django.urls import path
from .views import HotelDetailView,all_hotel,HotelDetailsView,book_hotel,hotel_details
urlpatterns = [
    # path('hotel_details/<int:id>',HotelDetailView.as_view(),name='hotel_details'),
    # path('hotel_details/<int:id>/',HotelDetailsView.as_view(),name='hotel_details'),
    path('hotel_details/<int:id>/',hotel_details,name='hotel_details'),
    path('book/<int:id>/',book_hotel,name='book'),
    # path('book_hotel/<int:id>',book_hotel,name='book_hotel'),
    path('all_hotel/',all_hotel,name='all_hotel'),
]