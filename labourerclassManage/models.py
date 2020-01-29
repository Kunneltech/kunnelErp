from django.db import models

# Create your models here.
class labourerclass(models.Model):

    labourerclass   = models.CharField(max_length=50)
    wageclass       = models.CharField(max_length=50)
    labourerclassid = models.CharField(max_length=50)
    compensation    = models.BooleanField()
    retention       = models.BooleanField()
    advance         = models.BooleanField()
    concretecharges = models.BooleanField()


