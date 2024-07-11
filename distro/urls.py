from django.contrib import admin
from django.urls import path, include

from distro.apps.demo.sites import distro_admin_site


urlpatterns = [
    path('', include('distro.apps.landing.urls')),
    path('contact/', include('distro.apps.contact.urls')),
    path('demo/', distro_admin_site.urls),
]