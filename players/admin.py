# Register your models here.
from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'country', 'rating', 'created_at']
    search_fields = ['nickname', 'country']
    list_filter = ['country', 'created_at']