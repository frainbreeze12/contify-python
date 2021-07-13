from get_rss import get_rss
from apscheduler.schedulers.background import BackgroundScheduler


def rss_links():

    home_links    = ("https://www.reddit.com/r/popular/.rss", "https://www.reddit.com/r/europe/.rss","https://www.reddit.com/r/hongkong/.rss", 
                     "https://www.reddit.com/r/AskReddit/.rss", "https://www.reddit.com/r/pathofexile/.rss", "https://www.reddit.com/r/todayilearned/.rss",
                     "https://www.reddit.com/r/BikiniBottomTwitter/.rss", "https://www.reddit.com/r/KidsAreFuckingStupid/.rss", "https://www.reddit.com/r/gaming/.rss")
    
    get_rss(home_links, "home")
    
sched = BackgroundScheduler()
sched.add_job(rss_links, 'interval', minutes=30)
sched.start()
