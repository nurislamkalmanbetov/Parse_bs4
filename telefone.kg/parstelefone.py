import requests
import csv
from bs4 import BeautifulSoup


def scrape_mobile_info(num_pages):
    HOST = 'https://telefon.kg/'
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
    }

    with open('my-project-env/telefone.csv', 'w', newline='', encoding='utf-8') as csv_file:
        file = csv.writer(csv_file, delimiter=',')
        file.writerow(['Название', 'Цена', 'Описание', 'Картинка'])

        for i in range(num_pages):
            URL = f'https://telefon.kg/smartphone?page={i}'
            result_html = requests.get(url=URL, headers=HEADERS)
            soup = BeautifulSoup(result_html.text, 'lxml')
            items = soup.findAll('div', class_='product-thumb thumbnail')

            for item in items:
                temp_list = list()
                temp_list.append(item.find('div', class_="caption").get_text(strip=True))
                temp_list.append(item.find('p', class_='price').get_text(strip=True))
                temp_list.append(item.find('p', class_='description').get_text(strip=True))
                img_url = item.find("img")["src"]
                temp_list.append(img_url)

                file.writerow(temp_list)

scrape_mobile_info(23)
