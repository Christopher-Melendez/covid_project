from django.urls import path
# . indicates current directory, betablog; imports views.py so that now you can use functions from it
#by doing views.FUNCTIONNAME
from .import views

urlpatterns = [
    # when using this url, will invoke this view
    path('blog/', views.index, name = 'blog-index'),
    path('blogdetails/<int:pk>/', views.detailedPost, name = 'postdetails'),
    path('blogedit/<int:pk>/', views.PostEdits, name = 'postedit'),
    path('deletepost/<int:pk>/', views.deletepost, name = 'deletepost'),
]