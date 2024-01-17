# Generated by Django 5.0 on 2024-01-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0011_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='product price'),
        ),
    ]
