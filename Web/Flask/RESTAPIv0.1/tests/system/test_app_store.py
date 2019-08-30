import json
from tests.conftest import *


def test_create_store(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            resp = client.post(f'/store/{storename}')

            assert resp.status_code == 201
            assert StoreModel.find_by_name(storename) is not None
            assert {'name': storename, 'items': []} == json.loads(resp.data)


def test_create_duplicate_store(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            client.post(f'/store/{storename}')
            resp = client.post(f'/store/{storename}')

            assert resp.status_code == 400


def test_delete_store(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()
            resp = client.delete(f'/store/{storename}')

            assert 200 == resp.status_code
            assert {'message': 'Store deleted'} == json.loads(resp.data)


def test_find_store(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()
            resp = client.get(f'/store/{storename}')

            assert 200 == resp.status_code
            assert {'name': storename, 'items': []} == json.loads(resp.data)


def test_store_not_found(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()
            resp = client.get(f'/store/test334rfdgw5345')

            assert 404 == resp.status_code
            assert {'message': 'Store not found'} == json.loads(resp.data)


def test_store_with_items(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()
            ItemModel(name, price, store_id).save_to_db()

            resp = client.get(f'/store/{storename}')

            assert 200 == resp.status_code
            # print(resp.data)
            assert {'name': storename,
                    'items': [{'name': name,
                               'price': price}]
                    } == json.loads(resp.data)


def test_store_list(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()

            resp = client.get(f'/stores')

            assert 200 == resp.status_code
            # print(resp.data)
            assert {'stores': [{'name': storename,
                                'items': []
                                }]
                    } == json.loads(resp.data)


def test_store_list_with_items(get_app_context, get_app_client):
    with get_app_client() as client:
        with get_app_context():
            StoreModel(storename).save_to_db()
            ItemModel(name, price, store_id).save_to_db()

            resp = client.get(f'/stores')

            assert 200 == resp.status_code
            # print(resp.data)
            assert {'stores': [{'name': storename,
                                'items': [{'name': name,
                                           'price': price
                                           }]
                                }]
                    } == json.loads(resp.data)