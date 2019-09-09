from flask import render_template, request, redirect, url_for, Blueprint, flash

from forms import TextForm
from models import Text

texts = Blueprint("texts", __name__, template_folder="templates")


@texts.route('/')
def homepage():
    return render_template("homepage.html")


def store(o):
    from models import db
    db.session.add(o)
    db.session.commit()


@texts.route('/text', methods=['GET', 'POST'])
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


@texts.route('/text/<int:text_id>', methods=['GET', 'POST'])
def edit(text_id):
    text_data = Text.query.get_or_404(text_id)
    form = TextForm()
    print("retrieving text")
    if request.method == 'POST' and form.validate_on_submit():
        text_data.text = form.ticker_text.data
        store(text_data)
        flash("Saved")
        return redirect(url_for('texts.homepage'))
    else:
        form = TextForm()
        form.id = text_data.id
        form.active.data = text_data.active
        form.ticker_text.data = text_data.text
    return render_template("edit_text.html", form=form)


@texts.route('/index')
def index():
    all_texts = Text.query.filter_by(active=True).order_by(Text.created).all()

    return render_template("index.html", texts=all_texts)
