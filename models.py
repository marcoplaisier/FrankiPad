from datetime import datetime
from app import db
from forms import MAX_TEXT_LENGTH


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(MAX_TEXT_LENGTH))
    active = db.Column(db.Boolean)
    created = db.Column(db.DateTime)

    @staticmethod
    def create_text_from_form(form):
        return Text(text=form.ticker_text.data, active=form.active.data, created=datetime.now())
