from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from forms import MAX_TEXT_LENGTH

db = SQLAlchemy()

next_texts = db.Table(
    'next_texts',
    db.Column('current_text', db.Integer, db.ForeignKey('text.id')),
    db.Column('next_text', db.Integer, db.ForeignKey('text.id'))
)

current_text = db.Table(
    'current_text',
    db.Column('current_text', db.Integer, db.ForeignKey('text.id'))
)


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(MAX_TEXT_LENGTH))
    next_text_id = db.relationship(
        'Text',
        secondary=next_texts,
        primaryjoin=(next_texts.c.current_text == id),
        secondaryjoin=(next_texts.c.next_text == id),
        backref=db.backref('next_texts', lazy=True),
        lazy=True,
        uselist=False

    )
    active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime, default=datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.now())

    @staticmethod
    def create_text_from_form(form):
        return Text(text=form.ticker_text.data, active=form.active.data)
