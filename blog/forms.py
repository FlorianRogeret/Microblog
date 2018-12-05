from django import forms
from . import models

class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    object = forms.CharField(max_length=500)
