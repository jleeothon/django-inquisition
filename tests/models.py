from django.db import models
from django.utils.text import slugify


from inquisition import SearchManager


__all__ = ['BikeSparePart']


class BikeSparePart(models.Model):

    COO_CHOICES = (
        ('CHN', 'China'),
        ('JPN', 'Japan'),
        ('TWN', 'Taiwan'),
        ('VNM', 'Vietnam'),
    )

    name = models.CharField(max_length=50, unique=True)
    coo = models.CharField(max_length=5, choices=COO_CHOICES)

    def save(self, *args, **kwargs):
        self.lookup = slugify(self.name)
        super(BikeSparePart, self).save(*args, **kwargs)

    objects = models.Manager()

    objects1 = SearchManager(search_fields=['name'],
                             search_order_fields=['name'])

    objects2 = SearchManager(search_fields=['name', 'coo'],
                             search_order_fields=['name'])
