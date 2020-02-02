from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    description = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)



