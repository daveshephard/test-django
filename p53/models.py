from django.db import models

# Create your models here.
from django.utils import timezone
import uuid
from datetime import datetime

# Create your models here.

#1 - makemigrations
#2 - migrate
#3 - test

class Season(models.Model):
    season = models.IntegerField(primary_key=True)

class Week(models.Model):
    week = models.IntegerField(primary_key=True)

class Team(models.Model):
    team_id = models.TextField(max_length = 3, primary_key=True)
    team_name = models.TextField()
    team_city = models.TextField()
    team_stadium = models.TextField()
    indoor_outdoor = models.TextField()
    turf_type = models.TextField()
    team_division = models.TextField()
    team_conference = models.TextField()
    team_color = models.TextField()
    team_logo = models.TextField()
    team_lat = models.FloatField()
    team_long = models.FloatField()
    team_time_zone = models.IntegerField()

class Game(models.Model):
    game_id = models.TextField(max_length = 14, primary_key=True)
    game_datetime = models.DateTimeField(null=True)
    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='away_team')
    home_score = models.IntegerField(null = True)
    away_score = models.IntegerField(null = True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)

class Prediction(models.Model):
    prediction_id = models.UUIDField(primary_key=True,  default=uuid.uuid4)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    vegas_spread = models.FloatField()
    vegas_total = models.FloatField()
    predicted_spread = models.FloatField()
    predicted_total = models.FloatField()
    bet_mgm_spread = models.FloatField()
    bet_rivers_spread = models.FloatField()
    draftkings_spread = models.FloatField()
    fanduel_spread = models.FloatField()
    bovada_spread = models.FloatField()
    bet_mgm_total = models.FloatField()
    bet_rivers_total = models.FloatField()
    draftkings_total = models.FloatField()
    fanduel_total = models.FloatField()
    bovada_total = models.FloatField()
    spread_pick = models.BooleanField(default=False)
    total_pick = models.BooleanField(default=False)
    spread_correct = models.BooleanField()
    total_correct = models.BooleanField()