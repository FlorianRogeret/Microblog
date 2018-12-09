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
        article = Article.objects.get(id = id)
        #Post it to article_detail.html so it can use it
        return render(request,'article_detail.html',{'article':article})

#Home page where all articles are findable order by the creation_date
def article_user(request,author):
        #Use to find all articles 
        author = Article.objects.get(author = author)
        article = Article.objects.filter(author).order_by('-creation_date')
        #Post them to the index.html so it can use it
        return render(request, 'article_user.html',{'article':article})


@login_required(login_url="/compte/login/")
def delete_article(request, id, author): 
        instance = Article.objects.get(id = id)
        author = Article.objects.get(author = author)
        #creator= instance.user.username
        if request.method == "POST" and request.user.is_authenticated and request.user.username == author:
                instance.delete()
        return redirect('article:index')

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

def article_update(request, author, title, body): 

        if request.method == 'POST' and author.is_authenticated():  # S'il s'agit d'une requête POST
                form = forms.EditArticles(request.POST)  # Nous reprenons les données
  
                if form.is_valid(): # Nous vérifions que les données envoyées sont valides
        
                        # Ici nous pouvons traiter les données du formulaire
                        title = form.cleaned_data['title']
                        body = form.cleaned_data['body']
                        
                        return render(request, 'index.html') # Redirect after POST
  
        else: # Si ce n'est pas du POST, c'est probablement une requête GET
                # Nous créons un formulaire pré-rempli
                form = forms.EditArticles(title = title, body = body)
  
        return render(request, 'index.html')