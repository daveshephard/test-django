# Generated by Django 4.0.4 on 2023-10-12 01:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.TextField(max_length=14, primary_key=True, serialize=False)),
                ('game_datetime', models.DateTimeField(null=True)),
                ('home_score', models.IntegerField(null=True)),
                ('away_score', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('season', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.TextField(max_length=3, primary_key=True, serialize=False)),
                ('team_name', models.TextField()),
                ('team_city', models.TextField()),
                ('team_stadium', models.TextField()),
                ('indoor_outdoor', models.TextField()),
                ('turf_type', models.TextField()),
                ('team_division', models.TextField()),
                ('team_conference', models.TextField()),
                ('team_color', models.TextField()),
                ('team_logo', models.TextField()),
                ('team_lat', models.FloatField()),
                ('team_long', models.FloatField()),
                ('team_time_zone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('week', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('prediction_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('vegas_spread', models.FloatField()),
                ('vegas_total', models.FloatField()),
                ('predicted_spread', models.FloatField()),
                ('predicted_total', models.FloatField()),
                ('bet_mgm_spread', models.FloatField()),
                ('bet_rivers_spread', models.FloatField()),
                ('draftkings_spread', models.FloatField()),
                ('fanduel_spread', models.FloatField()),
                ('bovada_spread', models.FloatField()),
                ('bet_mgm_total', models.FloatField()),
                ('bet_rivers_total', models.FloatField()),
                ('draftkings_total', models.FloatField()),
                ('fanduel_total', models.FloatField()),
                ('bovada_total', models.FloatField()),
                ('spread_pick', models.BooleanField(default=False)),
                ('total_pick', models.BooleanField(default=False)),
                ('spread_correct', models.BooleanField()),
                ('total_correct', models.BooleanField()),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p53.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='away_team', to='p53.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_team', to='p53.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p53.season'),
        ),
        migrations.AddField(
            model_name='game',
            name='week',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p53.week'),
        ),
    ]
