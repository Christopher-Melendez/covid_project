from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import SignUpForm
# Create your views here.

def nametest(request):
    # if this value "Tammy" instead came from a database, it would be 
    #something like user.name and that will send dynamic data for that user
    #name = 'Tammy'
    #add in the {} to add the key and value (like a dictionary)
    #in order to be able to access this variable because of this key 
    #in your nametest.html

    #rather than do the key and value one at a time and list in { }, we can 
    #put them all in a list that we name context

    context = {
        'name' : 'Patrick',
        'date' : '10/19/21'    
    }

    # and then add context to the return
    return render(request, 'nametest.html', context)




def log_req_view(request, *args, **kwargs):
    username_in = request.POST.get('username')
    password_in = request.POST.get('password')
    email_in = request.POST.get('email_in')
    user = authenticate(request, username=username_in, password=password_in)
    
    if user is not None:
        login(request, user)
    
    else:
        print("Not Logged IN: ", request.user)


    web_context = {
        'username' : username_in,
        'password' : password_in,
        'email': email_in,
    }
    
    if not request.user.is_authenticated:
        return login_view(request, log_req_view)
        #return render(request, 'login_error.html', {})
    else: 
        logout(request)
        return render(request, 'nametest.html', {})

def signup_view(request, view):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password1')
            user = authenticate(username-username, password=raw_pass)
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
