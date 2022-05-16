from django.db import models
from default.models import CustomUser

# Create your models here.

class TeamRoster(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.CharField(max_length=180, blank=False, null=False)
    leader = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user')
    is_visible = models.BooleanField()

    def __str__(self):
        return self.name