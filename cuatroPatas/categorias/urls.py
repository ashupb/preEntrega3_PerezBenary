from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('collares/', collares, name="collares"),
    path('alimentacion/', alimentacion, name="alimentacion"),
    path('confort/', confort, name="confort"),

    path('collaresForm/', collaresForm, name="collaresForm"),
    path('alimentacionForm/', alimentacionForm, name="alimentacionForm"),
    path('confortForm/', confortForm, name="confortForm"),

    path('buscarConfort/', buscarConfort, name="buscarConfort"),
    path('encontrarConfort/', encontrarConfort, name="encontrarConfort"),
]