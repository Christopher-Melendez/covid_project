from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import SignUpForm, UpdateProfileForm
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        #Call Modified Signup Form
        form = SignUpForm(request.POST)

        #If form is filled out & has valid inputs, collect variables and authenticate & login
        if form.is_valid():
            form.save()
            in_username = form.cleaned_data.get('username')
            in_pass = form.cleaned_data.get('password1')
            user = authenticate(username=in_username, password=in_pass)
            login(request, user)
            #new_profile = Profile.objects.create(user=request.user)
            return redirect('/')
        #Else Present blank form
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        #Call Django Login Form
        form = AuthenticationForm(request, request.POST)
        #If form filled out and valid, collect input and authenticate and login
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_pass)
            if user is not None:
                login(request, user)
                #Currently redirecting to home page on success
                return redirect('/')
            else:
                pass
    #Else Present blank form
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

def logout_view(request):
    #Logout and Redirect home
    logout(request)
    return redirect('/')

def login_error_view(request):
    #For Failed Login / Bugs, Logout and attempt to relogin
    logout(request)
    return render(request, 'login_error.html', {})

#Temporary Debugging View
def log_req_view(request, *args, **kwargs):
    logged_in = False

    if not request.user.is_authenticated:
        return login_view(request, log_req_view(request))
    else:
        logged_in = True
        return render(request, 'nametest.html', {'logged_in': logged_in})

def account_view(request, *args, **kwargs):
    instance = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if 'update_password' in request.POST:
            #Call Modified Signup Form
            form_pass = PasswordChangeForm(request.user, request.POST)

            #If form is filled out & has valid inputs, collect variables and authenticate & login
            if form_pass.is_valid():
                form_pass.save()
                user = User.objects.get(username = request.user)
                in_pass = form_pass.cleaned_data.get('password')
                user.set_password(in_pass)
                user.save()
                login(request, user)
                return redirect('/')
            #Else Present blank form
            else:
                form_pass = PasswordChangeForm(request.user)

        elif 'update_photo' in request.POST:
            form_photo = UpdateProfileForm(request.POST, request.FILES, instance=instance)
            if form_photo.is_valid():
                
                photo = form_photo.save()
                
                # #uploaded_avatar_img.avatar_img_data = form.cleaned_data['avatar_img'].file.read()
                # print(uploaded_avatar_img.avatar_img_data)
                # uploaded_avatar_img.save()
                return redirect('account')
            else:
                form_photo = UpdateProfileForm()
    else:
        form_pass = PasswordChangeForm(request.user)
        form_photo = UpdateProfileForm()
    


    return render(request, 'account.html', {'form_photo': form_photo, 'form_pass': form_pass, 'instance': instance})


