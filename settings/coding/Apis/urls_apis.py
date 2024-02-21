from django.urls import path, include
from .brand import urls as brand_urls
from .varations import urls as var_urls
urlpatterns = [
    path('brand/', include(brand_urls)),
    path('variant/', include(var_urls))
]