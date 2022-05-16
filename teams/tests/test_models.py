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

class TestTeamBuilding(TestCase):

    def setUp(self):
        emails = [
            'fushiguro@jujutsutech.jp',
            'aoi@jujutsutech.jp',
            'yuta@jujutsutech.jp',
            'nobara@jujutsutech.jp',
            'yuji@jujutsutech.jp',
            'inumaki@jujutsutech.jp',
            'maki@jujutsutech.jp',
            'panda@jujutsutech.jp',
            'mai@jujutsutech.jp',
            'kasumi@jujutsutech.jp',
        ]
        first_names = [
            'Fushiguro',
            'Aoi',
            'Yuta',
            'Yuji',
            'Nobara',
            'Inumaki',
            'Maki',
            'Panda',
            'Mai',
            'Kasumi'
        ]

        member_emails = [
            'nobara@jujutsutech.jp',
            'panda@jujutsutech.jp',
            'maki@jujutsutech.jp',
            'inumaki@jujutsutech.jp',
            'mai@jujutsutech.jp',
            'kasumi@jujutsutech.jp',
            'yuji@jujutsutech.jp',
        ]

        team_names = [
            'tokyo',
            'kyoto',
            'special-grade',
        ]

        for i in range (len(emails)):
            user = CustomUser.objects.create(email=emails[i], first_name=[i])
            hacker = HackerInfo.objects.create(user=user)
        
        for i in range (len(team_names)):
            team = TeamRoster.objects.create(name=team_names[i], leader=CustomUser.objects.get(email=emails[i]), is_visible=False)
        
        
    def test_multiple_team_members(self):
        self.fixture_data = (
            (
                'nobara@jujutsutech.jp','tokyo',
            ),
            (
                'panda@jujutsutech.jp', 'tokyo',
            ),
            (
                'maki@jujutsutech.jp', 'tokyo',
            ),
            (
                'inumaki@jujutsutech.jp', 'tokyo',
            ),
            (
                'mai@jujutsutech.jp', 'kyoto',
            ),
            (
                'kasumi@jujutsutech.jp', 'kyoto',
            ),
            (
                'yuji@jujutsutech.jp', 'special-grade',
            ),
        )

        for member, team_name in self.fixture_data:
            with self.subTest(context=member):
                hacker = HackerInfo.objects.get(user__email=member)
                team_obj = TeamRoster.objects.get(name=team_name)
                hacker.team = team_obj
                hacker.save()

                check_hacker_team = HackerInfo.objects.get(user__email=member)
                self.assertEqual(check_hacker_team.team.name, team_name)
