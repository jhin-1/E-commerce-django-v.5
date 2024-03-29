# Generated by Django 5.0 on 2024-02-18 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name  brand')),
                ('description', models.TextField(blank=True, max_length=100, null=True, verbose_name='description brand ')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': "brand's",
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name color')),
                ('code_color', models.CharField(blank=True, max_length=30, null=True, verbose_name='code color')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': "color's",
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name size')),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': "size's",
            },
        ),
        migrations.CreateModel(
            name='Var_Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='title main')),
            ],
            options={
                'verbose_name': 'Var_main',
                'verbose_name_plural': 'Var_main',
            },
        ),
        migrations.CreateModel(
            name='CustomizeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='name sub')),
                ('main', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.var_main', verbose_name='sub variation')),
            ],
            options={
                'verbose_name': 'Customize Variant',
                'verbose_name_plural': "Customize Variant's",
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.color')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.size')),
            ],
        ),
    ]
