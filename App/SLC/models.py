from django.db import models

from django.contrib.auth.models import User



    

class Itens(models.Model):

    texto = models.TextField(default='Sem itens')

class Lista(models.Model):

    titulo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Itens)
    
    def __str__(self):
        return self.titulo + ' - By: ' + self.user.username

