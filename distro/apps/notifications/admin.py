from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Notification
from distro.apps.demo.sites import distro_admin_site

@admin.register(Notification, site=distro_admin_site)
class NotificationAdmin(ModelAdmin):   
    list_display = ('message', 'user', 'created_at', 'read_at')
    search_fields = ('user__username', 'title', 'message', 'read_at')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    search_fields = ('user__username', 'message')