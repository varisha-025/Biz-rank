from django.db import models

from brands.models import Brand
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    # product_images = models.ImageField(upload_to='product_images', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return f"{self.name}"