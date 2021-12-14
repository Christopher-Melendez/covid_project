from django import forms
from .models import PostModels, commentsModels

class PostModelForm(forms.ModelForm):
    #changing field size of forms and label and adding a placeholder to prompt user to enter text in the box
    content = forms.CharField(label = 'Share your story!', widget=forms.Textarea(attrs={'rows' : 4, 'placeholder': 'Enter text here...'}))
    title = forms.CharField(label = 'Post Title', widget=forms.Textarea(attrs={'rows' : 1, 'placeholder': 'Enter text here...'}))
    class Meta:
        # two parameters when doing forms, which model we are creating the form for
        model = PostModels
        # fields --> which fields within the model you want to have access to (look in models.py)
        # we only want the user to access the title and the content, not the author and date created
        fields = ('title', 'content')

# form to edit posts
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModels
        fields = ('title', 'content')

# form to make comments
class CommentForm(forms.ModelForm):
    comment = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder': 'Add comment here...'}))
    class Meta:
        model = commentsModels
        fields = ('comment', )

# form to edit comments
class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = commentsModels
        fields =  ('comment', )