from django.test import TestCase
from default.models import CustomUser
from hacker.models import HackerInfo
from teams.models import TeamRoster
from teams.utility import is_in_team, add_member

class TeamsRosterTest(TestCase):
    
    def create_hacker(self, email="limitless@tokyo-jujutsu.jp", first_name="gojo", last_name="satoru"):
        test_user_obj = CustomUser.objects.create(email=email, first_name=first_name, last_name=last_name)
        return HackerInfo.objects.create(user=test_user_obj)
    
    def create_team(self, name="tokyo-jujutsu-tech", description="first years at jujutsu sorcery tech"):
        strongest_sorcerer = self.create_hacker()
        return TeamRoster.objects.create(name=name, description=description, leader=strongest_sorcerer.user,is_visible=False)
    
    """
    This model function test solely test the orm creation. No logical constraints are tied to this one. Everything after this uses the utility functions to work with all 
    the team management logical constraints
    """
    def test_create_team(self):
        test_team = self.create_team()
        self.assertTrue(isinstance(test_team, TeamRoster))
        self.assertEqual(test_team.__str__(), test_team.name)
    
    def test_team_creation(self):
        user_leader = CustomUser.objects.create(email='limitless@tokyo-jujutsu.jp', first_name='gojo', last_name='satoru')
        hacker_leader = HackerInfo.objects.create(user=user_leader)

        if is_in_team(user_leader):
            team = TeamRoster.objects.create(name='tokyo-jujutsu-tech', description='first years at jujutsu sorcery tech', leader=user_leader,is_visible=False)
            add_member(user_leader, team)
        
        self.assertTrue(is_in_team(user_leader), True)
        self.assertTrue(isinstance(team, TeamRoster))
        self.assertEqual(team.__str__(), team.name)

    def test_add_member(self):
        test_team = self.create_team()
        new_user = CustomUser.objects.create(email='sukuna@jujutsu-tech.jp', first_name='yuuji', last_name='itadori')
        hacker = HackerInfo.objects.create(user=new_user)

        if is_in_team(new_user):
            add_member(new_user, test_team)

        self.assertTrue(is_in_team(new_user), True)
    
     