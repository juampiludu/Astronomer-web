from django.db import models

# Create your models here.

class SolarEclipse(models.Model):
    date_type = models.CharField(max_length=30, null=False)
    eclipse_info = models.TextField(null=False)
    short_eclipse_info = models.TextField(null=False, default="")
    eclipse_image_route = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=40, null=False)

class LunarEclipse(models.Model):
    date_type = models.CharField(max_length=30, null=False)
    eclipse_info = models.TextField(null=False)
    short_eclipse_info = models.TextField(null=False, default="")
    eclipse_image_route = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=40, null=False)