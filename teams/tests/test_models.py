from django.test import TestCase
from default.models import CustomUser
from hacker.models import HackerInfo
from teams.models import TeamRoster


class TeamsRosterTest(TestCase):
    
    def create_hacker(self, email="limitless@tokyo-jujutsu.jp", first_name="gojo", last_name="satoru"):
        test_user_obj = CustomUser.objects.create(email=email, first_name=first_name, last_name=last_name)
        return HackerInfo.objects.create(user=test_user_obj)
    
    def create_team(self, name="tokyo-jujutsu-tech", description="first years at jujutsu sorcery tech"):
        strongest_sorcerer = self.create_hacker()
        return TeamRoster.objects.create(name=name, description=description, leader=strongest_sorcerer.user,is_visible=False)
    
    def test_create_team(self):
        test_team = self.create_team()
        self.assertTrue(isinstance(test_team, TeamRoster))
        self.assertEqual(test_team.__str__(), test_team.name)