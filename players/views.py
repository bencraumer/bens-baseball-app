from django.shortcuts import get_object_or_404, render

from .models import Team, Player

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'players/team_list.html', {'teams': teams})

def player_list(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'players/player_list.html', {'team': team})

def player_detail(request, team_pk, player_pk):
    player = get_object_or_404(Player, team_id=team_pk, pk=player_pk)
    return render(request, 'players/player_detail.html', {'player': player})
