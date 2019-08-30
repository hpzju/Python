import sys
import logging
from dec_logger import logger
from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    @logger(logging.DEBUG)
    def __init__(self, name=None):
        self._name = name

    @logger(logging.DEBUG)
    def __set__(self, obj, value):
        if not isinstance(value, self._expected_type):
            raise TypeError(f'Expected {self._expected_type}, Got {type(value)}')
        obj.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class List(Typed):
    _expected_type = list


class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()

    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, self.clsname))
        super().__setitem__(name, value)


class TypedMeta(type):
    @classmethod
    @logger(logging.DEBUG)
    def __prepare__(mcs, clsname, bases):
        print(f'TypedMeta __prepare__')
        return NoDupOrderedDict(clsname)

    @logger(logging.DEBUG)
    def __new__(mcs, clsname, bases, clsdict):
        print(f'TypedMeta __new__')
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(mcs, clsname, bases, d)


class Structure(metaclass=TypedMeta):
    pass


class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    @logger(logging.DEBUG)
    def __init__(self, name, shares, price):
        print(f'Stock __init__')
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    print('!!!!!' * 10)
    a = Stock('GOOG', 100, 490.1)
    print('@@@@@'*10)
    b = Stock('AAPL','a lot', 610.23)
    print('Done')
