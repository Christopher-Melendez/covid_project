from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def nametest(request):
    # if this value "Tammy" instead came from a database, it would be 
    #something like user.name and that will send dynamic data for that user
    #name = 'Tammy'
    #add in the {} to add the key and value (like a dictionary)
    #in order to be able to access this variable because of this key 
    #in your nametest.html

    #rather than do the key and value one at a time and list in { }, we can 
    #put them all in a list that we name context

    context = {
        'name' : 'Patrick', #substitute with name variable later on
        'date' : '10/19/21'    
    }

    # and then add context to the return
    return render(request, 'nametest.html', context)

