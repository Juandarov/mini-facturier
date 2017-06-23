from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    Project_name = models.CharField(max_length = 50)
    creation_date = models.DateField()
    status = models.ForeignKey('Status')
    client = models.ForeignKey('Client')

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.Project_name


class Client(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Status(models.Model):
    label = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"


class ProjectLine(models.Model):
    label = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    project = models.ForeignKey('Project')
