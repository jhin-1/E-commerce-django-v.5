from django.urls import path
from .Apis_code import *


urlpatterns = [
    path('all', All_api),
    path('open', open_api),
]
