from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Genre

from distro.apps.demo.sites import distro_admin_site

@admin.register(Genre, site=distro_admin_site)
class GenreAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)