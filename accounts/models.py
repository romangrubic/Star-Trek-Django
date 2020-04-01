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
    cosplay_image1 = models.ImageField(default='no-cosplay-img.jpg', upload_to='cosplay_pic')
    cosplay_image2 = models.ImageField(upload_to='cosplay_pic', blank=True)
    cosplay_image3 = models.ImageField(upload_to='cosplay_pic', blank=True)


    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    reciever = models.ForeignKey(User, related_name="receiver")
    msg_title = models.CharField(max_length=40)
    msg_content = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
