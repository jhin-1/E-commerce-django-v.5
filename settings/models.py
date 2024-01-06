from django.db import models
from django.utils.translation import gettext as _


# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name  brand")
    description = models.TextField(max_length=100, blank=True, null=True, verbose_name="description brand ")

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brand's")

    def __str__(self):
        return self.name


class Variant(models.Model):  # the is model of variation
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="name  variant")
    description = models.TextField(max_length=100, blank=True, null=True, verbose_name="description variant")

    class Meta:
        verbose_name = _("variant")
        verbose_name_plural = _("variant's")

    def __str__(self):
        return self.name
