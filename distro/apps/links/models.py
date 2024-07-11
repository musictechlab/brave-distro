from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=255, help_text="The title of the link.")
    help_text = models.CharField(max_length=255, blank=True, null=True, help_text="Additional help text for the link. Optional.")
    font_icon = models.CharField(max_length=255, blank=True, null=True, help_text="CSS class for the font icon associated with the link. Optional.")

    def __str__(self):
        return self.title