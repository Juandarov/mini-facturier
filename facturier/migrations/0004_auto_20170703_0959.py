# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0003_auto_20170619_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('dear', 'devis archive'), ('deco', 'devis en cours'), ('faar', 'facture archive'), ('faco', 'facture en cours')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
