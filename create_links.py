import csv
from templates.template import TEMPLATE
from urllib.parse import urlparse

def create_links():
    with open('resources/summary.csv', 'r') as sumRes:
        reader = sumRes.readlines()
        numLines = sum(1 for row in reader)
        splitLinks = []
        splitTitle = []
        links=""

        i = 0
        while i < numLines:
            if i == 0 or i % 2 == 0:
                splitLinks += reader[i].split(';')
                i += 1
            else:
                splitTitle += reader[i].split(';')
                i += 1

        lenList = len(splitLinks)

        i = 1
        while i <= lenList:
            if i == 1:
                links += '<div class="col s12 m6 xl4">\n<ul class="collection with-header z-depth-1">\n'
                if urlparse(splitLinks[i-1].strip("'")).hostname == "www.techstage.de":
                    links += '<li class="collection-header"> <h5>www.heise.de</h5></li>'
                else:    
                    links += '<li class="collection-header"> <h5>' + urlparse(splitLinks[i-1].strip("'")).hostname + ' </h5></li>'
                links += '<li class="collection-item truncate"><a href=' + splitLinks[i-1].strip() + '>' + splitTitle[i-1].strip() + '</a></li>\n'
                i += 1
            elif i == lenList:
                links += '<li class="collection-item truncate"><a href=' + splitLinks[i-1].strip() + '>' + splitTitle[i-1].strip() + '</a></li>\n'
                links += '</ul>\n</div>\n'
                i += 1
            elif i % 5 == 0:
                links += '<li class="collection-item truncate"><a href=' + splitLinks[i-1].strip() + '>' + splitTitle[i-1].strip() + '</a></li>\n'
                links += '</ul>\n</div>\n'
                links += '<div class="col s12 m6 xl4">\n<ul class="collection with-header z-depth-1">\n'
                links += '<li class="collection-header"> <h5>' + urlparse(splitLinks[i].strip("'")).hostname + ' </h5></li>\n'
                i += 1
            else:
                links += '<li class="collection-item truncate"><a href=' + splitLinks[i-1].strip() + '>' + splitTitle[i-1].strip() + '</a></li>\n'
                i += 1
    return(links)