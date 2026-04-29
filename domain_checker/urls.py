"""
URL configuration for domain_checker project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('checker/', include('checker.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
