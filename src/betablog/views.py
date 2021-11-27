from django.shortcuts import render
# Create your views here.

def index(request):
    # can render templates
    # render(request, TEMPLATENAME)
    return render(request, 'blog_index.html')

