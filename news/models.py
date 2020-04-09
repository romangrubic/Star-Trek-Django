from django.db import models
from django.utils import timezone
from .choices import NEWS_CHOICES
from django.contrib.auth.models import User
from accounts.models import Profile


# Create your models here.
class News(models.Model):
    """A single news"""
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=1, choices=NEWS_CHOICES)
    image = models.ImageField(upload_to="news_image")
    image2 = models.ImageField(upload_to="news_image", blank=True)
    image3 = models.ImageField(upload_to="news_image", blank=True)
    forum_thread = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.title


class NewsComment(models.Model):
    news = models.ForeignKey(News, related_name="newscomments")
    profile = models.ForeignKey(Profile)
    user = models.ForeignKey(User)
    content = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.post.title, str(self.user.username), str(self.content))