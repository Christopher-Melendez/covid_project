from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import loader


from heat_map.models import Map
from .forms import MapForm
from heat_map.maps import maps

# Create your views here.
def home_view(request, *args, **kwargs):
    #template = loader.get_template('home.html')
    return render(request, 'home.html', {})


def maps_view(request, *args, **kewargs):
    form = MapForm(request.POST or None)
    if form.is_valid():
       form.save()
    
    map_choice_in = request.GET.get('map-choice')
    print(map_choice_in)
   
    #map_obj = Map.objects.get(id=1)
    
    web_context = {
        'form': form,
        'map_html': maps(map_choice_in),
        'map_choice': map_choice_in
    }
    return render(request, 'maps.html', web_context)

def tables_view(request, *args, **kewargs):
    return render(request, 'tables.html', {})