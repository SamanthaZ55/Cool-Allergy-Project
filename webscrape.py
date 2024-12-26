from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

def webscrape():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    product_name = input("what you want?")
    product_name = put_tics_appropriately(product_name)
    search_page = "https://incidecoder.com/products/" + product_name
    #page = requests.get('https://skinsort.com/')
    page = requests.get(search_page, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    a_elements = soup.find_all(class_='ingred-link black')

    ingredients = set()

    for a_element in a_elements:
        # extract the text of the ingredient
        ingredients.add(a_element.text)

    for ingredient in ingredients:
        print(ingredient)


def put_tics_appropriately(input_str):
    output_str = ""
    for let in input_str: 
        if let == ' ': output_str += '-'
        else: output_str += let
    print(output_str)
    return output_str.lower() #search is case sensitive 

# def scrape():
#     product_name = input("what you want?")
#     product_name = put_tics_appropriately(product_name)
#     url = f"https://incidecoder.com/products/{product_name}"
#     print(str(url))
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     ingredient_list = soup.select_one('.ingredlist-short-like-section')

#     print(ingredient_list)

    
if __name__ == "__main__": 
    webscrape() 
