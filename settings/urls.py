from django.urls import path, include
from .coding import urls_coding as coding_urls


app_name = 'settings'

urlpatterns = [
    path('dash/', include(coding_urls))

]

