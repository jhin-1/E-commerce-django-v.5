# Generated by Django 5.0 on 2024-02-01 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0022_rename_maincategory_maincategorymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.maincategorymodel', verbose_name='main category'),
        ),
    ]