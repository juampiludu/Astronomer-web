from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(LunarEclipse)
@admin.register(SolarEclipse)

class LunarEclipseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_type')
    list_display_links = ('id', 'date_type')

class SolarEclipseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_type')
    list_display_links = ('id', 'date_type')