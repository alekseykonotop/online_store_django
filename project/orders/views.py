from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    errors = []
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clean()

                return render(request, 'order/created.html', {'errors': errors})
        else:
            errors.append('Для оформления заказа необходимо авторизоваться.')

        return render(request, 'cart/detail.html', {'errors': errors})



