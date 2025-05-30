from django.db import models
from django.conf import settings
from .client import Client
from .worker import Worker
from .group import Group


class Project(models.Model):

    STATUS_CHOICES= [('open', 'open'),
                    ('closed','closed'),
                    ('upcoming', 'upcoming')]
    
    client= models.ForeignKey(Client, on_delete=models.CASCADE,related_name="projects")
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    start_date = models.DateField()
    end_date = models.DateField()
    expected_duration = models.PositiveIntegerField(default=3, help_text="duration in days")
    workers = models.ManyToManyField(Worker, through="ProjectWorker", related_name="projects")
    groups = models.ManyToManyField(Group, through="ProjectGroup", related_name='projects')


    def __str__(self):
        return self.name 


