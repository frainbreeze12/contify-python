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


@app.route('/finance')
def finance():
    return render_template("finance.html")


@app.route('/gaming')
def gaming():
    return render_template("gaming.html")


@app.route('/memes')
def memes():
    return render_template("memes.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
