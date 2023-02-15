# import requests
# import csv
# from bs4 import BeautifulSoup
#
#
# def scrape_mobile_info(num_pages):
#     HOST = 'https://softech.kg/'
#
#     URL = 'https://softech.kg/phones/apple-smartphone/'
#
#     HEADERS = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
#     }
#
#     result_html = requests.get(url=URL, headers=HEADERS)
#
#     with open('softtech.html', 'w') as file:
#         file.write(result_html.text)
#
#
#     with open('softtech.csv', 'w') as csv_file:
#         file = csv.writer(csv_file, delimiter=',')
#         file.writerow(['Название', 'Цена', 'Описание', 'Картинка'])
#
#         for i in range(1):
#             URL = f'https://softech.kg/phones/apple-smartphone/={i}'
#
#             result_html = requests.get(url=URL, headers=HEADERS)
#             soup = BeautifulSoup(result_html.text, 'lxml')
#             items = soup.findAll('div', class_='product-thumb transition ')
#
#             for item in items:
#                 temp_list = list()
#                 temp_list.append(item.find('div', class_="description-small").get_text(strip=True))
#                 # temp_list.append(item.find('p', class_='price').get_text(strip=True))
#                 # temp_list.append(item.find('p', class_='description').get_text(strip=True))
#                 # img_url = item.find("img")["src"]
#                 # temp_list.append(img_url)
#
#                 file.writerow(temp_list)
#
# scrape_mobile_info(23)

import requests
import csv
from bs4 import BeautifulSoup


def scrape_mobile_info(num_pages, responsive=None):
    HOST = 'https://softech.kg/'

    URL = 'https://softech.kg/phones/apple-smartphone/'

    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
    }

    with open('softtech.csv', 'w') as csv_file:
        file = csv.writer(csv_file, delimiter=',')
        file.writerow(['Название', 'Цена', 'Описание', 'Картинка'])

        for i in range(num_pages):
            URL = f'https://softech.kg/phones/apple-smartphone/?page={i}'

            result_html = requests.get(url=URL, headers=HEADERS)
            soup = BeautifulSoup(result_html.text, 'lxml')
            items = soup.findAll('div', class_='product-thumb transition')

            for item in items:
                temp_list = list()
                temp_list.append(item.find('div', class_="name").get_text(strip=True))
                temp_list.append(item.find('div', class_='price').get_text(strip=True))
                temp_list.append(item.find('div', class_='description-small').get_text(strip=True))
                temp_list.append(item.find('a').get('href'))
                # img_url = item.find("img")["src"]
                # temp_list.append(img_url)

                file.writerow(temp_list)

scrape_mobile_info(23)