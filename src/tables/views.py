from django.shortcuts import render

# Create your views here.

def tables_view(request, *args, **kewargs):
    return render(request, 'tables.html', {})