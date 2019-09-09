import feedparser
from templates.template import TEMPLATE
from apscheduler.schedulers.background import BackgroundScheduler

content = TEMPLATE
VAR_LINKS = '{{VAR_LINKS}}'

def get_sec_rss():
    content = TEMPLATE
    VAR_LINKS = '{{VAR_LINKS}}'
    allStuff = ""
    securityLinks = ("https://www.heise.de/security/rss/news-atom.xml", "https://www.heise.de/security/rss/alert-news-atom.xml", "https://www.security-insider.de/rss/news.xml",
                     "https://threatpost.com/feed/", "http://feeds.feedburner.com/Securityweek?format=xml", "https://feeds.feedburner.com/TheHackersNews", 
                     "https://www.darkreading.com/rss_simple.asp", "https://cyware.com/allnews/feed", "https://www.securitymagazine.com/rss/topic/2236")

    for sec in securityLinks:
        d = feedparser.parse(sec)
        limit = 1

        allStuff += '<div class="col s12 m6 xl4"><ul class="collection with-header z-depth-1 hoverable">'
        allStuff += '<li class="collection-header"> <h6>{}</h6></li>'.format(d.feed.title)
        """ allStuff += '<li class="collection-header"> <h6>Seite</h6></li>' """
        for post in d.entries:
            allStuff += '<li class="collection-item truncate"><a href="{}">{}</a></li>'.format(post.link, post.title)
            if limit == 10:
                break
            limit+=1
        allStuff += '</ul></div>'

    content = content.replace(VAR_LINKS, allStuff)

    with open('templates/security.html', "w", encoding='utf-8') as sr:
        print("Security .rss successful")
        sr.write(content)

sched = BackgroundScheduler()
sched.add_job(get_sec_rss, 'interval', minutes=5)
sched.start()