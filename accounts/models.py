from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="uprofile")
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    name = models.CharField(max_length=40)
    bio = models.TextField(max_length=500)
    favourite_series = models.CharField(max_length=40)
    favourite_character = models.CharField(max_length=40)
    favourite_quote = models.TextField(max_length=500)
    cosplay_input = models.TextField(max_length=500)
    cosplay_image1 = models.ImageField(default='default.jpg', upload_to='cosplay_pic')
    cosplay_image2 = models.ImageField(default='default.jpg', upload_to='cosplay_pic')

    def __str__(self):
        return self.name
