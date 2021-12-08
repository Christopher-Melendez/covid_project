from django.db import models
from django.contrib.auth.models import User    
from django.db.models.signals import post_save
from datetime import datetime, timezone, tzinfo, timedelta

#Currently Unused..
class Profile(models.Model):
    id = models.BigIntegerField(primary_key='true', default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #last_active = models.DateTimeField(default=datetime.now())
    #avatar_img = models.FileField(default='cat.jpeg')
    #avatar_img_data = models.BinaryField(null=True)
    photo = models.ImageField(default='cat.jpeg') 

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
