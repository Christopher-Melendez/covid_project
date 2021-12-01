from django.db import models
from django.contrib.auth.models import User    
from datetime import datetime, timezone, tzinfo, timedelta

#Currently Unused..
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_active = models.DateTimeField(default=datetime.now())
    #last_url = ? Might be good idea...
     
