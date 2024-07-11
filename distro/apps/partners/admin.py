from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Partner

from distro.apps.demo.sites import distro_admin_site

@admin.register(Partner, site=distro_admin_site)
class PartnerAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('name', 'country', 'website', 'email', 'phone')
    search_fields = ('name', 'country', 'email')
    list_filter = ('country',)
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'country', 'website', 'email', 'phone', 'address', 'description')
        }),
    )