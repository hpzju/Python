from queue import Queue
from functools import wraps
import multiprocessing


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __repr__(self):
        return f'Async({self.func.__qualname__}, {self.args})'


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def dec_inline_async(func):

    @wraps(func)
    def wrapper(*args):
        # get generator
        f = func(*args)
        print(f'wrapper: f = {f}')
        result_queue = Queue()
        # priming
        result_queue.put(None)
        while True:
            result = result_queue.get()
            print(f'wrapper: result = {result}')
            try:
                a = f.send(result)
                print(f'wrapper: a = {a}')
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def adder(a, b):
    return a + b


@dec_inline_async
def run_async():
    r = yield Async(adder, (2, 3))
    print(r)
    r = yield Async(adder, ('hello ', 'world'))
    print(r)
    for i in range(10):
        r = yield  Async(adder, (i, i))
        print(r)
    print('done!')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async
    run_async()
