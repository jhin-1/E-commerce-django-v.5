# Generated by Django 5.0 on 2024-02-18 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_remove_product_price_remove_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
