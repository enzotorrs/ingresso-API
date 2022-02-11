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
            titulo = filme['name']
            imagem = filme['img']
            atores = filme['actors']
            descricao = filme['description']
            produtora = filme['productionCompany']
            pais = filme['countryOfOrigin']
            diretor = filme['director']
            categorias = filme['categorias']

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
                atores=atores,
                descricao=descricao,
                produtora=produtora,
                pais=pais,
                diretor=diretor,
                categorias=categorias,
            )
            self.stdout.write('filme "%s" adicionado ao banco' % titulo)
            novo_filme.save()

        self.stdout.write(self.style.SUCCESS('filmes atualizados com sucesso'))


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
            self.stdout.write('noticia "%s" adicionada ao banco' % noticia['titulo'])
        self.stdout.write(self.style.SUCCESS('noticias atualizadas'))
    
    def atualiza_filmes_breve(self):
        filmes_breve = scraping.filmes_breve()

        models.FilmeBreve.objects.all().delete()

        for filme in filmes_breve:
            novo_filme = models.FilmeBreve(
                titulo=filme['titulo'],
                data_lancamento=filme['data'],
                imagem_font=filme['img'],
            )
            novo_filme.save()
            
    def atualiza_fanshop(self):
        fan_shop = scraping.fanshop()

        models.FanShop.objects.all().delete()

        for imagem in fan_shop:
            nova_imagem = models.FanShop(
            imagem_font=imagem,
            )
            nova_imagem.save()

    def atualiza_cinemas(self):
        dados_cinemas = scraping.cinemas()

        models.Cinema.objects.all().delete()

        for bairro in dados_cinemas.keys():
            for cinema in dados_cinemas[bairro]:
                novo_cinema = models.Cinema(
                    bairro=bairro,
                    nome=cinema['nome'],
                    endereco=cinema['endereco'],
                )
                self.stdout.write('cinema "%s" adicionado ao banco' % cinema['nome'])
                novo_cinema.save()
        self.stdout.write(self.style.SUCCESS('cinemas atualizados com sucesso'))

    def handle(self, *args, **kwargs):
        self.atualiza_filmes()
        self.atualiza_noticias()
        self.atualiza_filmes_breve()
        self.atualiza_fanshop()
        self.atualiza_cinemas()
