from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user:
            login(request , user)
            return redirect('index')
        # user = NONE
        messages.warning(request , 'Wrong Credentials')
        return redirect('login')
        pass

    # GET request
    return render(request , 'access/login.html')

def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                messages.warning(request , 'Password and Confirmation password doesn\'t match')
                return redirect('register')

            password1 = make_password(password1)
            user = User.objects.create(username = username , password = password1 , email = email)
            
            messages.success(request,"Registered Successfully")
            login(request , user)
            return redirect('index')
        messages.warning(request , 'Invalid Input')
    # GET request
    form = RegisterForm()
    return render(request , 'access/register.html' , {'form' : form})