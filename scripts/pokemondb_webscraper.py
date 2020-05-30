from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from time import time
from warnings import warn
import shutil

BASE_URL = 'https://pokemondb.net'
start_time = time()


def download_image(image):
    response = get(image[1], stream=True)
    # realname = ''.join(e for e in image[1] if e.isalnum())
    
    file = open(('C://Users//Miko Planas//Documents//GitHub'
    '//ProGAN-on-PokemonDB//'
    'dataset//pokemondb//{}.jpg').format(image[0]), 'wb')
    
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response


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
        hrefs.append(soup['href'])

    # line below removes duplicates from list
    final_list = list(dict.fromkeys(hrefs))
    print("Successfully got %d pokemon hrefs" % len(final_list))
    return final_list

url_list = get_href()

# stopped at 518 had too many requests haha
new_url_list = url_list[518:]

requests = 0
for url in new_url_list:

    current_url = BASE_URL + url
    response = get(current_url)

    # youngsleepyboi
    requests += 1
    sleep(randint(8,15))
    elapsed_time = time() - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requests
    , requests/elapsed_time))

    # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    soupy = BeautifulSoup(response.text, "html.parser")

    image = (soupy.find_all('img')[0]['alt'],
            soupy.find_all('img')[0]['src'])
    download_image(image)

# THIS ENDED AT request 518





