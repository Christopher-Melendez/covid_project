from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.template import loader

from heat_map.models import Map
from heat_map.maps import maps

from login.views import login_view

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home_view(request):
    
    return render(request, 'home.html', {})



