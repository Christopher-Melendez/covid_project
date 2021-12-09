#need to import redirect to redirect to another url after saving a post
from django.shortcuts import render, redirect
# Create your views here.
from .models import PostModels
#import forms
from .forms import PostModelForm, PostUpdateForm
from login.models import Profile

from login.views import login_view, log_req_view


def index(request):
    if not request.user.is_authenticated:
        return login_view(request)
    else:
        # django's ORM (object relational mapper) lets you interact with your database
        # way of rewriting queries 
        # takes all the PostModels objects in the queryset
        posts = PostModels.objects.all()
        if request.method == 'POST':
            # will grab the request of whichever data we are trying to pass in
            form = PostModelForm(request.POST)
            if form.is_valid():
                # commit=False b/c we do not want it to save yet 
                instance = form.save(commit=False)
                # the author will be the logged in user 
                instance.author = request.user
                instance.save()
                # redirects to the url in url.py (the name of the url we associated it with is
                # in urls.py 
                return redirect('blog-index')
        else:
            form = PostModelForm()

        # context dictionary to pass multiple attributes to the index file
        # in a more systematic way 

        #Temp thing to make pics work :D
        profiles = Profile.objects.all()
        

        context = {
            'posts' : posts,
            'form' : form,
            'profiles': profiles,
        }
        # can render templates
        # render(request, TEMPLATENAME)
        # passing the dictionary {'posts' : posts} allows this queryset to be accessible 
        # by index.html so that the html can be connected to the queryset
        return render(request, 'blog_index.html', context)

# view for detailed posts
def detailedPost(request, pk):
    post = PostModels.objects.get(id = pk)
    profiles = Profile.objects.all()
    context = {
        'post' : post,
        'profiles': profiles,
    }
    return render(request, 'detailedPost.html', context)

# to edit posts
def PostEdits(request, pk):
    post = PostModels.objects.get(id=pk)

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('postdetails', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post' : post,
        'form' : form,
        

    }
    return render(request, 'postedits.html', context)

# views for deleting posts
def deletepost(request, pk):
    post = PostModels.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post' : post,
    }
    return render(request, 'deletepost.html', context)

