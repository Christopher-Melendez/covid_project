from django.db import models
# imports the user we created in the admin page
#from django.contrib.auth.models import User

#class Post(models.Model):
    #defining things we want in our blog posts
    #title = models.CharField(max_length = 255)
    # the author is taken from the user from the admin page
    # on deleting the user, will delete all of the user's blog posts
    #author = models.ForeignKey(User, on_delete=models.CASCADE, default = 'no author')
    #body = models.TextField()

    
    #def __str__(self):
        # on the admin page will be able to see the title of the blog post and author rather then a string of numbers
        #return self.title + ' | ' + str(self.author)