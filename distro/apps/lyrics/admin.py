from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, SelectableFieldsExportForm
from import_export.admin import ImportExportModelAdmin
from .models import Lyricist, Lyrics

from distro.apps.demo.sites import distro_admin_site

@admin.register(Lyricist, site=distro_admin_site)
class LyricistAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('first_name', 'last_name', 'nationality', 'get_truncated_biography')
    search_fields = ('first_name', 'last_name', 'nationality')
    list_filter = ('nationality',)
    ordering = ('last_name', 'first_name')

    def get_truncated_biography(self, obj):
        return (obj.biography[:50] + '..') if len(obj.biography) > 50 else obj.biography
    get_truncated_biography.short_description = 'Biography'


@admin.register(Lyrics, site=distro_admin_site)
class LyricsAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm
    list_display = ('track', 'get_truncated_title', 'language')
    search_fields = ('track__title', 'language')
    list_filter = ('track', 'language')
    ordering = ('track',)

    def get_truncated_title(self, obj):
        return (obj.content[:50] + '..') if len(obj.content) > 50 else obj.content
    get_truncated_title.short_description = 'Lyrics'   