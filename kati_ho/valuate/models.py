from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    battery = models.IntegerField()
    back_camera = models.IntegerField()
    front_camera = models.IntegerField()
    ram = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #image = models.ImageField()

    def __str__(self):
        value = self.brand+ " "+self.want
        return (value)

class Compare(models.Model):
    price = models.IntegerField()
    fc = models.CharField(max_length=10)
    pc = models.CharField(max_length=10)
    display = models.FloatField()
    res = models.CharField(max_length=10)
    Model = models.CharField(max_length=100)
    battery = models.IntegerField()
    Link = models.CharField(max_length=200)
