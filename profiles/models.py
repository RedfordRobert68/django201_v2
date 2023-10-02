from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    image = ImageField(
        default='/media/profiles/default_bg.jpg',
        upload_to = 'profiles'
    )

    def __str__(self):
	    return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): # Signal
    """Create a new Profile() object when a Django user is created""" # Doc string
    if created:
         Profile.objects.create(user=instance)
         

