import feedparser
from templates.template import TEMPLATE

content = TEMPLATE
VAR_LINKS = '{{VAR_LINKS}}'

def get_rss(links, name):
    content = TEMPLATE
    VAR_LINKS = '{{VAR_LINKS}}'
    allStuff = ""
    redditList = links

    for sub in redditList:
        d = feedparser.parse(sub)
        limit = 1

        allStuff += '<div class="col s12 m6 xl4">\n<ul class="collection with-header z-depth-1 hoverable">\n'
        if(d.feed.title == ""):
            allStuff += '<li class="collection-header"><h6>WirtschaftsWoche</h6></li>\n'
        else:
            allStuff += '<li class="collection-header"><h6>{}</h6></li>\n'.format(d.feed.title)
        for post in d.entries:
            allStuff += '<li class="collection-item truncate"><a href="{}">{}</a></li>\n'.format(post.link, post.title)
            if limit == 10:
                break
            limit+=1
        allStuff += '</ul>\n</div>\n'

    content = content.replace(VAR_LINKS, allStuff)

    with open('templates/{}.html'.format(name), "w", encoding='utf-8') as sr:
        print("{}.rss successful".format(name))
        sr.write(content)