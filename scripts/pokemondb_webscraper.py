from requests import get
from bs4 import BeautifulSoup

url = 'https://pokemondb.net/pokedex/charizard'
response = get(url)
# print(response.text)

html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup.find_all('img'))

