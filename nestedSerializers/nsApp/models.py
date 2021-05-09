from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Author(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=6)


class Book(models.Model):
    title = models.CharField(max_length=20)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)
