from funçoes import *
import re
import requests
from bs4 import BeautifulSoup
def raspagem():
    #from time import sleep

    # padrão de pesquisa do google : https://www.google.com.br/search?q=motos

    pesquisa = input("o que vc procura?: ")


    r = requests.get(f'https://www.google.com.br/search?q={pesquisa}')
    #sleep(2)
    soup = BeautifulSoup(r.text, 'html.parser')
    #
    # tag = soup.findAllNext('h3')
    # # tag['class'] = 'card-title'
    # print(tag)

    parametro_busca = {'href': re.compile('http')}
    file = open('index_data.txt', 'w')

    for tag in soup.find_all('a', attrs=parametro_busca):
        soup_tag = str(tag.get('href'))
        cabecalho(soup_tag)
        file.write((soup_tag))
        file.write('\n')
    file.flush()
    file.close()

raspagem()