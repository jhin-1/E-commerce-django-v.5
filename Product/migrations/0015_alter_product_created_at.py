# Generated by Django 5.0 on 2024-01-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0014_alter_product_cost_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
