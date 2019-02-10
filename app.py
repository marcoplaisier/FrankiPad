from flask import Flask, render_template, flash

from forms import TextForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "Ng6R83e9JvOV35Bc"


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/text', methods=['GET', 'POST'])
def text():

    form = TextForm()
    if form.is_submitted():
        if form.validate_on_submit():
            flash("Saved")
            print(form.ticker_text.data)
        else:
            for _field, error_messages in form.errors.items():
                for error_message in error_messages:
                    flash(error_message)
    return render_template("text.html", form=form)


@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
