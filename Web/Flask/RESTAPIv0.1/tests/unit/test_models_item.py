import pytest
from models.item import ItemModel
from models.store import StoreModel

name = 'string name'
price = 1923.23
store_id = 1


@pytest.fixture
def item():
    return ItemModel(name, price, store_id)


def test_itemmodel_init(item):
    assert name == item.name
    assert abs(price - item.price) < 0.000001
    assert store_id == 1