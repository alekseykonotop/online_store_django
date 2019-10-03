from django.urls import path
# from .views import IndexView, ProductDetalView, CategoryListView, CategoryDetailView, ProductDetailAndFeedbackView
from .views import IndexView, ProductDetailView, FeedbackAddView, CategoryListView, CategoryDetailView

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/add_feedback/', FeedbackAddView.as_view(), name='add_feedback'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
]
