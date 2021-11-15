from django.db import models
from django.contrib.auth.models import User    
from datetime import datetime, timezone, tzinfo, timedelta

# Create your models here.
#time_limit = 15

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_active = models.DateTimeField(default=datetime.now())

# class profile_manager(models.Manager):
#     def create_profile(self, title):
#         profile = self.create(title=title)
#         return profile

#     def check_active(self):
#         p_last_active = Profile.last_active
#         p_user = Profile.last_active
#         if (p_last_active - timedelta(minutes = time_limit) > time_limit):
            
