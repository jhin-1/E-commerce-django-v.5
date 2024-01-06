# Generated by Django 5.0 on 2023-12-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('cost', models.DecimalField(decimal_places=3, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
