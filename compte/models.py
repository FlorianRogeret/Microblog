from django.db import models
#from __future__ import unicode_literals

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=30)