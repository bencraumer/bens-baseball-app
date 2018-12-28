from django.db import models

class Team(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    record = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    positions = models.TextField()
    bats = models.TextField()
    throws = models.TextField()
    bio = models.TextField()
    hits = models.IntegerField()
    hr = models.IntegerField()
    rbi = models.IntegerField()
    obp = models.CharField(max_length=10)
    slg = models.CharField(max_length=10)
    ops = models.CharField(max_length=10)

    def __str__(self):
        return self.name
