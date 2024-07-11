from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from .models import Artist, ArtistLink

from distro.apps.demo.sites import distro_admin_site


class ArtistLinkInline(TabularInline):
    model = ArtistLink
    extra = 5  # Number of extra empty forms in the inline


@admin.register(Artist, site=distro_admin_site)
class ArtistAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('name', 'birth_date', 'ipi_code', 'isni_code', 'pro', 'recording_label', 'country', 'city', 'website', 'email', 'phone', 'contact_number', 'background_color')
    search_fields = ('name', 'ipi_code', 'isni_code', 'pro', 'recording_label__name', 'country', 'city', 'email', 'contact_number')
    list_filter = ('country', 'city', 'recording_label')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'birth_date')
        }),
        ('Identifiers', {
            'fields': ('ipi_code', 'isni_code', 'pro')
        }),
        ('Label Information', {
            'fields': ('recording_label',)
        }),
        ('Contact Information', {
            'fields': ('country', 'city', 'website', 'email', 'phone', 'contact_number')
        }),
        ('Biography', {
            'fields': ('bio_description',)
        }),
        ('Background', {
            'fields': ('background_color', 'background_image')
        }),
    )
    inlines = [ArtistLinkInline]
