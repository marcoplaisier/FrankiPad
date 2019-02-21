from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

MAX_TEXT_LENGTH = 140


class TextForm(FlaskForm):
    ticker_text = TextAreaField("Text",
                                validators=[DataRequired(),
                                            Length(max=MAX_TEXT_LENGTH,
                                                   message=f"Text must be shorter than {MAX_TEXT_LENGTH} characters")
                                            ],
                                default="Type some text here")
    active = BooleanField("Active", default=True)
    submit = SubmitField("Save")
    cancel = SubmitField("Cancel")
