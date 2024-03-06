from django.urls import path
from .varaint_apis import *

urlpatterns = [
    path('color/all', all_color),
    path('color/open', open_color),
    path('color/create', create_color),
    path('color/update', update_color),
    path('color/delete', delete_color),
    # # --------------------------------------------------------------------------------------
    path("size/all", all_size),
    path("size/open", open_size),
    path("size/create", create_size),
    path("size/update", update_size),
    path("size/delete", delete_size),
    # ----------------------------------------------------------------------------------------
    path('variant/all', all_variants),
    path('variant/open', open_variants),
    path('variant/create', create_variant),
    path('variant/update', update_variant),
    path('variant/delete', delete_variant),
    # path('variation/create', create_variant),
    # path('variation/update', update_variant),
    # path('variation/delete', delete_variant),

]