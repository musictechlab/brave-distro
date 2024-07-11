from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Label
from distro.apps.demo.sites import distro_admin_site


@admin.register(Label, site=distro_admin_site)
class LabelAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('name', 'founded_date', 'founder', 'country', 'city', 'website', 'email', 'phone')
    search_fields = ('name', 'founder', 'country', 'city')
    list_filter = ('country', 'city')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'founded_date', 'founder')
        }),
        ('Contact Information', {
            'fields': ('country', 'city', 'website', 'email', 'phone')
        }),
    )

