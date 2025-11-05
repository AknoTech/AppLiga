# Este é o NOVO arquivo liga/admin.py

from django.contrib import admin
# Importamos agora o Time, o Jogo E o Post
from .models import Time, Jogo, Post

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('time_casa', 'placar_casa', 'time_visitante', 'placar_visitante', 'data_jogo', 'realizado')
    list_filter = ('realizado', 'data_jogo')
    search_fields = ('time_casa__nome', 'time_visitante__nome')

# -----------------------------------------------
# --- NOVO REGISTRO DO POST (Fase 3) ---
# -----------------------------------------------
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # O que vai aparecer na lista de notícias
    list_display = ('titulo', 'data_publicacao')
    # Campos para busca
    search_fields = ('titulo', 'conteudo')
    # Filtro rápido pela data
    list_filter = ('data_publicacao',)