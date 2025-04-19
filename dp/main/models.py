from django.db import models

class Recipe(models.Model):
    title = models.CharField('Наименование:', max_length=200)
    description = models.TextField('Описание/текст')
    time = models.IntegerField('Време за приготвяне', default=10)
    category = models.CharField('Категория', max_length=100, default='')
    picture = models.ImageField('Снимка:', upload_to='pictures/')
    attachment = models.FileField('Файл', upload_to='files/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепта'
        verbose_name_plural = 'Рецепти'
