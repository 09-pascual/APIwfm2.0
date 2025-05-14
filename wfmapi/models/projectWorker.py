from django.db import models
from django.conf import settings
from .project import Project
from .worker import Worker




class ProjectWorker(models.Model):

    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)    

    class Meta:
        unique_together = ('project', 'worker')
    
    def __str__(self):
        return f"{self.worker} on {self.project}"