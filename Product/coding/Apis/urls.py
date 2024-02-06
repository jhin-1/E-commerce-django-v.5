from django.urls import path, include
from .category import urls as category_urls
from .product import urls as product_urls

urlpatterns = [
    path('categories/', include(category_urls)),
    path('products/', include(product_urls)),
]