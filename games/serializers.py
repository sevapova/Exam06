from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'location', 'start_date', 'description', 'created_at']

class GameListSerializer(serializers.ModelSerializer):
    total_players = serializers.SerializerMethodField()
    total_games = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'title', 'location', 'start_date', 'total_players', 'total_games', 'created_at']

    def get_total_players(self, obj):
        return obj.score_set.values('player').distinct().count()

    def get_total_games(self, obj):
        return obj.score_set.count()