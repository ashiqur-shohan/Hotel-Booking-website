from django.shortcuts import render,redirect
from .forms import ContactForm
# Create your views here.

def ContactView(request):
    print('in cont view ')
    if request.method == "POST":
        print('in post')
        form = ContactForm(request.POST)
        if form.is_valid():
            print('in valid')
            form.save()
            return redirect('home')
    else:
        print('in else')
        form = ContactForm()
    return render(request,"contact_us.html",{'form':form})

def about_us(request):
    return render(request,'about_us.html')