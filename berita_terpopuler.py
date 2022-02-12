# Scrape KEMKES
# Data: Berita Terpopuler
# https://github.com/karvanpy/ScrapingKEMKES

import csv
import json
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

url = "https://www.kemkes.go.id"

content = requests.get(url)

soup = BeautifulSoup(content.text, "html.parser")

berita_terpopuler = []

daftar_berita_terpopuler = soup.find_all("ul", {"class": "ants-news-list"})
for berita in daftar_berita_terpopuler[2]:
    berita_terpopuler.append(
        {
            "judul": berita.text.split(" Hits")[1],
            "jumlah_tayangan": berita.text.split(" Hits")[0].replace(".", "")
        }
    )
    
def export_to(format):
    if format == "txt":
        with open("result_berita-terpopuler.txt", "w") as file:
            for berita in berita_terpopuler:
                file.write(berita["judul"] + "," + berita["jumlah_tayangan"])
                file.write("\n")
                
    if format == "csv":
        with open("result_berita-terpopuler.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["judul", "jumlah_tayangan"])
            writer.writeheader()
            writer.writerows(berita_terpopuler)

print(json.dumps(berita_terpopuler, indent=2))      # show the output to the screen in json format
print(tabulate(berita_terpopuler, tablefmt="grid")) # show the output to the screen in table 
# export_to("csv")                                  # uncomment if you want export the output to format like 'csv' or 'plain/txt'
