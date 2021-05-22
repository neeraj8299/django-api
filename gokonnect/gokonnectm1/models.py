from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(min=3, max_length=10)
    lastName = models.CharField(min=3, max_length=10)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    country_code = models.IntegerField()
    gender = models.Choices(('male', 'Male'), ('female', 'Female'),
                            ('prefer_not_to_say', 'Prefer Not to say'))
