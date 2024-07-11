from django.db import models
from django.conf import settings

class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, help_text="The user associated with the participant. Can be null.")
    full_name = models.CharField(max_length=255, help_text="The full name of the participant.")
    isni = models.CharField(max_length=16, blank=True, null=True, help_text="Enter Number in Standard ISNI Notation [0000000123456789]")
    ipn = models.CharField(max_length=255, blank=True, null=True, help_text="International Performer Number (IPN) or PayPal Email Address")
    paypal_email = models.EmailField(max_length=255, blank=True, null=True, help_text="PayPal Email Address")

    def __str__(self):
        return self.full_name

class ParticipantRole(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the role associated with a participant.")

    def __str__(self):
        return self.name