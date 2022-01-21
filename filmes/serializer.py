from rest_framework import serializers
from . import models


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filme
        fields = '__all__'
