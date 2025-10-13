# Register your models here.
from django.contrib import admin

from .models.fichas import Ficha


@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ("nome", "classe", "raca", "nivel", "jogador", "updated_at")
    search_fields = ("nome", "classe", "jogador", "raca")
    readonly_fields = ("created_at", "updated_at")
