from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    title = models.CharField(max_length=200)
    about_image = models.URLField(max_length=1024, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
