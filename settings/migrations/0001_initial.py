# Generated by Django 5.0 on 2024-01-03 20:02

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
            name='variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name  variant')),
                ('description', models.TextField(blank=True, max_length=100, null=True, verbose_name='description variant')),
            ],
            options={
                'verbose_name': 'variant',
                'verbose_name_plural': "variant's",
            },
        ),
    ]