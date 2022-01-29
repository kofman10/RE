from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="", required=True, widget=forms.TextInput(attrs={"class":"focus:outline-none border border-black px-2 py-2","type":"text", "placeholder":"First Name"}))
    last_name = forms.CharField(max_length=100, label="",required=True, widget=forms.TextInput(attrs={"class":"focus:outline-none border border-black px-2 py-2 ml-4","type":"text", "placeholder":"Last Name"}))
    email = forms.EmailField (label="Email", required=True, widget=forms.TextInput(attrs={"class":"focus:outline-none border border-black px-2 py-2","type":"email", "placeholder":"Email"}))
    password1 = forms.CharField(label="Enter password", required=True, widget=forms.PasswordInput(attrs={"class":"focus:outline-none border border-black px-2 py-2","type":"password", "placeholder":"*********"}))
    password2 = forms.CharField(label="Confirm Password", required=True, widget=forms.PasswordInput(attrs={"class":"focus:outline-none border border-black px-2 py-2","type":"password", "placeholder":"*********"}))
    
    class Meta:
        model = Account
        fields = [
            "first_name","last_name","email","password1","password2"
            
        ]