from django.db import models
from django.conf import settings
from .project import Project
from .group import Group


class ProjectGroup(models.Model):

    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'group')
    
    def __str__(self):
        return f"{self.group} is assigned to {self.project}"