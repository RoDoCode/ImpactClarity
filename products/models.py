from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Series(models.Model):

    class Meta:
        verbose_name_plural = 'Series'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=34.99)
    series_no = models.PositiveIntegerField(unique=True)
    categories = models.ManyToManyField(
        Category,
        related_name='series',
        blank=True,
    )
    video = models.FileField(
        upload_to='series_videos/',
        null=True,
        blank=True
    )
    screenshot_1 = models.ImageField(
        upload_to='series_screenshots/',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='series_images/',
        null=True,
        blank=True
    )

    def count_products(self):
        return self.product_set.count()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(
        default="20 minutes",
        max_length=254,
        null=True,
        blank=True
    )
    series_no = models.ForeignKey(
        "Series",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Series Number'
    )
    image = models.ImageField(
        upload_to='product_images/',
        null=True,
        blank=True
    )
    video = models.FileField(
        upload_to='product_videos/',
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
