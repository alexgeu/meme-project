from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# User is the sender

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    The signal is used to create a profile for each newly created user
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saved_profile(sender, instance, **kwargs):
    instance.profile.save()
