# imports
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Account

#ekhane user model and account model. dui ta model ek sathe ache. so model.forms diye form crete korte chaile amk duita form create kora lagto.tai usercreationform use kora hocche
class UserRegistrationForm(UserCreationForm):
    
    mobile_no = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','mobile_no' , 'password1', 'password2']
    
    #ekhane user form fillup korbe ekta. kintu data save hobe dui model a .
    #tai save function niye kaj korte hobe
    def save(self, commit=True):
        print("inside save")
        
        #user er data gulo niye ashchi. ebong ekhn o model save kori nai
        user = super().save(commit=False)
        user.is_active = False
        if commit == True:
            user.save() #user model er data gulo save korlam 
            mobile_no = self.cleaned_data.get('mobile_no')
            #account model er object create kortesi
            Account.objects.create(
                user = user,
                mobile_no = mobile_no,
            )
            user.is_active = False
        return user
    
    #input field ta ke style kortesi
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            # single field style dite chaile
            # self.fields['username'].widget.attrs.update({'class':'mt-1'})
            #ei vhabe na kore direct template file a jeye kora jabe django-widget-tweaks er maddhome

            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
    
class UserUpdateForm(forms.ModelForm):
    # image = forms.ImageField()
    mobile_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','mobile_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        if self.instance:
            try:
                user_account = self.instance.account
                
            except Account.DoesNotExist:
                user_account = None
                

            if user_account:
                self.fields['mobile_no'].initial = user_account.mobile_no
                

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = Account.objects.get_or_create(user=user)  
            user_account.mobile_no = self.cleaned_data['mobile_no']
            user_account.save()
        return user