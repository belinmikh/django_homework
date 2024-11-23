from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to='catalog/images',
        blank=True, null=True,
        verbose_name='Изображение'
    )
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='products'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at']

    def __str__(self):
        return f'{self.name}: {self.price}'
