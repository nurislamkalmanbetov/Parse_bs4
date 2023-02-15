# example1
# import requests
# import csv
# from bs4 import BeautifulSoup
#
#
# def scrape_mobile_info(num_pages):
#     HOST = 'https://myphone.kg/'
#     HEADERS = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
#     }
#
#     with open('my-project-env/myphone.csv', 'w', newline='', encoding='utf-8') as csv_file:
#         file = csv.writer(csv_file, delimiter=',')
#         file.writerow(['Название', 'Цена', 'Описание', 'Картинка', 'Ссылка на товар'])
#
#         for i in range(num_pages):
#             URL = f'https://myphone.kg/ru/catalog/cell={i}'
#             result_html = requests.get(url=URL, headers=HEADERS)
#             soup = BeautifulSoup(result_html.text, 'lxml')
#             items = soup.findAll('div', class_='col-sm-4 col-xs-6')
#
#             for item in items:
#                 temp_list = list()
#                 temp_list.append(item.find('div', class_="title").get_text(strip=True))
#                 temp_list.append(item.find('div', class_='price').get_text(strip=True))
#                 temp_list.append(item.find('span').get_text(strip=True))
#                 # temp_list.append(item.find('a').get('href'))
#                 img_url = item.find("img")["src"]
#                 temp_list.append(img_url)
#                 domain = 'https://myphone.kg'
#                 temp_list.append(domain + item.find('a').get('href'))
#                 file.writerow(temp_list)
#
# scrape_mobile_info(23)
# __________________________________________________________________________
# example 2
# import requests
# import csv
# from bs4 import BeautifulSoup
#
#
# HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
#     'User-Agen :Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
# }
#
#
# def get_html_page(url, params=''):
#     response = requests.get(url=url, headers=HEADERS, params=params)
#
#     if response.status_code == 200:
#         return response.text
#     else:
#         return False
#
#
# def get_one_block(block, tag, tag_class):
#     return block.find(tag, class_=tag_class)
#
#
# def get_all_block(html, tag, tag_class):
#     return html.findAll(tag, class_=tag_class)
#
#
# def get_detail_info(url):
#     html = get_html_page(url)
#     if html:
#         soup_html = BeautifulSoup(html, 'html.parser')
#         return get_one_block(soup_html, 'div', 'cont')
#
#
# def get_content():
#     url = 'https://www.myphone.kg/ru/catalog/cell?sort%5Bby%5D=id&sort%5Bord%5D=desc&brn%5B%5D=5&price%5Bmin%5D=&price%5Bmax%5D='
#     result_list = list()
#
#     for i in range(1):
#         html = get_html_page(url)
#
#         if html:
#             soup_html = BeautifulSoup(html, 'html.parser')
#             products = get_all_block(soup_html, 'div', 'block-content')
#
#             for prod in products:
#                 temp_list = list()
#                 title = prod.find('div', class_='title')
#                 temp_list.append(
#                     title.get_text(strip=True))
#                 price = prod.find('div', class_='price')
#                 if price:
#                     temp_list.append(price.get_text(strip=True))
#                 else:
#                     temp_list.append('')
#
#                 if title.find('a'):
#                     detail_url = f"https://myphone.kg{title.find('a').get('href')}"
#                     data = get_detail_info(detail_url)
#                     temp_list.append(data.get_text(strip=True))
#
#                 result_list.append(temp_list)
#
#                 # img_url = prod.find('img')['src']
#                 # temp_list.append(img_url)
#
#     return result_list
#
#
# def get_content_info():
#     url = 'https://www.myphone.kg/ru/catalog/cell/i3000/iphone_14_pro'
#     result_list = list()
#
#     for i in range(1):
#         html = get_html_page(url)
#
#         if html:
#             soup = BeautifulSoup(html, 'html.parser')
#             products = get_all_block(soup, 'div', 'cont product-spec')
#
#             for prod in products:
#                 temp_list = list()
#                 temp_info = prod.find('div', class_='la3zd')
#                 if temp_info:
#                     temp_list.append(temp_info.get_text(strip=True))
#                 else:
#                     temp_list.append('')
#                 result_list.append(temp_list)
#
#                 with open('phone.csv', 'a+') as csv_file:
#                     file = csv.writer(csv_file, delimiter=',')
#                     file.writerow(['Описание'])
#                     file.writerows(result_list)
#
#     return result_list
#
#
# def data_to_csv(data_list):
#     with open('myphone.csv', 'w') as csv_file:
#         file = csv.writer(csv_file, delimiter=',')
#         file.writerow(['Название', 'Цена', 'Описание'])
#         for line in data_list:
#             file.writerow(line)
#
#
# res = get_content()
#
# data_to_csv(res)
