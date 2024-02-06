from django.urls import path
from .Apis_brand import *

urlpatterns = [
    path('all', all_),
    path('open', open_brand),
    path('create', create_brand),
    path('delete', delete_brand),
]
