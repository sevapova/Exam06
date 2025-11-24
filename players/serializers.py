from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    total_games = serializers.ReadOnlyField()
    wins = serializers.ReadOnlyField()
    draws = serializers.ReadOnlyField()
    losses = serializers.ReadOnlyField()

    class Meta:
        model = Player
        fields = ['id', 'nickname', 'country', 'rating', 'total_games', 
                 'wins', 'draws', 'losses', 'created_at']

class PlayerListSerializer(serializers.ModelSerializer):
    total_games = serializers.ReadOnlyField()

    class Meta:
        model = Player
        fields = ['id', 'nickname', 'country', 'rating', 'total_games', 'created_at']