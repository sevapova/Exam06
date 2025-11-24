from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameListCreateView.as_view(), name='game-list-create'),
    path('<int:pk>/', views.GameRetrieveUpdateDestroyView.as_view(), name='game-detail'),
]