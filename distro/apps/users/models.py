# apps/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    biography = models.TextField(_("biography"), null=True, blank=True, default=None)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified at"), auto_now=True)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email if self.email else self.username

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name}"

        return None
