# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
        return render(request, 'index.html', locals())

def register(request):
        return render(request, 'registerform.html', locals())

def log(request):
        return render(request, 'logform.html', locals())

def post(request):
        return render(request, 'postform.html', locals())

def createusr(request):
        pseudo = request.POST['pseudo']
        passwd = request.POST['passwd']
        user = User.objects.create_user(username=pseudo,password=passwd)
        if user is None or pseudo.exists():
                return redirect('register')
        else:
                user.save()
                login(request, user)
                return redirect('') 

def logusr(request):
        pseudo = request.POST['pseudo','']
        passwd = request.POST['passwd','']
        user = authenticate(request, username=pseudo, password=passwd)
        if user is not None:
                login(request, user)
                return render(request, 'index.html', locals())
        else:
                return render(request, 'logform.html', locals())