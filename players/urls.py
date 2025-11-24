from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerListCreateView.as_view(), name='player-list-create'),
    path('<int:pk>/', views.PlayerRetrieveUpdateDestroyView.as_view(), name='player-detail'),
]