# valuables/models.py
from django.db import models


class Valuable(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='cover_images/')
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
