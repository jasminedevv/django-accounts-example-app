from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save 
from django.dispatch import receiver

class User(AbstractUser):
    """auth/login-related fields"""
    pass
    # Examples:
    # email (if used for login)
    # extra permissions
    # NOTE: before putting something here make sure it wouldn't be better in the profile model

class Profile(models.Model):
    """non-auth-related/cosmetic fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Examples:
    # Display Name
    # Bios, descriptions, taglines
    # Theme (light or dark)
    # email (if not used to log in)

"""receivers to add a Profile for newly created users"""
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(user=instance)
@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()