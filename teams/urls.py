from django.urls import path, re_path
from teams import views 

urlpatterns = [
    path('team', views.team_dash, name='team-dash'),
]