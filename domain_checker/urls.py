from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django built-in auth (login, logout, password reset)
    path('accounts/', include('django.contrib.auth.urls')),

    # Apps
    path('users/', include('users.urls')),
    path('checker/', include('checker.urls')),

    # Home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
