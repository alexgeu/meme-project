from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='images/', blank = True)

    def __str__(self):
        return self.title

class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(default='True')
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'my_id' : self.id})

class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class MemeImage(models.Model):
    imgCaption = models.CharField(max_length=200)
    meme_Main_Img = models.ImageField(default='default.jpg', upload_to='memes', blank = True)




