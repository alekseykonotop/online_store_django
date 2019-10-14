from django.urls import path
from .views import IndexView, product_detail, CategoryView

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('category/<int:pk>', CategoryView.as_view(), name='category_detail'),
    # path('categories/', CategoryListView.as_view(), name='categories'),

]
