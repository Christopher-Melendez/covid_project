from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from login.models import Profile

from login.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please Provide a Valid Email Address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', ) 


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar_img']