from django.db import models
from django_countries.fields import CountryField

class Album(models.Model):
    title = models.CharField(max_length=255, help_text="The title of the album.")
    release_date = models.DateField(blank=True, null=True, help_text="The release date of the album. Can be left blank if unknown.")
    genres = models.ManyToManyField('genres.Genre', related_name='related_albums', help_text="Genres associated with the album.")
    artists = models.ManyToManyField('artists.Artist', related_name='related_albums', help_text="Artists who performed in the album.")
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True, help_text="Cover image of the album. Optional.")
    label = models.ForeignKey('labels.Label', on_delete=models.CASCADE, related_name='related_albums', help_text="The record label that released the album.")
    description = models.TextField(blank=True, null=True, help_text="A brief description of the album. Optional.")
    country = CountryField(blank=True, null=True, help_text="The country where the album was produced or released.")

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['title']

    def __str__(self):
        return self.title