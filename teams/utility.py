"""
A utility file with helper functions that handles all the constraints of
HackTCNJ team management
"""

from .models import TeamRoster
from default.models import CustomUser


"""
Anyone in a team cannot create or join a team. 
This function tests if a user is in a team
"""
def is_in_team(user):
    hacker_object = HackerInfo.objects.get(user = user)
    return hacker_object.team is not None



    