from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Release, ReleaseHistory, ReleaseReview

from distro.apps.demo.sites import distro_admin_site

@admin.register(Release, site=distro_admin_site)
class ReleaseAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('album', 'partner', 'is_dolby_atmos', 'date_original_release')
    search_fields = ('album__title', 'partner__name', 'date_original_release')
    list_filter = ('is_dolby_atmos', 'date_original_release', 'partner')
    ordering = ('album__title',)
    fieldsets = (
        (None, {
            'fields': ('album', 'partner', 'is_dolby_atmos', 'date_original_release')
        }),
    )

@admin.register(ReleaseHistory, site=distro_admin_site)
class ReleaseHistoryAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('release', 'change_date', 'changed_by', 'get_truncated_change_description')
    search_fields = ('release__album__title', 'changed_by__username', 'change_description')
    list_filter = ('change_date', 'changed_by')
    ordering = ('-change_date',)
    fieldsets = (
        (None, {
            'fields': ('release', 'changed_by', 'change_description')
        }),
    )

    def get_truncated_change_description(self, obj):
        return (obj.change_description[:50] + '...') if len(obj.change_description) > 50 else obj.change_description
    get_truncated_change_description.short_description = 'Change Description'



@admin.register(ReleaseReview, site=distro_admin_site)
class ReleaseReviewAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('release', 'release_date', 'date_added', 'date_updated')
    list_filter = ('release_date', 'date_added', 'date_updated')
    ordering = ('-date_added',)
    fieldsets = (
        (None, {
            'fields': ('release', 'release_date', 'date_added', 'date_updated')
        }),
    )