from django.test import TestCase
from hacker.models import HackerInfo

from default.models import CustomUser


class HackerInfoTest(TestCase):

    def create_hacker(self, email="limitless@jujutsutech.jp", first_name="gojo", last_name="satoru"):
        test_user_obj = CustomUser.objects.create(email=email, first_name=first_name, last_name=last_name)
        return HackerInfo.objects.create(user=test_use_obj)
        