


def debugmethods(cls):
    print(f'decorating: {cls}')
    print(f'namespace: {dir(cls)}')
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        # if callable(self.__dict__.get(name, None)):
        #     print(f'Calling: {name}')
        # else:
        print(f'{self} Getting: {name}')
        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__

    return cls


class DebugMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        print(f'in DebugMeta new: {mcs}')
        print(f'\t {clsname}: {clsdict}')
        clsobj = super().__new__(mcs, clsname, bases, clsdict)

        clsobj = debugmethods(clsobj)
        print(f'\t {clsobj.__qualname__}: {dir(clsobj)}')
        return clsobj


class A(metaclass=DebugMeta):
    a = 3

    def __init__(self):
        self._a, self.b = 1, 2

    def imeth(self):
        print(f'in imeth: {vars(self)}')

    @classmethod
    def cmeth(cls):
        print(f'in cmeth: {vars(cls)}')

    @staticmethod
    def smeth():
        print(f'in smeth: {A.smeth}')


if __name__ == '__main__':
    print('-----'*20)
    c = A()
    s1 = set(c.__dict__)
    print(s1)
    s2 = set(c.__class__.__dict__)
    print(s2)
    s3 = set(dir(c))
    print(s3)
    print(s3-s2)
    c.imeth()
    c.cmeth()
    c.smeth()
    A.cmeth()
    A.smeth()
    print(c)
    c.a
    c.b
    A.a

