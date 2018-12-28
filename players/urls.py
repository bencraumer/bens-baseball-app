from django.conf.urls import url
from django.urls import path

from . import views

app_name = "players"

urlpatterns = [
    path('', views.team_list, name="team_list"),
    path('<int:team_pk>/<int:player_pk>/', views.player_detail, name="player_detail"),
    path('<int:pk>/', views.player_list, name="player_list"),
]
