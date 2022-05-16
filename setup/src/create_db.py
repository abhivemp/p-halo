# This python file creates 5 organizers, 21 hackers

# new_user = User.objects.create(username = row["email"], first_name= row["first"], last_name= row["last"], email = row["email"] + "@tcnj.edu")
#             new_user.set_password('tacos')
#             new_user.save()

from dotenv import load_dotenv

import os
import json
import datetime
import random

from django.contrib.auth.models import User, Group
from default.models import CustomUser
from organizer.models import OrganizerInfo, WebsiteSettings, FeaturePermission, OrganizerPermission
from hacker.models import HackerInfo
from default.helper import add_group
from teams.models import TeamRoster

load_dotenv()


# total count (make less than 30 for each for now)
TOTAL_ORGANIZERS = 5
TOTAL_VOLUNTEERS = 3
TOTAL_HACKERS = 10

first_name_organizers = [
    'Abhi',
    'Kevin',
    'Sterly',
    'JM',
    'Tracy'
]

last_name_organizers = [
    'Vempati',
    'Williams',
    'Deracy',
    'JM',
    'McGrady'
]

email_organizers = [
    'abhi@aslan.com',
    'kevin@aslan.com',
    'sterly@aslan.com',
    'jm@aslan.com',
    'tracy@aslan.com'
]
address_organizers = [
    '2 Braemer Dr',
    '100 Primrose Cr',
    '10 Crabapple Ct',
    '5 Bellflower Ct',
    '6 Cranberry Ct'
]

###################################
first_name_volunteers = [
    'Sahi',
    'David',
    'Dom',

]

last_name_volunteers = [
    'Reganta',
    'Greco',
    'Lamastra',
]

email_volunteers = [
    'sahi@aslan.com',
    'david@aslan.com',
    'dom@aslan.com',
]
address_volunteers = [
    '23 inumaki St',
    '25 Warren Ave',
    '100 Campus Town',
]


###################################
###################################


first_name_hackers = [
    'Sophie',
    'Daryll',
    'Chandler',
    'Rachel',
    'Tony',
    'Jake',
    'Amy',
    'Raymond',
    'Mani',
    'Sabrina',
    'Brandon'
]

last_name_hackers = [
    'Goldberg',
    'Johnson',
    'Bing',
    'Green',
    'Stark',
    'Peralta',
    'Santiago',
    'Holt',
    'Yeluri',
    'May',
    'Kim'
]
email_hackers = [
    'sophie@tcnj.edu',
    'daryl@dm.com',
    'chandler@ps.com',
    'rachel@rl.com',
    'tony@mit.edu',
    'jake@b99.gov',
    'amy@b99.gov',
    'ray@b99.gov',
    'mani@tcnj.edu',
    'brandon@tcnj.edu'
]
address_hackers = [
    '56 Matawan Ln',
    '44 Scranton Rd',
    '120 46 W 10 Ave',
    '121 46 W 10 Ave',
    '1044 Malibu Pt',
    '33 Brooklyn Ln',
    '33 Brooklyn Ln',
    '60 Brooklyn Ln',
    '4 Galborti Dr',
    '30 Pennington Rd',

]

majors = [
    'Accounting',
    'Biology',
    'Biomedical Engineering',
    'Business Administration',
    'Chemistry',
    'Civil Engineering',
    'Communications',
    'Computer Engineering',
    'Computer Science',
    'Construction Management',
    'Cybersecurity',
    'Economics',
    'Education',
    'Electronics Engineering',
    'English',
    'Finance',
    'Game Design',
    'Health Informatics',
    'Industrial Engineering',
    'Interactive Multimedia'
    'Information Technology',
    'Liberal Arts',
    'Management',
    'Management Information Systems',
    'Marketing',
    'Mechanical Engineering',
    'Nuclear Engineering',
    'Nursing',
    'Petroleum Engineering',
    'Physics',
    'Political Science',
    'Public Administration',
    'Software Engineering'
]

education_hackers = [
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "High School/Secondary School",
    "University (Undergrad)",
    "University (Undergrad)"
]

food_choices_hackers = [
    "Vegan",
    "Gluten-Free",
    "Vegetarian",
    "None",
    "None",
    "None",
    "Vegetarian",
    "Vegetarian",
    "None",
    "None",
]

shirt_sizes_hackers = [
    "Unisex (M)",
    "Unisex (M)",
    "Unisex (S)",
    "Unisex (S)",
    "Unisex (L)",
    "Unisex (L)",
    "Unisex (M)",
    "Unisex (M)",
    "Unisex (L)",
    "Unisex (L)",

]

team_names = [
    ('avengers', 'avengers assemble!!!'),
   ( 'leaf village', ' we live in the shadows'),
    ('brooklyn nine-nine', 'NINE NINE!!'),
]

