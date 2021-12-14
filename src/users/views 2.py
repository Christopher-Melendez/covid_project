from django.shortcuts import render
# django default form to create users
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def sign_up(request):
    return render(request, 'sign_up.html')
