from django.db import models
from django.contrib.postgres.fields import ArrayField

from user.models import User
# Create your models here.

class Brand(models.Model):
    logo = models.ImageField(upload_to='images/', null = True, blank = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    website = models.URLField(null = True, blank = True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    payment_options = ArrayField(models.CharField(max_length=64), null = True, blank = True)
    social_media = models.JSONField(null=True, blank = True)
    delivery_time = models.CharField(max_length=200)
    delivery_fee = models.CharField(max_length=200)
    product_categories = models.CharField(max_length=200)
    FAQs = models.JSONField(null = True, blank = True)

    def __str__(self):
        return f"{self.name}"
    

class BrandOwnership(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} - {self.user.first_name}"
