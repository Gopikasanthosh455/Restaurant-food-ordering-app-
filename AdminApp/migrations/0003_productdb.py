# Generated by Django 5.1.4 on 2025-01-02 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_rename_name_categorydb_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='productDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Product_image', models.ImageField(blank=True, null=True, upload_to='Product')),
            ],
        ),
    ]
