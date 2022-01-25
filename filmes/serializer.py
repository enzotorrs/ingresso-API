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


class FilmeBreveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilmeBreve
        fields = '__all__'

class FanShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FanShop
        fields = '__all__'
