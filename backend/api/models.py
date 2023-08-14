from django.db import models

# Create your models here.

class Product(models.Model):
    CHOICES = [
        (0, "Sold Out"),
        (1, "In Stock"),
        (2, "In Order")
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    
    def __str__(self):
        return self.name
