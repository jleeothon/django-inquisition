from django.db import models
from django.utils.text import slugify


__all__ = ['BikeSparePart']


class BikeSparePart(models.Model):

    name = models.CharField(max_length=50, unique=True)
    lookup = models.SlugField()

    def save(self, *args, **kwargs):
        self.lookup = slugify(self.name)
        super(BikeSparePart, self).save(*args, **kwargs)
