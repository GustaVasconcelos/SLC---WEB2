from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('home', views.home, name='home' ),
    path('sair', views.sair, name='sair'),
]