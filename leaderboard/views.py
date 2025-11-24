# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from games.models import Game
from players.models import Player
from scores.models import Score

class GameLeaderboardView(APIView):
    def get(self, request):
        game_id = request.GET.get('game_id')
        if not game_id:
            return Response({"error": "game_id parameter is required"}, status=400)

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=404)

        # Get all players who participated in this game
        players_data = Player.objects.filter(
            score__game_id=game_id
        ).annotate(
            total_points=Sum('score__points'),
            wins=Count('score', filter=Q(score__result='win')),
            draws=Count('score', filter=Q(score__result='draw')),
            losses=Count('score', filter=Q(score__result='loss'))
        ).order_by('-total_points')

        leaderboard = []
        for rank, player in enumerate(players_data, 1):
            leaderboard.append({
                'rank': rank,
                'player': player.nickname,
                'player_id': player.id,
                'country': player.country,
                'rating': player.rating,
                'points': player.total_points or 0,
                'wins': player.wins,
                'draws': player.draws,
                'losses': player.losses,
                'rating_change': player.total_points or 0
            })

        return Response(leaderboard)

class TopPlayersLeaderboardView(APIView):
    def get(self, request):
        game_id = request.GET.get('game_id')
        limit = int(request.GET.get('limit', 10))
        
        if not game_id:
            return Response({"error": "game_id parameter is required"}, status=400)

        if limit > 50:
            limit = 50

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=404)

        players_data = Player.objects.filter(
            score__game_id=game_id
        ).annotate(
            total_points=Sum('score__points')
        ).order_by('-total_points')[:limit]

        leaderboard = []
        for rank, player in enumerate(players_data, 1):
            leaderboard.append({
                'rank': rank,
                'player': player.nickname,
                'country': player.country,
                'rating': player.rating,
                'points': player.total_points or 0
            })

        return Response({
            'game_id': game_id,
            'game_title': game.title,
            'limit': limit,
            'total_players': Player.objects.filter(score__game_id=game_id).distinct().count(),
            'leaderboard': leaderboard
        })

class GlobalRatingLeaderboardView(APIView):
    def get(self, request):
        country = request.GET.get('country')
        limit = int(request.GET.get('limit', 100))
        
        if limit > 500:
            limit = 500

        players = Player.objects.all()
        
        if country:
            players = players.filter(country__iexact=country)

        players = players.order_by('-rating')[:limit]

        leaderboard = []
        for rank, player in enumerate(players, 1):
            leaderboard.append({
                'rank': rank,
                'player': player.nickname,
                'rating': player.rating,
                'total_games': player.total_games,
                'country': player.country
            })

        return Response({
            'total_players': Player.objects.count(),
            'country': country,
            'leaderboard': leaderboard
        })
