from django.shortcuts import render
from .maps import maps

# Create your views here.
def maps_view(request, *args, **kwargs):
         
    map_choice_in = request.POST.get('map-choice')

    map_choice_in1 = request.POST.get('map-choice1')
    map_choice_in2 = request.POST.get('map-choice2')
    comparison_mode1 = request.POST.get('comparison-mode1')
    comparison_mode2 = request.POST.get('comparison-mode2')

    web_context = {
        'map_html': maps(map_choice_in),
        'map_choice': map_choice_in,
        'map_html1': maps(map_choice_in1),
        'map_html2': maps(map_choice_in2),
        'map_choice1': map_choice_in1,
        'map_choice2': map_choice_in2,
        'comparison_mode_context1': comparison_mode1,
        'comparison_mode_context2': comparison_mode2,
    }

    if comparison_mode1 == 'true' or comparison_mode2 == 'true':
        return render(request, 'maps_compare.html', web_context)
    else:
        web_context['comparison_mode_context1'] = 'false'
        web_context['comparison_mode_context2'] = 'false'
        return render(request, 'maps.html', web_context)