from django.urls import path, include
from .product import urls as product_urls

urlpatterns = [
    path('product/', include(product_urls)),
]