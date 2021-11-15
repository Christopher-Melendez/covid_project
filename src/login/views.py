from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from .forms import SignUpForm
from .models import Profile

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            in_username = form.cleaned_data.get('username')
            in_pass = form.cleaned_data.get('password1')
            user = authenticate(username=in_username, password=in_pass)
            login(request, user)
            print("STUFF", request.user)
            return redirect('/')
    else:
        print("ELSE")
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        print('Submitting Login')
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_pass)
            if user is not None:
                login(request, user)
                print("LOGGED IN: ", request.user)
                return redirect('/')
            else:
                print("ERROR1")
    
    print("ELSE LOGIN: ")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

def logout_view(request):
    logout(request)
    print("Logout")
    return redirect('/')

def login_error_view(request):
    logout(request)
    print("Logout If Possible")
    return render(request, 'login_error.html', {})


def log_req_view(request, *args, **kwargs):
    logged_in = False

    #login_listener(request, log_req_view(request))

    if not request.user.is_authenticated:
        return login_view(request, log_req_view(request))
    else:
        logged_in = True
        print(request.POST.get) 
        print(request.user.is_authenticated)
        return render(request, 'nametest.html', {'logged_in': logged_in})


