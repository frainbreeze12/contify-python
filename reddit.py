import feedparser
from templates.template import TEMPLATE
from apscheduler.schedulers.background import BackgroundScheduler

content = TEMPLATE
VAR_LINKS = '{{VAR_LINKS}}'

def get_rss():
    content = TEMPLATE
    VAR_LINKS = '{{VAR_LINKS}}'
    allStuff = ""
    redditList = ("http://www.reddit.com/r/popular/.rss", "http://www.reddit.com/r/technology/.rss", "https://www.reddit.com/r/news/.rss",
                  "http://www.reddit.com/r/worldnews/.rss", "http://www.reddit.com/r/europe/.rss","http://www.reddit.com/r/hongkong/.rss",
                  "http://www.reddit.com/r/gaming/.rss", "http://www.reddit.com/r/Showerthoughts/.rss", "http://www.reddit.com/r/KidsAreFuckingStupid/.rss",
                  "http://www.reddit.com/r/dankmemes/.rss")

    for sub in redditList:
        d = feedparser.parse(sub)
        limit = 1

        allStuff += '<div class="col s12 m6 xl4"><ul class="collection with-header z-depth-1 hoverable">'
        allStuff += '<li class="collection-header"> <h6>{}</h6></li>'.format(d['feed']["tags"][0].label)
        for post in d.entries:
            allStuff += '<li class="collection-item truncate"><a href="{}">{}</a></li>'.format(post.link, post.title)
            if limit == 10:
                break
            limit+=1
        allStuff += '</ul></div>'

    content = content.replace(VAR_LINKS, allStuff)

    with open('templates/subreddit.html', "w", encoding='utf-8') as sr:
        print("Reddit .rss successful")
        sr.write(content)

sched = BackgroundScheduler()
sched.add_job(get_rss, 'interval', minutes=5)
sched.start()