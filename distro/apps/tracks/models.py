from django.db import models
from django_countries.fields import CountryField


class Track(models.Model):
    TITLE_MAX_LENGTH = 255
    ISRC_MAX_LENGTH = 12
    ISWC_MAX_LENGTH = 11

    PARENTAL_ADVISORY_CHOICES = [
        ('N', 'None'),
        ('E', 'Explicit'),
        ('C', 'Clean')
    ]

    AVAILABILITY_CHOICES = [
        ('D', 'Download'),
        ('S', 'Stream')
    ]

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH, 
        help_text="The name of the track."
    )
    isrc = models.CharField(
        max_length=ISRC_MAX_LENGTH, 
        unique=True, 
        help_text="International Standard Recording Code."
    )
    artists = models.ManyToManyField(
        'artists.Artist', 
        related_name='tracks', 
        help_text="Artists who performed the track."
    )
    featured_artists = models.ManyToManyField(
        'artists.Artist', 
        related_name='featured_tracks', 
        blank=True, 
        help_text="Artists who are featured in the track."
    )
    genres = models.ManyToManyField(
        'genres.Genre', 
        related_name='tracks', 
        help_text="Genres associated with the track."
    )
    iswc = models.CharField(
        max_length=ISWC_MAX_LENGTH, 
        blank=True, 
        null=True, 
        help_text="International Standard Musical Work Code."
    )
    language = models.CharField(
        max_length=2, 
        blank=True, 
        null=True, 
        help_text="Language of the track, represented by ISO code."
    )
    parental_advisory = models.CharField(
        max_length=1, 
        choices=PARENTAL_ADVISORY_CHOICES, 
        default='N', 
        help_text="Parental advisory status."
    )
    available_for = models.CharField(
        max_length=1, 
        choices=AVAILABILITY_CHOICES, 
        default='S', 
        help_text="Availability of the track for download or streaming."
    )
    file = models.FileField(
        upload_to='tracks/', 
        blank=True, 
        null=True, 
        help_text="File upload for the track."
    )
    album = models.ForeignKey(
        'albums.Album', 
        related_name='tracks', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        help_text="Album in which the track is included."
    )
    release_date = models.DateField(
        blank=True, 
        null=True, 
        help_text="Release date of the track."
    )
    duration = models.DurationField(
        blank=True, 
        null=True, 
        help_text="Duration of the track."
    )
    composer = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Composer of the track."
    )
    # producer = models.CharField(
    #     max_length=255, 
    #     blank=True, 
    #     null=True, 
    #     help_text="Producer of the track."
    # )
    # record_label = models.CharField(
    #     max_length=255, 
    #     blank=True, 
    #     null=True, 
    #     help_text="Record label of the track."
    # )
    cover_art = models.ImageField(
        upload_to='cover_arts/', 
        blank=True, 
        null=True, 
        help_text="Cover art image for the track."
    )
    bpm = models.PositiveIntegerField(
        blank=True, 
        null=True, 
        help_text="Beats per minute (tempo) of the track."
    )
    key = models.CharField(
        max_length=3, 
        blank=True, 
        null=True, 
        help_text="Musical key of the track."
    )
    # lyrics = models.TextField(
    #     blank=True, 
    #     null=True, 
    #     help_text="Lyrics of the track."
    # )
    # streaming_url = models.URLField(
    #     blank=True, 
    #     null=True, 
    #     help_text="Streaming URL for the track."
    # )
    copyright_info = models.TextField(
        blank=True, 
        null=True, 
        help_text="Copyright information for the track."
    )
    credits = models.TextField(
        blank=True, 
        null=True, 
        help_text="Additional credits for contributors."
    )

    def __str__(self):
        return self.title