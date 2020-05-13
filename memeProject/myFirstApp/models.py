from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(default=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'my_id' : self.id})


    # def get_api_url(self):
    #     return reverse("posts-api:detail", kwargs={"slug": self.slug})
    def __str__(self):
        return str(self.title)
    '''
    def get_like_url(self):
        return reverse("like-toggle", kwargs={"my_id": self.id})

    def get_api_like_url(self):
        return reverse("posts-like-api-toggle", kwargs={"my_id": self.id})
'''
    @property
    def num_likes(self):
        return self.liked.all().count


class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        return str (self.product)

class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField(max_length=240)
    timestamp = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='commented')

    def __str__(self):
        return '{}-{}'.format(self.product, str(self.user.username))