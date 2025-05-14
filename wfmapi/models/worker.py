from django.db import models
from django.conf import settings


class Worker(models.Model):

    STATUS_CHOICES= [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('on_leave','On Leave'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="worker_profile")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    

    def __str__(self):
        return f"worker: {self.user.email}"
