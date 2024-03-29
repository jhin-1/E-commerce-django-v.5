# Generated by Django 5.0 on 2024-02-18 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_customizevariant_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.color', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.size', verbose_name='size'),
        ),
    ]
