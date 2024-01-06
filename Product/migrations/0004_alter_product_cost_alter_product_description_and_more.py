# Generated by Django 5.0 on 2024-01-02 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_product_cost_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='product cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='product description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='product price'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, max_length=80, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('cat_parent', models.ForeignKey(blank=True, limit_choices_to={'cat_parent_': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.category')),
            ],
        ),
    ]
