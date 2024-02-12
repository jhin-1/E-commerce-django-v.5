from django.db import models
from django.utils.translation import gettext as _


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


class Color(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True, verbose_name="color")
    code_color = models.CharField(max_length=30, blank=True, null=True, verbose_name="code color")

    objects = models.Manager()

    class Meta:
        verbose_name = _("color")
        verbose_name_plural = _("color's")

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True, verbose_name="size name")

    objects = models.Manager()

    class Meta:
        verbose_name = _("size")
        verbose_name_plural = _("size's")

    def __str__(self):
        return self.title


class Quantity(models.Model):
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantity number")

    objects = models.Manager()

    class Meta:
        verbose_name = _("quantity")
        verbose_name_plural = _("quantity's")


class variant(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="variants_color")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="variants_size")
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE, related_name="variants_quantity")

    objects = models.Manager()

    class Meta:
        verbose_name = _('variant')
        verbose_name_plural = _('variants')
