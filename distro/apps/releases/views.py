from django.db import models
from django_countries.fields import CountryField


class Release(models.Model):
    album_id = models.CharField(max_length=100, help_text="The ID of the album.")
    history_id = models.IntegerField(default=0, help_text="The history ID of the release.")
    album_status_field = models.IntegerField(default=3, help_text="Status field of the album.")
    partner_id = models.IntegerField(help_text="ID of the partner.")
    valid_product_format = models.BooleanField(default=True, help_text="Indicates if the product format is valid.")
    
    subscription_plan_id = models.CharField(max_length=100, help_text="The subscription plan ID for this release.")
    product_type = models.CharField(max_length=50, help_text="Type of the release.")
    is_dolby_atmos = models.BooleanField(default=False, help_text="Indicates if the release is in Dolby Atmos format.")
    product_title = models.CharField(max_length=250, help_text="Title of the release.")
    content_supplier_id = models.CharField(max_length=100, help_text="ID of the content supplier (label name).")
    product_id_type = models.CharField(max_length=50, help_text="ID type (EAN/UPC) for the stereo release.")
    product_id = models.CharField(max_length=13, help_text="Product ID (EAN/UPC) for the stereo release.")
    dolby_product_id_type = models.CharField(max_length=50, blank=True, null=True, help_text="ID type (EAN/UPC) for the Dolby Atmos release.")
    dolby_product_id = models.CharField(max_length=13, blank=True, null=True, help_text="Product ID (EAN/UPC) for the Dolby Atmos release.")
    sony_product_id_type = models.CharField(max_length=50, blank=True, null=True, help_text="ID type (EAN/UPC) for the 360RA release.")
    sony_product_id = models.CharField(max_length=13, blank=True, null=True, help_text="Product ID (EAN/UPC) for the 360RA release.")
    date_original_release = models.DateField(help_text="Original release date.")

    def __str__(self):
        return self.product_title