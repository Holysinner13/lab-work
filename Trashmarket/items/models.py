from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Items(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(upload_to='items_images', blank=True, null=True, verbose_name='Картинка')
    is_sold = models.BooleanField(default=False, verbose_name='Продано')
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, verbose_name='Создано')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
