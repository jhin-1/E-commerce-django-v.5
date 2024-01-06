from django.urls import path, include
from .api_product import urls as api_product


urlpatterns = [
    path('api/', include(api_product))
]
