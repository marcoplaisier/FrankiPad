from datetime import datetime
import os

from flask import Flask, render_template, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from forms import TextForm, MAX_TEXT_LENGTH

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getcwd()}/quotepad.db"
app.config['SECRET_KEY'] = "Ng6R83e9JvOV35Bc"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/text', methods=['GET', 'POST'])
def text():
    form = TextForm()
    if form.is_submitted():
        if form.validate_on_submit():
            new_text = Text(text=form.ticker_text.data, active=form.active.data, created=datetime.now())
            db.session.add(new_text)
            db.session.commit()

            flash("Saved")
        else:
            for _field, error_messages in form.errors.items():
                for error_message in error_messages:
                    flash(error_message)
    return render_template("text.html", form=form)


@app.route('/index')
def index():
    return render_template("index.html")


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(MAX_TEXT_LENGTH))
    active = db.Column(db.Boolean)
    created = db.Column(db.DateTime)


if __name__ == '__main__':
    app.run()
