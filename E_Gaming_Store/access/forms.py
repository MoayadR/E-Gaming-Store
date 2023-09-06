from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username:' , max_length=150 , required=True)
    email = forms.CharField(label='Email:' , max_length=150 , required=True , widget=forms.widgets.EmailInput)
    password1 = forms.CharField(label='Password:' , max_length=150 , required=True , widget=forms.widgets.PasswordInput)
    password2 = forms.CharField(label='Confirmation Password:' , max_length=150 , required=True , widget=forms.widgets.PasswordInput)
