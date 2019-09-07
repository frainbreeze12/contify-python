from flask import Flask
from flask import render_template
from flask import Markup
from main import do_magic
from reddit import get_rss

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

do_magic()
get_rss()

@app.route('/')
def index():
    return render_template("summary.html")

@app.route('/wirtschaft')
def wirtschaft():
    return render_template("wirtschaft.html")

@app.route('/politik')
def politik():
    return render_template("politik.html")

@app.route('/technologie')
def technologie():
    return render_template("technologie.html")

@app.route('/subreddit')
def reddit():
    return render_template("subreddit.html")