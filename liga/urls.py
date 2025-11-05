# Este é o NOVO arquivo liga/urls.py

from django.urls import path
from . import views  # Importa o arquivo "views.py" da mesma pasta

urlpatterns = [
    # Quando alguém acessar o endereço "", use a função "pagina_inicial"
    path('', views.pagina_inicial, name='pagina_inicial'),
]