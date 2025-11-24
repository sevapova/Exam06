import django_filters
from .models import Player

class PlayerFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='iexact')
    min_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    search = django_filters.CharFilter(field_name='nickname', lookup_expr='icontains')

    class Meta:
        model = Player
        fields = ['country']