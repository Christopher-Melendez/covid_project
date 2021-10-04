from django.db import models

# Create your models here.
class Map(models.Model):
    name = models.TextField()
    text = models.TextField()
