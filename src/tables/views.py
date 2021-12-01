from django.shortcuts import render

from tables.models import covid_cases
from .tables import make_table, model_to_df

# Create your views here.

def tables_view(request, *args, **kewargs):
    #Read Submitted Post Variable From Select Form
    table_choice_in = request.POST.get('table-choice')

    #Apply Default Case
    if str(table_choice_in) == 'None':
        table_choice_in = 'COVID-19 Cases'
        
    #Update Context Variable for Template
    web_context = {
        'table_choice': table_choice_in,
        #Call Make Table With Given Choice to Create HTML Text for Tables
        'table_html': make_table(table_choice_in),
    }
        
    return render(request, 'tables.html', web_context)