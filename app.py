import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import SignupForm

from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)

@app.route("/success")
def success():
    return "Thank you for signing up!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
