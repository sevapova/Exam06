# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Player
from .serializers import PlayerSerializer, PlayerListSerializer
from .filters import PlayerFilter

class PlayerListCreateView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PlayerFilter
    search_fields = ['nickname']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlayerListSerializer
        return PlayerSerializer

class PlayerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

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