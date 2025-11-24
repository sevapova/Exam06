from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameLeaderboardView.as_view(), name='game-leaderboard'),
    path('top/', views.TopPlayersLeaderboardView.as_view(), name='top-players'),
    path('global/', views.GlobalRatingLeaderboardView.as_view(), name='global-leaderboard'),
]