from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Category, Product, Article, Feedback
from .forms import FeedbackForm
from cart.forms import CartAddProductForm


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.filter(is_active=True)

        return context


def product_detail(request, pk):
    context = {}
    template_name = 'store/detail.html'
    product = get_object_or_404(Product, id=pk, available=True)
    context['product'] = product
    context['feedbacks'] = Feedback.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    context['cart_product_form'] = cart_product_form

    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        new_feedback = f.save(commit=False)
        new_feedback.product = Product.objects.get(pk=pk)
        new_feedback.save()

    context['form'] = FeedbackForm()

    if not request.session.get('reviewed_products', False):
        request.session["reviewed_products"] = [True]
        context['is_review_exist'] = False

        return render(request, template_name, context)

    if pk in request.session["reviewed_products"]:
        context['is_review_exist'] = True
    else:
        request.session["reviewed_products"] += [pk]
        context['is_review_exist'] = False

    return render(request, template_name, context)


class CategoryView(ListView):
    template_name = 'store/category.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form

        return context
