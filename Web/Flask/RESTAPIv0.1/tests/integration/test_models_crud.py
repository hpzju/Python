from tests.conftest import *


def test_item_crud(item, get_app_context):
    with get_app_context():
        assert ItemModel.find_by_name(name) is None
        item.save_to_db()
        assert ItemModel.find_by_name(name) is not None
        item.delete_from_db()
        assert ItemModel.find_by_name(name) is None


def test_store_crud(store, get_app_context):
    with get_app_context():
        assert StoreModel.find_by_name(storename) is None
        store.save_to_db()
        assert StoreModel.find_by_name(storename) is not None
        store.delete_from_db()
        assert StoreModel.find_by_name(storename) is None


