from django.shortcuts import render, redirect
# django default form to create users
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        # takes the info that the user filled out (request.POST) to fill out the UserCreationForm
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # after the user submits the signup, we want to redirect them to the homepage so put in the name of the url you want it to redirect to
            return redirect('blog-index')

    else:
        form = SignUpForm()
    context = {
        'form' : form,
    }
    return render(request, 'sign_up.html', context)
    

