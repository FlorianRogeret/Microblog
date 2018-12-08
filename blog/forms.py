from django import forms
from . import models

# Form to create a new article using the needed fields (title,body) findable in the models.py 
class CreateArticles(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body']
