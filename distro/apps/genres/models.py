from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the genre.")

    def __str__(self):
        return self.name