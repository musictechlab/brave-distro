from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Name should contain only letters and spaces.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "@" in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message should be at least 10 characters long.")
        return message