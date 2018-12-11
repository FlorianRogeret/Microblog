# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    #Id of the article as a primary key
    id = models.AutoField(primary_key=True)
    #Title of the article with a max lentgh of 100
    title = models.CharField(max_length=100)
    #Body of the article
    body = models.TextField()
    #Creation date of the article
    creation_date = models.DateTimeField(auto_now_add=True)
    #Update date of the article
    update_date = models.DateTimeField(auto_now_add=True)
    #Author of the article get thanks to a foreign key to User model
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

    #Use to reduce body's article up to 100 charactres
    def snippet(self):
        #If the length of the body is < to 100 characters
        if len(self.body) < 100:
            #It display the body
            return self.body
        else:
            #It display the first 100 characters + '...'
            return self.body[:100] + '...'