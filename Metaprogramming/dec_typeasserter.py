from dec_logger import logger
from functools import wraps
from inspect import signature
import logging


def type_asserter(*typeargs, **typekwargs):

    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*typeargs, **typekwargs).arguments
        print(f'types: {bound_types}')

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            print(f'values: {bound_values}')
            for typename, value in bound_values.arguments.items():
                print(f'{typename}: {value}')
                if typename in bound_types:
                    if not isinstance(value, bound_types[typename]):
                        raise TypeError(f'Argument {typename} must be {bound_types[typename]}')
            return func(*args, **kwargs)
        return wrapper

    return decorate


@logger(logging.DEBUG)
@type_asserter(int, int, int, int, tuple)
def adder(a, b, c, d, *args):
    return a+b+c+d+sum(args)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(adder(1, 3, 4, 10,3))

    # print(adder(1, 3, '4', 10, 8, 9, 10))