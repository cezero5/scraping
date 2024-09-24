import requests
from bs4 import BeautifulSoup as bs
import re
import csv

url_cali ="https://www.linkedin.com/jobs/search/?currentJobId=3926548913&distance=5&f_E=1%2C2&f_WT=1%2C2%2C3&geoId=103204161&keywords=Ciberseguridad&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
url_colombia = "https://www.linkedin.com/jobs/search/?currentJobId=4021550675&f_E=1%2C2&f_WT=2&geoId=100876405&keywords=Ciberseguridad&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
url_latinamerica = "https://www.linkedin.com/jobs/search/?currentJobId=4021550675&f_E=1%2C2&f_WT=2&geoId=91000011&keywords=Ciberseguridad&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true"

response_cali = requests.get(url_cali) 
response_colombia = requests.get(url_colombia)
response_latinamerica = requests.get(url_latinamerica)
response_all = f'{response_cali} {response_colombia} {response_latinamerica}'

if response_cali.status_code == 200:
    soup = bs(response_all.text, 'html.parser')
    
    elements = soup.find_all()
    print(elements)