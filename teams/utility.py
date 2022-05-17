"""
A utility file with helper functions that handles all the constraints of
HackTCNJ team management
"""

from .models import TeamRoster
from default.models import CustomUser
from hacker.models import HackerInfo


"""
Anyone in a team cannot create or join a team. 
This function tests if a user is in a team
returns TRUE if user is in team
"""
def is_in_team(user):
    hacker_object = HackerInfo.objects.get(user = user)
    return not (hacker_object.team is None)

"""
Adds a member to the team
"""
def add_member(user, team):
    hacker_obj = HackerInfo.objects.get(user = user)
    hacker_obj.team = team
    hacker_obj.save()
    return hacker_obj.team == team