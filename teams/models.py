from django.db import models

# Create your models here.

class TeamRoster(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.CharField(max_length=180, blank=False, null=False)
    is_visible = models.BooleanField()