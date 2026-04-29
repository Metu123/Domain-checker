from django.contrib import admin
from .models import DomainCheck


class DomainCheckAdmin(admin.ModelAdmin):
    list_display = ('domain', 'status', 'user', 'checked_at')
    list_filter = ('status', 'checked_at')
    search_fields = ('domain', 'user__username')
    readonly_fields = ('checked_at',)


admin.site.register(DomainCheck, DomainCheckAdmin)
