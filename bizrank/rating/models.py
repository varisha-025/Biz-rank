from django.db import models

# Create your models here.


class Rating:
    rating = models.IntegerField()
    brand = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return f"{self.brand} {self.user}"
    
    
class Suggestion:
    title = models.CharField(max_length=50)
    description = models.TextField()
    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.user}"
    

