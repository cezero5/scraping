import re
import csv
import requests

website = "https://vulnhub.com/"

result =requests.get(website)

content = result.text
patron = r"/entry/[\w-]*"

machines_repit = re.findall(patron, str(content))
non_repit = list(set(machines_repit))
info_clean = []

file = open("scraped.csv", "w")
writer = csv.writer(file)

writer.writerow(["Name Machines"])

for i in non_repit:
    name_machines = i.replace("/entry/", "")
    info_clean.append(name_machines)
    print(name_machines)
        

file.close
