from flask import Flask
from flask import render_template
from flask import Markup
from main import do_magic
from reddit import get_rss

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

do_magic()
content = Markup(get_rss())

@app.route('/')
def index():
    return render_template("summary.html")  

@app.route('/quellen')
def quellen():
    return render_template("source.html")

@app.route('/subreddit')
def reddit():
    return render_template("subreddit.html", content=content)