from functools import wraps
from gen_stamper import stampit
import logging


def logger(level, name=None, msg=None):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        funcname = msg if msg else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, f'{next(stampit)} {funcname}({args},{kwargs})')
            return func(*args, **kwargs)
        return wrapper

    return decorate


@logger(logging.DEBUG)
def adder(*args):
    return sum(args)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(adder(1, 3, 4, 4))
