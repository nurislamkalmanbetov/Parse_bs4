import requests
import csv
from bs4 import BeautifulSoup

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    'User-Agen :Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
}


def get_html_page(url, params):
    response = requests.get(url=url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return False

def get_all_block(html, tag, tag_class):
    return html.findAll(tag, class_=tag_class)


def get_content():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    result_list = list()
    with open('mobiles2.csv', 'w') as csv_file:
        file = csv.writer(csv_file, delimiter=',')
        file.writerow(['Название', 'Цена', 'Скидка', 'Описание', 'Картинка'])
        for i in range(1,10):
            html = get_html_page(url, {'page': i})
            if html:
                soup_html = BeautifulSoup(html, 'html.parser')
                products = get_all_block(soup_html, 'div', 'item product_listbox oh')
                for item in products:
                    temp_list = list()
                    temp_list.append(item.find('div', class_="listbox_title oh").get_text(strip=True))
                    price = item.find('div', class_='listbox_price text-center')
                    temp_list.append(price.find('strong').get_text(strip=True))
                    oldprice = price.find('span', class_='oldprice')
                    if oldprice:
                        temp_list.append(oldprice.get_text(strip=True))
                    else:
                        temp_list.append('')
                        temp_list.append(item.find('div', class_='product_text pull-left').get_text(strip=True))
                    result_list.append(temp_list)
        return result_list



res = get_content()

for i in res:
    print(i)

