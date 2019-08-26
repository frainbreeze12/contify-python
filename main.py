import requests
import time
import csv
import os
from bs4 import BeautifulSoup
from templates.template import TEMPLATE
from create_links import create_links
from write_to_csv import write_to_csv
from urllib.parse import urlparse
from datetime import datetime

heise = requests.get("https://www.heise.de/newsticker")
heiseSoup = BeautifulSoup(heise.content, 'html.parser')
golem = requests.get("https://www.golem.de/")
golemSoup = BeautifulSoup(golem.content, 'html.parser')
t3n = requests.get("https://t3n.de/news/")
t3nSoup = BeautifulSoup(t3n.content, 'html.parser')
spiegel = requests.get("https://www.spiegel.de/schlagzeilen/")
spiegelSoup = BeautifulSoup(spiegel.content, 'html.parser')
welt = requests.get("https://www.welt.de/newsticker/")
weltSoup = BeautifulSoup(welt.content, 'html.parser')
bi = requests.get("https://www.businessinsider.de/")
biSoup = BeautifulSoup(bi.content, 'html.parser')
netzwelt = requests.get("https://www.netzwelt.de/news/index.html")
netzweltSoup = BeautifulSoup(netzwelt.content, 'html.parser')

content = TEMPLATE
VAR_LINKS = '{{VAR_LINKS}}'
VAR_TIME = '{{VAR_TIME}}'
links = ""

heiseLinks = []
heiseTitle = []
golemLinks = []
golemTitle = []
t3nLinks = []
t3nTitle = []
spiegelLinks = []
spiegelTitle = []
weltLinks = []
weltTitle = []
biLinks = []
biTitle = []
netzweltLinks = []
netzweltTitle = []

#removing summary.csv if exists
if os.path.exists("resources/summary.csv"):
    print("Deleting summary.csv")
    os.remove("resources/summary.csv")
else:
    print("Summary.csv does currently no exist")


#getting all the content
print("Getting links from Heise")
for link in heiseSoup.find_all('a', class_={'archiv-liste__text'}, limit=5):
    if urlparse(link.get('href')).hostname == "www.techstage.de":
        heiseLinks.append("'" + link.get('href') + "'")
    else:    
        heiseLinks.append("'https://www.heise.de" + link.get('href') + "'")
    heiseTitle.append(link.get('title'))

print("Getting links from Golem")
golemResult = golemSoup.select('.list-articles li', limit=5)
for article in golemResult:
    golemLinks.append("'" + article.select('a')[0].get('href') + "'")
    golemTitle.append(article.select('a')[0].get('title'))

print("Getting links from t3n")
for article in t3nSoup.find_all('a', class_={'c-newslist__link'}, limit=5):
    t3nLinks.append("'" + article.get('href') + "'")
    t3nTitle.append(article.get_text())

print("Getting links from Spiegel")
spiegelResult = spiegelSoup.select('.schlagzeilen-content a', limit=5)
for article in spiegelResult:
    spiegelLinks.append("'https://www.spiegel.de" + article.get('href') + "'")
    spiegelTitle.append(article.get('title'))

print("Getting links from Welt")
for article in weltSoup.find_all('a', class_={'o-teaser__link--is-headline'}, limit=5):
    weltLinks.append("'https://www.welt.de" + article.get('href') + "'")
    weltTitle.append(article.get('title'))

print("Getting links from Business Insider")
for article in biSoup.find_all('a', class_={'title'}, limit=5):
    biLinks.append("'" + article.get('href') + "'")
    biTitle.append(article.get_text())

print("Getting links from netzwelt")
for article in netzweltSoup.find_all('a', class_={'cl-ap'}, limit=5):
    netzweltLinks.append("'" + article.get('href') + "'")
    netzweltTitle.append(article.get('title'))


#adding links to summary.csv
print("Writing links to summary.csv")
write_to_csv(heiseLinks, heiseTitle)
write_to_csv(golemLinks, golemTitle)
write_to_csv(t3nLinks, t3nTitle)
write_to_csv(spiegelLinks, spiegelTitle)
write_to_csv(weltLinks, weltTitle)
write_to_csv(biLinks, biTitle)
write_to_csv(netzweltLinks, netzweltTitle)

#adding links to the template file
content = content.replace(VAR_LINKS, create_links())
content = content.replace(VAR_TIME, datetime.now().strftime('%d.%m.%y %H:%M:%S'))

#write data into the final html file
with open('web/summary.html', "w", encoding='utf-8') as summary:
    print("Writing links to summary.html")
    summary.write(content)
