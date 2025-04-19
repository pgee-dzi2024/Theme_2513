from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('recipes', views.recipes, name='recipes'),
    path('details/<int:pk>/', views.recipe_details, name='recipe_details'),

    path('recipes/new/', views.recipe_create_or_edit, name='recipe_create'),
    path('recipes/<int:pk>/edit/', views.recipe_create_or_edit, name='recipe_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)