from django.contrib import admin

from .models import Team, Player

class PlayerInLine(admin.StackedInline):
    model = Player

class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInLine,]

admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
