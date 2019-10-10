from django.urls import path
from .views import IndexView, product_detail

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    # path('categories/', CategoryListView.as_view(), name='categories'),
    # path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
]
