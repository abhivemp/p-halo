from django.test import TestCase
from hacker.models import HackerInfo

from default.models import CustomUser


class HackerInfoTest(TestCase):

    def create_hacker(self, email="sukuna@jujutsutech.jp", first_name="yuuji", last_name="itadori"):
        test_user_obj = CustomUser.objects.create(email=email, first_name=first_name, last_name=last_name)
        return HackerInfo.objects.create(user=test_user_obj)
    
    def test_create_hacker(self):
        test_hacker = self.create_hacker()
        self.assertTrue(isinstance(test_hacker,HackerInfo))
        self.assertTrue(test_hacker.__str__(), "sukuna@jujutsutech.jp: yuuji itadori")
        