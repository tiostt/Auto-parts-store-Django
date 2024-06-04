from django.db import models


class Suppliers(models.Model):

    name = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='Название')

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Поставщика'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class Products(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    articul = models.CharField(max_length=100, blank=False, unique=True, null=False, verbose_name='Артикул')
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, verbose_name='Поставщик')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ("id",)

    def __str__(self):
        return self.name