from django.urls import path
from django.conf.urls import url
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/',views.signup_view,name="signup")
    #path('', views.index, name='index'),
    #path('log/', views.log, name='logform'),
    #path('logusr/', views.logusr, name='logusr'),
    #path('createusr/', views.createusr, name='createusr'),
    #path('register/', views.register, name='registerform'),
]