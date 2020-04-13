from django.db import models
from django.urls import reverse
# Create your models here.

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

    