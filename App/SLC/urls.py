from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('usuarios', views.usuarios, name='listagem_usuarios')
]