from django.urls import path

from app_products.views import ProductDetailView, ProductListView

app_name = "orders"

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='list'),
]