from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.CharField(max_length=30)

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name