from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)  # to be register the models to admin site
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
