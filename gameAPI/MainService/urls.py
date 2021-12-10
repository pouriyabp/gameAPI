from django.urls import path
from . import views

urlpatterns = [
    path('games-based-rank/', views.GamesBasedRankAPI.as_view(), name='games_based_rank'),
    path('games-based-name/', views.GamesBasedNameAPI.as_view(), name='games_based_name'),
    path('n-games-based-platform/', views.NGamesBasedPlatformAPI.as_view(), name='n_games_based_platform'),
    path('n-games-based-year/', views.NGamesBasedYearAPI.as_view(), name='n_games_based_year'),
    path('n-games-based-genre/', views.NGamesBasedGenreAPI.as_view(), name='n_games_based_genre'),
    path('five-top-games/', views.FiveTopGamesAPI.as_view(), name='five_top_games'),
    path('games-EU-sales-gt-NA-sales/', views.GamesEUgtNAAPI.as_view(),
         name='games_EU_sales_gt_NA_sales/'),
]