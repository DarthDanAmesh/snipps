from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


# this is used in the models as objects = CustomUserManager()
class CustomUserManager(BaseUserManager):
    # create and save user with the given email and password
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email is required!"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        # creates and saves superuser with their email and password
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff set to True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser set to True."))
        return self.create_user(email, password, **extra_fields)
