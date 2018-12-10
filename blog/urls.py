from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    #Home page of the site
    path('', views.article_liste, name='index'),
    #Page that allow user to create a new article
    path('createarticle/',views.article_create, name='create'),
    #page that redirect to a specif article
    path('articledetail/<int:id>/',views.article_detail, name='detail'),

    path('authorarticle/<str:username>/',views.article_user, name='article_user'),

    path('deletearticle/<int:id>/',views.delete_article, name='delete'),

    path('updatearticle/<int:id>/',views.article_update, name='modifie'),

    path('doupdatearticle/<int:id>/',views.article_doupdate, name='domodifie'),
]

