# Generated by Django 5.1.4 on 2025-02-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_cartdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdb',
            name='Product_image',
            field=models.ImageField(blank=True, null=True, upload_to='Cart'),
        ),
    ]
