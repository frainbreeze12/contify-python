from flask import Flask
from flask import render_template
from main import do_magic

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

do_magic()

@app.route('/')
def index():
    return render_template("summary.html")