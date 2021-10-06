from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def home_view(request, *args, **kwargs):
    #template = loader.get_template('home.html')
    return render(request, 'home.html', {})

def maps_view(request, *args, **kewargs):
    return render(request, 'maps.html', {})

def tables_view(request, *args, **kewargs):
    return render(request, 'tables.html', {})