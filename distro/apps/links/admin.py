from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Link
from distro.apps.demo.sites import distro_admin_site


@admin.register(Link, site=distro_admin_site)
class LinkAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('title', 'help_text', 'font_icon')
    search_fields = ('title', 'help_text')
    ordering = ('title',)
   