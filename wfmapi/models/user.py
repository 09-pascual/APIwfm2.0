from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    is_owner = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email