# Generated by Django 3.2 on 2021-05-11 21:12

from django.db import migrations, models
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.FileField(blank=True, null=True, storage=products.storages.ProtectedStorage, upload_to='products/'),
        ),
    ]
