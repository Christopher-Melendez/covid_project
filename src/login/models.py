from django.db import models
from django.contrib.auth.models import User    
from django.db.models.signals import post_save
from datetime import datetime, timezone, tzinfo, timedelta

#Currently Unused..
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='cat.jpeg') 

#Constructor for Profile Instance
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)

#Signal Listening for when a User is Created which triggers profile to also be made
post_save.connect(create_profile, sender=User)
