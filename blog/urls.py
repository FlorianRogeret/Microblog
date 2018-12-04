from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log/', views.log, name='logform'),
    path('logusr/', views.logusr, name='logusr'),
    path('createusr/', views.createusr, name='createusr'),
    path('register/', views.register, name='registerform'),
    path('post/', views.post, name='postform'),
]