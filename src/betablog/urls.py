from django.urls import path
# . indicates current directory, betablog; imports views.py so that now you can use functions from it
#by doing views.FUNCTIONNAME
from .import views

urlpatterns = [
    # when using this url, will invoke this view
    path('blog/', views.index, name = 'blog-index'),
]