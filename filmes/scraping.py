import requests
from bs4 import BeautifulSoup


def filmes_em_alta() -> list:
    filmes_em_alta = []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    carrosel = soup.find(class_='em-alta carousel-box')
    filmes = carrosel.find_all('article')

    for filme in filmes:
        caracteristicas = {}

        caracteristicas['titulo'] = filme.get_text().strip()

        img = filme.find('img')
        caracteristicas['img'] =  img['src'].strip()

        filmes_em_alta.append(caracteristicas.copy())
    return filmes_em_alta
