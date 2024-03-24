from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name' : 'Natalicio Nascimento' 
    })

def sobre(request):
    return HttpResponse('Seção sobre')

def contatos(request):
    return HttpResponse('Seção contatos')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name' : 'Natalicio Nascimento' 
    })