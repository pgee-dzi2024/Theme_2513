from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe

# Изглед за начален екран
def index(request):
    recipes_list = Recipe.objects.all().order_by('-id')[:3]
    context = {'recipes':recipes_list}
    return render(request, 'main/index.html', context)

# Изглед за страница "Всички рецепти"
def recipes(request):
    recipes_list = Recipe.objects.all()
    context = {'recipes':recipes_list}
    return render(request, 'main/recipes.html', context)

# Изглед за страница "Рецепта"
def recipe_details(request,pk=None):
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
    else:
        recipe = None
    return render(request, 'main/recipes_details.html', {'recipe': recipe, })

# Изглед за страница "Нова рецепта"
def recipe_new(request):
    return render(request, 'main/recipes_new.html')

# Изглед за страница "Добави/промени рецепта"
def recipe_create_or_edit(request, pk=None):
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
    else:
        recipe = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            saved_recipe = form.save()  # запазваме записа
            # Пренасочваме към същия изглед (edit mode)
            return redirect('recipe_edit', pk=saved_recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'main/recipes_new.html', {
        'form': form,
        'recipe': recipe,  # това ти дава достъп до всички полета
    })