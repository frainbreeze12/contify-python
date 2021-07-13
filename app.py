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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
