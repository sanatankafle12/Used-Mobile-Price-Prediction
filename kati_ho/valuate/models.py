from django.db import models

# Create your models here.
class Listing(models.Model):
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    back_camera = models.IntegerField()
    front_camera = models.IntegerField()
    ram = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()
    #image = models.ImageField()

    def __str__(self):
        value = self.brand+self.description
        return (value)
    
    