from django import forms
from .models import Recipe

CATEGORY_CHOICES = [
    ('Предястия', 'Предястия'),
    ('Супи', 'Супи'),
    ('Основни', 'Основни'),
    ('Десерти', 'Десерти'),
]

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'category', 'time', 'picture', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Наименование',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Наименование на ястието'",
                'required': True,
                'class': 'single-input'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Описание',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Описание на рецепата'",
                'required': True,
                'class': 'single-textarea'
            }),
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={
                'class': 'form-select',  # основен клас
                # Ако държиш да има и id="default-select":
                'id': 'default-select',
            }),
            'time': forms.NumberInput(attrs={
                'placeholder': 'time',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'time'",
                'required': True,
                'class': 'single-input'
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'hidden', 'id': 'id_picture',
            }),
            'attachment': forms.ClearableFileInput(attrs={
                'class': 'hidden', 'id': 'id_attachment',
            }),
        }
