from graphs.graphs import create_graph
from django.shortcuts import render
import plotly.offline 

# Create your views here.

def graphs_view(request, *args, **kwargs):

    graph_choice_in = request.POST.get('graph-choice')

    if str(graph_choice_in) == 'None':
        graph_choice_in = 'COVID-19 Cases'

    plot_div = plotly.offline.plot(create_graph(graph_choice_in), auto_open = False, output_type="div")

    web_context = {
        'graph_choice_in': graph_choice_in,
        'plot_div': plot_div
    }

    return render(request, 'graphs.html', web_context)