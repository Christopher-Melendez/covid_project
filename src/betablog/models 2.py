from django.db import models
from django.contrib.auth.models import User
# default django model where django stores all the user on the app


# Create your models here.
class PostModels(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # the authors is imported from the Users model that django has on the admin panel
    #on_delete=models.CASCADE makes sure that whenever a user is deleted, the system 
    #automatically deletes every post associated with the user 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # this class adds some metadata to this model
    class Meta:
        # orders the blog from most recent to oldest
        # this tuple (finite list) 
        # the - makes sure you have the reverse of the dates 
        # the comma is needed for it to understand it is a tuple or list even though we
        # are only ordering by one field
        ordering = ('-date_created',)

    # in order to have the post hyperlink or object be described by the title
    def __str__(self):
        return self.title