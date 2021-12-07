from django.urls import path
from . import views

urlpatterns = [
    path('compare-two-games/', views.CompareTwoGamesAPI.as_view(), name='compare_two_games'),
    path('years-sales/', views.YearsSalesAPI.as_view(), name='compare_two_games'),

]
