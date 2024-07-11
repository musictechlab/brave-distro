from django.contrib import admin, messages
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.core.validators import EMPTY_VALUES
from django.db import models
from django.db.models import OuterRef, Q, Sum
from django.shortcuts import redirect
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _


from unfold.admin import (
    ModelAdmin
)

from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import action, display
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import User

from distro.apps.demo.sites import distro_admin_site
admin.site.unregister(Group)


@admin.register(User, site=distro_admin_site)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = [
        "display_header",
        "is_active",
        "display_staff",
        "display_superuser",
        "display_created",
    ]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (("first_name", "last_name"), "email", "biography"),
                "classes": ["tab"],
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ["tab"],
            },
        ),
        (
            _("Important dates"),
            {
                "fields": ("last_login", "date_joined"),
                "classes": ["tab"],
            },
        ),
    )
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    readonly_fields = ["last_login", "date_joined"]

    @display(description=_("User"))
    def display_header(self, instance: User):
        return instance.username

    @display(description=_("Staff"), boolean=True)
    def display_staff(self, instance: User):
        return instance.is_staff

    @display(description=_("Superuser"), boolean=True)
    def display_superuser(self, instance: User):
        return instance.is_superuser

    @display(description=_("Created"))
    def display_created(self, instance: User):
        return instance.created_at


@admin.register(Group, site=distro_admin_site)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
