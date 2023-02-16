import requests
from bs4 import BeautifulSoup as BS

URL = "https://www.house.kg/snyat-kvartiru?region=1&town=2&sort_by=upped_at+desc"

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_posts_links(html): # доставет 10 ссылок, с каждой страницы
    links = []
    soup = BS(html, "html.parser")
    container = soup.find("div", {"class":"container body-container"}) #главный container где все продукты
    main = container.find("div", {"class":"main-content"})
    listings = main.find("div", {"class":"listings-wrapper"})
    posts = listings.find_all("div", {"class":"listing"})
    for post in posts:
        header = post.find("div", {"class":"left-side"}) # header - переменная, чтобы выташить описание из дива
        link = header.find("a").get("href")
        full_link = "https://www.house.kg"+link
        links.append(full_link)
    return links


def get_post_data(html): # функция, для вывоза инвы с детальной страницы изнутри
    soup = BS(html, "html.parser")
    main = soup.find("div", {"class":"main-content"}) # внутренний див страницы 
    header = main.find("div", {"class":"details-header"})
    title = header.find("div", {"class":"left"}).find("h1").text.strip()
    address = header.find("div", {"class":"address"}).text.strip()
    som = header.find("div", {"class":"price-som"}).text.strip()
    dollar = header.find("div", {"class":"price-dollar"}).text.strip()
    mobile = main.find("div", {"class":"number"}).text.strip()
    desc = main.find("div", {"class":"details-main"}).find("div", {"class":"description"}).text.strip()
    lon = main.find("div", {"id":"map2gis"}).get("data-lon")
    lat = main.find("div", {"id":"map2gis"}).get("data-lat")


def main():
    html = get_html(URL)

    links=get_posts_links(html)
    for link in links:
        detail_html = get_html(link)
        get_post_data(detail_html) # вызывает



if __name__=="__main__": # парсинг обещан запускатся на прямую таким образом
    main()
