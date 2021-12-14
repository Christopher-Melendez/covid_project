#need to import redirect to redirect to another url after saving a post
from django.shortcuts import render, redirect
# Create your views here.
from .models import PostModels, commentsModels
#import forms
from .forms import PostModelForm, PostUpdateForm, CommentForm, CommentUpdateForm
from login.models import Profile

from login.views import login_view, log_req_view


def index(request):
    # makes sure the user is logged in
    if not request.user.is_authenticated:
        return login_view(request)
    else:
        # takes all the PostModels objects in the queryset
        posts = PostModels.objects.all()
        if request.method == 'POST':
            form = PostModelForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('blog-index')
        else:
            form = PostModelForm()
        # context dictionary to pass multiple attributes to the index file
        # in a more systematic way 
        profiles = Profile.objects.all()
        context = {
            'posts' : posts,
            'form' : form,
            'profiles': profiles,
        }
        # can render templates
        # passing the dictionary {'posts' : posts} allows this queryset to be accessible 
        # by the html so that it can be connected to the queryset
        return render(request, 'blog_index.html', context)

# view for detailed posts
def detailedPost(request, pk):
    post = PostModels.objects.get(id = pk)
    profiles = Profile.objects.all()
    # for comments
    if request.method == 'POST':
        com_form = CommentForm(request.POST)
        # saving valid comment forms; need to assign every value in the commentsmodel
        if com_form.is_valid():
            instance = com_form.save(commit=False)
            # user = logged in user
            instance.user = request.user
            instance.post = post
            # save and redirect to detailed post site
            instance.save()
            return redirect('postdetails', pk=post.id)

    else:
        com_form = CommentForm()

    context = {
        'post' : post,
        'profiles': profiles,
        'com_form' : com_form,
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

# to edit comments
def commentedits(request, pk):
    post = PostModels.objects.get(id=pk)
    comment = commentsModels.objects.all()

    if request.method == 'POST':
        form = CommentUpdateForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
            return redirect('postdetails', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'commentedits.html', context)

# views for deleting comments
def deletecomment(request, pk):
    post = PostModels.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('postdetails', pk=post.id)
    context = {
        'post' : post,
    }
    return render(request, 'deletecomment.html', context)
