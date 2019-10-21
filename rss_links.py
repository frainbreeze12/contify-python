from get_rss import get_rss
from apscheduler.schedulers.background import BackgroundScheduler


def rss_links():
    home_links      = ("http://www.makronom.de/feed", "https://www.n-tv.de/politik/rss", "https://www.heise.de/security/rss/news-atom.xml",
                       "https://www.security-insider.de/rss/news.xml", "http://www.reddit.com/r/popular/.rss")

    economy_links   = ("http://www.makronom.de/feed", "https://www.gruenderszene.de/feed", "https://www.wiwo.de/contentexport/feed/rss/schlagzeilen",
                       "https://www.businessinsider.de/rss", "https://www.handelsblatt.com/contentexport/feed/wirtschaft", "http://www.manager-magazin.de/news/index.rss")

    politic_links   = ("https://www.n-tv.de/politik/rss", "https://www.handelsblatt.com/contentexport/feed/politik", "https://www.dgb.de/@@rss?count=20&feed=9ba1995a-0fe3-11df-7728-00093d10fae2",
                       "https://netzpolitik.org/feed")

    tech_links      = ("https://www.heise.de/rss/heise-top-atom.xml", "https://rss.golem.de/rss.php?feed=ATOM1.0", "http://www.reddit.com/r/technology/.rss",
                       "https://news.ycombinator.com/rss","https://www.wired.com/feed/rss", "http://rss.slashdot.org/Slashdot/slashdotMainatom", 
                       "https://feeds.howtogeek.com/howtogeek/features", "https://www.eff.org/rss/updates.xml", "https://www.techrepublic.com/rssfeeds/articles/", 
                       "http://feeds.feedburner.com/TechCrunch/")

    security_links  = ("https://www.heise.de/security/rss/news-atom.xml", "https://www.heise.de/security/rss/alert-news-atom.xml", "https://www.security-insider.de/rss/news.xml",
                       "https://threatpost.com/feed/", "http://feeds.feedburner.com/Securityweek?format=xml", "https://feeds.feedburner.com/TheHackersNews", 
                       "https://krebsonsecurity.com/feed/", "https://www.darkreading.com/rss_simple.asp", "https://cyware.com/allnews/feed", 
                       "https://www.securitymagazine.com/rss/topic/2236")

    reddit_links    = ("http://www.reddit.com/r/popular/.rss", "http://www.reddit.com/r/europe/.rss","http://www.reddit.com/r/hongkong/.rss", 
                       "http://www.reddit.com/r/gaming/.rss", "http://www.reddit.com/r/Bossfight/.rss", "http://www.reddit.com/r/todayilearned/.rss",
                       "http://www.reddit.com/r/BikiniBottomTwitter/.rss", "http://www.reddit.com/r/KidsAreFuckingStupid/.rss", "http://www.reddit.com/r/dankmemes/.rss")

    webcomic_links  = ("https://xkcd.com/atom.xml", "https://xkcd.com/rss.xml")

    get_rss(home_links, "home")
    get_rss(economy_links, "economy")
    get_rss(politic_links, "politics")
    get_rss(tech_links, "technology")
    get_rss(security_links, "security")
    get_rss(reddit_links, "subreddit")
    get_rss(webcomic_links, "webcomics")
    

sched = BackgroundScheduler()
sched.add_job(rss_links, 'interval', minutes=30)
sched.start()