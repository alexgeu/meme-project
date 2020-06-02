from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here

CATEGORY_CHOICES=[
	('Nerd', 'Nerd'),
	('Quotes', 'Quotes'),
	('Programming', 'Programming'),
	('Daily struggle', 'Daily Struggle'),
]

@property
def num_likes(self):
    return self.liked.all().count
    
class Meme(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/meme_images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='No category chosen')
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('memes:meme-detail', kwargs={'my_id' : self.id})

    class Meta:
        ordering = ['-timestamp']
        
    def __str__(self):
        return str(self.title)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        return str (self.meme)

    @property
    def num_likes(self):
        return self.liked.all().count
  
class Comment(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField(max_length=240)
    timestamp = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='commented')

    def __str__(self):
        return '{}-{}'.format(self.meme.title, str(self.user.username))