from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import SignUpForm

from .models import Profile
from datetime import datetime, timedelta

from .views import login_view, signup_view

# def check_active(user, view):
#     #user_profile = profile.objects.filter(user = request.user)
#     pass
#     return


