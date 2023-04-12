from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




def index(request):

    if request.method == 'GET':
        return render(request,'SLC/index.html', {
        'form': AuthenticationForm
        })

    else:
        user = authenticate(

            request, username=request.POST['usuario'], password=request.POST['senha'])

        if user is None:
            return render(request, 'SLC/index.html', {
                    'form' : AuthenticationForm,
                    'error': 'Usuário ou senha está incorreto'
                })

        else:
                login(request, user)
                return redirect('home')    

def cadastro(request):
    if request.method == 'GET':

        return render(request,'SLC/register.html', {
            'form' : UserCreationForm
        } )   

    else: 
        if request.POST['senha'] == request.POST['senha2']:

            try: 
                
                user = User.objects.create_user(username=request.POST['usuario'], password=request.POST['senha'])
                user.save()
                
                login(request, user)
               
                return redirect('home')
                
            except:
                return render (request,'SLC/register.html', { 
                    'form' : UserCreationForm ,
                    "error": 'Usuário já existe'
                    
                    } ) 
           
        return render (request,'SLC/register.html', { 
                    'form' : UserCreationForm ,
                    "error": 'as senhas são diferentes'
                    
                    } ) 
    
@login_required   
def sair(request):
    logout (request)
    return redirect('/')

@login_required
def home(request):

    return render(request, 'SLC/home.html')