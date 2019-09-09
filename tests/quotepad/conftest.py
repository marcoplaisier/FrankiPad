import pytest

from main import create_app
from models import db as _db


@pytest.fixture(scope='session')
def app(request):
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': 'so secret',
        'WTF_CSRF_ENABLED': False
    }

    app = create_app(__name__, settings_override)

    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope='session')
def db(app, request):
    _db.app = app
    _db.create_all()

    return _db


@pytest.fixture
def client(app, db):
    return app.test_client()


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session
    yield session
    transaction.rollback()
    connection.close()
    session.remove()
