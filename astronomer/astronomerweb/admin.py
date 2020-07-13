from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Eclipses)

class EclipsesAdmin(admin.ModelAdmin):
    list_display = ('id', 'eclipse_title', 'solar_lunar')
    list_display_links = ('id', 'eclipse_title', 'solar_lunar')