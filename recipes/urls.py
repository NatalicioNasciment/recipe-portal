from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
    path('contatos/', views.contatos),
    path('recipes/<int:id>', views.recipe),

]
