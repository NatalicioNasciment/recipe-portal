from django.urls import path
from . import views

app_name='recipes'

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('sobre/', views.sobre),
    path('contatos/', views.contatos),
    path('recipes/category/<int:category_id>', views.category, name='category'),
    path('recipes/<int:id>', views.recipe, name='recipes-recipe'),


]
