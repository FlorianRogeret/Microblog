from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=30)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=30)

class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    object = forms.CharField(max_length=500)
