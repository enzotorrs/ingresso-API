from rest_framework import serializers
from . import models


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filme
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Noticia
        fields = '__all__'
