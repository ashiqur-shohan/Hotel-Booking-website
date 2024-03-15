from django.shortcuts import render,redirect
from .forms import ReviewForm
# Create your views here.

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ReviewForm()
    return render(request,'')