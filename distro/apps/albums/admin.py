from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Album#, Track, Participant
from distro.apps.demo.sites import distro_admin_site


@admin.register(Album, site=distro_admin_site)
class AlbumAdmin(ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title',)
    list_filter = ('release_date',)
    