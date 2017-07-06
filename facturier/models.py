from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models


# Create your models here.
STATUS_CHOICES = (
    ("dear", 'devis archive'),
    ("deco", 'devis en cours'),
    ("faar", 'facture archive'),
    ("faco", 'facture en cours'),
)

class Project(models.Model):
    Project_name = models.CharField(max_length = 50)
    creation_date = models.DateField()
    user = models.ForeignKey(User)
    client = models.ForeignKey('Client')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)


    def __unicode__(self):
        return self.Project_name

class Client(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class ProjectLine(models.Model):
    label = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    project = models.ForeignKey('Project')

    def project_price(self):
        return self.unit_price * self.quantity
