from django.urls import path
from .views import home
from django.contrib.auth import login

urlpatterns = [
    path('', home, name="home"),
    path('login', login,{'template_name':'login.html'}, name="login"),


]
