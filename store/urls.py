from django.urls import path
from .views import ProductListView, Product, CategoryItemView, CategoryListView

urlpatterns = [
    path('api/store/', ProductListView.as_view(), name='store_home'),
    path('api/store/categories/', CategoryListView.as_view(), name='categories'),
    path('api/store/<slug:slug>/', Product.as_view(), name='product'),
    path('api/store/categories/<slug:slug>/',
         CategoryItemView.as_view(), name='category_item'),
]
