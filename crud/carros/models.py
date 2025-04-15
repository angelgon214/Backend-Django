from django.db import models

# Create your models here.
class Carros(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    plate = models.CharField(max_length=7)
    color = models.CharField(max_length=20)
    price = models.IntegerField()