import html
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.olx.ua/uk/transport/legkovye-avtomobili/"
HOST = "https://www.olx.ua"
CSV = "cool.csv"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

}

title_class = "css-hzlye5"
price_class = "css-blr5zl"
location_class = "css-1b24pxk"
specifications_class = "css-h59g4b"
link_class = "css-1tqlkj0"
image_class = "css-8wsg1m"


def get_html(url, params=""):
    request = requests.get(url, headers = HEADERS, params = params)
    return request

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="css-1r93q13")
    cards = []
    for item in items:
        title_item = item.find("h4", class_=title_class)
        title = title_item.get_text(strip=True) if title_item else "No title"

        price_item = item.find("p", class_=price_class)
        price = price_item.get_text(strip=True) if price_item else "No price"

        location_item = item.find("p", class_=location_class)
        location = location_item.get_text(strip=True) if location_item else "No location"

        specifications_item = item.find("span", class_=specifications_class)
        specifications = specifications_item.get_text(strip=True) if specifications_item else "No specifications"

        link_item = item.find("a", class_=link_class)
        link = HOST + link_item.get("href") if link_item and link_item.get("href") else "No link"

        image_item = item.find("img", class_=image_class)
        image = image_item.get("src") if image_item and image_item.get("src") else "No image"

        cards.append({
            "Title": title,
            "Price": price,
            "Location": location,
            "Specifications": specifications,
            "Link": link,
            "Image": image
        })
    return cards


def save_to_csv(cards,path):
    with open(path, "w", newline="", encoding ="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Title', 'Price', 'Location', 'Specifications', 'Link', 'Image'])
        for card in cards:
            writer.writerow([
                card["Title"],
                card['Price'],
                card['Location'],
                card['Specifications'],
                card['Link'],
                card['Image']
            ])
def parser():
    pagination = int(input("Enter the number of pages to parse > "))
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1,pagination + 1):
            print(f"Parsing page {str(page)}/{pagination}...")
            html = get_html(URL, params={"page": page})
            cards.extend(get_content(html.text))
        save_to_csv(cards,CSV)
        print(f"Done! Parsed {len(cards)} cards. Saved to {CSV}")
    else:
        print("Error")

parser()