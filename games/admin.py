# Register your models here.
from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'start_date', 'created_at']
    search_fields = ['title', 'location']
    list_filter = ['start_date', 'created_at']