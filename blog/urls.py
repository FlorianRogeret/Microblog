from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_liste, name='list'),
    path('(?P<slug>[\w]+)/$',views.article_detail, name='detail'),
]

