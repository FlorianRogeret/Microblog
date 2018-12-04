# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)