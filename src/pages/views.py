from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def home_view(request, *args, **kwargs):
    #template = loader.get_template('home.html')
    return render(request, 'home.html', {})

def map_view(request, *args, **kewargs):
    return HttpResponse("<h1>MAPS GO HERE</h1>")