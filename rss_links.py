from get_rss import get_rss
from apscheduler.schedulers.background import BackgroundScheduler


def rss_links():
    security_links = ("https://www.heise.de/security/rss/news-atom.xml", "https://www.heise.de/security/rss/alert-news-atom.xml", "https://www.security-insider.de/rss/news.xml",
                      "https://threatpost.com/feed/", "http://feeds.feedburner.com/Securityweek?format=xml", "https://feeds.feedburner.com/TheHackersNews", 
                      "https://www.darkreading.com/rss_simple.asp", "https://cyware.com/allnews/feed", "https://www.securitymagazine.com/rss/topic/2236")

    reddit_links = ("http://www.reddit.com/r/popular/.rss", "http://www.reddit.com/r/technology/.rss", "https://www.reddit.com/r/news/.rss",
                    "http://www.reddit.com/r/europe/.rss","http://www.reddit.com/r/hongkong/.rss", "http://www.reddit.com/r/gaming/.rss",
                    "http://www.reddit.com/r/Showerthoughts/.rss", "http://www.reddit.com/r/KidsAreFuckingStupid/.rss", "http://www.reddit.com/r/dankmemes/.rss")

    tech_links = ("https://www.heise.de/rss/heise-top-atom.xml", "https://rss.golem.de/rss.php?feed=ATOM1.0", "https://news.ycombinator.com/rss",
                  "https://www.nytimes.com/svc/collections/v1/publish/http://www.nytimes.com/section/science/rss.xml")

    get_rss(tech_links, "technology")
"""     get_rss(security_links, "security")
    get_rss(reddit_links, "subreddit") """


sched = BackgroundScheduler()
sched.add_job(rss_links, 'interval', minutes=5)
sched.start()