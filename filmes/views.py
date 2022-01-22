from rest_framework import viewsets
from . import models
from . import serializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.all()
    serializer_class = serializer.FilmeSerializer


class FilmeAltaViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(em_alta=True)
    serializer_class = serializer.FilmeSerializer


class FilmeCartazViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(em_cartaz=True)
    serializer_class = serializer.FilmeSerializer


class FilmePrincipalViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(principal=True)
    serializer_class = serializer.FilmeSerializer
