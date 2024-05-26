from django.urls import path
from .views import ListCategoryAPIView

urlpatterns = [
    path('category-list', ListCategoryAPIView.as_view(),name='category-list'),

]