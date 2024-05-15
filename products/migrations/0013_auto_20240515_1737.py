# Generated by Django 3.2.25 on 2024-05-15 17:37

from django.db import migrations, models
import urllib.request
from django.core.files import File
import os


def copy_urls_to_files(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    for product in Product.objects.all():
        if product.image_url:
            result = urllib.request.urlretrieve(product.image_url)
            product.image.save(
                os.path.basename(product.image_url),
                File(open(result[0], 'rb'))
            )
        if product.video_url:
            result = urllib.request.urlretrieve(product.video_url)
            product.video.save(
                os.path.basename(product.video_url),
                File(open(result[0], 'rb'))
            )
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20240514_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='product_videos/'),
        ),

        migrations.RunPython(copy_urls_to_files),
    ]
