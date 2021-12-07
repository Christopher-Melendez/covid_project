"""covid_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from heat_map.views import maps_view
from tables.views import tables_view
from blog.views import blog_view
from login.views import log_req_view, login_view, logout_view, signup_view, login_error_view
from graphs.views import graphs_view


urlpatterns = [
    path('', home_view, name='home'),
    path('maps/', maps_view, name='maps'),
    path('tables/', tables_view, name='tables'),
    path('blog/', blog_view, name='blog'),
    path('log_req_view', log_req_view, name="log_req_view"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name="signup"),
    path('login_error/', login_error_view, name="login_error"),
    path('graphs/', graphs_view, name="graphs"),
    #path('sign_up/', signup_view, name="signup_view"),
    path('admin/', admin.site.urls),
]
