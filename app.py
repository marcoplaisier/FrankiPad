import os
from datetime import datetime

from flask import Flask, render_template, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getcwd()}/quotepad.db"
app.config['SECRET_KEY'] = "Ng6R83e9JvOV35Bc"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from forms import TextForm
from models import Text


@app.route('/')
def homepage():
    return render_template("homepage.html")


def store(object):
    db.session.add(object)
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


@app.route('/index')
def index():
    all_texts = Text.query.filter_by(active=True).order_by(Text.created).all()
    return render_template("index.html", texts=all_texts)


if __name__ == '__main__':
    app.run()
