from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="The name of the recording label.")
    founded_date = models.DateField(help_text="The date when the recording label was founded.")
    founder = models.CharField(max_length=255, help_text="The name of the founder of the recording label.")
    country = models.CharField(max_length=100, help_text="The country where the recording label is based.")
    city = models.CharField(max_length=100, help_text="The city where the recording label is based.")
    website = models.URLField(blank=True, null=True, help_text="The official website of the recording label. Optional.")
    email = models.EmailField(blank=True, null=True, help_text="Contact email of the recording label. Optional.")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Contact phone number of the recording label. Optional.")

    class Meta:
        verbose_name = 'Recording Label'
        verbose_name_plural = 'Recording Labels'
        ordering = ['name']

    def __str__(self):
        return self.name