from django.db import models

# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('bola', 'Bola'),
        ('sepatu', 'Sepatu'),
        ('jersey', 'Jersey'),
        ('kaos', 'Kaos'),
        ('celana', 'Celana'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='bola')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name   
    