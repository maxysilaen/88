from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.

class TasksList(models.Model):
    name_task = models.CharField(max_length=120)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __unicode__(self):
        return self.name_task
