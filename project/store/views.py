from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse
from .models import Category, Product, Article, Feedback
from .forms import FeedbackForm


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.filter(is_active=True)
        context['main_categories'] = Category.objects.filter(parent__isnull=True)

        return context


def product_detail(request, pk):
    context = {}
    template_name = 'store/detail.html'
    product = get_object_or_404(Product, id=pk, available=True)
    context['product'] = product
    context['main_categories'] = Category.objects.filter(parent__isnull=True)
    context['feedbacks'] = Feedback.objects.filter(product=product)

    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        new_feedback = f.save(commit=False)
        new_feedback.product = Product.objects.get(pk=pk)
        new_feedback.save()

    context['form'] = FeedbackForm()

    return render(request, template_name, context)


class CategoryView(ListView):
    template_name = 'store/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['main_categories'] = Category.objects.filter(parent__isnull=True)

        return context
