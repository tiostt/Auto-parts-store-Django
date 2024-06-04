from django.db import models

from catalog.models import Products
from users.models import User

# это не таблица базы данных
class BasketQueryset(models.QuerySet):
     
    def total_price(self):
        return sum(float(basket.product_price()) for basket in self)

    def total_quantity(self):
        if self:
            return sum(basket.quantity for basket in self)
        
        return 0

# это таблица под корзину
class Basket(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'basket'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    objects = BasketQueryset().as_manager()

    def product_price(self):
        if self.quantity >= 10:
            return round((int(self.product.price * self.quantity) * 0.8), 2)

        return round((self.product.price * self.quantity), 2)
    

    def __str__(self):
        return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
