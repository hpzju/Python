import time
from functools import wraps


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time_ns()
        result = func(*args, **kwargs)
        end = time.process_time_ns()
        print(f'{func.__qualname__}({args}, {kwargs}) Elapsed: {(end-start)/10**6} ms')
        return result

    return wrapper


@time_this
def range2listN(n):
    l = [i for i in range(n)]
    return l


if __name__ == '__main__':
    range2listN(10000)
    range2listN(100000)
    range2listN(1000000)
    range2listN(10000000)
