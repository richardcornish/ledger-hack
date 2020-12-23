from django.db import models
from django.urls import reverse

from hashid_field import HashidAutoField


class Victim(models.Model):
    reference_id = HashidAutoField(verbose_name='reference ID', primary_key=True)
    email = models.EmailField('e-mail address', unique=True)
    name = models.CharField(blank=True, max_length=254)
    address_1 = models.CharField(blank=True, max_length=254)
    address_2 = models.CharField(blank=True, max_length=254)
    country = models.CharField(blank=True, max_length=254)
    phone = models.CharField(blank=True, max_length=254)
    newsletter = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return '%s' % self.email

    def get_absolute_url(self):
        return reverse('victims:detail', args=[str(self.reference_id)])
