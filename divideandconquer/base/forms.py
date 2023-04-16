from django import forms
from .models import Client
from django.contrib.auth.forms import UserCreationForm
from base.models import MyUser, Request
from django.contrib.auth.forms import AuthenticationForm
import datetime

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

class Client_requests(forms.ModelForm):
    class Meta:
        model = Request
        fields = {'type', 'comments'}

    


class SignupForm(UserCreationForm):
    
    email = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    company_name = forms.CharField(max_length=150)
    phone_num = forms.CharField(max_length=11)
    company_name = forms.CharField(max_length=50)
    company_addr = forms.CharField(max_length= 100)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['company_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your company name',
        })

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'password1','password2']
        


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        client = Client(profile=user, company_name = self.cleaned_data['company_name'], company_addr=self.cleaned_data['company_name'],  phone_num = self.cleaned_data['phone_num'])
        if commit:
            client.save()
        return user