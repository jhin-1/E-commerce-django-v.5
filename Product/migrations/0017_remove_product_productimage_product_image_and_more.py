# Generated by Django 5.0 on 2024-01-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0016_remove_productimage_product_product_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productimage',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='image product'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]