import requests
import time
import csv
import os
from bs4 import BeautifulSoup
from templates.template import TEMPLATE
from create_links import create_links
from write_to_csv import write_to_csv
from urllib.parse import urlparse
from apscheduler.schedulers.background import BackgroundScheduler

def do_magic():
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

    allStuff = [[] for _ in range(14)]

    #removing summary.csv if exists
    if os.path.exists("resources/summary.csv"):
        print("Deleting summary.csv")
        os.remove("resources/summary.csv")
    else:
        print("Summary.csv does currently no exist")

    #getting all the content
    for link in heiseSoup.find_all('a', class_={'archiv-liste__text'}, limit=5):
        if urlparse(link.get('href')).hostname == "www.techstage.de":
            allStuff[0].append("'" + link.get('href') + "'")
        else:
            allStuff[0].append("'https://www.heise.de" + link.get('href') + "'")
        allStuff[1].append(link.get('title'))

    golemResult = golemSoup.select('.list-articles li', limit=5)
    for article in golemResult:
        allStuff[2].append("'" + article.select('a')[0].get('href') + "'")
        allStuff[3].append(article.select('a')[0].get('title'))

    for article in t3nSoup.find_all('a', class_={'c-newslist__link'}, limit=5):
        allStuff[4].append("'" + article.get('href') + "'")
        allStuff[5].append(article.get_text())

    spiegelResult = spiegelSoup.select('.schlagzeilen-content a', limit=5)
    for article in spiegelResult:
        if urlparse(article.get('href')).hostname == "www.spiegel.de":
            allStuff[6].append("'" + article.get('href') + "'")
        else:
            allStuff[6].append("'https://www.spiegel.de" + article.get('href') + "'")
        allStuff[7].append(article.get('title'))

    for article in weltSoup.find_all('a', class_={'o-teaser__link--is-headline'}, limit=5):
        allStuff[8].append("'https://www.welt.de" + article.get('href') + "'")
        allStuff[9].append(article.get('title'))

    for article in biSoup.find_all('a', class_={'title'}, limit=5):
        allStuff[10].append("'" + article.get('href') + "'")
        allStuff[11].append(article.get_text())

    for article in netzweltSoup.find_all('a', class_={'cl-ap'}, limit=5):
        allStuff[12].append("'" + article.get('href') + "'")
        allStuff[13].append(article.get('title'))

    #adding links to summary.csv
    write_to_csv(allStuff, "summary")

    #adding links to the template file
    content = content.replace(VAR_LINKS, create_links())

    #write data into the final html file
    with open('templates/summary.html', "w", encoding='utf-8') as summary:
        print("Update Successful")
        summary.write(content)

sched = BackgroundScheduler()
sched.add_job(do_magic, 'interval', minutes=5)
sched.start()