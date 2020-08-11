from PIL import Image
from glob import glob
from tqdm import tqdm
import os
from requests import get
from bs4 import BeautifulSoup

# sorry i'm not using my other script for this
def get_href():
    '''
    returns full list of pokemon hyperlink references
    in the format '/pokedex/bulbasaur'

    using this for image scraping on multiple pages
    '''

    URL = 'https://pokemondb.net/pokedex/all'
    hrefs = []

    response = get(URL)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    html_soup_1 = html_soup.find_all('a', class_="ent-name")

    for soup in html_soup_1:
        hrefs.append(soup.text)

    # line below removes duplicates from list
    final_list = list(dict.fromkeys(hrefs))
    print("Successfully got %d pokemon hrefs" % len(final_list))
    return final_list

url_list = sorted(get_href())

print(url_list[0])
os.chdir('C://Users//Miko Planas//Documents//GitHub//ProGAN-on-PokemonDB//dataset//pokemondb_raw')

bg = Image.new('RGB',(500,500), color=(255, 255, 255))

# names for the pokemon jpgs
# how to perfectly center for all

num = 0

for file in glob('*.jpg'):
    os.chdir('C://Users//Miko Planas//Documents//GitHub//ProGAN-on-PokemonDB//dataset//pokemondb_raw')
    im1 = Image.open(file)
    bg_copy = bg.copy()
    bg_copy.paste(im1, (50, 50))
    os.chdir('C://Users//Miko Planas//Documents//GitHub//ProGAN-on-PokemonDB//dataset//pokemon_dataset')
    bg_copy.save('{}.jpg'.format(url_list[num]))
    num += 1