from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Platform
from distro.apps.demo.sites import distro_admin_site

@admin.register(Platform, site=distro_admin_site)
class PlatformAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)
    fields = ('name', 'description')

