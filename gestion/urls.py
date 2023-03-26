from django.urls import path
from .views import home, inscripcion_encuentro, home_encuentro
# from django.contrib.auth import login

urlpatterns = [
    path('', home, name="home"),
    path('encuentro-brigada', home_encuentro , name="home_encuentro"),
    path('encuentro-brigada/inscripcion', inscripcion_encuentro , name="inscripcion_encuentro"),


]
