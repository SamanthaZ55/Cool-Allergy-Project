from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://incidecoder.com/products/benton-snail-bee-high-content-essence-5', headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

a_elements = soup.find_all(class_='ingred-link black')

ingredients = set()

for a_element in a_elements:
    # extract the text of the ingredient
    ingredients.add(a_element.text)

for ingredient in ingredients:
    print(ingredient)
