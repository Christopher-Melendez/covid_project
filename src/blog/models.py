from django.db import models
from datetime import datetime
#from datetime import datetime # will give you that date and time

# Create your models here.

# to create a model that essentially acts as a table that will be 
# stored in our database
class Post(models.Model):
    title = models.CharField(max_length = 255)
    #slug = models.SlugField()
    #intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(default =datetime.now, blank=True)

    class Meta:
            ordering = ['-created_at']