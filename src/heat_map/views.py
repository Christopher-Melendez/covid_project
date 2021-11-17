from django.shortcuts import render
from .maps import maps

# Create your views here.
def maps_view(request, *args, **kwargs):
         
    map_choice_in = request.POST.get('map-choice')

    web_context = {
        'map_html': maps(map_choice_in),
        'map_choice': map_choice_in
    }
    return render(request, 'maps.html', web_context)