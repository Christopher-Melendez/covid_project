#from django.contrib import auth
#from django.shortcuts import render, redirect
#from django.http import HttpResponse

#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User

#from django.views.generic import ListView, DetailView

#from blog.models import Post
# list - all of blog posts for overview
# detail - one blog post when clicking into one 

#Create your views here.

# we want to list all our blogs on the home page
#class BlogHome(ListView):
    #post_data = Post.objects.get(title = 'first post')
    #print('HERE')
    #print(post_data)
    #template_name = 'bloghome.html'


#def blog_view(request):
    #if request.user.is_authenticated:

        # if this value "Tammy" instead came from a database, it would be 
        #something like user.name and that will send dynamic data for that user
        #name = 'Tammy'
        #add in the {} to add the key and value (like a dictionary)
        #in order to be able to access this variable because of this key 
        #in your nametest.html

        #rather than do the key and value one at a time and list in { }, we can 
        #put them all in a list that we name context

        #context = {
            #'name' : 'Patrick',
            #'date' : '10/19/21'    
        #}

        # and then add context to the return
        #return render(request, 'nametest.html', context)
    #else: 
        #return redirect('login_error')

#def home(request): 
    #return render(request, 'nametest.html', {})
