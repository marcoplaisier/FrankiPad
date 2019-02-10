from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/create')
def create():
    return render_template("create.html")


@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
