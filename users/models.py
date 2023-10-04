from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, null=True, blank=True)
    division = models.CharField(max_length=50, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True, choices=[("Male", "Male"),
                                                                 ("Female", "Female")])
    hr_number = models.CharField(max_length=20, blank=False)

    # create the user profile
    # post_save is hooking signal for creating and saving the user
    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # save the user profile
    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user
