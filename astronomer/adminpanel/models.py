from django.db import models

class Years(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.year
