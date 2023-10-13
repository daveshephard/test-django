from django.shortcuts import render
from django.http import HttpResponse
from .models import Prediction


def index(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing.html')

def predictions_by_year_month(request, year, week):
    
    posts = Prediction.objects.filter(game__season=year, game__week=week)
    context = {
        'year': year,
        'week': week,
        'posts': posts,
    }
    
    return render(request, 'prediction_view.html', context)