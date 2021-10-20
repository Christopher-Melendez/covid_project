from django.shortcuts import render
from django.http import HttpResponse
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
        'name' : 'Patrick',
        'date' : '10/19/21'    
    }

    # and then add context to the return
    return render(request, 'nametest.html', context)