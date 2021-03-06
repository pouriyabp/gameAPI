from django.urls import path
from . import views

urlpatterns = [
    path('compare-two-games/', views.CompareTwoGamesAPI.as_view(), name='compare_two_games'),
    path('years-sales/', views.YearsSalesAPI.as_view(), name='compare_two_games'),
    path('producers-sales/', views.ProducersSalesAPI.as_view(), name='compare_two_games'),
    path('category-sales/', views.CategorySalesAPI.as_view(), name='compare_two_games'),

]
