from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer
from . import scraping


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.all()
    serializer_class = serializer.FilmeSerializer


def atualiza_banco(request):
    filmes_em_alta = scraping.filmes_em_alta()
    
    models.Filme.objects.all().delete()

    for filme in filmes_em_alta:
        novo_filme = models.Filme(
            nome_filme=filme['titulo'],
            imagem_font=filme['img'],
            em_alta= True,
            em_cartaz=True,
        )
        novo_filme.save()

    return render(request, 'atualiza_banco.html')
