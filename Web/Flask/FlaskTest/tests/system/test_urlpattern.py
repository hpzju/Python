import pytest
from FlaskTest.src.app import app
import json


@pytest.fixture(scope='module')
def get_app_client():
    return app.test_client


def test_home_page(get_app_client):
    with get_app_client() as client:
        resp = client.get('/')

        assert 200 == resp.status_code
        assert {'msg': 'Hello Flask'} == json.loads(resp.get_data())


def test_hello(get_app_client):
    with get_app_client() as client:
        resp = client.get('/hello')

        assert 200 == resp.status_code
        assert 'Hello, World' == resp.get_data().decode()


def test_show_user_profile(get_app_client):
    with get_app_client() as client:
        resp = client.get('/user/myname')

        assert 200 == resp.status_code
        assert 'User myname' == resp.get_data().decode()


def test_show_post(get_app_client):
    with get_app_client() as client:
        resp = client.get('/post/32123')

        assert 200 == resp.status_code
        assert 'Post ID 32123' == resp.get_data().decode()


def test_show_float(get_app_client):
    with get_app_client() as client:
        resp = client.get('/post/3212.3')

        assert 200 == resp.status_code
        assert 'Post Score 3212.3' == resp.get_data().decode()


def test_show_uuid(get_app_client):
    with get_app_client() as client:
        resp = client.get('/uuid/00000000-0000-0000-0000-000000000000')

        assert 200 == resp.status_code
        assert 'uuid 00000000-0000-0000-0000-000000000000' == resp.get_data().decode()


@pytest.mark.xfail
def test_show_uuid_not_valid(get_app_client):
    with get_app_client() as client:
        resp = client.get('/uuid/123565440000')

        assert 200 == resp.status_code
        assert 'uuid 123565440000' == resp.get_data().decode()