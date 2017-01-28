from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contests(models.Model):
    #id = models.IntegerField(primary_key=True,db_index=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    organiser = models.CharField(max_length=200)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    announcment = models.TextField()

    class Meta:
        managed = True
        db_table = 'contests'
        verbose_name_plural = 'contests'
