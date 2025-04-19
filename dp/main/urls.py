from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('recipes', views.recipes, name='recipes'),
    path('details', views.recipe_details, name='recipe_details'),
    path('new', views.recipe_create_or_edit, name='recipe_new'),
    path('edit/<int:pk>/', views.recipe_create_or_edit, name='recipe_edit'),
]
