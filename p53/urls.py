from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path('predictions/<int:year>/<int:week>/', views.predictions_by_year_month, name='predictions_by_year_month'),
]