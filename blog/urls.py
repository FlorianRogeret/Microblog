from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    #Home page of the site
    path('', views.article_liste, name='index'),
    #Page that allow user to create a new article
    path('create/',views.article_create, name='create'),
    #page that redirect to a specif article
    path('<slug>[\w]+)/',views.article_detail, name='detail'),
    #Allow the user to delete an article
    path('delete/',views.delete_view, name="delete"),
    #Allow the user to modifie an article
    path ('modifie/', views.modifie_view, name="modifie")
]

