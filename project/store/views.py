from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Category, Product, Article

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['articles'] = Article.objects.filter(is_active=True)

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
