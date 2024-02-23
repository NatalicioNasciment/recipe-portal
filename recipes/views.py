from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name' : 'Natalicio Nascimento' 
    })

def sobre(request):
    return HttpResponse('Seção sobre')

def contatos(request):
    return HttpResponse('Seção contatos')