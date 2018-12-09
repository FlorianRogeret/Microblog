from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    #Home page of the site
    path('', views.article_liste, name='index'),
    #Page that allow user to create a new article
    path('createarticle/',views.article_create, name='create'),
    #page that redirect to a specif article
    path('articledetail/<id>/',views.article_detail, name='detail'),

    path('authorarticle/<author>/',views.article_user, name='article_user'),

    path('deletearticle/<id><author>/',views.delete_article, name='delete'),

    path('updatearticle/<author><title><body>/',views.article_update, name='modifie'),
]

