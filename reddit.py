import feedparser

def get_rss():
    content = ""
    redditList = ("http://www.reddit.com/r/news/.rss", "http://www.reddit.com/r/technology/.rss", "http://www.reddit.com/r/worldnews/.rss",
                  "http://www.reddit.com/r/gaming/.rss", "http://www.reddit.com/r/Showerthoughts/.rss", "http://www.reddit.com/r/hongkong/.rss",
                  "http://www.reddit.com/r/europe/.rss", "http://www.reddit.com/r/dankmemes/.rss", "http://www.reddit.com/r/KidsAreFuckingStupid/.rss")

    for sub in redditList:
        d = feedparser.parse(sub)
        limit = 1

        content += '<div class="col s12 m6 xl4"><ul class="collection with-header z-depth-1 hoverable">'
        content += '<li class="collection-header"> <h5>{}</h5></li>'.format(d['feed']["tags"][0].label)
        for post in d.entries:
            content += '<li class="collection-item truncate"><a href="{}">{}</a></li>'.format(post.link, post.title)
            if limit == 10:
                break
            limit+=1
        content += '</ul></div>'

    return content 
