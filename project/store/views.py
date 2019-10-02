from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.urls import reverse
from .models import Category, Product, Article
from .forms import FeedbackForm
from cart.forms import CartAddProductForm

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.filter(is_active=True)
        context['main_categories'] = Category.objects.filter(parent__isnull=True)

        return context


class ShowCategoryView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['articles'] = Article.objects.filter(is_active=True)

        return context


class ShowProductView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['articles'] = Article.objects.filter(is_active=True)

        return context


def product_detail(request, product_id):
    product = get_object_or_404(Product,
                                id=product_id,
                                available=True)

    return render(request, 'store/detail.html', {'product': product})


def FeedbackAddView(FormView):
    template_name = 'store/detail.html'
    form_class = FeedbackForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)

        return self.object

    def get_succes_url(self):

        return reverse('store:product_detail',
                       kwargs={'product_id': self.object.cleaned_data['product'].pk})
