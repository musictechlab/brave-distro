from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Participant, ParticipantRole
from distro.apps.demo.sites import distro_admin_site


@admin.register(Participant, site=distro_admin_site)
class ParticipantAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('full_name', 'isni', 'ipn', 'paypal_email', 'user')
    search_fields = ('full_name', 'isni', 'ipn', 'paypal_email', 'user__username')
    list_filter = ('user',)
    ordering = ('full_name',)
    fieldsets = (
        (None, {
            'fields': ('full_name',)
        }),
        ('Identifiers', {
            'fields': ('isni', 'ipn')
        }),
        ('Contact Information', {
            'fields': ('paypal_email', 'user')
        }),
    )

@admin.register(ParticipantRole, site=distro_admin_site)
class ParticipantRoleAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('name',)
    search_fields = ('name',)