from django.db import models

class Filme(models.Model):
    nome_filme = models.CharField(max_length=255)
    imagem_font = models.TextField()
    em_alta = models.BooleanField(default=False)
    em_cartaz = models.BooleanField(default=False)
    principal = models.BooleanField(default=False)
    principal_imagem_font = models.TextField(null=True)


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.TextField()


class FilmeBreve(models.Model):
    titulo = models.CharField(max_length=255)
    imagem_font = models.TextField()
    data_lancamento = models.CharField(max_length=20, null=True, blank=True, default=None)
