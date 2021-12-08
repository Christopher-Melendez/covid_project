from django.db import models
from django.contrib.auth.models import User    
from datetime import datetime, timezone, tzinfo, timedelta

#Currently Unused..
class Profile(models.Model):
    id = models.BigIntegerField(primary_key='true', default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #last_active = models.DateTimeField(default=datetime.now())
    avatar_img = models.FileField(default=0)
    avatar_img_data = models.BinaryField(null=True) 
