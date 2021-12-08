from django import forms
from .models import PostModels

class PostModelForm(forms.ModelForm):
    #changing field size of forms
    content = forms.CharField(widget=forms.Textarea(attrs={'rows' : 4}))
    class Meta:
        # two parameters when doing forms, which model we are creating the form for
        model = PostModels
        # fields --> which fields within the model you want to have access to (look in models.py)
        # we only want the user to access the title and the content, not the author and date created
        fields = ('title', 'content')
        