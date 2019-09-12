from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from forms import MAX_TEXT_LENGTH

db = SQLAlchemy()

current_text = db.Table(
    'current_text',
    db.Column('current_text', db.Integer, db.ForeignKey('text.id'))
)


class Text(db.Model):
    __tablename__ = 'text'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(MAX_TEXT_LENGTH))
    active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime, default=datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.now())

    @staticmethod
    def create_text_from_form(form):
        return Text(text=form.ticker_text.data, active=form.active.data)


