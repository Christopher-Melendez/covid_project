from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def home_view(request, *args, **kwargs):
    #template = loader.get_template('home.html')
    return render(request, 'home.html', {})

from heat_map.__init__ import data
def maps_view(request, *args, **kewargs):
    my_context = {
        "map_html": data,
        "my_number": 123
    }
    return render(request, 'maps.html', my_context)

def tables_view(request, *args, **kewargs):
    return render(request, 'tables.html', {})