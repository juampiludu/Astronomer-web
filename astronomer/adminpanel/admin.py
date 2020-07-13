from django.contrib import admin
from .models import Years

@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
    list_display = ('year',)
