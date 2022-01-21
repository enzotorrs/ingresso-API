from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .import serializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.all()
    serializer_class = serializer.FilmeSerializer


def atualiza_banco(request):
    return render(request, 'atualiza_banco.html')
