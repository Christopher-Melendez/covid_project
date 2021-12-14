from django.db import models
from django.contrib.auth.models import User
# default django model where django stores all the user on the app


# Create your models here.

class PostModels(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # orders the blog from most recent to oldest
        ordering = ('-date_created',)
    
    # to count the number of comments
    def comment_count(self):
        return self.commentsmodels_set.all().count()

    # in order to have the post hyperlink or object be described by the title
    def __str__(self):
        return self.title

# comments model to store comments
class commentsModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModels, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment