from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer
from . import scraping


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.all()
    serializer_class = serializer.FilmeSerializer


class FilmeAltaViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(em_alta=True)
    serializer_class = serializer.FilmeSerializer

class FilmeCartazViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(em_cartaz=True)
    serializer_class = serializer.FilmeSerializer


def atualiza_banco(request):
    filmes = scraping.filmes()
    filmes_em_alta = scraping.filmes_em_alta()
    filmes_em_cartaz = scraping.filmes_em_cartaz()
    
    models.Filme.objects.all().delete()

    for filme in filmes:
        novo_filme = models.Filme(
            nome_filme=filme['titulo'],
            imagem_font=filme['img'],
            em_alta=filme['titulo'] in filmes_em_alta,
            em_cartaz=filme['titulo'] in filmes_em_cartaz,
        )
        novo_filme.save()

    return render(request, 'atualiza_banco.html')
