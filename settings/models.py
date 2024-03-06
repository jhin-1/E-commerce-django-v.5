from django.db import models
from django.utils.translation import gettext as _
from .var_image import *

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name  brand")
    description = models.TextField(max_length=100, blank=True, null=True, verbose_name="description brand ")

    objects = models.Manager()

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brand's")

    def __str__(self):
        return self.name


# class Variant(models.Model):  # the is model of variation
#     name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name variant")
#     units = models.IntegerField(blank=True, null=True)
#     UN_price = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
#
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = _("variant")
#         verbose_name_plural = _("variant's")
#
#     def __str__(self):
#         return self.name


# class Color(models.Model):
#     title = models.CharField(max_length=30, unique=True, blank=True, verbose_name="color")
#     code_color = models.CharField(max_length=30, unique=True, blank=True, null=True, verbose_name="code color")
#
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = _("color")
#         verbose_name_plural = _("color's")
#
#     def __str__(self):
#         return self.title
#
#
# class Size(models.Model):
#     title = models.CharField(max_length=30, unique=True, blank=True, null=True, verbose_name="size name")
#
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = _("size")
#         verbose_name_plural = _("size's")
#
#     def __str__(self):
#         return self.title


# class Quantity(models.Model):
#     quantity = models.IntegerField(unique=True, blank=True, null=True, verbose_name="quantity number")
#
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = _("quantity")
#         verbose_name_plural = _("quantity's")


# class Variant(models.Model):
#     color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True, related_name="variants_color")
#     size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True, related_name="variants_size")
#     quantity = models.PositiveIntegerField(null=True, blank=True)
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return str(self.color)
#
#     class Meta:
#         verbose_name = _('variant')
#         verbose_name_plural = _('variants')

class Var_Main(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True, verbose_name="title main")

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Var_main')
        verbose_name_plural = _("Var_main")


class CustomizeVariant(models.Model):
    main = models.ForeignKey(Var_Main, on_delete=models.CASCADE, null=True, blank=True, verbose_name="var_main")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="name_sub")
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Customize Variant')
        verbose_name_plural = _("Customize Variant's")


class Color(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name color")
    code_color = models.CharField(max_length=30, blank=True, null=True, verbose_name="code color")
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _("color's")


class Size(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name size")
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _("size's")


class ImageVariant(models.Model):
    image = models.ImageField(upload_to=get_image, null=True, blank=True, verbose_name="image variant")
    objects = models.Manager()

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = _('image variant')
        verbose_name_plural = _('image variants')


class Variant(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True, verbose_name="color")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True, verbose_name="size")
    quantity = models.IntegerField(null=True, blank=True, verbose_name="quantity")
    price = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True, verbose_name="price of variant")
    objects = models.Manager()

    def __str__(self):
        return self.color.name + " " + self.size.name + " " + str(self.quantity) + " " + str(self.price)



