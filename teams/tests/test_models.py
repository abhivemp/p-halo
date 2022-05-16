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
    
     
    def test_team_deletion(self):
        test_team = self.create_team()
        test_team_name = test_team.name
        test_team.delete()
        find_test_team = TeamRoster.objects.filter(name=test_team_name).exists()

        self.assertFalse(find_test_team, False)

    # I tried to write a test that would test to see if an error was raised to test the one to one relationship between team and hacker
    # def test_team_leader_uniqueness(self):
    #     test_team_1 = self.create_team()
    #     user_leader = test_team_1.leader
    #     with self.assertRaises(RuntimeError) as ue:
    #         test_team_2 = TeamRoster.objects.create(name='kyoto-jujutsu-tech', description='second years at jujutsu sorcery tech', leader=user_leader,is_visible=False)

    #     self.assertEqual(str(ue.exception), 'UNIQUE constraint failed')