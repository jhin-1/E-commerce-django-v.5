from django.urls import path
from .Apis_code import *


urlpatterns = [
    path('all', all_product),
    path('open', open_product),
    path('create', create_product),
    path('update', update_product),
    path('delete', delete_product),

]
