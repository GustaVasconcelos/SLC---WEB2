from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import ListaForm
from .models import Lista




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
    lista = Lista.objects.filter(user=request.user) 
    return render(request, 'SLC/home.html', { 'lista' : lista })
    

@login_required
def criando_lista(request):

    if request.method == 'GET':
        return render(request, 'SLC/home.html',{
            'form':ListaForm
        })
    
    else:

        try:
            form = ListaForm(request.POST)

            nova_lista = form.save(commit=False)

            nova_lista.user = request.user

            nova_lista.save()

            return redirect('home')
        except ValueError:

            return render(request,'SLC/home.html', {
                'form' : ListaForm,
                'error' : 'Favor inserir dados validos'
            })     
        
@login_required  
def deletar_tarefa(request):
    lista = get_object_or_404(Lista, pk=request.POST['id'], user=request.user)

    if request.method == 'POST':
        lista.delete()
        return redirect('home')