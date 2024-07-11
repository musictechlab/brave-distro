from django.db import models
from django_countries.fields import CountryField

class Lyricist(models.Model):
    first_name = models.CharField(max_length=100, help_text="First name of the lyricist.")
    last_name = models.CharField(max_length=100, help_text="Last name of the lyricist.")
    birth_date = models.DateField(blank=True, null=True, help_text="Birth date of the lyricist.")
    nationality = CountryField(blank=True, null=True, help_text="Nationality of the lyricist.")
    biography = models.TextField(blank=True, null=True, help_text="Biography of the lyricist.")
    website = models.URLField(blank=True, null=True, help_text="Official website of the lyricist.")
    photo = models.ImageField(upload_to='lyricists/', blank=True, null=True, help_text="Photo of the lyricist.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Lyrics(models.Model):
    lyricist = models.ForeignKey('lyrics.Lyricist', blank=True, null=True, on_delete=models.CASCADE, related_name='lyrics', help_text="The lyricist who wrote the lyrics.")
    track = models.ForeignKey('tracks.Track', blank=True, null=True, on_delete=models.CASCADE, related_name='lyrics', help_text="The track associated with these lyrics.")
    content = models.TextField(help_text="The content of the lyrics.")
    language = CountryField(blank=True, null=True, help_text="The language of the lyrics.")

    def __str__(self):
        return f"Lyrics for {self.track}"