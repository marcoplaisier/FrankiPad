from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length

MAX_TEXT_LENGTH = 140


class TextForm(FlaskForm):
    id = HiddenField("id")
    ticker_text = TextAreaField("Text",
                                validators=[DataRequired(),
                                            Length(max=MAX_TEXT_LENGTH,
                                                   message="Text must be shorter than {} characters".format(MAX_TEXT_LENGTH))
                                            ],
                                default="Type some text here")
    active = BooleanField("Active", default=True)
    submit = SubmitField("Save")
