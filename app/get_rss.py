import feedparser
from templates.template import TEMPLATE

content = TEMPLATE
VAR_LINKS = '{{VAR_LINKS}}'

def get_rss(links, name):
    content = TEMPLATE
    VAR_LINKS = '{{VAR_LINKS}}'
    allStuff = ""
    feedList = links
    log = ""

    log += "Currently fetching from: {}<br>\n".format(name)

    for feed in feedList:
        d = feedparser.parse(feed)
        limit = 1

        if(d.status != 200 and d.status != 301):
            print("{} is currently dead".format(feed))
            log += "{} is currently dead<br>\n".format(feed)
        elif(d.status == 301):
            print("{} is redirected".format(feed))
            log += "{} is redirected<br>\n".format(feed)
        elif (d.status == 200):
            allStuff += '<div class="col s12 m6 xl4">\n<ul class="collection with-header z-depth-1 hoverable">\n'

            print("fetching feed from: {}".format(feed))
            log += "fetching feed from: {}<br>\n".format(feed)

            allStuff += '<li class="collection-header"><h6><a href="{}" rel="noopener">{}</a></h6></li>\n'.format(d.feed.link ,d.feed.title)
            
            for post in d.entries:
                allStuff += '<li class="collection-item"><a href="{}" target="_blank" rel="noopener" class="truncate">{}</a></li>\n'.format(post.link, post.title)
                if limit == 10:
                    break
                limit+=1
            allStuff += '</ul>\n</div>\n'

    content = content.replace(VAR_LINKS, allStuff)

    with open('templates/{}.html'.format(name), "w", encoding='utf-8') as sr:
        print("{}.rss successful".format(name))
        sr.write(content)

    if(name == "home"):
        with open('templates/status.html', "w", encoding='utf-8') as st:
            st.write(log)
    else:
        with open('templates/status.html', "a", encoding='utf-8') as st:
            st.write(log)
