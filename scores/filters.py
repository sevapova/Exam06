import django_filters
from .models import Score

class ScoreFilter(django_filters.FilterSet):
    game_id = django_filters.NumberFilter(field_name='game_id')
    player_id = django_filters.NumberFilter(field_name='player_id')
    result = django_filters.ChoiceFilter(choices=Score.RESULT_CHOICES)

    class Meta:
        model = Score
        fields = ['game_id', 'player_id', 'result']