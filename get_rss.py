import feedparser
from templates.template import TEMPLATE

content = TEMPLATE
VAR_LINKS = '{{VAR_LINKS}}'

def get_rss(links, name):
    content = TEMPLATE
    VAR_LINKS = '{{VAR_LINKS}}'
    allStuff = ""
    redditList = links

    if(name == "home"):
        allStuff += '<h4 class="center-align">Help Contify grow!</h4> <p class="center-align">Feel free to submit a new news source via a github issue! Please label them accordingly with a content label <a href="https://github.com/frainbreeze12/contify-python/issues">here</a>.</p>'

    for sub in redditList:
        d = feedparser.parse(sub)
        limit = 1

        allStuff += '<div class="col s12 m6 xl4">\n<ul class="collection with-header z-depth-1 hoverable">\n'
        if(d.feed.title == ""):
            allStuff += '<li class="collection-header"><h6><a href="{}">WirtschaftsWoche</a></h6></li>\n'.format(d.feed.link)
        else:
            allStuff += '<li class="collection-header"><h6><a href="{}">{}</a></h6></li>\n'.format(d.feed.link ,d.feed.title)
        for post in d.entries:
            allStuff += '<li class="collection-item"><a href="{}" target="_blank" class="truncate">{}</a></li>\n'.format(post.link, post.title)
            if limit == 10:
                break
            limit+=1
        allStuff += '</ul>\n</div>\n'

    content = content.replace(VAR_LINKS, allStuff)

    with open('templates/{}.html'.format(name), "w", encoding='utf-8') as sr:
        print("{}.rss successful".format(name))
        sr.write(content)