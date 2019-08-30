import pytest
from models.item import ItemModel
from models.store import StoreModel
from app import app
from db import db


# session level initialization
def pytest_configure(config):
    # print('---------------setup------------------')
    # print('*****************Init APP DB*****************')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
    with app.app_context():
        db.init_app(app)
    # print('*****************Init APP DB Done*****************')


# module level initialization
name = 'string name'
price = 1923.23
store_id = 1
storename = 'Starbucks'


@pytest.fixture(scope='module')
def store():
    return StoreModel(storename)


@pytest.fixture(scope='module')
def item():
    return ItemModel(name, price, store_id)


@pytest.fixture(scope='module')
def get_app_client():
    return app.test_client


# function level initialization
@pytest.fixture(scope='function')
def get_app_context():
    with app.app_context():
        db.create_all()
    # print("-------------setup_app_context---------------")
    yield app.app_context

    with app.app_context():
        db.session.remove()
        db.drop_all()
    # print("-------------teardown_app_context---------------")
