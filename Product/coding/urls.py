from django.urls import path, include
from .api_product import urls as api_product
from .api_category import urls as api_category

urlpatterns = [
    path('api/', include(api_product)),
    path('api/', include(api_category)),
]
