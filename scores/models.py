# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class Score(models.Model):
    RESULT_CHOICES = [
        ('win', 'Win'),
        ('draw', 'Draw'),
        ('loss', 'Loss'),
    ]

    game = models.ForeignKey('games.Game', on_delete=models.PROTECT)
    player = models.ForeignKey('players.Player', on_delete=models.PROTECT)
    result = models.CharField(max_length=10, choices=RESULT_CHOICES)
    points = models.IntegerField(blank=True, null=True)
    opponent_name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.player.nickname} - {self.result}"

    def clean(self):
        if self.result not in dict(self.RESULT_CHOICES):
            raise ValidationError({
                'result': f"Result must be one of: {', '.join(dict(self.RESULT_CHOICES).keys())}"
            })

    def save(self):
        points_map = {'win': 10, 'draw': 5, 'loss': 0}
        self.points = points_map.get(self.result, 0)
        
        super().save()
        
        self.update_player_rating()

    def update_player_rating(self):
        player = self.player
        total_points = sum(score.points for score in player.score_set.all())
        player.rating = total_points
        player.save()

    def delete(self):
        player = self.player
        super().delete()
        player_scores = player.score_set.all()
        if player_scores.exists():
            total_points = sum(score.points for score in player_scores)
            player.rating = total_points
        else:
            player.rating = 0
        player.save()
