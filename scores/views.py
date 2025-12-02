from rest_framework import generics
from .models import Score
from .serializers import ScoreSerializer

class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
