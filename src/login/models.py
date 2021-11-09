from django.db import models
from django.contrib.auth.models import User    
from datetime import datetime, timezone, tzinfo

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_active = models.DateTimeField(default=datetime.now())
