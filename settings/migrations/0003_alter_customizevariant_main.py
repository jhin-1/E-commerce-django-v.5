# Generated by Django 5.0 on 2024-02-18 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_customizevariant_main_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizevariant',
            name='main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.var_main', verbose_name='var_main'),
        ),
    ]