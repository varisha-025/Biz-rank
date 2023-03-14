from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """User model."""

    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=25, null=True, blank=True)
    # most_shopped_brand = models.CharField(max_length=200)
    # favorite_brands = ArrayField(models.CharField(max_length=200))
    # favorite_products = ArrayField(models.CharField(max_length=200))
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"