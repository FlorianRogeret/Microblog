from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
        return render(request, 'blog/index.html')

def register(request):
        return render(request, 'registerform.html')

def log(request):
        return render(request, 'logform.html')

def createusr(request):
        pseudo = None
        passwd = None
        if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                        pseudo = request.POST.get('pseudo')
                        passwd = request.POST.get('passwd')
                        user = User.objects.create_user(username=pseudo,password=passwd)
                        user.save()
                        if user is None:
                                return redirect('register')
                        else:
                                user.save()
                                login(request, user)
                                return redirect('') 
        else:
                form = RegisterForm()

        return render(request, 'test.html', {'form': form}) 

def logusr(request):
        pseudo = request.POST['pseudo','']
        passwd = request.POST['passwd','']
        user = authenticate(request, username=pseudo, password=passwd)
        if user is not None:
                login(request, user)
                return render(request, 'index.html')
        else:
                return render(request, 'logform.html')