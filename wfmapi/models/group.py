from django.db import models
from django.conf import settings
from .worker import Worker



class Group(models.Model):

    name = models.CharField(max_length=150)
    workers = models.ManyToManyField(Worker, through='GroupWorker', related_name='groups')

    
    def __str__(self):
        return self.name
    