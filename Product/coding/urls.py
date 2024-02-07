from django.urls import path, include
from .Apis import urls as api_product


urlpatterns = [
    path('apis/', include(api_product))
]
