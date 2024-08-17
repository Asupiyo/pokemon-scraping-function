# This is a sample Python script.
import requests
import csv
import os
from bs4 import BeautifulSoup


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def delete_file():
    file_path = 'pokemon_data.csv'
    if os.path.exists(file_path):
        os.remove(file_path)


def scrape():
    # Use a breakpoint in the code line below to debug your script.
    pokemons_data = []
    result = requests.get("https://gamewith.jp/pokemon-sv/article/show/372239")
    html_doc = result.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    for pokemon in soup.find_all('table')[0].find_all('tr')[1:]:
        name = pokemon.find_all('td')[0].text
        photo = pokemon.find_all('img')[1]['src']
        if pokemon.find_all('td')[1].find('br').next_sibling.strip() != '①「ふしぎなおくりもの」を選択':
            password = pokemon.find_all('td')[1].find('br').next_sibling.strip()
        else:
            password = "ふしぎなおくりものを選択して、インターネットで受け取るを選ぶ"
        span_with_keyword = pokemon.find('span', string=lambda t: '受取期限' in t)
        br_after_span = span_with_keyword.find_next('br')
        if br_after_span.next_sibling.name == 'span':
            due_to = br_after_span.next_sibling.text.strip()
        else:
            due_to = br_after_span.next_sibling.strip()
        pokemon_data = {'name': name, 'photo': photo, 'password': password, 'due_to': due_to}
        pokemons_data.append(pokemon_data)
    return pokemons_data


def write_to_file(pokemon_rows):
    with open('pokemon_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        for pokemon_row in pokemon_rows[0:]:
            writer = csv.writer(csvfile)
            writer.writerow([pokemon_row['name'], pokemon_row['photo'], pokemon_row['password'], pokemon_row['due_to']])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # delete_file()
    write_to_file(scrape())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
