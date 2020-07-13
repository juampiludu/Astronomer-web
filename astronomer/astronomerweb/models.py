from django.db import models

class Eclipses(models.Model):
    eclipse_title = models.CharField(max_length=50)
    solar_lunar = models.CharField(max_length=50)
    eclipse_type = models.CharField(max_length=50)
    eclipse_info = models.TextField()
    eclipse_date = models.CharField(max_length=50)
    eclipse_time = models.CharField(max_length=50, default="")
    eclipse_datetime = models.CharField(max_length=50, default="")