from django.urls import path
from .views import HomePageView, ShowCategoryView, ShowProductView, product_detail

app_name = 'store'

urlpatterns = [
    path('', HomePageView.as_view()),
    path('store/products/detail/<product_id>', product_detail, name='product_detail'),

]
