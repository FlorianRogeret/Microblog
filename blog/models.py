# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    #update_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    #Use to reduce body's article up to 100 charactres
    def snippet(self):
        return self.body[:100] + '...'