from django.urls import path
from .views import HomePageView, ShowCategoryView, ShowProductView

urlpatterns = [
    path('', HomePageView.as_view()),

]
