import asyncio
import requests
from bs4 import BeautifulSoup
from pyppeteer import launch 
from time import sleep


def filmes_em_alta() -> list:
    filmes_em_alta = []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    carrosel = soup.find(class_='em-alta carousel-box')
    filmes = carrosel.find_all('article')

    for filme in filmes:
        titulo_filme_html = filme.find(attrs={'itemprop': 'name'})
        titulo_filme = titulo_filme_html.get_text().strip()

        filmes_em_alta.append(titulo_filme)

    return filmes_em_alta

def filmes_em_cartaz() -> list:
    filmes_em_cartaz= []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    carrosel = soup.find(class_='em-cartaz carousel-box')
    filmes = carrosel.find_all('article')

    for filme in filmes:
        titulo_filme_html = filme.find(attrs={'itemprop': 'name'})
        if titulo_filme_html is None:
            continue
        titulo_filme = titulo_filme_html.get_text().strip()

        filmes_em_cartaz.append(titulo_filme)

    return filmes_em_cartaz

async def get_filmes():
    browser = await launch(
    handleSIGINT=False,
    handleSIGTERM=False,
    handleSIGHUP=False,
    headless=True,
    args=['--no-sandbox'],

    )
    page = await browser.newPage()
    await page.goto('https://www.ingresso.com/filmes?city=sao-paulo&partnership=home', {'waitUntil' : 'networkidle2'})
    page_content = await page.content() 

    await browser.close()

    return page_content

def extrai_categorias(filmes) -> str:
    atributos = filmes.find(attrs={'onmousedown': True})
    html = atributos['onmousedown']

    if 'trackProductClick' and 'category' in html:
        html = html.split('\n')
        html = html[4].split(':')
        html = html[1].replace("'", "").replace(',', '').strip()
        return html

def filmes() -> list:
    todos_filmes = []

    page = asyncio.run(get_filmes())
    soup = BeautifulSoup(page, 'html.parser')

    filmes = soup.find_all(class_='card ing-small')

    for filme in filmes:
        caracteristicas = {}
        caracteristicas['categorias'] = extrai_categorias(filme)
        propriedades = filme.find_all(attrs={'itemprop': True})

        for propriedade in propriedades:
            if propriedade['itemprop'] == 'image':
                continue

            try:
                caracteristicas[propriedade['itemprop']] = propriedade['content'].strip()

            except KeyError:
                caracteristicas[propriedade['itemprop']] = propriedade.get_text().strip()

        img = filme.find('img')
        caracteristicas['img'] =  img['src'].strip()

        todos_filmes.append(caracteristicas.copy())

    return todos_filmes

def filme_principal() -> dict:
    filme = {}

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    banner = soup.find_all(class_='main-home-banner')[1]
    
    titulo = banner.get_text().strip()

    titulo = titulo.split('\n')
    filme['titulo'] = titulo[0] 

    picture = banner.find('picture')
    source = picture.find('source')
    filme['img'] = source['srcset']

    return filme

def noticias() -> list:
    noticias = []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    noticias_html = soup.find_all(class_='news-h-article')

    for noticia in noticias_html:
        caracteristicas = {}

        img = noticia.find('img')

        caracteristicas['img'] = img['src']

        caracteristicas['titulo'] = noticia.find('h2').get_text()
        caracteristicas['descricao'] = noticia.find('p').get_text()

        noticias.append(caracteristicas.copy())

    return noticias

async def get_filmes_em_breve():
    browser = await launch(
    handleSIGINT=False,
    handleSIGTERM=False,
    handleSIGHUP=False,
    headless=True,
    args=['--no-sandbox'],
    )

    page = await browser.newPage()
    await page.goto('https://www.ingresso.com/filmes?city=sao-paulo&partnership=home', {'waitUntil' : 'networkidle2'})

    botao_breve = await page.querySelector('#tab-coming-soon')

    await page.evaluate('(botao_breve) => botao_breve.click()', botao_breve)
    await page.waitForSelector('#coming-soon .movie-list-small li:nth-child(20)')
    
    page_content = await page.content() 
    await browser.close()

    return page_content

def filmes_breve() -> list:
    filmes_em_breve = []

    page = asyncio.run(get_filmes_em_breve())
    soup = BeautifulSoup(page, 'html.parser')

    filmes = soup.find_all(class_='movie-list-small')[1]

    for filme in filmes:
        caracteristicas = {}

        artigo = filme.find('article')
        if artigo == -1:
            continue 

        caracteristicas['titulo'] = artigo.find(class_='card-title').get_text().strip()

        data = artigo.find(class_='tags-box')
        data = data.get_text().strip()
        if data == '':
            data = None

        caracteristicas['data'] = data

        img = artigo.find('img')
        caracteristicas['img'] = img['src'].strip()

        filmes_em_breve.append(caracteristicas.copy())

    return filmes_em_breve

def fanshop() -> list:
    imagems_produtos = []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    carrosel_produtos = soup.find(attrs={'data-ride':'swiper-ingresso-list-products'})
    produtos = carrosel_produtos.find_all(class_="swiper-slide")
    for produto in produtos:
        img = produto.find('img')
        imagems_produtos.append(img['src'])

    return imagems_produtos 

def cinemas() -> dict:
    dados = dict()
    cinemas = list()
    cinema = dict()

    page = requests.get('https://www.ingresso.com/cinemas?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.content, 'html.parser')

    lista_de_bairros = soup.find(class_='o-hidden')
    bairros = lista_de_bairros.find_all(class_='hide-favorite')

    for bairro in bairros:
        nome_do_bairro = bairro.find('span').get_text().strip()
        cinemas_soup = bairro.find_all(class_='card-theater')

        for cinema_soup in cinemas_soup:
            propriedades = cinema_soup.find_all(attrs={'itemprop': True})
            for propriedade in propriedades:
                if propriedade['itemprop'] == 'address':
                    cinema['endereco'] = propriedade['content']

                elif propriedade['itemprop'] == 'name':
                    cinema['nome'] = propriedade.get_text().strip()

            cinemas.append(cinema.copy())

        dados[nome_do_bairro] = cinemas.copy()
        cinemas.clear()

    return dados
if __name__ == '__main__':
    for filme in filmes_em_alta():
        print(filme)
    for filme in filmes_em_cartaz():
        print(filme)
