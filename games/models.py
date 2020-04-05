from django.db import models


# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image1 = models.ImageField(upload_to='games_images')
    image2 = models.ImageField(upload_to='games_images')
    image3 = models.ImageField(upload_to='games_images')
    image4 = models.ImageField(upload_to='games_images')
    image5 = models.ImageField(upload_to='games_images')
    game_link = models.CharField(max_length=254)
    forum_thread = models.CharField(max_length=254, blank=True)


    def __str__(self):
        return self.name
