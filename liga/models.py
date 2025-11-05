# Este é o NOVO arquivo liga/models.py
from django.db import models
from django.utils import timezone # Adicionamos este import

# --- DEFINIÇÃO DO TIME ---
class Time(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'
    
    def __str__(self):
        return self.nome

# --- DEFINIÇÃO DO JOGO ---
class Jogo(models.Model):
    time_casa = models.ForeignKey(Time, related_name='jogos_casa', on_delete=models.CASCADE)
    placar_casa = models.PositiveIntegerField(default=0)
    
    time_visitante = models.ForeignKey(Time, related_name='jogos_visitante', on_delete=models.CASCADE)
    placar_visitante = models.PositiveIntegerField(default=0)
    
    data_jogo = models.DateTimeField()
    realizado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.time_casa} vs {self.time_visitante} ({self.data_jogo.strftime('%d/%m/%Y')})"

# -----------------------------------------------
# --- NOVA CLASSE: POST DE NOTÍCIA (Fase 3) ---
# -----------------------------------------------
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    # O upload_to='posts/' vai salvar as imagens na pasta /media/posts/
    imagem_capa = models.ImageField(upload_to='posts/', null=True, blank=True)
    # TextField é usado para textos longos
    conteudo = models.TextField()
    # auto_now_add=True define a data automaticamente quando o post é criado
    data_publicacao = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        # Ordena as notícias da mais nova para a mais antiga por padrão
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo