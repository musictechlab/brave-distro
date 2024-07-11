from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the platform.")
    description = models.TextField(blank=True, null=True, help_text="A brief description of the platform. Optional.")

    def __str__(self):
        return self.name