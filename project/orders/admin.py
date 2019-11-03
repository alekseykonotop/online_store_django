from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_total_sum', 'get_items_count', 'created', ]
    list_filter = ['created', ]
    inlines = [OrderItemInline]

    def get_items_count(self, order):
        return f'{order.items.count()}'

    get_items_count.short_description = 'Колличество позиций, шт.'

    def get_total_sum(self, order):
        return sum([item.price * item.quantity for item in order.items.all()])

    get_total_sum.short_description = 'Сумма заказа, руб.'


admin.site.register(Order, OrderAdmin)
