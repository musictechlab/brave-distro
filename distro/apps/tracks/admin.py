from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Track
from distro.apps.demo.sites import distro_admin_site


@admin.register(Track, site=distro_admin_site)
class TrackAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('title', 'isrc', 'iswc', 'language', 'parental_advisory', 'available_for', 'album', 'release_date', 'duration', 'bpm', 'key', 'get_truncated_credits')
    search_fields = ('title', 'isrc', 'artists__name', 'featured_artists__name', 'genres__name', 'iswc', 'language', 'album__title')
    list_filter = ('genres', 'parental_advisory', 'available_for', 'album', 'release_date')
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'isrc', 'artists', 'featured_artists', 'genres', 'album')
        }),
        ('Identifiers', {
            'fields': ('iswc',)
        }),
        ('Details', {
            'fields': ('language', 'parental_advisory', 'available_for', 'release_date', 'duration', 'bpm', 'key', 'cover_art', 'copyright_info', 'credits')
        }),
    )
    filter_horizontal = ('artists', 'featured_artists', 'genres')

    def get_truncated_credits(self, obj):
        return ((obj.credits[:50] + '..') if len(obj.credits) > 50 else obj.credits) if obj.credits else '-'
    get_truncated_credits.short_description = 'Credits'