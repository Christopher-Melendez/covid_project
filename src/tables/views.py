from django.shortcuts import render

from tables.models import covid_cases
from .tables import make_table, model_to_df

# Create your views here.

def tables_view(request, *args, **kewargs):
    #Read Submitted Post Variable From Select Form
    table_choice_in = request.POST.get('table-choice')

    table_choice_in1 = request.POST.get('table-choice1')
    table_choice_in2 = request.POST.get('table-choice2')
    comparison_mode1 = request.POST.get('comparison-mode1')
    comparison_mode2 = request.POST.get('comparison-mode2')

    #Apply Default Case
    if str(table_choice_in) or str(table_choice_in1) or str(table_choice_in2)  == 'None':
        table_choice_in = 'COVID-19 Cases'
        table_choice_in1 = 'COVID-19 Cases'
        table_choice_in2 = 'COVID-19 Deaths'
        
    #Update Context Variable for Template
    web_context = {
        'table_html': make_table(table_choice_in),
        'table_choice': table_choice_in,
        'table_html1': make_table(table_choice_in1),
        'table_html2': make_table(table_choice_in2),
        'table_choice1': table_choice_in1,
        'table_choice2': table_choice_in2,
        'comparison_mode_context1': comparison_mode1,
        'comparison_mode_context2': comparison_mode2,
    }

    if comparison_mode1 == 'true' or comparison_mode2 == 'true':
        return render(request, 'tables_compare.html', web_context)
    else:
        web_context['comparison_mode_context1'] = 'false'
        web_context['comparison_mode_context2'] = 'false'
        return render(request, 'tables.html', web_context)