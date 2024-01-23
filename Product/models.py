from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("product name"), blank=True, null=True)
    category = models.ForeignKey("SubCategory", on_delete=models.CASCADE, blank=True, null=True)
#  we put the Category in double "" to tell Django this class is after this class
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name=_("image product"))
    brand = models.ForeignKey("settings.Brand", on_delete=models.CASCADE, blank=True, null=True)
#  we import model form  another model by set the name of app and the class we want to related with him Like this(setting.Brand)
    description = models.TextField(max_length=100, verbose_name=_("product description"), blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name=_("product price"), blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=0, verbose_name=_("product cost"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = _('product')  # for the name of class in the admin site
        verbose_name_plural = _('product')

    def __str__(self):
        return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name of category")
#     cat_parent = models.ForeignKey('self', limit_choices_to={'cat_parent__isnull': True}, on_delete=models.CASCADE, blank=True, null=True)  # this relation is self relation
#     description = models.TextField(max_length=80, blank=True, null=True, verbose_name="description of category")
#     image = models.ImageField(upload_to="category/", blank=True, null=True, verbose_name="image of category")
#
#     class Meta:
#         verbose_name = _('category')  # for admin name of the class model
#         verbose_name_plural = _('categories')
#
#     def __str__(self):
#         return self.name
class MainCategory(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('name'))
    description = models.TextField(max_length=80, null=True, blank=True, verbose_name=_('description'))
    image = models.ImageField(upload_to="category/main", blank=True, null=True, verbose_name=_('image main category'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = _('main category')
        verbose_name_plural = _("main categories")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    main_category = models.OneToOneField(MainCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('sub category'))
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('name sub cat'))
    description = models.TextField(max_length=80, blank=True, null=True, verbose_name=_('description sub cat'))
    image = models.ImageField(upload_to="category/sub", blank=True, null=True, verbose_name=_('image sub cat'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = _("sub category")
        verbose_name_plural = _("sub categories")

    def __str__(self):
        return self.name


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
