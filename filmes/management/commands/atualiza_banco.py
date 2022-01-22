from django.core.management.base import BaseCommand
from filmes import scraping, models


class Command(BaseCommand):
    help = 'faz scraping do site e atualiza os filmes no banco'

    def handle(self, *args, **kwargs):
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

            self.stdout.write('banco atualizado')
