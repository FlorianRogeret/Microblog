from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    #Home page of the site
    path('', views.article_liste, name='index'),
    #Page that allow user to create a new article
    path('create/',views.article_create, name='create'),
    #page that redirect to a specif article
    path(r'<id>[\w]+)/',views.article_detail, name='detail'),

    path(r'<author>[\w]+)/',views.article_user, name='article_user'),

    path('delete/',views.delete_article, name='delete')
]

