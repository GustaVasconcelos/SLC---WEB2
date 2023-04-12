from django.db import models

from django.contrib.auth.models import User

class Lista(models.Model):

    titulo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - By: ' + self.user.usuario

