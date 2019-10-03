from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from .models import Category, Product, Article, Feedback
from .forms import FeedbackForm
from django.views import generic
from cart.forms import CartAddProductForm

# Create your views here.


class IndexView(TemplateView):
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


# def product_detail(request, product_id):
#     product = get_object_or_404(Product,
#                                 id=product_id,
#                                 available=True)
#
#     return render(request, 'store/detail.html', {'product': product})


class ProductDetailView(generic.DetailView):
    template_name = 'store/detail.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['main_categories'] = Category.objects.filter(parent__isnull=True)
        # object = self.get_object()
        product_id = Product.objects.get(pk=self.object.pk)
        print(f'self.object.pk ===> {self.object.pk}')
        context['feedbacks'] = Feedback.objects.filter(product=product_id)
        print(f'feedbacks ==> {context["feedbacks"]}')

        return context


class FeedbackAddView(FormView):
    template_name = 'store/detail.html'
    form_class = FeedbackForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['main_categories'] = Category.objects.filter(parent__isnull=True)
        context['feedbacks'] = Feedback.objects.filter(pk=self.object.cleaned_data['product'].pk)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)

        return self.object

    def get_success_url(self):

        return reverse('store:product_detail',
                       kwargs={'product_id': self.object.cleaned_data['product'].pk})




class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 10


class CategoryDetailView(generic.DetailView):
    model = Category


