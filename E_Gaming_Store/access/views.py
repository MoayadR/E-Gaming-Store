from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.hashers import make_password
from django.contrib import messages

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