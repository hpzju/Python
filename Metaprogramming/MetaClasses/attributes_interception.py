from Metaprogramming import dec_timethis


class MetaAttr(type):
    def __new__(mcs, clsname, bases, clsdict):
        print('MetaAttr new:')
        clsobj = super().__new__(mcs, clsname, bases, clsdict)
        setattr(clsobj, '__repr__', strer)
        setattr(clsobj, '__getattr__', getter)
        setattr(clsobj, '__setattr__', setter)
        setattr(clsobj, '__init__', initor)
        return clsobj


def strer(obj):
    props = ', '.join(f'{k[1:]}={obj.__dict__[k]}' for k in filter(lambda x: not x.startswith('__'), sorted(obj.__dict__.keys())))
    return f'{obj.__class__.__name__}({props})'


def getter(obj, name):
    attrname = '_'+name
    if attrname not in obj.__dict__:
        raise AttributeError
    return getattr(obj, attrname, None)


def setter(obj, name, value):
    attrname = '_' + name
    if attrname in obj.__dict__:
        obj.__dict__[attrname] = value
    else:
        raise AttributeError


def initor(obj, **kwargs):
    # print(f'{obj.__class__.__name__}.__init__')
    # print(f'kwargs = {kwargs}')
    attrnames = {'_'+k: v for k, v in kwargs.items()}
    obj.__dict__.update(attrnames)


class Vector(metaclass=MetaAttr):
    pass


class Vector2:
    def __init__(self, **kwargs):
        attrnames = {'_' + k: v for k, v in kwargs.items()}
        self.__dict__.update(attrnames)


@dec_timethis.time_this
def perf(n):
    for i in range(n):
        v = Vector(a=i-1, b=i, c=i+1)


@dec_timethis.time_this
def perf2(n):
    for i in range(n):
        v = Vector2(a=i-1, b=i, c=i+1)


if __name__ == '__main__':
    print('-----'*20)
    v = Vector(a=1, b=2)
    print(v)
    v2 = Vector2(a=1, b=2)
    print(v2)
    print('*****' * 20)

    perf(10000)
    perf2(10000)
    perf(100000)
    perf2(100000)
    perf(1000000)
    perf2(1000000)