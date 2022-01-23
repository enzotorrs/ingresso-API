from django.core.management.base import BaseCommand
from filmes import scraping, models


class Command(BaseCommand):
    help = 'faz scraping do site e atualiza os filmes no banco'

    def handle(self, *args, **kwargs):
        filmes = scraping.filmes()
        filmes_em_alta = scraping.filmes_em_alta()
        filmes_em_cartaz = scraping.filmes_em_cartaz()
        filme_principal = scraping.filme_principal()
        
        models.Filme.objects.all().delete()

        for filme in filmes:
            titulo = filme['titulo']
            imagem = filme['img']

            if '\n' in titulo:
                continue

            if titulo == filme_principal['titulo']:
                imagem_principal = filme_principal['img']
                principal = True

            else:
                principal = False
                imagem_principal = None

            novo_filme = models.Filme(
                nome_filme=titulo,
                imagem_font=imagem,
                em_alta=titulo in filmes_em_alta,
                em_cartaz=titulo in filmes_em_cartaz,
                principal=principal,
                principal_imagem_font= imagem_principal,
            )
            novo_filme.save()

        self.stdout.write('banco atualizado')
