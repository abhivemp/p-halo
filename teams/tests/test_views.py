from django.test import TestCase, Client
from default.models import CustomUser
from hacker.models import HackerInfo
from teams.models import TeamRoster
from teams.utility import is_in_team, add_member

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.http import HttpResponse
import os
from dotenv import load_dotenv
load_dotenv()


class TestPublicTeamsDash(TestCase):

    def setUp(self):
        emails = [
            'fushiguro@jujutsutech.jp',
            'aoi@jujutsutech.jp',
            'yuta@jujutsutech.jp',
            'yuji@jujutsutech.jp',
        ]
        first_names = [
            'Fushiguro',
            'Aoi',
            'Yuta',
            'Yuji',
        ]

        team_names = [
            'tokyo',
            'kyoto',
            'special-grade',
        ]

        for i in range (len(emails)):
            user = CustomUser.objects.create(email=emails[i], first_name=[i], password='randompass')
            hacker = HackerInfo.objects.create(user=user)
        
        for i in range (len(team_names)):
            team = TeamRoster.objects.create(name=team_names[i], leader=CustomUser.objects.get(email=emails[i]), is_visible=False)
         
        
        self.driver = webdriver.Chrome('./chromedriver')
        

        self.driver.get("http://localhost:8000/login")

        self.driver.maximize_window() # For maximizing window
        self.driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        user_elem = self.driver.find_element_by_name("email")
        user_elem.send_keys('yuji@jujutsutech.jp')
        
        pass_elem = self.driver.find_element_by_name("password")
        pass_elem.send_keys('randompass')
        self.driver.implicitly_wait(20)
        pass_elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(20)
        
    def test_teams_public_dash(self):
        driver = self.driver
        driver.get("http://localhost:8000/team")
        get_count = driver.find_element_by_id("team-count")
        self.assertTrue(get_count, 3)

        # self.assertEqual()

    def tearDown(self):
        self.driver.close()