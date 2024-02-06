from django.urls import path, include
from .Apis import urls_apis as apis_urls

urlpatterns = [
    path('apis/', include(apis_urls)),
]
