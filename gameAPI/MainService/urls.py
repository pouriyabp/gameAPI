from django.urls import path
from . import views


urlpatterns = [
    path('games-based-rank/', views.GamesBasedRankAPI.as_view(), name='games_based_rank')
]