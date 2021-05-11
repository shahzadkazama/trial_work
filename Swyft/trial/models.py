from django.db import models


# Create your models here.


class Transport(models.Model):
    type = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Vehicle(Transport):
    model = models.TextField(null=True, blank=True)
    make = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    year = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Car(Vehicle):
    pass
