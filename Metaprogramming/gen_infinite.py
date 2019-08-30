import sys


class GenRegister:
    gens = {}

    def __init__(self, genfunc):
        print(f'registering {genfunc}')
        GenRegister.gens[genfunc.__qualname__] = genfunc
        self._gen = genfunc

    def __call__(self, *args, **kwargs):
        print(f'name {self._gen.__qualname__}')
        print(f'args {args}')
        print(f'kwargs {kwargs}')
        print(f'size {sys.getsizeof(self._gen)}')

        return GenRegister.gens[self._gen.__qualname__](*args, **kwargs)


@GenRegister
def gen_infinite():
    count = 0
    while True:
        count += 1
        yield count


@GenRegister
def gen_toN(n):
    for i in range(n):
        yield i


if __name__ == '__main__':
    g1 = gen_infinite()
    for i in g1:
        print(i)
        if i > 10:
            break

    for i in gen_toN(5):
        print(i)
