from django.urls import path, include
from .category import urls as category_urls

urlpatterns = [
    path('category/', include(category_urls))
]