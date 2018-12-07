from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    #Allow the user to signup
    path('signup/',views.signup_view,name="signup"),
    #Allow the user to login
    path('login/',views.login_view, name="login"),
    #Allow the user to logout
    path('logout/',views.logout_view, name ="logout")
]