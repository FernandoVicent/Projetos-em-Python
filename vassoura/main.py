from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://larouge-belle.com.br/'

response = urlopen(url)
html = response.read
html
