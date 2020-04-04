from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="uprofile")
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    name = models.CharField(default='New user', max_length=40)
    bio = models.TextField(default='Since you are new here, you could introduce yourself. This page servers exactly this purpose. Here you can introduce yourself to users who visits you profile!', max_length=500)
    favourite_series = models.CharField(default='All of them', max_length=40)
    favourite_character = models.CharField(default='Everyone', max_length=40)
    favourite_quote = models.TextField(default='Live long and prosper!', max_length=500)
    cosplay_input = models.TextField(default='If you like to dress like you favourite character, you can show it here!', max_length=500)
    cosplay_image1 = models.ImageField(default='no-cosplay-img.jpg', upload_to='cosplay_pic')
    cosplay_image2 = models.ImageField(upload_to='cosplay_pic', blank=True)
    cosplay_image3 = models.ImageField(upload_to='cosplay_pic', blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ForeignKey(User, related_name="receiver")
    title = models.CharField(max_length=40)
    message = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}-{}'.format(self.sender, str(self.receiver), str(self.title))


class Reply(models.Model):
    message = models.ForeignKey(Message, related_name="reply")
    profile = models.ForeignKey(Profile)
    user = models.ForeignKey(User)
    reply = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}'.format(self.message, str(self.created_date))