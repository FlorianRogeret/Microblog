# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm



def index(request):
    return render(request, 'index.html', locals())

def register(request):
    return render(request, 'registerform.html', locals())

def log(request):
    return render(request, 'logform.html', locals())

def post(request):
    return render(request, 'postform.html', locals())

#    form = RegisterForm(request.POST or None)

#    if form.is_valid(): 
#        username = form.cleaned_data['username']
#        password = form.cleaned_data['password']
#        envoi = True