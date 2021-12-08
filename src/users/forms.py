from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # model in this case we want to be the users model that django already has (can view the data values stored in the admin panel)
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #gets rid of the bulky help text
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
