from get_rss import get_rss
from apscheduler.schedulers.background import BackgroundScheduler


def rss_links():

    home_links    = ("https://www.reddit.com/r/popular/.rss", "https://www.reddit.com/r/europe/.rss","https://www.reddit.com/r/de/.rss", 
                     "https://www.reddit.com/r/AskReddit/.rss", "https://www.reddit.com/r/antiwork/.rss", "https://www.reddit.com/r/recruitinghell/.rss")
    finance_links = ("https://www.reddit.com/r/finance/.rss", "https://www.reddit.com/r/finanzen/.rss")
    gaming_links  = ("https://www.reddit.com/r/gaming/.rss", "https://www.reddit.com/r/pathofexile/.rss", "https://www.reddit.com/r/wow/.rss",
                     "https://www.reddit.com/r/terraria/.rss", "https://www.reddit.com/r/blackdesertonline/.rss", "https://www.reddit.com/r/newworldgame/.rss",
                     "https://www.reddit.com/r/ffxiv/.rss", "https://www.reddit.com/r/leagueoflegends/.rss", "https://www.reddit.com/r/TheSilphRoad/.rss")
    memes_links  = ("https://www.reddit.com/r/me_irl/.rss", "https://www.reddit.com/r/ich_iel/.rss", "https://www.reddit.com/r/shitposting/.rss",
                    "https://www.reddit.com/r/ape/.rss", "https://www.reddit.com/r/shitpostcrusaders/.rss", "https://www.reddit.com/r/terriblefacebookmemes/.rss",
                    "https://www.reddit.com/r/ichbin40undlustig/.rss", "https://www.reddit.com/r/wasletztepreis/.rss", "https://www.reddit.com/r/lotrmemes/.rss")
    
    get_rss(home_links, "home")
    get_rss(finance_links, "finance")
    get_rss(gaming_links, "gaming")
    get_rss(memes_links, "memes")
    
sched = BackgroundScheduler()
sched.add_job(rss_links, 'interval', minutes=30)
sched.start()
