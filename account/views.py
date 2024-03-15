from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserUpdateForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

# class AccountCreateView()

#form niye kaj korle FormView ta niye kaj kora uchit
class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('registration')

    #built-in method
    #ei class based view te django form ta pass kore de ei method a 
    # def form_valid(self, form):
    #     # Userregistrationform a save function ke modify kore eshechi. save function ta return kore user ke
    #     user = form.save()
        # token = default_token_generator.make_token(user)
        # uid = urlsafe_base64_encode(force_bytes(user.pk))
        # confirm_link = f"http://127.0.0.1:8000/registration/active/{uid}/{token}"
        # email_subject = "Confirm Your Account"
        # email_body = render_to_string('confirm_email.html',{"confirm_link":confirm_link})
        # email = EmailMultiAlternatives(email_subject,'',to=[self.user.email])
        # email.attach_alternative(email_body,'text/html')
        # email.send()
        # messages.success(self.request,f'Check your email to active your account.')
    #     # nijei nije ke call kortese. tar jonno ei code likha
    #     return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            user = form.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/registration/active/{uid}/{token}"
            email_subject = "Confirm Your Account"
            email_body = render_to_string('confirm_email.html',{"confirm_link":confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            messages.success(self.request,f'Check your email to active your account.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Some field is inputed wrongly.')
        return super().form_invalid(form)

def active(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        #decode kora uid ta kon user er sheita ber kore niye ashtese
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('login')


class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        messages.success(self.request, 'User logged in ')
        return reverse_lazy('home')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def deposite(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount"))
        print(amount)
        account = request.user.account
        account.balance += amount
        account.save(update_fields=['balance'])
    return render(request,'deposite.html')

        
class AccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('update')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    
class UserPasswordChangeView(PasswordChangeView):
    template_name = "password_change.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # send_email(self.request.user, "", 'pass_change',  'Password Change Success Message', 'transactions/email_template.html')
        messages.success(self.request, 'Password changed successfully done')
        return super().form_valid(form)
    
#for check purpose
# class UserPasswordChangeView(PasswordChangeView):
#     template_name = "password_change.html"
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy('home')