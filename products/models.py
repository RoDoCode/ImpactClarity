from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


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

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    series_no = models.PositiveIntegerField(unique=True)
    categories = models.ManyToManyField(Category, related_name='series', blank=True,)

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
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(default="20 minutes", max_length=254, null=True, blank=True)
    series_no = models.ForeignKey("Series", on_delete=models.SET_NULL, null=True, verbose_name='Series Number')
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class CoachingToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    identifier_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    session = models.ForeignKey('CoachingSession', on_delete=models.SET_NULL, null=True, blank=True, related_name='tokens')

    def __str__(self):
        return f"{self.identifier_code} - {'Used' if self.is_used else 'Available'}"


class CoachingSession(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coaching_sessions')
    date_time = models.DateTimeField()
    topic = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.topic} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"