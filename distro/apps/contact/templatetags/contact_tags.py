from django import template
from ..forms import ContactForm

register = template.Library()

@register.inclusion_tag('contact/contact_form.html')
def render_contact_form():
    form = ContactForm()
    return {'form': form}