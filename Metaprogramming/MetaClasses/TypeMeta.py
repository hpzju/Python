from inspect import signature, Parameter, Signature


def make_sig(argnames):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
                     for name in argnames)


def repr(cls):
    values = ', '.join(str(getattr(cls, name)) for name in cls._fields)
    return f'{cls.__class__.__qualname__}({values})'


class StructMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        clsobj = super().__new__(mcs, clsname, bases, clsdict)
        sig = make_sig(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        setattr(clsobj, '__repr__', repr)
        return clsobj


class Structure(metaclass=StructMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']


class Host(Structure):
    _fields = ['address', 'port']


if __name__ == '__main__':
    s = Stock('APPL', 100, 980)
    p = Point(2, 3)
    h = Host('10.10.10.10', 34234)
    print(s)
    print(h)
    print(p)