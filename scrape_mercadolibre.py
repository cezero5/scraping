import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://listado.mercadolibre.com.co/xiaomi-poco#trends_tracking_id=c517079a-95e6-4bac-b8b1-c576ec69b68b&component_id=MOST_WANTED"

response = requests.get(url)

if response.status_code == 200:
    soup = bs(response.text, 'html.parser')
    elements = soup.find_all('div', class_="ui-search-result__wrapper")
    file = open("scraped.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Cellphone", "Price", "Url"])
    for element in elements:
        title = element.find('h2', class_="poly-box poly-component__title").getText()
        price = element.find('span', class_="andes-money-amount andes-money-amount--cents-superscript").getText()
        path = element.find('a').get('href')
        
        if title:
            writer.writerow([title, price, path ])

else: 
    print(f"No open website, code: {response.status_code}")

file.close