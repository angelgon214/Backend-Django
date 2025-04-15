from django.db import models

# Create your models here.
class Hamburguesa(models.Model):
    name = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length=100)
    price = models.IntegerField()
    client = models.CharField(max_length=30)