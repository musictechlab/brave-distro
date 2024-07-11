from django.db import models
from django_countries.fields import CountryField
from django.conf import settings


class Partner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text="The user who made the change.")
    name = models.CharField(max_length=255, help_text="Name of the partner.")
    country = CountryField(blank=True, null=True, help_text="Country of the partner.")
    website = models.URLField(blank=True, null=True, help_text="Website of the partner.")
    email = models.EmailField(blank=True, null=True, help_text="Contact email of the partner.")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Contact phone number of the partner.")
    address = models.TextField(blank=True, null=True, help_text="Address of the partner.")
    description = models.TextField(blank=True, null=True, help_text="Description of the partner.")

    def __str__(self):
        return self.name