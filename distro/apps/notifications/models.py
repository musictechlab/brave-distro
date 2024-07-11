from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name='notifications', help_text="The user who receives the notification.")
    title = models.TextField(help_text="The title of the notification.")
    message = models.TextField(help_text="The message content of the notification.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the notification was created.")
    read_at = models.DateTimeField(null=True, blank=True, help_text="The date and time when the notification was read.")  # New field to track when the notification was read
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'