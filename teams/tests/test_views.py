from django.test import TestCase
from default.models import CustomUser
from hacker.models import HackerInfo
from teams.models import TeamRoster
from teams.utility import is_in_team, add_member

from selenium import webdriver
from selenium.webdriver.common.keys import Keys