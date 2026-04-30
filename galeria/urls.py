from django.urls import path
from galeria.views import index, imagem
from galeria.views import buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:fotografia_id>/', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
]