from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Usuario

def index(request):
    return render(request,"SLC/index.html")

def cadastro(request):
    return render(request,"SLC/register.html")

def usuarios(request):
    new_user = Usuario()
    new_user.usuario = request.POST.get('usuario')
    new_user.senha = request.POST.get('senha')
    new_user.save()

    return render(request,"SLC/register.html")