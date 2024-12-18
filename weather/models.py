from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
