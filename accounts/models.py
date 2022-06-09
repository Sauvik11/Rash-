from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.



class carModel(models.Model):
    # symboling=  models.IntegerField(max_length=4,null=True,blank=True, unique=True)
    make = models.CharField(max_length=100,null=True,blank=True)
    fueltype = models.CharField(max_length=10,null=True,blank=True)
    numofdoors = models.CharField(max_length=10,null=True,blank=True)
    bodystyle = models.CharField(max_length=10,null=True,blank=True)
    drivewheels= models.CharField(max_length=10,null=True,blank=True)
    enginelocation = models.CharField(max_length=10,null=True,blank=True)
    bootSpacelt= models.IntegerField(max_length=50,null=True,blank=True)
    # wheelbase = models.FloatField(max_length=50,blank=True,null=True)
    price= models.IntegerField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.make


    
