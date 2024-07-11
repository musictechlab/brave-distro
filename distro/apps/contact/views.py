from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send confirmation email
            send_confirmation_email(form.cleaned_data['email'], form.cleaned_data['name'], form.cleaned_data['message'])
            return redirect('contact:success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'contact/success.html')


def send_confirmation_email(email, name, message):
    subject = 'Thank you for contacting us'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [from_email, email]

    text_content = f'Name: {name}\n\nEmail: {email}\n\nMessage: {message}\n\n'
    html_content = render_to_string('contact/email_confirmation.html', {'name': name, 'email': email, 'message': message})

    msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()