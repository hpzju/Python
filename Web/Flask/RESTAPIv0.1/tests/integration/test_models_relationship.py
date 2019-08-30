from tests.resources import *


def test_relationship(store, item, get_app_context):
    with get_app_context():
        store.save_to_db()
        item.save_to_db()

        assert item.store.name == storename