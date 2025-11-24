# Register your models here.
from django.contrib import admin
from .models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['player', 'game', 'result', 'points', 'created_at']
    list_filter = ['result', 'game', 'created_at']
    search_fields = ['player__nickname', 'game__title', 'opponent_name']