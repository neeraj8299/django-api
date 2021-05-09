from django.db import models

# Create your models here.


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.id+self.name+self.score


class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastname = models.CharField(max_length=10)
    travelEndPoint = models.CharField(max_length=10)
