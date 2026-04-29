from django.db import models
from django.contrib.auth.models import User


class DomainCheck(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('registered', 'Registered (No DNS)'),
        ('not_found', 'Not Found'),
        ('error', 'Error'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='domain_checks')
    domain = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ip_addresses = models.JSONField(default=list)
    registrar = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.CharField(max_length=255, blank=True, null=True)
    expiry_date = models.CharField(max_length=255, blank=True, null=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-checked_at']

    def __str__(self):
        return f"{self.domain} - {self.status}"
