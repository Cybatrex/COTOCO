# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from activities.models import Activity
from clients.models import Client


class Project(models.Model):
    project_name = models.CharField(max_length=255, verbose_name='Nombre')
    project_description = models.CharField(blank=True ,max_length=255, verbose_name='Descripción', default='')
    project_client = models.ForeignKey(Client, verbose_name='Cliente del proyecto')
    project_activity = models.ManyToManyField(Activity, verbose_name='Actividades', blank=True)
    project_active = models.BooleanField(verbose_name='Proyecto activo?', default=True)

    def __unicode__(self):
        return '%s' % self.project_name

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']
