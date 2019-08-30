import json
from tests.conftest import *


def test_create_item(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()
            resp = client.post(f'/item/{name}',
                               data={'price': price, 'store_id': store_id})

            assert resp.status_code == 201
            assert StoreModel.find_by_name(storename) is not None
            assert {'name': name, 'price': price} == json.loads(resp.data)


def test_create_duplicate_item(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()
            client.post(f'/item/{name}',
                        data={'price': price, 'store_id': store_id})
            resp = client.post(f'/item/{name}',
                               data={'price': price, 'store_id': store_id})

            assert resp.status_code == 400
            assert {'message':
                        f"An item with name '{name}' already exists."
                    } == json.loads(resp.data)


def test_read_item(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            ItemModel(name, price, store_id).save_to_db()
            resp = client.get(f'/item/{name}')

            assert 200 == resp.status_code
            assert {'name': name, 'price': price} == json.loads(resp.data)


def test_read_not_found(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            ItemModel(name, price, store_id).save_to_db()
            resp = client.get(f'/item/fhwireo393e')

            assert 404 == resp.status_code
            assert {'message': 'Item not found'} == json.loads(resp.data)


def test_put_item(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()

            resp = client.put(f'/item/{name}',
                              data={'price': price, 'store_id': store_id})

            assert 200 == resp.status_code
            assert {'name': name, 'price': price} == json.loads(resp.data)


def test_update_item(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()

            resp = client.put(f'/item/{name}',
                              data={'price': price+1, 'store_id': store_id})

            assert 200 == resp.status_code
            assert {'name': name, 'price': price+1} == json.loads(resp.data)


def test_delete_item(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            ItemModel(name, price, store_id).save_to_db()
            resp = client.delete(f'/item/{name}')

            assert 200 == resp.status_code
            assert {'message': 'Item deleted'} == json.loads(resp.data)


def test_get_itemlist(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            ItemModel(name, price, store_id).save_to_db()

            resp = client.get(f'/items')

            assert 200 == resp.status_code
            # print(resp.data)
            assert {'items': [{'name': name,
                               'price': price}]
                    } == json.loads(resp.data)
