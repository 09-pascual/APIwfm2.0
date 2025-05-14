from django.db import models
from django.conf import settings


class Client(models.Model):
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"