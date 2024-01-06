from django.urls import path, include
from .coding import urls as coding_urls


app_name = 'product'

urlpatterns = [
    path('dash/', include(coding_urls))

]
