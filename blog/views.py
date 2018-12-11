from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from django.db import connection
from django.core.paginator import Paginator
from datetime import datetime
from django.urls import reverse

#Home page where all articles are findable order by the creation_date
def article_liste(request):
        #Use to find all articles 
        article = Article.objects.all().order_by('-update_date')
        #Create the pages with only 5 articles
        paginator = Paginator(article,5)
        #Page form the url
        page = request.GET.get('page')
        #Send the article from that page
        article = paginator.get_page(page)        
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
        #Use to find all articles from a specific user
        author = get_object_or_404(User, username = username)
        article = Article.objects.all().filter(author = author).order_by('-creation_date')
        #Create the pages with only 5 articles
        paginator = Paginator(article,5)
        #Page form the url
        page = request.GET.get('page')
        #Send the article from that page
        article = paginator.get_page(page)        
        #Post the articles and the author to the article_user.html so it can use it
        return render(request, 'article_user.html', {'article':article, 'author':author})


@login_required(login_url="/compte/login/")
def delete_article(request, id): 
        #Use to find all articles
        article = get_object_or_404(Article, id=id)
        if request.user.username == article.author.username:
                article.delete()
                #Use to find all articles 
                article = Article.objects.all().order_by('-update_date')
                #Create the pages with only 5 articles
                paginator = Paginator(article,5)
                #Page form the url
                page = request.GET.get('page')
                #Send the article from that page
                article = paginator.get_page(page)        
                #Post them to the index.html so it can use it
                return render(request,'index.html',{'article':article})
        return render(request,'article_detail.html')

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
        #Use to find all articles
        article = get_object_or_404(Article, id=id)
        #If the user currently log is the author
        if request.user.username == article.author.username:
                #We send him to the article.modifie.html page
                return render(request, 'article_modifie.html', {'article' : article})               
        else:
                #If not we send him to  article_detail.html
                return render(request,'article_detail.html')

@login_required(login_url='compte/login/')
def article_doupdate(request, id):
        #We get the article thanks to the id
        article = get_object_or_404(Article, id = id)
        #The title's article became the one register in the form
        article.title = request.POST['title']
        #The body's article became the one register in the form
        article.body = request.POST['body']
        #We update the update date
        article.update_date = datetime.now()
        #We save the article
        article.save()
        #We redirect him to the article's page
        return render(request,'article_detail.html',{'article':article})
        
                        