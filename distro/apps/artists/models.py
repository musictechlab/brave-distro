from django.db import models
from django_countries.fields import CountryField

class Artist(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the artist.")
    birth_date = models.DateField(blank=True, null=True, help_text="The birth date of the artist. Can be left blank if unknown.")
    genres = models.ManyToManyField('genres.Genre', related_name='artists', help_text="Genres associated with the artist.")
    ipi_code = models.CharField(max_length=11, unique=True, blank=True, null=True, help_text="International Standard Musical Work Code (IPI). Usually 11 characters.")
    isni_code = models.CharField(max_length=16, unique=True, blank=True, null=True, help_text="International Standard Name Identifier (ISNI). 16 characters.")
    pro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Performing Rights Organization", help_text="Performing Rights Organization the artist is affiliated with.")
    recording_label = models.ForeignKey('labels.Label', on_delete=models.CASCADE, related_name='artists', help_text="The record label the artist is signed to.")
    country = CountryField(blank=True, null=True, help_text="The country where the artist is based.")
    city = models.CharField(max_length=100, blank=True, null=True, help_text="The city where the artist is based.")
    website = models.URLField(blank=True, null=True, help_text="The official website of the artist.")
    email = models.EmailField(blank=True, null=True, help_text="Contact email of the artist.")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Contact phone number of the artist.")
    contact_number = models.CharField(max_length=20, blank=True, null=True, help_text="Alternative contact number for the artist.")
    bio_description = models.TextField(blank=True, null=True, help_text="A brief biography of the artist.")
    background_color = models.CharField(max_length=7, blank=True, null=True, help_text="Background color for the artist's profile (Hex color code).")
    background_image = models.ImageField(upload_to='artist_backgrounds/', blank=True, null=True, help_text="Background image for the artist's profile.")

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
        ordering = ['name']

    def __str__(self):
        return self.name

class ArtistLink(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='links', help_text="The artist associated with this link.")
    link = models.ForeignKey('links.Link', on_delete=models.CASCADE, help_text="The link type (e.g., social media, website).")
    url = models.URLField(help_text="The URL of the link.")

    def __str__(self):
        return f"{self.artist.name} - {self.link.title}"