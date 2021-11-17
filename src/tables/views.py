from django.shortcuts import render

from tables.models import covid_cases
from .tables import make_table, model_to_df

# Create your views here.

def tables_view(request, *args, **kewargs):
   
   table_choice_in = request.POST.get('table-choice')
   
   web_context = {
       'table_choice': table_choice_in,
       'table_html': make_table(table_choice_in),
   }
      
   return render(request, 'tables.html', web_context)