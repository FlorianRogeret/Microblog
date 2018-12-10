from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from django.db import connection

#Home page where all articles are findable order by the creation_date
def article_liste(request):
        #Use to find all articles 
        article = Article.objects.all().order_by('-creation_date')
        #Post them to the index.html so it can use it
        return render(request,'index.html',{'article':article})

#Page when you click on an article so it redirect to it
def article_detail(request, id):
        #find the id of an article
        article = get_object_or_404(Article, id = id)
        #Post it to article_detail.html so it can use it
        return render(request,'article_detail.html',{'article':article})

#Home page where all articles are findable order by the creation_date
def article_user(request,username):
        #Use to find all articles 
        author = get_object_or_404(User, username = username)
        article = Article.objects.all().filter(author = author).order_by('-creation_date')
        #Post them to the index.html so it can use it
        return render(request, 'article_user.html', {'article':article, 'author':author})


@login_required(login_url="/compte/login/")
def delete_article(request, id): 
        #article = Article.objects.get(id = id)
        article = get_object_or_404(Article, id=id)
        if request.user.username == article.author.username:
                article.delete()
        return render(request,'article_detail.html',{'article':article})

#View that allow to create an article only if the user is logged in
@login_required(login_url="/compte/login/")
def article_create(request):
        #if the method used is a post 
        if request.method == 'POST':
                #Get the information entered in the differents forms
                form = forms.CreateArticles(request.POST)
                #If they are valid
                if form.is_valid():
                        #It will save the informations of thoses forms but no commit it yet 
                        instance = form.save(commit = False)
                        #It will take the author username
                        instance.author = request.user
                        #and then save the article
                        instance.save()
                        #It will then redirect to the homepage
                        return redirect('article:index')
        #If the method is not a post
        else : 
                #It will create news empty forms
                form = forms.CreateArticles()
        #If the form is not valid it will redirect the user to tis same page
        return render(request,'article_create.html',{'form':form})

@login_required(login_url="/compte/login/")
def article_update(request, id): 
        article = get_object_or_404(Article, id=id)
        if request.user.username == article.author.username:
                return render(request, 'article_modifie.html', {'article' : article})               
        else:
                return render(request,'article_detail.html',{'article':article})

@login_required(login_url='compte/login/')
def article_doupdate(request, id):
        if request.method == 'POST':
                article = get_object_or_404(Article, id = id)
                article.title = request.POST['title']
                article.body = request.POST['body']
                #article.updated = now()
                article.save()
                return render(request,'article_detail.html',{'article':article})
        else:
                return render(request,'article_modifie.html',{'article':article})
        
                        