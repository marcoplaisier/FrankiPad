from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from forms import MAX_TEXT_LENGTH

db = SQLAlchemy()


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(MAX_TEXT_LENGTH))
    last_sent = db.Column(db.Boolean, default=False)
    next_text = db.Column(db.Integer, db.ForeignKey(id), nullable=True)
    active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime, default=datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.now())

    @staticmethod
    def create_text_from_form(form):
        return Text(text=form.ticker_text.data, active=form.active.data)
