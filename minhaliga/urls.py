# Este é o NOVO E CORRIGIDO arquivo minhaliga/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # <-- ADICIONE ESTA LINHA
from django.conf.urls.static import static # <-- ADICIONE ESTA LINHA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('liga.urls')),
]

# Esta linha mágica diz ao Django para servir
# os arquivos de /media/ quando DEBUG = False
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)