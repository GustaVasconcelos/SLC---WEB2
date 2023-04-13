from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('home', views.home, name='home' ),
    path('sair', views.sair, name='sair'),
    path('criando/lista', views.criando_lista, name='criando_lista'),
    path('deletando/lista', views.deletar_tarefa, name='deletando_lista'),
    path('adicionando/lista', views.adicionar_lista, name='adicionando_lista'),
    path('deletar/item', views.deletar_item, name='deletar_item')
]