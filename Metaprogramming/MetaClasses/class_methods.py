class A:
    a = 3

    def __init__(self):
        self.a, self.b = 1, 2

    def imeth(self):
        print(f'in imeth: {vars(self)}')

    @classmethod
    def cmeth(cls):
        print(f'in cmeth: {vars(cls)}')

    @staticmethod
    def smeth():
        print(f'in smeth: {A.smeth}')


if __name__ == '__main__':
    c = A()
    print(dir(c))
    print(dir(c.__class__))
    print(id(c.a), id(A.a))
    print(id(c.imeth), id(A.imeth))
    print(id(c.cmeth), id(A.cmeth))
    print(id(c.smeth), id(A.smeth))
    print(id(c.imeth), type(c.imeth))
    print(id(c.cmeth), type(A.cmeth))
    print(id(c.smeth), type(A.smeth))
    c.imeth()
    c.cmeth()
    c.smeth()
    A.cmeth()
    A.smeth()