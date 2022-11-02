from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio=models.TextField()
    created_on = models.DateTimeField()
    profile_image_url = models.TextField()
    active = models.BooleanField(True)
    
    