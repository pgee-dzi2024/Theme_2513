from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def recipes(request):
    return render(request, 'main/recipes.html')

def recipe_details(request):
    return render(request, 'main/recipes_details.html')

def recipe_new(request):
    return render(request, 'main/recipes_new.html')

from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe

def recipe_create_or_edit(request, pk=None):
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
    else:
        recipe = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')  # или друга подходяща страница
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'main/recipes_new.html', {'form': form, 'recipe': recipe})