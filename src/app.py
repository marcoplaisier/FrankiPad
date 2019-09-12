import random

from flask import Flask

from texts import texts
from models import db
import os


def create_app(name=__name__, settings=None):
    app = Flask(name)
    if settings:
        app.config.from_mapping(settings)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getcwd()}/data/quotepad.db"
        app.config['SECRET_KEY'] = str(random.getrandbits(60))
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)

    from flask_migrate import Migrate
    migrate = Migrate()
    migrate.init_app(app=app, db=db)

    # from quotepad import interfaces
    # interfaces.run()

    app.register_blueprint(texts.texts)
    return app
