from django.shortcuts import render


# Create your views here.
def home_view(request):
    #Basic Index Page.
    return render(request, 'home.html', {})



