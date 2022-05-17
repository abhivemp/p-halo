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
    current_hacker = HackerInfo.objects.get(user=request.user)
    team_status = is_in_team(request.user)

    if not is_in_team(request.user):
        public_teams = TeamRoster.objects.filter(is_visible=True)
        count_public_teams = public_teams.count()
        context = {'teams': public_teams, 'team_count': count_public_teams}
    else:
        context = {}

    context.update({'team_status': team_status})
    return render(request, 'teams/team-dash.html', context)
