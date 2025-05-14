from django.db import models
from django.conf import settings
from .group import Group
from .worker import Worker


class GroupWorker(models.Model):
    
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'worker')
    
    def __str__(self):
        return f"{self.worker} in {self.group}"
    