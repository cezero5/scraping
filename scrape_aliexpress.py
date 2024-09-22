import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://www.aliexpress.com/gcp/300000533/KDdtyft4ys?spm=a2g0o.best.testStatic.3.544b22aebRQo39&disableNav=YES&pha_manifest=ssr&_immersiveMode=true&_gl=1*10lfh4p*_gcl_aw*R0NMLjE3MjY5ODAxNjYuQ2owS0NRanczYm0zQmhESkFSSXNBS25Ib1ZVMkM1djR0NV81UHdvREVOOVZXRUxxanc1Qk1Yb25JemhhN2szV2JoZUxJaGxKdnNYdzJjSWFBbFBfRUFMd193Y0I.*_gcl_au*OTUzMTY0MjU0LjE3MjY5ODAxNjU.*_ga*NDc3MDM3MDE0LjE3MjY5ODAxNjY.*_ga_VED1YSGNC7*MTcyNjk4MDE2NS4xLjAuMTcyNjk4MDE2NS42MC4wLjA."

response = requests.get(url)

if response.status_code == 200:
    file = open("scraped.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Name Console", "Price", "Url"])
    soup = bs(response.text, 'html.parser')
    elements = soup.find_all('a', class_="productContainer ")
    for element in elements:
        name_console = element.find('span', class_="AIC-ATM-multiLine")
        price_console = element.find('div', class_="rax-view-v2")
        url_console = element.find('a')
        
        if name_console:
            writer.writerow([name_console.text.strip(), price_console.text.strip(), url_console['href'] ])
else:
    print(f"No open website, code: {response.status_code}")