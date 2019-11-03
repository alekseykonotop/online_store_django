from django.db import models
from store.models import Product
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='orders', verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_count(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='order_items',
                                verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Колличество')

    class Meta:
        ordering = ('product',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
