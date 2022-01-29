# Scraping KEMKES

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.kemkes.go.id"

content = requests.get(url)

soup = BeautifulSoup(content.text, 'html.parser')

covid_case = soup.find("div", {"class" : "covid-case-container"})

info_case = covid_case.find("li", {"class" : "info-case"}).find_all("td", {"class" : "case"})
date = covid_case.find("li", {"class" : "info-date"}).text
date = ' '.join(date.split()[1:])

info_case = {
      'data' : [{'data': date, 'positive' : info_case[0].text, 'recover' : info_case[1].text, 'died' : info_case[2].text}]
  }

print(json.dumps(info_case, indent=4))
