from django.db import models
from .choices import PRODUCT_FILTERS
from django.contrib.auth.models import User
from accounts.models import Profile


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_image')
    image2 = models.ImageField(upload_to="product_image", blank=True)
    image3 = models.ImageField(upload_to="product_image", blank=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=1, choices=PRODUCT_FILTERS)
    size = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name="productreview")
    profile = models.ForeignKey(Profile)
    user = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.post.title, str(self.user.username), str(self.content))