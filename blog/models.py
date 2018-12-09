# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    #update_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    def __del__(self):
        return self.id

    def __aut__(self):
        return self.author

    #Use to reduce body's article up to 100 charactres
    def snippet(self):
        if len(self.body) < 100:
            return self.body
        else:
            return self.body[:100] + '...'