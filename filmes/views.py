from rest_framework import viewsets
from . import models
from . import serializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.all()
    serializer_class = serializer.FilmeSerializer
    http_method_names = ['get', 'head']


class FilmeAltaViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(em_alta=True)
    serializer_class = serializer.FilmeSerializer
    http_method_names = ['get', 'head']


class FilmeCartazViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(em_cartaz=True)
    serializer_class = serializer.FilmeSerializer
    http_method_names = ['get', 'head']


class FilmePrincipalViewSet(viewsets.ModelViewSet):
    queryset = models.Filme.objects.filter(principal=True)
    serializer_class = serializer.FilmeSerializer
    http_method_names = ['get', 'head']


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = models.Noticia.objects.all()
    serializer_class = serializer.NoticiaSerializer
    http_method_names = ['get', 'head']


class FilmeBreveViewSet(viewsets.ModelViewSet):
    queryset = models.FilmeBreve.objects.all()
    serializer_class = serializer.FilmeBreveSerializer
    http_method_names = ['get', 'head']

class FanShopViewSet(viewsets.ModelViewSet):
    queryset = models.FanShop.objects.all()
    serializer_class = serializer.FanShopSerializer
    http_method_names = ['get', 'head']

class CinemaViewSet(viewsets.ModelViewSet):
    queryset = models.Cinema.objects.all()
    serializer_class = serializer.CinemaSerializer
    http_method_names = ['get', 'head']
