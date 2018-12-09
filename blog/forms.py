from django import forms
from . import models

# Form to create a new article using the needed fields (title,body) findable in the models.py 
class CreateArticles(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body']

class EditArticles(forms.Form):
    def __init__(self,*args,**kwargs):
        title = Article.objects.filter(id=id).values_list('title', flat=True)
        body = Article.objects.filter(id=id).values_list('body', flat=True)
        #title = kwargs.pop("title")
        #body = kwargs.pop("body")
 
        super(EditArticles, self).__init__(*args,**kwargs)
        self.fields['title'] = forms.CharField(max_length=100, initial=title)
        self.fields['body'] = forms.CharField(initial=body)