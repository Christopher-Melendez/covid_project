from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from datetime import datetime

from .forms import SignUpForm
from .models import profile

# Create your views here.
def signup_view(request, view):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            in_username = form.cleaned_data.get('username')
            in_pass = form.cleaned_data.get('password1')
            user = authenticate(username=in_username, password=in_pass)
            profile.last_active = datetime.now()
            login(request, user)
            return redirect(view)
    else:
        print("ELSE")
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request, view):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password')
            user = authenticate(username-username, password=raw_pass)
            if user is not None:
                login(request, user)
                print("LOGGED IN: ", request.user)
                return redirect(view)
            else:
                print("ERROR")
        else:
            print("Error")
    
    print("ELSE LOGIN: ")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

def log_req_view(request, *args, **kwargs):
    username_in = request.POST.get('username')
    password_in = request.POST.get('password')
    user = authenticate(request, username=username_in, password=password_in)
    
    if user is not None:
        login(request, user)
    
    else:
        print("Not Logged IN: ", request.user)

    
    if not request.user.is_authenticated:
        return login_view(request, log_req_view)
        #return render(request, 'login_error.html', {})
    else: 
        logout(request)
        return render(request, 'nametest.html', {})


