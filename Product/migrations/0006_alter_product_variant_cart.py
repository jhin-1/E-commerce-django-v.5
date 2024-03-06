# Generated by Django 5.0 on 2024-03-03 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_product_price_product_quantity'),
        ('settings', '0007_imagevariant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.ManyToManyField(blank=True, null=True, to='settings.variant', verbose_name='variant of product'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='Pro_cart')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': "Cart's",
            },
        ),
    ]