from django.urls import path
from .Apis_code import *

urlpatterns = [
    path('main-category/all', all_category),
    path('main-category/open', opem_m_category),
    path('main-category/create', create_m_category),
    path('main-category/update', update_m_category),
    path('main-category/delete', delete_m_category),
    path('sub-category/all', all_s_category),
    path('sub-category/open', open_s_category),
    path('sub-category/create', create_s_category),
    path('sub-category/update', update_s_category),
    path('sub-category/delete', delete_s_category),

]
