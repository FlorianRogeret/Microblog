from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

#This is the view that allow user to signup
def signup_view(request):
        # if the method used is a post
        if request.method == 'POST':
                #It will save the information entered into the forms into form
                form = UserCreationForm(request.POST)
                #If the informations are correct
                if form.is_valid():
                        #It will save the user
                        user = form.save()
                        #And logging it
                        login(request, user)
                        #And finaly redirect it to the homepage
                        return redirect('article:index')
        #If the method is not a post
        else :
                #It will create a new empty form 
                form = UserCreationForm()
        #If the form is not valid it will redirect the user to that same page
        return render(request,'signup.html',{'form':form})
        
#This view allow the user to loggin
def login_view(request):
        #If the method used is a post
        if request.method == 'POST':
                #It will save the entered information into form
                form = AuthenticationForm(data = request.POST)
                #If the form is valid
                if form.is_valid():
                        #It will get the user reference to the username
                        user = form.get_user()
                        #And then loggin the user
                        login(request, user)
                        #This is used to catch the following url (if there is one) 
                        #(for exemple when he try to post something but he's not connected and then loggin)
                        if 'next' in request.POST:
                                #If there is one the user will be redirect to it
                                return redirect (request.POST.get('next'))
                        else:
                                #If there's not he will be redirect to the homepage
                                return redirect('article:index')
        #If the method is not a post
        else:
                #It will create a new empty form
                form = AuthenticationForm()
        #If the form is not valid it will redirect the user to that same page
        return render(request,'login.html',{'form':form})

#This allow the user to logout
def logout_view(request):
        #If the method is a post
        if request.method =='POST':
                #It will logout the user
                logout(request)
                #And redirect it to the homepage
                return redirect('article:index')