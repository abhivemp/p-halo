from django.db import models
from default.models import CustomUser
from teams.models import TeamRoster
# Create your models here.


class HackerInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="hacker")
    team = models.ForeignKey(TeamRoster, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Hacker'
    
    def __str__(self):
        return self.user.email + ": " + self.user.first_name + " " + self.user.last_name