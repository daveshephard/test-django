from django.contrib import admin

# Register your models here.
from .models import Game, Season, Week, Team, Prediction

admin.site.register(Game)
admin.site.register(Season)
admin.site.register(Week)
admin.site.register(Team)
admin.site.register(Prediction)