from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    print(f'product ==> {product}')
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(f'quantity ==> {cd["quantity"]}, need_update ==> {cd["update"]}',)
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')


def cart_detail(request):
    context = {}
    context['cart'] = Cart(request)
    context['main_categories'] = Category.objects.filter(parent__isnull=True)

    return render(request, 'cart/detail.html', context)