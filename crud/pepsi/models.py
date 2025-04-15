from django.db import models

# Create your models here.
class Pepsi(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
