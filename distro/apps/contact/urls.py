from django.urls import path
from .views import contact_view, success_view

app_name = 'contact'

urlpatterns = [
    path('', contact_view, name='contact_form'),
    path('success/', success_view, name='success'),
]