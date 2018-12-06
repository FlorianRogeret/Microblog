from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def article_liste(request):
        articles = Article.objects.all().order_by('creation_date')
        return render(request, 'blog/index.html',{'articles':articles})

def article_detail(request, slug):
        #return HttpResponse(slug)
        article = Article.objects.get(slug=slug)
        return render(request,'blog/article_detail.html',{'article':article})