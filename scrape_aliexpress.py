from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import csv
import re

driver = webdriver.Chrome()
url = "https://www.aliexpress.com/gcp/300000533/KDdtyft4ys?spm=a2g0o.best.testStatic.3.544b22aebRQo39&disableNav=YES&pha_manifest=ssr&_immersiveMode=true"

driver.get(url)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "productContainer"))
    )
    page_source = driver.page_source
    soup = bs(page_source, 'html.parser')
    
    elements = soup.find_all('a', class_="productContainer")
    
    with open("scraped.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name Console", "Price", "Discount", "Url"])

        for element in elements:
            # Verifica la estructura del HTML para asegurarte de que estas clases son correctas
            name_console = element.find('span', class_='AIC-ATM-multiLine').find('span', style=re.compile("line-height: 16px; font-size: 12px;"))
            price_console = element.find('div', class_="rax-view-v2", style=re.compile("display: flex; flex-direction: row; align-items: flex-start; direction: ltr;")).find('span', class_="rax-text-v2  rax-text-v2--overflow-hidden rax-text-v2--singleline", style=re.compile("margin-top: 5px; margin-left: 4px; font-size: 12px; line-height: 16px; height: 16px; color: rgba(0, 0, 0, 0.5); text-decoration: line-through; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;"))
            print(str(price_console))
            discount= element.find('div', class_="rax-view-v2").find('span', class_='rax-text-v2  rax-text-v2--overflow-hidden rax-text-v2--singleline', style=re.compile("margin-left: 4px; margin-top: 5px; max-width: 208px; font-size: 12px; line-height: 16px; height: 16px; color: rgb(253, 56, 79); text-overflow: ellipsis; overflow: hidden; direction: ltr;"))
            
            url_console = element.get('href')

            name_console = name_console.get_text(strip=True) if name_console else str(name_console)
            price_console = price_console.get_text(strip=True) if price_console else str(price_console)
            discount = discount.get_text(strip=True) if discount else str(discount)
            url_console = url_console if url_console else str(url_console)

            print(f"Nombre: {name_console}, Precio: {price_console}, Sale: {discount}, URL: https{url_console}")
            writer.writerow([name_console, price_console, discount, f'https{url_console}'])  # Asegúrate de que esto esté dentro del bloque with
finally:
    driver.quit()
