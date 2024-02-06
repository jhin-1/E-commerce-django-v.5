from django.urls import path, include
from .brand import urls as brand_urls

urlpatterns = [
    path('brand/', include(brand_urls))
]