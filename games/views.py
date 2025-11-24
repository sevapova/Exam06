# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Game
from .serializers import GameSerializer, GameListSerializer
from .filters import GameFilter

class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = GameFilter
    search_fields = ['title', 'location']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GameListSerializer
        return GameSerializer

class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )