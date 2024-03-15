# from typing import Any
from django.shortcuts import render,redirect
from .models import Hotel
from booking.models import Booking
from booking.forms import BookingForm
from django.views.generic import DetailView
from review.forms import ReviewForm
from review.models import Review

# Create your views here.

class HotelDetailView(DetailView):
    model = Hotel
    pk_url_kwarg = 'id'
    template_name = 'hotel_details.html'

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     hotel = self.object
def all_hotel(request):
    hotel = Hotel.objects.all()
    return render(request,'all_hotel.html',{'data':hotel})


def hotel_details(request,id):
    hotel = Hotel.objects.get(pk=id)
    review = Review.objects.filter(hotel=hotel)
    booking_check = None 
    if request.user.is_authenticated:      
        account = request.user.account
        booking_check = Booking.objects.filter(account=account,hotel=hotel).first()
        
    if request.method =="POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.account = request.user.account
            review_form.hotel = hotel
            review_form.save()
    else:
        review_form = ReviewForm()
    context = {'object' : hotel,"review_form":review_form,"booking_check":booking_check,'reviews':review}
    return render(request,'hotel_details.html',context)
    # return redirect('hotel_details.html',context,id=id)





class HotelDetailsView(DetailView):
    model = Hotel
    pk_url_kwarg = 'id'
    template_name = 'hotel_details.html'

    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(data=self.request.POST)
        hotelmodel = self.get_object()
        if review_form.is_valid():
            new_comment = review_form.save(commit=False)
            new_comment.account = self.request.user.account
            new_comment.hotel = hotelmodel
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hotel = self.object
        # if self.user.is_authenticated:
        #     account = self.user.account
        #     booking_check = Booking.objects.filter(account=account,hotel=hotel).first()



        reviews = hotel.review.all()
        
        review_form = ReviewForm()
        booking_form = BookingForm()
        context['reviews'] = reviews
        context['review_form'] = review_form
        context['booking_form'] = booking_form
        # if self.user.is_authenticated:
        #     context['booking_check'] = booking_check
        return context

# def book_hotel(request,id):
#     print("book hotel view")
#     if request.method=="POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             print("in post")
#             # date = request.POST.get('date')
            
#             hotel_model = Hotel.objects.get(pk=id)
#             user = request.user.account
#             if user.balance > hotel_model.price:
#                 print("in logic")
#                 user.balance -= hotel_model.price
#                 user.save(update_fields=['balance'])
#                 Booking.objects.create(
#                     account = user,
#                     hotel = hotel_model,
#                     # booking_date = date
#                 )
#     else:
#         print('userpost kore nai')
#         form = BookingForm()
#     return render(request,"hotel_details", {"form":form} ,  id=id )
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         hotel = self.object
#         reviews = hotel.review.all()
#         review_form = ReviewForm()
#         booking_form = BookingForm()
#         context['reviews'] = reviews
#         context['review_form'] = review_form
#         context['booking_form'] = booking_form
#         return context

def book_hotel(request,id):
    print("book hotel view")
    if request.method=="POST":
        print("in post")
        date = request.POST.get('date')
        print(date)
        hotel_model = Hotel.objects.get(pk=id)
        user = request.user.account
        if user.balance > hotel_model.price:
            print("in logic")
            user.balance -= hotel_model.price
            user.save(update_fields=['balance'])
            Booking.objects.create(
                account = user,
                hotel = hotel_model,
                booking_date = date
            )
    # return render(request,"hotel_details", id=id )
    return redirect("hotel_details", id=id )

# def book_hotel(request,id):
#     print("book hotel view")
#     if request.method=="POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             print("in post")
#             # date = request.POST.get('date')
            
#             hotel_model = Hotel.objects.get(pk=id)
#             user = request.user.account
#             if user.balance > hotel_model.price:
#                 print("in logic")
#                 user.balance -= hotel_model.price
#                 user.save(update_fields=['balance'])
#                 Booking.objects.create(
#                     account = user,
#                     hotel = hotel_model,
#                     # booking_date = date
#                 )
#     else:
#         print('userpost kore nai')
#         form = BookingForm()
#     return render(request,"hotel_details", {"form":form} ,  id=id )