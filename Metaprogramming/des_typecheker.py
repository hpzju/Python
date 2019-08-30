import sys
import logging
from dec_logger import logger


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


class A:
    i = Integer()
    f = Float()
    s = String()
    l = List()


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    a = A()
    print([i for i in filter(lambda s: not s.startswith('__'), dir(a))])
    a.i = 10
    a.f = 10.1
    a.l = []
    a.s = ''
    print('Done')
    a.s = 4
