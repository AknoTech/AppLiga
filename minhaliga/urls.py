# Este é o NOVO E CORRIGIDO arquivo minhaliga/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # <-- ADICIONE ESTA LINHA
from django.conf.urls.static import static # <-- ADICIONE ESTA LINHA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('liga.urls')),
]

# ESTE BLOCO MÁGICO CONSERTA O ERRO 500
# Ele diz ao Django para mostrar as imagens de mídia
# mesmo quando DEBUG = False
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)