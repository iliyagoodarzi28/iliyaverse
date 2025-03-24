# admin.py
from django.contrib import admin
from .models import SiteInfo

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')