team_leaders = [
    'tony@mit.edu',
    'amy@b99.gov',
    'ray@b99.gov',
]
# Create the necessary groups for the users


def create_groups():
    Group.objects.create(name="hacker")
    Group.objects.create(name="organizer")
    Group.objects.create(name="head-organizer")
    Group.objects.create(name="checked-in")


def create_super_user():
    new_admin=CustomUser.objects.create_superuser(email=os.getenv('HEAD_ORG_EMAIL'), password=os.getenv('HEAD_ORG_PASSWORD'))
    new_admin.first_name=os.getenv('HEAD_ORG_FIRST_NAME')
    new_admin.last_name=os.getenv('HEAD_ORG_LAST_NAME')

def create_teams():
    for i in range(len(team_names)):
        lead = CustomUser.objects.get(email=team_leaders[i])
        new_team = TeamRoster.objects.create(name=team_names[i][0], description=team_names[i][1], leader=lead, is_visible=True)
        lead.team = new_team
        lead.save()

def create_users():
    for i in range(TOTAL_ORGANIZERS):
        new_user = CustomUser.objects.create(
            email=email_organizers[i], first_name=first_name_organizers[i], 
            last_name=last_name_organizers[i], address=address_organizers[i], major="Computer Science", resume="/test_resume.txt", age=random.randint(14,22)
        )
        new_user.set_password(os.getenv('ORGANIZER_PASSWORD'))
        new_user.save()
        OrganizerInfo.objects.create(user=new_user)
        add_group(new_user, 'organizer')

    for i in range(TOTAL_VOLUNTEERS):
        new_user = CustomUser.objects.create(email=email_volunteers[i], 
        first_name=first_name_volunteers[i], last_name=last_name_volunteers[i], 
        address=address_volunteers[i], major="Computer Science", resume="/test_resume.txt", age=random.randint(14,22)
        )

        new_user.set_password(os.getenv('ORGANIZER_PASSWORD'))
        new_user.save()
        OrganizerInfo.objects.create(user=new_user)
        add_group(new_user, 'organizer')
        
    for i in range(TOTAL_HACKERS):
        new_user = CustomUser.objects.create(email=email_hackers[i], first_name=first_name_hackers[i], last_name=last_name_hackers[i],
                                            address=address_hackers[i], food_preference=food_choices_hackers[i], shirt_size=shirt_sizes_hackers[i], resume="/test_resume.txt", age=random.randint(14,22)
                                            )
        new_user.set_password(os.getenv('HACKER_PASSWORD'))
        new_user.save()
        HackerInfo.objects.create(user=new_user)
        add_group(new_user, 'hacker')


def add_admin_to_group():
    admin_user = CustomUser.objects.get(email=os.getenv('HEAD_ORG_EMAIL'))
    add_group(admin_user, 'head-organizer')


def add_website_setting():
    WebsiteSettings.objects.create(waiting_list_status=False)


permissions_list = []


def create_feature_permissions():
    permissions_list.append(FeaturePermission.objects.create(
        url_name='display-hackers', permission_name='h-Hackers'))
    permissions_list.append(
        FeaturePermission.objects.create(url_name='qr-checkin', permission_name='h-QR Checkin'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='manual-checkin', permission_name='h-Checkin'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='waiting-list', permission_name='w-Waiting List'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='edit-waiting-list', permission_name='w-Edit Waiting List'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='statistics', permission_name='s-Stats'))

def add_organizers_to_features():
    user = CustomUser.objects.get(email='admin@aslan.com')
    head_org = OrganizerPermission.objects.create(user=user)
    head_org.permission.add(permissions_list[0], permissions_list[1], permissions_list[2], 
                            permissions_list[3], permissions_list[4], permissions_list[5])
    for i in range(TOTAL_ORGANIZERS):
        user = CustomUser.objects.get(email=email_organizers[i])
 

        org_perm = OrganizerPermission.objects.create(user=user)
        org_perm.permission.add(permissions_list[0], permissions_list[1],
                                permissions_list[2], permissions_list[3], permissions_list[4])

        if i % 2 ==  0:
            org_perm.permission.add(permissions_list[5])

    for i in range(TOTAL_VOLUNTEERS):
        user = CustomUser.objects.get(email=email_volunteers[i])
 

        org_perm = OrganizerPermission.objects.create(user=user)
        org_perm.permission.add(permissions_list[1],
                                permissions_list[2], permissions_list[3])


# Driver code
# site startup code
create_groups()
create_super_user()
create_users()
# admin startup code
'''
NOTE: Please run create_feature_permissions() together with add_organizers_to_features()
'''
add_admin_to_group()
add_website_setting()
create_feature_permissions()
add_organizers_to_features()

create_teams()