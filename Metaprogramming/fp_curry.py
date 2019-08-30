import functools
import inspect


def curry(func):
    print(f"decorating: {func.__qualname__}")

    def wrapper_func(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            print(f"evaluating: {args}, {kwargs}")
            return func(*args, **kwargs)
        print(f"currying: {args}, {kwargs}")
        return (lambda *args2, **kwargs2:
                wrapper_func(*(args + args2), **dict(kwargs, **kwargs2)))

    return wrapper_func


def adder(a, b, c):
    return a+b+c


@curry
def add(a, b, c):
    return a+b+c


if __name__ == '__main__':
    print(adder(1, 2, 3))
    print(add(10)(20)(30))
