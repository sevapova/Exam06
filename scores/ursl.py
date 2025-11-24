from django.urls import path
from . import views

urlpatterns = [
    path('', views.ScoreListCreateView.as_view(), name='score-list-create'),
    path('<int:pk>/', views.ScoreRetrieveDestroyView.as_view(), name='score-detail'),
]