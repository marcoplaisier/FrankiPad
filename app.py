import os
import random

from flask import Flask, render_template, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getcwd()}/quotepad.db"
app.config['SECRET_KEY'] = str(random.getrandbits(60))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from forms import TextForm
from models import Text


@app.route('/')
def homepage():
    return render_template("homepage.html")


def store(o):
    db.session.add(o)
    db.session.commit()


@app.route('/text', methods=['GET', 'POST'])
def text():
    form = TextForm()
    if form.is_submitted():
        if form.validate_on_submit():
            new_text = Text.create_text_from_form(form)
            store(new_text)
            flash("Saved")
        else:
            for _field, error_messages in form.errors.items():
                for error_message in error_messages:
                    flash(error_message)
    return render_template("text.html", form=form)


@app.route('/text/<int:text_id>')
def update(text_id):
    text_data = Text.query.get_or_404(text_id)
    form = TextForm()
    form.active.data = text_data.active
    form.ticker_text.data = text_data.text
    return render_template("text.html", form=form)


@app.route('/index')
def index():
    all_texts = Text.query.filter_by(active=True).order_by(Text.created).all()
    return render_template("index.html", texts=all_texts)


if __name__ == '__main__':
    app.run()
