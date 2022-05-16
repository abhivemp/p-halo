from django.shortcuts import render
from .models import TeamRoster
from hacker.models import HackerInfo
from default.models import CustomUser

from .utility import is_in_team
# Create your views here.
"""
Display public teams if the user is not in a team. 
If the user is in a team, show the user's team info page
"""
def team_dash(request):

    context = {}
    return render(request, 'teams/team-dash.html', context)
