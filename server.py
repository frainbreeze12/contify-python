from flask import Flask
from flask import render_template
from flask import Markup
from rss_links import rss_links

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

rss_links()


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/economy')
def wirtschaft():
    return render_template("economy.html")


@app.route('/politics')
def politik():
    return render_template("politics.html")


@app.route('/tech&science')
def technologie():
    return render_template("technology.html")


@app.route('/security')
def security():
    return render_template("security.html")


@app.route('/subreddit')
def reddit():
    return render_template("subreddit.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
