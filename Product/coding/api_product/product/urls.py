from django.urls import path
from .Apis_code import *


urlpatterns = [
    path('all', all_api),
    path('open', open_api),
    path('create', create_api),
]
