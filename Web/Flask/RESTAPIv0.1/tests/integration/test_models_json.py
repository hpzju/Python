from tests.resources import *


def test_item_json(item, store, get_app_context):
    with get_app_context():
        store.save_to_db()
        item.save_to_db()
        assert item.json() == {'name': item.name,
                               'price': item.price}
        assert store.json() == {'name': store.name,
                               'items': [item.json()]}

        item.delete_from_db()
        store.delete_from_db()