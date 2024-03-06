import django_filters
from django.db import models
from django.utils.translation import gettext as _
from .image_urls import *
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("product name"), blank=True, null=True)
    category = models.ForeignKey("Subcategory", on_delete=models.CASCADE, blank=True, null=True)
#  we put the Category in double "" to tell Django this class is after this class
    brand = models.ForeignKey("settings.Brand", on_delete=models.CASCADE, blank=True, null=True)
#  we import model form  another model by set the name of app and the class we want to related with him Like this(setting.Brand)
    description = models.TextField(max_length=100, verbose_name=_("product description"), blank=True, null=True)
    variant = models.ManyToManyField("settings.Variant", blank=True, null=True, verbose_name=_("variant of product"))
    customize = models.ForeignKey("settings.CustomizeVariant", on_delete=models.CASCADE, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=0, verbose_name=_("product cost"), blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True, verbose_name="price of product")
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name="quantity of product")
    image = models.ImageField(upload_to=get_product, null=True, blank=True, verbose_name=" product image ")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = _("product's")
        verbose_name = _('product')  # for admin name of the class model

    def __str__(self):
        return self.name


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "name": ["exact"],
            "description": ["exact"],
            "cost": ["exact"],
        }


# class ProductImage(models.Model):
#     # that's means The product have many images relationship 1:M
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)  # cascade if delete product will delete all images
#     productImage = models.ImageField(upload_to="products/", verbose_name="product Image")
#
#     def __str__(self):
#         return str(self.product)  # لقد تم استخدام استرينح لانه يحمل قيمه انتيجر
class MainCategoryModel(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name of category")
    description = models.TextField(max_length=80, blank=True, null=True, verbose_name="description of category")
    image = models.ImageField(upload_to=get_main_category, blank=True, null=True, verbose_name="image of category")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = _(' main category')  # for admin name of the class model
        verbose_name_plural = _('main categories')

    def __str__(self):
        return self.name


class MainCategoryModelFilter(django_filters.FilterSet):
    class Meta:
        model = MainCategoryModel
        fields = {
            "name": ["exact"],
            "description": ["exact"],
        }


class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategoryModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name="main category")
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name of category")
    description = models.TextField(max_length=80, blank=True, null=True, verbose_name="description of category")
    image = models.ImageField(upload_to=get_sub_category, blank=True, null=True, verbose_name="image of category")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = _('sub category')  # for admin name of the class model
        verbose_name_plural = _(' sub categories')

    def __str__(self):
        return self.name


class SubCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = SubCategory
        fields = {
            "name": ["exact"],
            "description": ["exact"],
        }


class Product_Alternative(models.Model):   # بدائل المنتج
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="main_product")
    alternative_product = models.ManyToManyField(Product, related_name="alternative_products", verbose_name="Alternative")

    class Meta:
        verbose_name = _('Product_Alternative')  # for admin name of the class model
        verbose_name_plural = _('Product_Alternatives')

    def __str__(self):
        return str(self.product)


class Product_Accessories(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="mainAccessory_product")
    accessories_product = models.ManyToManyField(Product, related_name="accessories_products", verbose_name="Accessories")

    class Meta:
        verbose_name = _('Product_Accessory')  # for admin name of the class model
        verbose_name_plural = _('Product_Accessories')

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Pro_cart", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _("Cart's")

    def __str__(self):
        return self.product.name
