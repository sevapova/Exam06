from rest_framework import serializers
from .models import Score

class GameNestedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class PlayerNestedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nickname = serializers.CharField()

class ScoreSerializer(serializers.ModelSerializer):
    game = GameNestedSerializer(read_only=True)
    player = PlayerNestedSerializer(read_only=True)
    game_id = serializers.IntegerField(write_only=True)
    player_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Score
        fields = ['id', 'game', 'player', 'game_id', 'player_id', 'result', 
                 'points', 'opponent_name', 'created_at']

    def create(self, validated_data):
        from games.models import Game
        from players.models import Player
        
        game_id = validated_data.pop('game_id')
        player_id = validated_data.pop('player_id')
        
        try:
            game = Game.objects.get(id=game_id)
            player = Player.objects.get(id=player_id)
        except Game.DoesNotExist:
            raise serializers.ValidationError("Game not found")
        except Player.DoesNotExist:
            raise serializers.ValidationError("Player not found")
        
        score = Score.objects.create(game=game, player=player, **validated_data)
        return score