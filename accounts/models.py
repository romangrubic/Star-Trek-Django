from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="uprofile")
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    name = models.CharField(max_length=40)
    bio = models.TextField(max_length=500)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.name
