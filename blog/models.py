# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    creation_date = models.DateTimeField('date published')
    update_date = models.DateTimeField('date update')