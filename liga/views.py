# Este é o NOVO arquivo liga/views.py

from django.shortcuts import render
# Importamos agora Time, Jogo E Post
from .models import Time, Jogo, Post 
from django.utils import timezone

def pagina_inicial(request):
    
    # --- 1. LÓGICA DAS NOTÍCIAS (NOVO) ---
    # Busca os 3 posts mais recentes
    ultimas_noticias = Post.objects.all().order_by('-data_publicacao')[:3]

    # --- 2. LÓGICA DA TABELA DE CLASSIFICAÇÃO ---
    
    times = Time.objects.all()
    classificacao = []

    for time in times:
        jogos_casa = Jogo.objects.filter(time_casa=time, realizado=True)
        jogos_visitante = Jogo.objects.filter(time_visitante=time, realizado=True)

        vitorias = 0
        empates = 0
        derrotas = 0
        gols_pro = 0
        gols_contra = 0

        for jogo in jogos_casa:
            gols_pro += jogo.placar_casa
            gols_contra += jogo.placar_visitante
            if jogo.placar_casa > jogo.placar_visitante:
                vitorias += 1
            elif jogo.placar_casa == jogo.placar_visitante:
                empates += 1
            else:
                derrotas += 1
        
        for jogo in jogos_visitante:
            gols_pro += jogo.placar_visitante
            gols_contra += jogo.placar_casa
            if jogo.placar_visitante > jogo.placar_casa:
                vitorias += 1
            elif jogo.placar_visitante == jogo.placar_casa:
                empates += 1
            else:
                derrotas += 1
        
        pontos = (vitorias * 3) + empates
        jogos_disputados = vitorias + empates + derrotas
        saldo_gols = gols_pro - gols_contra

        classificacao.append({
            'time': time,
            'pontos': pontos,
            'jogos_disputados': jogos_disputados,
            'vitorias': vitorias,
            'empates': empates,
            'derrotas': derrotas,
            'gols_pro': gols_pro,
            'gols_contra': gols_contra,
            'saldo_gols': saldo_gols,
        })

    classificacao_ordenada = sorted(
        classificacao, 
        key=lambda item: (item['pontos'], item['saldo_gols'], item['gols_pro']), 
        reverse=True
    )

    # --- 3. LÓGICA DOS JOGOS (Últimos e Próximos) ---
    
    hoje = timezone.now()
    ultimos_resultados = Jogo.objects.filter(realizado=True).order_by('-data_jogo')[:4]
    proximos_jogos = Jogo.objects.filter(realizado=False, data_jogo__gte=hoje).order_by('data_jogo')[:4]

    # --- 4. ENVIAR TUDO PARA O TEMPLATE ---
    
    contexto = {
        'ultimas_noticias': ultimas_noticias,   # <-- Nova variável
        'classificacao': classificacao_ordenada,
        'ultimos_resultados': ultimos_resultados,
        'proximos_jogos': proximos_jogos,
    }
    
    return render(request, 'liga/pagina_inicial.html', contexto)