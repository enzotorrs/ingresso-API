from django.core.management.base import BaseCommand
from filmes import scraping, models


class Command(BaseCommand):
    help = 'faz scraping do site e atualiza os filmes no banco'
    
    def atualiza_filmes(self):
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


    def atualiza_noticias(self):
        noticias = scraping.noticias()

        models.Noticia.objects.all().delete()

        for noticia in noticias:
            nova_noticia = models.Noticia(
                titulo=noticia['titulo'],
                descricao=noticia['descricao'],
                imagem=noticia['img'],
            )
            nova_noticia.save()
        self.stdout.write('noticias atualizadas')
    
    def atualiza_filmes_breve(self):
        filmes_breve = scraping.filmes_breve()

        for filme in filmes_breve:
            novo_filme = models.FilmeBreve(
                titulo=filme['titulo'],
                data_lancamento=filme['data'],
                imagem_font=filme['img'],
            )
            novo_filme.save()
            
    def handle(self, *args, **kwargs):
        self.atualiza_filmes()
        self.atualiza_noticias()
        self.atualiza_filmes_breve()
